#!/usr/bin/env python3
"""Convert United States Code USLM XML (from fetch.py) into Markdown.

Layout written under <repo>/usc/:
  title-NN-<slug>/_title.md                 title heading, title-level notes, index of chapters
  title-NN-<slug>/chapter-NNN-<slug>.md      one file per chapter
  title-NN-<slug>/chapter-NNN-<slug>/...     chapters whose Markdown exceeds 5 MB are split into
                                             one file per subchapter/part (recursively), with
                                             chapter-level material in _chapter.md
Titles without chapters (some appendices) get one file per top-level division instead.

Usage: python convert.py [--raw DIR] [--out REPO_DIR] [--titles 01,26,...]
"""
import argparse
import datetime
import html
import json
import os
import re
import shutil
import sys
import unicodedata

from lxml import etree

U = "http://xml.house.gov/schemas/uslm/1.0"
XH = "http://www.w3.org/1999/xhtml"
HERE = os.path.dirname(os.path.abspath(__file__))
TODAY = datetime.date.today().isoformat()
MAX_FILE = 5 * 1024 * 1024

BIG = {"title", "subtitle", "chapter", "subchapter", "part", "subpart", "division", "subdivision",
       "article", "subarticle", "level", "compiledAct", "courtRules", "courtRule",
       "reorganizationPlans", "reorganizationPlan", "schedule", "appendix", "preliminary"}
SMALL = {"subsection", "paragraph", "subparagraph", "clause", "subclause", "item", "subitem",
         "subsubitem"}
INLINE_CONTAINERS = {"content", "chapeau", "continuation", "proviso", "text"}
SKIP = {"toc", "meta", "num", "heading"}
BLOCKY = BIG | SMALL | {"section", "p", "note", "notes", "table", "layout", "content", "chapeau",
                        "continuation", "sourceCredit", "quotedContent", "subheading"}


def ln(el):
    return etree.QName(el).localname if isinstance(el.tag, str) else None


def slug(s, maxlen=60):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s.lower()).strip("-")
    if len(s) > maxlen:
        s = s[:maxlen].rsplit("-", 1)[0]
    return s or "untitled"


def esc(s):
    s = s.replace("\\", "\\\\").replace("*", "\\*").replace("_", "\\_").replace("`", "\\`")
    s = re.sub(r"<(?=[A-Za-z/!?])", "&lt;", s)
    return s


def wrap(mark, t):
    """Wrap t in emphasis markers keeping surrounding whitespace outside."""
    m = re.match(r"^(\s*)(.*?)(\s*)$", t, re.S)
    if not m.group(2):
        return t
    inner = m.group(2)
    if mark == "**" and inner.startswith("**") and inner.endswith("**") and len(inner) > 4 \
            and "**" not in inner[2:-2]:
        return t
    return f"{m.group(1)}{mark}{m.group(2)}{mark}{m.group(3)}"


def norm_ws(s):
    s = re.sub(r"[^\S\u00a0]+", " ", s)
    s = s.replace("\x00", "  \n")
    return "\n".join(x.strip() for x in s.split("\n")).strip()


def block_start_escape(s):
    if re.match(r"^(#|>|[-+=]\s|\d+[.)]\s|\|)", s):
        return "\\" + s
    return s


# ---------------------------------------------------------------- inline rendering

def inline_node(c, md=True):
    """Render one child element (without its tail) inline."""
    name = ln(c)
    if name is None or name == "toc":
        return ""
    t = inline(c, md)
    if name == "note" and c.get("type") == "footnote":
        return " [footnote: " + t.strip() + "] "
    if not md:
        return (" " + t + " ") if (name == "p" or name in BIG or name in SMALL) else t
    if name in ("b", "strong"):
        t = wrap("**", t)
    elif name in ("i", "em"):
        t = wrap("*", t)
    elif name == "sup":
        t = f"<sup>{t.strip()}</sup>"
    elif name == "sub":
        t = f"<sub>{t.strip()}</sub>"
    elif name == "br":
        t = "\x00"
    elif name == "img":
        t = "[image]"
    elif name == "p" or name in BIG or name in SMALL or name == "section":
        t = " " + t + " "
    return t


def inline(el, md=True):
    """Flatten an element's content to a single inline string."""
    out = []
    if el.text:
        out.append(esc(el.text) if md else el.text)
    for c in el:
        out.append(inline_node(c, md))
        if c.tail:
            out.append(esc(c.tail) if md else c.tail)
    return "".join(out)


