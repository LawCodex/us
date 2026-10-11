#!/usr/bin/env python3
"""Convert eCFR bulk XML (GovInfo, from fetch_ecfr.py) into Markdown.

Layout under <repo>/cfr/:
  title-NN-<slug>/_title.md                                 title heading + index
  title-NN-<slug>/chapter-<n>-<slug>/part-NNNN-<slug>.md    one file per CFR part
Parts not inside a chapter are written directly in the title directory. Reserved parts with no
text are skipped (they appear in _title.md as index entries only). Directories that would hold
more than 900 parts are split into part-number ranges (parts-NNNN-NNNN/).

Usage: python convert_ecfr.py [--raw DIR] [--out REPO_DIR] [--titles 1,40,...]
"""
import argparse
import html
import datetime
import json
import os
import re
import shutil
import sys

from lxml import etree

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from convert import esc, norm_ws, slug, wrap, block_start_escape, yaml_str  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
TODAY = datetime.date.today().isoformat()
MAX_FILE = 5 * 1024 * 1024
MAX_DIR = 900

DIVS = {"DIV1", "DIV2", "DIV3", "DIV4", "DIV5", "DIV6", "DIV7", "DIV8", "DIV9"}
SKIP = {"PRTPAGE", "CFRTOC", "HEAD", "PTHD", "CHAPTI", "SECHD", "SUBJECT", "PG", "RESERVED"}
MONTHS = {m: i for i, m in enumerate(
    ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], 1)}


def tag(el):
    return el.tag if isinstance(el.tag, str) else None


# ---------------------------------------------------------------- inline

def inline(el, md=True):
    out = [esc(el.text) if (el.text and md) else (el.text or "")]
    for c in el:
        t = tag(c)
        if t is None or t in ("PRTPAGE",):
            pass
        elif not md and t in ("br", "BR"):
            out.append("\x00")
        else:
            s = inline(c, md)
            if md:
                if t == "E":
                    ty = c.get("T", "")
                    if ty in ("01", "03"):
                        s = wrap("**", s)
                    elif ty in ("02", "04", "05", "07", "0731", "0732"):
                        s = wrap("*", s)
                    elif ty in ("51", "53", "54"):
                        s = f"<sup>{s.strip()}</sup>" if ty != "54" else f"<sub>{s.strip()}</sub>"
                    elif ty in ("52",):
                        s = f"<sub>{s.strip()}</sub>"
                elif t in ("I",):
                    s = wrap("*", s)
                elif t in ("B",):
                    s = wrap("**", s)
                elif t in ("SU", "sup"):
                    s = f"<sup>{s.strip()}</sup>"
                elif t == "sub":
                    s = f"<sub>{s.strip()}</sub>"
                elif t == "img":
                    s = f"[image: {os.path.basename(c.get('src', ''))}]"
                elif t in ("GID",):
                    s = f"[image: {s.strip()}]"
                elif t in ("BR", "br"):
                    s = "\x00"
                elif t in ("P", "FP", "HD1", "HD2", "HD3", "HED", "LI"):
                    s = " " + s + " "
            out.append(s)
        if c.tail:
            out.append(esc(c.tail) if md else c.tail)
    return "".join(out)


def head_of(el):
    h = el.find("HEAD")
    return norm_ws(inline(h)) if h is not None else ""


def plain_head(el):
    h = el.find("HEAD")
    return norm_ws(inline(h, md=False)) if h is not None else ""


# ---------------------------------------------------------------- tables

def md_table(header, rows, ncols, caption=None):
    def cell(x):
        return x.replace("\n", " ").replace("|", "\\|")
    out = []
    if caption:
        out.append(wrap("**", caption))
    if not header and rows:
        header, rows = rows[0], rows[1:]
    if not header:
        return "\n\n".join(out)
    lines = ["| " + " | ".join(cell(c) for c in header + [""] * (ncols - len(header))) + " |",
             "|" + "---|" * ncols]
    for r in rows:
        r = r + [""] * (ncols - len(r))
        lines.append("| " + " | ".join(cell(c) for c in r[:max(ncols, len(r))]) + " |")
    out.append("\n".join(lines))
    return "\n\n".join(out)


