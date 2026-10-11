#!/usr/bin/env python3
"""Fetch the US Constitution and its amendments from the National Archives transcriptions
(https://www.archives.gov/founding-docs) and write Markdown into <repo>/constitution/.

Outputs:
  constitution/constitution.md                       Preamble, Articles I-VII, attestation, signers
  constitution/amendments.md                         Amendments I-XXVII
  constitution/1789-joint-resolution-bill-of-rights.md  The 1789 joint resolution proposing 12 amendments

Usage: python constitution.py [--raw DIR] [--out REPO_DIR]
"""
import argparse
import datetime
import os
import re
import time

import requests
from bs4 import BeautifulSoup, NavigableString, Tag

UA = "LawCodex/1.0 (+https://github.com/LawCodex)"
BASE = "https://www.archives.gov/founding-docs/"
PAGES = ["constitution-transcript", "bill-of-rights-transcript", "amendments-11-27"]
HERE = os.path.dirname(os.path.abspath(__file__))
TODAY = datetime.date.today().isoformat()


def fetch(raw):
    os.makedirs(raw, exist_ok=True)
    out = {}
    for p in PAGES:
        path = os.path.join(raw, p + ".html")
        if not os.path.exists(path):
            for i in range(5):
                try:
                    r = requests.get(BASE + p, headers={"User-Agent": UA}, timeout=60)
                    r.raise_for_status()
                    break
                except requests.RequestException:
                    time.sleep(5 * 2 ** i)
            else:
                raise RuntimeError("cannot fetch " + p)
            open(path, "w", encoding="utf-8").write(r.text)
            time.sleep(10)  # robots.txt Crawl-delay
        out[p] = BeautifulSoup(open(path, encoding="utf-8").read(), "lxml")
    return out


def esc(s):
    s = s.replace("\\", "\\\\").replace("*", "\\*").replace("_", "\\_")
    s = re.sub(r"^([#>+-])", r"\\\1", s)
    s = re.sub(r"^(\d+)\.", r"\1\\.", s)
    return s


def inline(el):
    parts = []
    for c in el.children:
        if isinstance(c, NavigableString):
            parts.append(esc(re.sub(r"\s+", " ", str(c))))
        elif isinstance(c, Tag):
            if c.name == "br":
                parts.append("  \n")
                continue
            t = inline(c)
            if not t.strip():
                parts.append(t)
            elif c.name in ("strong", "b"):
                parts.append(f"**{t.strip()}** " if t.endswith(" ") else f"**{t.strip()}**")
            elif c.name in ("em", "i"):
                parts.append(f"*{t.strip()}* " if t.endswith(" ") else f"*{t.strip()}*")
            elif c.name in ("sup",):
                parts.append(f"<sup>{t}</sup>")
            else:
                parts.append(t)
    return "".join(parts)


def para(el):
    t = inline(el)
    t = re.sub(r"[ \t]+", " ", t)
    t = "\n".join(x.strip() for x in t.split("\n"))
    return t.strip()


def blocks(soup):
    """Yield (tag_name, text) for headings and paragraphs inside the page body."""
    main = soup.find(id="block-system-main")
    for e in main.find_all(["h1", "h2", "h3", "h4", "p"]):
        if e.find_parent(class_="nsnippet"):
            continue
        txt = e.get_text(" ", strip=True)
        if not txt or txt.startswith("Back to ") or txt.startswith("For biographies"):
            continue
        yield e, txt


def ital(txt):
    txt = re.sub(r"\s*The blue hyperlink[^.]*\.", "", txt).strip()
    return f"*{esc(txt)}*\n"


def front(title, ident, typ, date, source, extra=None):
    lines = ["---", f'title: "{title}"', f'identifier: "{ident}"', f"type: {typ}",
             "jurisdiction: us", "language: en"]
    if date:
        lines.append(f"date: {date}")
    lines += ["status: in_force", f'source: "{source}"', f"retrieved: {TODAY}"]
    for k, v in (extra or {}).items():
        lines.append(f'{k}: "{v}"')
    lines.append("---\n")
    return "\n".join(lines)