def label(el):
    num = el.find(f"{{{U}}}num")
    head = el.find(f"{{{U}}}heading")
    n = norm_ws(inline(num)) if num is not None else ""
    h = norm_ws(inline(head)) if head is not None else ""
    if n and h:
        if n.endswith(("—", "-", "–")) or head.text and head.text[:1].isspace():
            return n + ("" if n.endswith(("—", "-", "–")) else " ") + h
        return n + " " + h
    return n or h


# ---------------------------------------------------------------- tables

def cells_of(row):
    return [c for c in row if ln(c) in ("td", "th", "column")]


def table_md(rows, head_rows):
    """rows: list of row elements (head rows first). Returns Markdown or HTML table string."""
    allrows = head_rows + rows
    if not allrows:
        return ""
    ncols = max(sum(int(c.get("colspan", "1") or 1) for c in cells_of(r)) for r in allrows) or 1
    caption = []
    hr = list(head_rows)
    while hr and len(cells_of(hr[0])) == 1 and ncols > 1:
        caption.append(norm_ws(inline(cells_of(hr[0])[0])))
        hr.pop(0)
    body = rows
    complex_ = any(int(c.get("colspan", "1") or 1) > 1 or int(c.get("rowspan", "1") or 1) > 1
                   for r in hr + body for c in cells_of(r)) or len(hr) > 1
    out = []
    if caption:
        out.append("\n\n".join(wrap("**", c) for c in caption if c))
    if complex_:
        h = ["<table>"]
        for tag, rs in (("th", hr), ("td", body)):
            for r in rs:
                h.append("<tr>" + "".join(
                    "<{t}{a}>{x}</{t}>".format(
                        t=tag,
                        a="".join(f' {k}="{c.get(k)}"' for k in ("colspan", "rowspan")
                                  if c.get(k) and c.get(k) != "1"),
                        x=html.escape(norm_ws(inline(c, md=False))))
                    for c in cells_of(r)) + "</tr>")
        h.append("</table>")
        out.append("\n".join(h))
    else:
        def mdrow(r):
            cs = [norm_ws(inline(c)).replace("\n", " ").replace("|", "\\|") for c in cells_of(r)]
            cs += [""] * (ncols - len(cs))
            return "| " + " | ".join(cs) + " |"
        if hr:
            header, rest = hr[-1], body
        elif body:
            header, rest = body[0], body[1:]
        else:
            return "\n\n".join(out)
        lines = [mdrow(header), "|" + "---|" * ncols] + [mdrow(r) for r in rest]
        out.append("\n".join(lines))
    return "\n\n".join(x for x in out if x)


def xhtml_table(t):
    head, body = [], []
    for sect in t:
        n = ln(sect)
        if n == "thead":
            head += [r for r in sect if ln(r) == "tr"]
        elif n in ("tbody", "tfoot"):
            body += [r for r in sect if ln(r) == "tr"]
        elif n == "tr":
            body.append(sect)
    return table_md(body, head)


def layout_table(t):
    head = [r for r in t if ln(r) == "header"]
    body = [r for r in t if ln(r) in ("tocItem", "row")]
    return table_md(body, head)


# ---------------------------------------------------------------- block rendering

class Out:
    def __init__(self, quote=False):
        self.blocks = []
        self.buf = []
        self.quote = quote

    def text(self, s):
        if s:
            self.buf.append(s)

    def flush(self):
        if self.buf:
            s = norm_ws("".join(self.buf))
            self.buf = []
            if s:
                self.blocks.append(block_start_escape(s))

    def block(self, s):
        self.flush()
        if s:
            self.blocks.append(s)


def has_blocks(el):
    return any(ln(c) in BLOCKY for c in el.iter() if c is not el)