def gpotable(el):
    caption = el.find("TTITLE")
    cap = norm_ws(inline(caption)) if caption is not None else None
    heads = []
    box = el.find("BOXHD")
    if box is not None:
        cheds = [(int(c.get("H", "1") or 1), norm_ws(inline(c))) for c in box if tag(c) == "CHED"]
        stack = []
        for i, (h, txt) in enumerate(cheds):
            stack = stack[:h - 1] + [txt]
            nxt = cheds[i + 1][0] if i + 1 < len(cheds) else 0
            if nxt <= h:
                heads.append(" — ".join(x for x in stack if x))
    rows = []
    for r in el.iter("ROW"):
        rows.append([norm_ws(inline(e)) for e in r if tag(e) == "ENT"])
    ncols = max([len(heads)] + [len(r) for r in rows] + [int(el.get("COLS", "1") or 1)])
    out = md_table(heads, rows, ncols, cap)
    notes = [norm_ws(inline(x)) for x in el if tag(x) in ("TNOTE", "TDESC", "SIG")]
    return "\n\n".join([out] + [block_start_escape(n) for n in notes if n])


def html_table(el):
    rows = [tr for tr in el.iter("TR")]
    if not rows:
        return ""
    def span(c, k):
        try:
            return int(c.get(k, "1") or 1)
        except ValueError:
            return 1
    head = []
    while len(head) < len(rows) and all(tag(c) == "TH" for c in rows[len(head)] if tag(c)):
        head.append(rows[len(head)])
    body = rows[len(head):]
    cells = lambda r: [c for c in r if tag(c) in ("TD", "TH")]  # noqa: E731
    complex_ = len(head) > 1 or any(span(c, "colspan") > 1 or span(c, "rowspan") > 1
                                    for r in rows for c in cells(r))
    if complex_:
        out = ["<table>"]
        for r in rows:
            tds = []
            for c in cells(r):
                t = "th" if tag(c) == "TH" else "td"
                attrs = "".join(f' {k}="{span(c, k)}"' for k in ("colspan", "rowspan") if span(c, k) > 1)
                txt = html.escape(norm_ws(inline(c, md=False)), quote=False).replace("  \n", "<br>")
                tds.append(f"<{t}{attrs}>{txt}</{t}>")
            out.append("<tr>" + "".join(tds) + "</tr>")
        out.append("</table>")
        return "\n".join(out)
    md = lambda r: [norm_ws(inline(c)).replace("  \n", "<br>") for c in cells(r)]  # noqa: E731
    ncols = max(len(cells(r)) for r in rows) or 1
    return md_table(md(head[0]) if head else None, [md(r) for r in body], ncols)


# ---------------------------------------------------------------- blocks

class Out:
    def __init__(self):
        self.blocks = []

    def add(self, s):
        if "\n|" not in s and not s.startswith((">", "<table", "**")) and "\n<table" not in s:
            s = norm_ws(s)
        s = s.strip()
        if s:
            self.blocks.append(s)


PARA_RE = re.compile(r"^(F?P|FRP|TCAP|BCAP|FL|P)[-0-9A-Z]*$")
BLOCK_TAGS = DIVS | {"P", "FP", "TABLE", "GPOTABLE", "EXTRACT", "EXAMPLE", "NOTE", "HD1", "HD2", "HD3",
                     "HD4", "HD5", "HED", "FTNT", "MATH", "GPH", "DIV", "CITA", "AUTH", "SOURCE",
                     "EDNOTE", "EFFDNOT", "SECAUTH", "APPRO", "CROSSREF", "XREF", "LDRWK", "SCOL2",
                     "LI", "STARS", "TTITLE", "TNOTE", "SIG", "img"}


def is_blockish(c):
    t = tag(c)
    return t is not None and (t in BLOCK_TAGS or bool(PARA_RE.match(t)))


