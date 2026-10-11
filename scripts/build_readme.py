#!/usr/bin/env python3
"""Regenerate README.md from scripts/stats.json, scripts/stats_ecfr.json and the repo tree."""
import datetime
import glob
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)


def load(name):
    p = os.path.join(HERE, name)
    return json.load(open(p)) if os.path.exists(p) else {}


def count_md(sub):
    return len(glob.glob(os.path.join(REPO, sub, "**", "*.md"), recursive=True))


def mb(n):
    return f"{n / 1048576:.1f} MB"


def main():
    usc, cfr = load("stats.json"), load("stats_ecfr.json")
    today = datetime.date.today().isoformat()
    rps = {}
    for t, s in usc.items():
        rps.setdefault(s.get("release_point"), []).append(t)
    main_rp = max(rps, key=lambda k: len(rps[k])) if rps else "?"
    others = {k: v for k, v in rps.items() if k != main_rp}

    def tkey(t):
        return (int("".join(c for c in t if c.isdigit())), t)

    usc_rows = "\n".join(
        f"| {t.upper().lstrip('0')} | [{s['heading']}](usc/{s['dir']}/) | {'yes' if s.get('positive_law') else 'no'} "
        f"| {s['chapters']} | {s['sections']} | {s['files']} | {s.get('release_point')} |"
        for t, s in sorted(usc.items(), key=lambda kv: tkey(kv[0])))
    cfr_rows = "\n".join(
        f"| {t} | [{s['heading']}](cfr/{s['dir']}/) | {s['parts']} | {s['sections']} | {s['files']} | {s.get('amended') or ''} |"
        for t, s in sorted(cfr.items(), key=lambda kv: int(kv[0])))
    tot = lambda d, k: sum(s.get(k, 0) for s in d.values())  # noqa: E731
    others_txt = "".join(
        f"\n- Title {', '.join(sorted(v, key=tkey))}: release point **{k}** (newest intact archived copy; see Gaps)."
        for k, v in sorted(others.items()))

    text = f"""# United States — LawCodex

Federal legislation of the **United States of America** as plain Markdown, part of
[LawCodex](https://github.com/LawCodex) (one repository per jurisdiction).

Retrieved: **{today}**.

## Contents

| Category | Directory | Files | Units |
|---|---|---|---|
| Constitution (text + 27 amendments + 1789 Bill of Rights resolution) | [`constitution/`](constitution/) | {count_md('constitution')} | 7 articles, 27 amendments |
| United States Code (all 53 titles + 5 title appendices) | [`usc/`](usc/) | {count_md('usc')} | {len(usc)} titles/appendices, {tot(usc, 'chapters')} chapters/units, {tot(usc, 'sections')} sections |
| Code of Federal Regulations (eCFR, all titles) | [`cfr/`](cfr/) | {count_md('cfr')} | {len(cfr)} titles, {tot(cfr, 'parts')} parts, {tot(cfr, 'sections')} sections |

Text sizes: USC {mb(tot(usc, 'bytes'))}, CFR {mb(tot(cfr, 'bytes'))}.

## Sources

| Corpus | Source | Format |
|---|---|---|
| Constitution | National Archives, "America's Founding Documents" transcriptions: [Constitution](https://www.archives.gov/founding-docs/constitution-transcript), [Bill of Rights](https://www.archives.gov/founding-docs/bill-of-rights-transcript), [Amendments 11–27](https://www.archives.gov/founding-docs/amendments-11-27) | HTML |
| United States Code | Office of the Law Revision Counsel (OLRC), U.S. House of Representatives — [USLM XML release points](https://uscode.house.gov/download/download.shtml) | USLM 1.0 XML |
| Code of Federal Regulations | Office of the Federal Register / GPO — [eCFR bulk data on GovInfo](https://www.govinfo.gov/bulkdata/ECFR) | eCFR XML |

**United States Code currency.** The corpus is the OLRC "prelim" online edition at release
point **{main_rp}** (current through Public Law 119-102 of 2026-07-12, except Public Law 119-101,
per the OLRC naming convention). Exceptions:
{others_txt}

uscode.house.gov was returning an "Under Maintenance" page for every request (including the
download page and all release-point zips) at retrieval time. The USLM zips were therefore taken
from the Internet Archive's Wayback Machine copies of the *official OLRC files*
(`https://web.archive.org/web/<timestamp>id_/https://uscode.house.gov/download/releasepoints/...`),
i.e. byte-for-byte the files OLRC published; each zip was integrity-checked before use.
`scripts/fetch.py` tries the official site first and only falls back to the archive when the
official site is unavailable, so a re-run once the site is back will pick up the current
release point.

**eCFR currency.** eCFR is the continuously updated, editorially compiled (unofficial but
authoritative, maintained by the Office of the Federal Register) version of the CFR. Each part
file records the title's latest amendment date (`last_amended`) and the bulk file timestamp.

## Structure

```
constitution/
  constitution.md                          Preamble, Articles I–VII, attestation, signers
  amendments.md                            Amendments I–XXVII
  1789-joint-resolution-bill-of-rights.md  Joint resolution proposing 12 amendments
usc/
  title-NN-<slug>/                          one directory per title (appendices: title-05a-appendix ...)
    _title.md                               title heading, title-level notes, index of chapters
    chapter-NNN-<slug>.md                   one file per chapter
    chapter-NNN-<slug>/                     chapters > 5 MB split by subchapter/part
      _chapter.md, subchapter-<n>-<slug>.md
cfr/
  title-NN-<slug>/
    _title.md                               index of subtitles/chapters/parts (reserved parts listed)
    chapter-<roman>-<slug>/part-NNNN-<slug>.md   one file per CFR part
```

Each file has YAML front matter (`title`, `identifier`, `type`, `jurisdiction`, `language`,
`status`, `source`, `retrieved`; USC files add `positive_law` and `release_point`; CFR files add
`last_amended`). Headings follow the legal hierarchy (title → subtitle → chapter → subchapter →
part → section); USC subsections/paragraphs/clauses are bold-labelled paragraphs. USC files
include the OLRC source credits and editorial/statutory notes (amendment history, short titles,
effective dates, etc.), clearly separated under **Editorial Notes** / **Statutory Notes** labels;
quoted statutory text in notes is rendered as block quotes. Tables are Markdown tables, or HTML
when they have merged cells.

### United States Code titles

| Title | Heading | Positive law | Chapters/units | Sections | Files | Release point |
|---|---|---|---|---|---|---|
{usc_rows}

### Code of Federal Regulations titles

| Title | Heading | Parts | Sections | Files | Last amended |
|---|---|---|---|---|---|
{cfr_rows}

## Not covered / gaps

- **Title 53** of the US Code is reserved (no content); OLRC publishes no XML for it.
- **Title 50 Appendix** was eliminated (its provisions were moved to title 50 and others); only
  the disposition note is included.
- US Code titles for which no intact archived copy of the newest release point existed are at an
  older release point (listed above under *United States Code currency*).
- Statutes at Large, uncodified public/private laws, treaties, executive orders (except where
  reproduced in USC notes or 3 CFR), court rules other than those in the USC appendices, and
  agency guidance are not included.
- **CFR title 35** (Panama Canal) is reserved and has no content.
- CFR parts that are only "[Reserved]" are not written as files (they are listed in each title's
  `_title.md`). Very large CFR parts that GPO splits across printed volumes (e.g. 26 CFR part 1,
  40 CFR parts 52/63) appear as several files named `part-NNNN-<slug>-continued-N.md`, in volume order.
- CFR graphics (images, some formulas) are not included; they are referenced as `[image: <id>]`.
- State and territorial law is out of scope.

## Licence / copyright

Works of the United States Government are not subject to copyright in the US (17 U.S.C. § 105):
the Constitution transcriptions, the United States Code (OLRC) and the eCFR (OFR/GPO) are in the
public domain. The Markdown conversion in this repository is likewise dedicated to the public
domain.

## Regenerating

```sh
pip install -r scripts/requirements.txt
python scripts/constitution.py      # National Archives -> constitution/
python scripts/fetch.py             # USLM XML -> ../_raw/us/xml (official site, archive fallback)
python scripts/convert.py           # -> usc/
python scripts/fetch_ecfr.py        # eCFR XML -> ../_raw/us/ecfr
python scripts/convert_ecfr.py      # -> cfr/
python scripts/build_readme.py      # this README
```

Raw downloads are cached in `../_raw/us/` (outside the repository) and are not committed.
"""
    open(os.path.join(REPO, "README.md"), "w", encoding="utf-8", newline="\n").write(text)
    print("README.md written")


if __name__ == "__main__":
    main()