class Renderer:
    def __init__(self, depth_cap=6):
        self.depth_cap = depth_cap

    def heading(self, out, text, depth):
        out.flush()
        if not text:
            return
        if out.quote or depth > self.depth_cap:
            out.block(wrap("**", text))
        else:
            out.block("#" * depth + " " + text)

    def walk_children(self, el, out, depth, inline_mode=False):
        if el.text and el.text.strip() or (inline_mode and el.text):
            out.text(esc(el.text))
        for c in el:
            self.node(c, out, depth, inline_mode)
            if c.tail and (c.tail.strip() or inline_mode):
                out.text(esc(c.tail))

    def node(self, el, out, depth, inline_mode=False):
        name = ln(el)
        if name is None or name in SKIP:
            return
        if name in BIG or name == "section":
            self.heading(out, label(el), depth)
            self.walk_children(el, out, depth + 1)
            out.flush()
        elif name in SMALL:
            out.flush()
            lab = label(el)
            if lab:
                out.text(wrap("**", lab) + " ")
            self.walk_children(el, out, depth, inline_mode=True)
            out.flush()
        elif name in INLINE_CONTAINERS:
            self.walk_children(el, out, depth, inline_mode=True)
            if name != "chapeau":
                out.flush()
        elif name in ("p", "sourceCredit", "subheading", "signature", "signatures"):
            out.flush()
            self.walk_children(el, out, depth, inline_mode=True)
            out.flush()
        elif name == "notes":
            out.flush()
            self.walk_children(el, out, depth)
        elif name == "note":
            out.flush()
            if el.get("type") == "footnote":
                num = el.find(f"{{{U}}}num")
                if num is not None:
                    out.text("<sup>" + norm_ws(inline(num)) + "</sup> ")
                self.walk_children(el, out, depth, inline_mode=True)
                out.flush()
                return
            h = label(el)
            if h:
                out.block(wrap("**", h))
            self.walk_children(el, out, depth, inline_mode=True)
            out.flush()
        elif name == "quotedContent":
            if has_blocks(el):
                out.flush()
                sub = Out(quote=True)
                self.walk_children(el, sub, depth, inline_mode=True)
                sub.flush()
                for b in sub.blocks:
                    out.blocks.append("\n".join(("> " + x) if x else ">" for x in b.split("\n")))
            else:
                out.text(inline(el))
        elif name == "table":
            out.block(xhtml_table(el))
        elif name == "layout":
            out.block(layout_table(el))
        elif name in ("b", "strong", "i", "em", "sup", "sub", "ref", "date", "inline", "span",
                      "a", "term", "quotedText", "shortTitle", "def", "del", "ins", "br", "img",
                      "entity", "marker", "name", "role", "organization", "place", "fillIn",
                      "checkBox", "footnote", "personalName", "abbr"):
            if has_blocks(el):
                self.walk_children(el, out, depth, inline_mode=True)
            else:
                out.text(inline_node(el))
        else:
            # unknown container: render children generically
            out.flush()
            self.walk_children(el, out, depth, inline_mode=True)
            out.flush()

    def render(self, el, depth):
        out = Out()
        self.node(el, out, depth)
        out.flush()
        return out.blocks


# ---------------------------------------------------------------- files