def render(el, out, depth, quote=False):
    t = tag(el)
    if t is None or t in SKIP:
        return
    if PARA_RE.match(t) and t not in DIVS and not any(is_blockish(c) for c in el):
        out.add(block_start_escape(norm_ws(inline(el))))
        return
    if t in DIVS:
        h = head_of(el)
        if h:
            if quote or depth > 6:
                out.add(wrap("**", h))
            else:
                out.add("#" * depth + " " + h)
        for c in el:
            render(c, out, depth + 1, quote)
        return
    if t in ("P", "FP", "FRP", "PSPACE", "LI", "CITA", "FTNT", "SIG", "TDESC", "NAME", "TITLE",
             "DATED", "PRTPAGE", "EDNOTE", "EFFDNOT", "SECAUTH", "APPRO", "FP-1", "FP-2",
             "FP1-2", "FP-DASH", "PARAUTH", "AMDPAR", "WIDE"):
        if any(tag(c) in ("P", "FP", "GPOTABLE", "TABLE", "EXTRACT", "NOTE", "HED") for c in el):
            for c in [el] if False else []:
                pass
            if el.text and el.text.strip():
                out.add(block_start_escape(norm_ws(esc(el.text))))
            for c in el:
                render(c, out, depth, quote)
                if c.tail and c.tail.strip():
                    out.add(block_start_escape(norm_ws(esc(c.tail))))
            return
        out.add(block_start_escape(norm_ws(inline(el))))
        return
    if t in ("HD1", "HD2", "HD3", "HD4", "HD5", "HED", "TTITLE", "HD"):
        out.add(wrap("**", norm_ws(inline(el))))
        return
    if t in ("AUTH", "SOURCE"):
        hed = el.find("HED")
        lab = norm_ws(inline(hed)) if hed is not None else ""
        body = " ".join(norm_ws(inline(c)) for c in el if tag(c) != "HED")
        out.add((wrap("**", lab) + " " if lab else "") + body)
        return
    if t in ("EXTRACT", "EXAMPLE", "QUOTE"):
        sub = Out()
        for c in el:
            render(c, sub, depth, True)
        if el.text and el.text.strip():
            sub.blocks.insert(0, norm_ws(esc(el.text)))
        for b in sub.blocks:
            out.blocks.append("\n".join(("> " + x) if x else ">" for x in b.split("\n")))
        return
    if t == "GPOTABLE":
        out.add(gpotable(el))
        return
    if t == "TABLE":
        out.add(html_table(el))
        return
    if t == "img":
        out.add(f"[image: {os.path.basename(el.get('src', ''))}]")
        return
    if t in ("GPH", "MATH"):
        gid = el.findtext(".//GID")
        imgs = [os.path.basename(i.get("src", "")) for i in el.iter("img")]
        if gid or imgs:
            out.add(" ".join(f"[image: {x.strip()}]" for x in ([gid] if gid else imgs)))
        else:
            out.add(norm_ws(inline(el)))
        return
    if t == "STARS":
        out.add("\\* \\* \\* \\* \\*")
        return
    if t in ("FTREF",):
        out.add(norm_ws(inline(el)))
        return
    # containers (NOTE, NOTES, CROSSREF, APPENDIX, DIV, SECTION, SUBPART-like, unknown)
    if not any(is_blockish(c) for c in el):
        out.add(block_start_escape(norm_ws(inline(el))))
        return
    if el.text and el.text.strip():
        out.add(block_start_escape(norm_ws(esc(el.text))))
    for c in el:
        render(c, out, depth, quote)
        if c.tail and c.tail.strip():
            out.add(block_start_escape(norm_ws(esc(c.tail))))


def render_unit(el, depth=1):
    out = Out()
    render(el, out, depth)
    return out.blocks


# ---------------------------------------------------------------- files

def part_filename(el, used):
    n = el.get("N", "")
    m = re.match(r"(\d+)(.*)", n)
    num = f"{int(m.group(1)):04d}{slug(m.group(2)) if m.group(2) else ''}" if m else slug(n)
    h = plain_head(el)
    h = re.sub(r"^\s*PART\s+[^\s—]+\s*—?\s*", "", h, flags=re.I)
    base = f"part-{num}-{slug(h)}".rstrip("-")[:100]
    fn, i = base + ".md", 2
    while fn in used:
        fn = f"{base}-{i}.md"
        i += 1
    used.add(fn)
    return fn


def div_dirname(el, kind, used):
    n = el.get("N", "")
    h = plain_head(el)
    h = re.sub(r"^\s*(CHAPTER|SUBTITLE)\s+[^\s—]+\s*—?\s*", "", h, flags=re.I)
    base = f"{kind}-{slug(n, 20)}-{slug(h, 60)}".rstrip("-")
    d, i = base, 2
    while d in used:
        d = f"{base}-{i}"
        i += 1
    used.add(d)
    return d