def constitution(soup):
    out = [front("Constitution of the United States", "US Constitution", "constitution",
                 "1787-09-17", BASE + "constitution-transcript",
                 {"note": "Transcription of the parchment as inscribed by Jacob Shallus; spelling and punctuation reflect the original (National Archives)."}),
           "# Constitution of the United States\n"]
    started = False
    for e, txt in blocks(soup):
        if e.name == "h1":
            continue
        if txt.startswith("Note:"):
            out.append(ital(txt))
            continue
        if not started and txt.startswith("We the People"):
            out.append("## Preamble\n")
            started = True
        if e.name == "h2":
            out.append(f"## {esc(txt)}\n")
        elif e.name == "h3":
            if txt.startswith("Section"):
                out.append(f"### {esc(txt)}\n")
            else:  # signers by state
                out.append(f"**{esc(txt)}**\n")
        else:
            if txt.startswith("Attest") and "## Signatories" not in out:
                out.append("## Attestation and Signatories\n")
            out.append(para(e) + "\n")
    return "\n".join(out)


ROMAN = {"I": 1, "V": 5, "X": 10, "L": 50}


def roman(s):
    n = 0
    for a, b in zip(s, s[1:] + " "):
        v = ROMAN[a]
        n += -v if b != " " and ROMAN.get(b, 0) > v else v
    return n


def amendments(bor, a1127):
    out = [front("Constitution of the United States — Amendments I–XXVII", "US Constitution, Amendments",
                 "constitution", None, BASE + "bill-of-rights-transcript",
                 {"source_2": BASE + "amendments-11-27"}),
           "# Constitution of the United States — Amendments\n"]
    # Amendments I-X: the "The U.S. Bill of Rights" section of the bill-of-rights page
    in_bor = False
    for e, txt in blocks(bor):
        if e.name == "h2":
            in_bor = txt.startswith("The U.S. Bill of Rights")
            continue
        if not in_bor or txt == "Amendments 11-27":
            continue
        m = re.match(r"Amendment ([IVXL]+)$", txt, re.I)
        if m:
            out.append(f"## Amendment {m.group(1).upper()}\n")
        elif txt.startswith("Note:"):
            out.append(ital(txt))
        else:
            out.append(para(e) + "\n")
    for e, txt in blocks(a1127):
        if e.name == "h1" or txt.startswith("Constitutional Amendments 1-10"):
            continue
        m = re.match(r"AMENDMENT ([IVXL]+)$", txt, re.I)
        if m:
            out.append(f"## Amendment {m.group(1).upper()}\n")
        elif e.name in ("h2", "h3", "h4"):
            out.append(f"### {esc(txt)}\n")
        elif re.match(r"(Passed by Congress|Originally proposed)", txt) or txt.startswith("Note:"):
            out.append(ital(txt))
        else:
            out.append(para(e) + "\n")
    return "\n".join(out)


def joint_resolution(bor):
    out = [front("Joint Resolution of Congress Proposing 12 Amendments to the U.S. Constitution (1789)",
                 "1 Stat. 97", "constitution", "1789-09-25", BASE + "bill-of-rights-transcript",
                 {"note": "Transcription of the enrolled original; articles three to twelve, ratified 1791, are Amendments I-X (the Bill of Rights); article two was ratified in 1992 as Amendment XXVII."}),
           "# Joint Resolution of Congress Proposing 12 Amendments to the U.S. Constitution (1789)\n"]
    take = False
    for e, txt in blocks(bor):
        if e.name == "h2":
            take = txt.startswith("Transcription of the 1789")
            continue
        if not take or txt == "Amendments 11-27":
            continue
        if txt.startswith("Note:"):
            out.append(ital(txt))
            continue
        m = re.match(r"\**(Article the \w+)\s*\.\.\.\s*\**\s*(.*)", para(e), re.S)
        if m:
            out.append(f"## {m.group(1)}\n")
            out.append(m.group(2).strip() + "\n")
        else:
            out.append(para(e) + "\n")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw", default=os.path.join(HERE, "..", "..", "_raw", "us", "const"))
    ap.add_argument("--out", default=os.path.join(HERE, ".."))
    a = ap.parse_args()
    pages = fetch(os.path.abspath(a.raw))
    d = os.path.join(a.out, "constitution")
    os.makedirs(d, exist_ok=True)
    files = {
        "constitution.md": constitution(pages["constitution-transcript"]),
        "amendments.md": amendments(pages["bill-of-rights-transcript"], pages["amendments-11-27"]),
        "1789-joint-resolution-bill-of-rights.md": joint_resolution(pages["bill-of-rights-transcript"]),
    }
    for name, text in files.items():
        text = re.sub(r"\n{3,}", "\n\n", text).rstrip() + "\n"
        open(os.path.join(d, name), "w", encoding="utf-8", newline="\n").write(text)
        print(name, len(text))


if __name__ == "__main__":
    main()