def yaml_str(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def status_of(el):
    st = el.get("status")
    lab = label(el)
    if st in ("repealed", "transferred", "omitted", "renumbered", "vacant", "reserved"):
        return "repealed" if st != "reserved" else "unknown"
    if lab.startswith("[") or re.search(r"\b(REPEALED|OMITTED|TRANSFERRED|RESERVED)\b", lab.upper()):
        if "RESERVED" in lab.upper() and not re.search(r"REPEALED|OMITTED|TRANSFERRED", lab.upper()):
            return "unknown"
        return "repealed"
    return "in_force"


class TitleConverter:
    def __init__(self, path, out_root, meta):
        self.tree = etree.parse(path, etree.XMLParser(huge_tree=True, remove_comments=True))
        self.root = self.tree.getroot()
        self.title = self.root.find(f"{{{U}}}main/*")
        if self.title is None:  # title appendices: <appendix> directly under <uscDoc>
            self.title = next(c for c in self.root if ln(c) and ln(c) != "meta")
        self.appendix = ln(self.title) == "appendix"
        self.meta = meta
        self.out_root = out_root
        self.r = Renderer()
        num = self.root.findtext(f".//{{{U}}}meta/{{{U}}}docNumber") or ""
        self.num = num
        m = re.match(r"(\d+)([A-Za-z]*)", num)
        self.tnum = f"{int(m.group(1)):02d}{m.group(2).lower()}" if m else slug(num)
        pl = self.root.find(f".//{{{U}}}meta/{{{U}}}property[@role='is-positive-law']")
        self.positive = pl is not None and (pl.text or "").strip() == "yes"
        self.pub = self.root.findtext(f".//{{{U}}}meta/{{{U}}}docPublicationName") or ""
        self.title_label = label(self.title)
        hd = self.title.find(f"{{{U}}}heading")
        tslug = "appendix" if self.appendix else slug(norm_ws(inline(hd, md=False)) if hd is not None else "")
        self.dir = os.path.join(out_root, f"title-{self.tnum}-{tslug}")
        self.files = []
        self.stats = {"chapters": 0, "sections": 0, "files": 0, "bytes": 0}

    def front(self, title, ident, status, extra=None):
        rp = self.meta.get("release_point") or self.pub.replace("Online@", "")
        lines = ["---", f"title: {yaml_str(title)}", f"identifier: {yaml_str(ident)}", "type: code",
                 "jurisdiction: us", "language: en", f"status: {status}",
                 f"positive_law: {'true' if self.positive else 'false'}",
                 f"release_point: {yaml_str(rp)}",
                 f"source: {yaml_str(self.source_url(ident))}",
                 f"retrieved: {TODAY}"]
        for k, v in (extra or {}).items():
            lines.append(f"{k}: {yaml_str(v)}")
        lines.append("---")
        return "\n".join(lines) + "\n\n"

    def source_url(self, ident):
        # /us/usc/t5/ptI/ch1/schII -> granuleid:USC-prelim-title5-chapter1-subchapter2-style ids
        m = re.match(r"/us/usc/t(\w+)(.*)", ident or "")
        if not m:
            return "https://uscode.house.gov/"
        parts = [f"title{m.group(1)}"]
        for seg in m.group(2).strip("/").split("/"):
            mm = re.match(r"(sch|ch)(\w+)$", seg)
            if mm:
                parts.append(("subchapter" if mm.group(1) == "sch" else "chapter") + mm.group(2))
        return ("https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-"
                + "-".join(parts) + "&edition=prelim")

    def write(self, path, text):
        text = re.sub(r"\n{3,}", "\n\n", text).rstrip() + "\n"
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
        self.stats["files"] += 1
        self.stats["bytes"] += len(text.encode())
        return path

    def ancestors_labels(self, el):
        labs = []
        p = el.getparent()
        while p is not None and ln(p) != "main":
            if ln(p) in BIG:
                labs.append(label(p))
            p = p.getparent()
        return list(reversed(labs))

    def unit_title(self, el):
        return " / ".join([x for x in self.ancestors_labels(el)] + [label(el)])

    def render_unit(self, el, path, ident_extra=None):
        """Write el (a chapter or division) to path (.md); split into a directory if too big."""
        blocks = self.r.render(el, 1)
        body = "\n\n".join(blocks)
        crumbs = self.ancestors_labels(el)
        title = " / ".join(crumbs + [label(el)])
        head = self.front(title, el.get("identifier") or "", status_of(el))
        crumb = ("*" + esc(" › ".join(crumbs)) + "*\n\n") if crumbs else ""
        text = head + crumb + body
        if len(text.encode()) <= MAX_FILE:
            return [self.write(path, text)]
        # split
        d = path[:-3]
        kids = [c for c in el if ln(c) in BIG]
        written = []
        if kids:
            used = set()
            rest = etree.Element(el.tag, el.attrib)
            for c in el:
                if ln(c) not in BIG:
                    rest.append(etree.fromstring(etree.tostring(c, with_tail=False)))
            rblocks = self.r.render(rest, 1)
            written.append(self.write(os.path.join(d, "_" + ln(el) + ".md"),
                                      head + crumb + "\n\n".join(rblocks) + "\n\n" +
                                      "\n".join(f"- {esc(label(c))}" for c in kids)))
            for c in kids:
                fn = self.unit_filename(c, used)
                written += self.render_unit(c, os.path.join(d, fn))
            return written
        # no sub-divisions: chunk by top-level children (sections)
        chunks, cur, size = [], [], 0
        for b in self.r.render(el, 1):
            bs = len(b.encode())
            if cur and size + bs > MAX_FILE - 200_000:
                chunks.append(cur)
                cur, size = [], 0
            cur.append(b)
            size += bs + 2
        if cur:
            chunks.append(cur)
        for i, ch in enumerate(chunks, 1):
            written.append(self.write(os.path.join(d, f"part-{i:02d}.md"),
                                      self.front(f"{title} (part {i} of {len(chunks)})",
                                                 el.get("identifier") or "", status_of(el))
                                      + crumb + "\n\n".join(ch)))
        return written

    def unit_filename(self, el, used):
        kind = {"compiledAct": "act", "courtRules": "rules", "courtRule": "rule",
                "reorganizationPlans": "reorganization", "reorganizationPlan": "plan",
                "level": ""}.get(ln(el), ln(el))
        num = el.find(f"{{{U}}}num")
        val = (num.get("value") if num is not None else None) or ""
        if not val and num is not None:
            val = re.sub(r"^\W*(chapter|subchapter|part|subpart|subtitle|division|article)\s*", "",
                         norm_ws(inline(num, md=False)), flags=re.I)
        val = re.sub(r"[^A-Za-z0-9]+", "", val)
        m = re.match(r"(\d+)(.*)", val)
        numpart = f"{int(m.group(1)):03d}{m.group(2).lower()}" if m else val.lower()
        head = el.find(f"{{{U}}}heading")
        h = slug(norm_ws(inline(head, md=False))) if head is not None else ""
        base = "-".join(x for x in (kind.lower(), numpart, h) if x)[:100].rstrip("-")
        base = re.sub(r"^(act|rules|reorganization)-\1-", r"\1-", base)
        fn, i = base + ".md", 2
        while fn in used:
            fn = f"{base}-{i}.md"
            i += 1
        used.add(fn)
        return fn

    def convert(self):
        if os.path.isdir(self.dir):
            shutil.rmtree(self.dir)
        os.makedirs(self.dir)
        chapters = [c for c in self.title.iter(f"{{{U}}}chapter")
                    if not any(ln(a) == "quotedContent" for a in c.iterancestors())]
        self.stats["sections"] = sum(1 for s in self.title.iter(f"{{{U}}}section")
                                     if not any(ln(a) == "quotedContent" for a in s.iterancestors()))
        used = set()
        index_targets = {}
        if chapters:
            units = chapters
        else:
            units = [c for c in self.title if ln(c) in BIG or ln(c) == "section"]
        for u in units:
            fn = self.unit_filename(u, used) if ln(u) != "section" else None
            if fn is None:
                continue
            index_targets[u] = fn
            self.render_unit(u, os.path.join(self.dir, fn))
        self.stats["chapters"] = len(index_targets)
        # sections not inside any unit, plus title-level notes and index
        out = Out()
        self.title_index(self.title, out, 1, index_targets)
        out.flush()
        self.write(os.path.join(self.dir, "_title.md"),
                   self.front(self.title_label, self.title.get("identifier") or "",
                              "in_force") + "\n\n".join(out.blocks))
        return self.stats

    def title_index(self, el, out, depth, targets):
        if el in targets:
            fn = targets[el]
            out.block(f"- [{esc(label(el))}]({fn})")
            return
        name = ln(el)
        if name in BIG:
            self.r.heading(out, label(el), depth)
            for c in el:
                if ln(c) in BIG or c in targets:
                    self.title_index(c, out, depth + 1, targets)
                else:
                    self.r.node(c, out, depth + 1)
            out.flush()
        else:
            self.r.node(el, out, depth)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw", default=os.path.join(HERE, "..", "..", "_raw", "us"))
    ap.add_argument("--out", default=os.path.join(HERE, ".."))
    ap.add_argument("--titles", default="")
    a = ap.parse_args()
    raw = os.path.abspath(a.raw)
    mpath = os.path.join(raw, "manifest.json")
    manifest = json.load(open(mpath)) if os.path.exists(mpath) else {}
    for f in sorted(os.listdir(os.path.join(raw, "xml"))):
        m = re.match(r"usc(\w+)\.xml$", f)
        if m and m.group(1).lower() not in manifest:
            manifest[m.group(1).lower()] = {}
    out_root = os.path.join(os.path.abspath(a.out), "usc")
    want = [t.strip().lower() for t in a.titles.split(",") if t.strip()]
    stats = {}
    spath = os.path.join(HERE, "stats.json")
    if os.path.exists(spath):
        stats = json.load(open(spath))
    for t in sorted(manifest):
        if want and t not in want:
            continue
        p = os.path.join(raw, "xml", f"usc{t}.xml")
        tc = TitleConverter(p, out_root, manifest[t])
        s = tc.convert()
        s.update({"dir": os.path.relpath(tc.dir, out_root), "heading": tc.title_label,
                  "release_point": manifest[t].get("release_point"), "positive_law": tc.positive})
        stats[t] = s
        print(t, s, flush=True)
        json.dump(stats, open(spath, "w"), indent=1, sort_keys=True)


if __name__ == "__main__":
    main()