def parse_amd(s):
    m = re.search(r"([A-Z][a-z]{2})[a-z]*\.? (\d{1,2}), (\d{4})", s or "")
    if not m or m.group(1) not in MONTHS:
        return None
    return f"{m.group(3)}-{MONTHS[m.group(1)]:02d}-{int(m.group(2)):02d}"


class TitleConv:
    def __init__(self, path, out_root, meta):
        self.tree = etree.parse(path, etree.XMLParser(huge_tree=True, remove_comments=True,
                                                      recover=True))
        self.root = self.tree.getroot()
        self.title = self.root.find(".//DIV1")
        self.num = (self.root.findtext(".//IDNO") or "").strip() or self.title.get("N")
        dates = [parse_amd(x.text) for x in self.root.iter("AMDDATE")]
        self.amd = max([d for d in dates if d], default=None)  # newest volume amendment date
        head = plain_head(self.title)
        self.heading = re.sub(r"--Volume.*$", "", head).strip()
        hslug = slug(re.sub(r"^Title \d+\s*[—-]\s*", "", self.heading))
        self.dir = os.path.join(out_root, f"title-{int(self.num):02d}-{hslug}")
        self.meta = meta
        self.stats = {"parts": 0, "sections": 0, "files": 0, "bytes": 0, "reserved_skipped": 0}

    def front(self, title, ident, url, status="in_force"):
        lines = ["---", f"title: {yaml_str(title)}", f"identifier: {yaml_str(ident)}",
                 "type: regulation", "jurisdiction: us", "language: en"]
        if self.amd:
            lines.append(f"last_amended: {self.amd}  # latest amendment date of the CFR title")
        lines += [f"status: {status}", f"source: {yaml_str(url)}", f"retrieved: {TODAY}"]
        if self.meta.get("modified"):
            lines.append(f"ecfr_bulk_modified: {yaml_str(self.meta['modified'])}")
        lines.append("---")
        return "\n".join(lines) + "\n\n"

    def write(self, path, text):
        text = re.sub(r"\n{3,}", "\n\n", text).rstrip() + "\n"
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
        self.stats["files"] += 1
        self.stats["bytes"] += len(text.encode())

    def crumbs(self, el):
        out = []
        p = el.getparent()
        while p is not None and tag(p) in DIVS:
            if tag(p) != "DIV1":
                out.append(plain_head(p))
            p = p.getparent()
        return [self.heading] + list(reversed(out))

    def write_part(self, el, path):
        n = el.get("N", "")
        blocks = render_unit(el, 1)
        crumbs = self.crumbs(el)
        h = plain_head(el)
        status = "repealed" if re.search(r"\[(RESERVED|REMOVED)\]", h, re.I) else "in_force"
        front = self.front(f"{self.num} CFR Part {n} — {re.sub(r'^PART [^\s—]+\s*—?', '', h).strip()}",
                           f"{self.num} CFR Part {n}",
                           f"https://www.ecfr.gov/current/title-{self.num}/part-{n}", status)
        crumb = "*" + esc(" › ".join(crumbs)) + "*\n\n"
        text = front + crumb + "\n\n".join(blocks)
        if len(text.encode()) <= MAX_FILE:
            self.write(path, text)
            return
        # split by subpart (DIV6) or else by chunks
        chunks, cur, size = [], [], 0
        for b in blocks:
            starts_sub = b.startswith("## ")
            if cur and (size + len(b.encode()) > MAX_FILE - 300_000 or
                        (starts_sub and size > MAX_FILE // 2)):
                chunks.append(cur)
                cur, size = [], 0
            cur.append(b)
            size += len(b.encode()) + 2
        if cur:
            chunks.append(cur)
        d = path[:-3]
        for i, ch in enumerate(chunks, 1):
            fr = self.front(f"{self.num} CFR Part {n} (file {i} of {len(chunks)})",
                            f"{self.num} CFR Part {n}",
                            f"https://www.ecfr.gov/current/title-{self.num}/part-{n}", status)
            self.write(os.path.join(d, f"{i:02d}.md"), fr + crumb + "\n\n".join(ch))

    def convert(self):
        if os.path.isdir(self.dir):
            shutil.rmtree(self.dir)
        os.makedirs(self.dir)
        body = self.root  # one ECFRBRWS/DIV1 per printed volume
        parts = list(body.iter("DIV5"))
        self.stats["sections"] = sum(1 for _ in body.iter("DIV8"))
        # Group parts by (subtitle, chapter). A chapter may be split over several volumes
        # (several DIV1 elements), so group by number rather than element.
        groups, order = {}, []
        for p in parts:
            anc = {tag(a): a for a in p.iterancestors() if tag(a) in DIVS}
            ch, st = anc.get("DIV3"), anc.get("DIV2")
            key = (st.get("N") if st is not None else None, ch.get("N") if ch is not None else None)
            if key not in groups:
                groups[key] = {"chapter": ch, "subtitle": st, "parts": []}
                order.append(key)
            groups[key]["parts"].append(p)
        used_dirs = set()
        out = Out()
        out.add("# " + esc(self.heading))
        # title-level material outside parts (notes etc.), excluding structure and TOCs
        for div in body.iter("DIV1", "DIV2", "DIV3", "DIV4"):
            for c in div:
                if tag(c) and tag(c) not in DIVS and tag(c) not in SKIP:
                    render(c, out, 2)
        last_st = None
        for key in order:
            g = groups[key]
            ch = g["chapter"]
            if g["subtitle"] is not None and key[0] != last_st:
                out.add("## " + head_of(g["subtitle"]))
                last_st = key[0]
            base = self.dir if ch is None else os.path.join(
                self.dir, div_dirname(ch, "chapter", used_dirs))
            if ch is not None:
                out.add(("### " if g["subtitle"] is not None else "## ") + head_of(ch))
            real = [p for p in g["parts"] if p.find(".//DIV8") is not None or
                    len(render_unit(p)) > 1]
            self.stats["reserved_skipped"] += len(g["parts"]) - len(real)
            used = set()
            lines = []
            for i, p in enumerate(g["parts"]):
                if p not in real:
                    lines.append(f"- {head_of(p)}")
                    continue
                j = real.index(p)
                sub = base
                if len(real) > MAX_DIR:
                    lo = j // MAX_DIR * MAX_DIR
                    hi = min(lo + MAX_DIR, len(real)) - 1
                    sub = os.path.join(base, f"parts-{slug(real[lo].get('N'))}-{slug(real[hi].get('N'))}")
                fn = part_filename(p, used)
                self.write_part(p, os.path.join(sub, fn))
                rel = os.path.relpath(os.path.join(sub, fn), self.dir)
                lines.append(f"- [{head_of(p)}]({rel})")
                self.stats["parts"] += 1
            out.blocks.append("\n".join(lines))
        self.write(os.path.join(self.dir, "_title.md"),
                   self.front(self.heading, f"{self.num} CFR",
                              f"https://www.ecfr.gov/current/title-{self.num}")
                   + "\n\n".join(out.blocks))
        return self.stats


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw", default=os.path.join(HERE, "..", "..", "_raw", "us"))
    ap.add_argument("--out", default=os.path.join(HERE, ".."))
    ap.add_argument("--titles", default="")
    a = ap.parse_args()
    d = os.path.join(os.path.abspath(a.raw), "ecfr")
    manifest = json.load(open(os.path.join(d, "manifest.json")))
    want = [x for x in a.titles.split(",") if x]
    spath = os.path.join(HERE, "stats_ecfr.json")
    stats = json.load(open(spath)) if os.path.exists(spath) else {}
    for t in sorted(manifest, key=int):
        if want and t not in want:
            continue
        tc = TitleConv(os.path.join(d, manifest[t]["file"]), os.path.join(os.path.abspath(a.out), "cfr"),
                       manifest[t])
        s = tc.convert()
        s.update({"dir": os.path.basename(tc.dir), "heading": tc.heading, "amended": tc.amd,
                  "bulk_modified": manifest[t].get("modified")})
        stats[t] = s
        print(t, s, flush=True)
        json.dump(stats, open(spath, "w"), indent=1, sort_keys=True)


if __name__ == "__main__":
    main()
