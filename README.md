# United States — LawCodex

Federal legislation of the **United States of America** as plain Markdown, part of
[LawCodex](https://github.com/LawCodex) (one repository per jurisdiction).

Retrieved: **2026-10-11**.

## Contents

| Category | Directory | Files | Units |
|---|---|---|---|
| Constitution (text + 27 amendments + 1789 Bill of Rights resolution) | [`constitution/`](constitution/) | 3 | 7 articles, 27 amendments |
| United States Code (all 53 titles + 5 title appendices) | [`usc/`](usc/) | 3090 | 58 titles/appendices, 2947 chapters/units, 60536 sections |
| Code of Federal Regulations (eCFR, all titles) | [`cfr/`](cfr/) | 8400 | 49 titles, 8351 parts, 227286 sections |

Text sizes: USC 324.6 MB, CFR 660.4 MB.

## Sources

| Corpus | Source | Format |
|---|---|---|
| Constitution | National Archives, "America's Founding Documents" transcriptions: [Constitution](https://www.archives.gov/founding-docs/constitution-transcript), [Bill of Rights](https://www.archives.gov/founding-docs/bill-of-rights-transcript), [Amendments 11–27](https://www.archives.gov/founding-docs/amendments-11-27) | HTML |
| United States Code | Office of the Law Revision Counsel (OLRC), U.S. House of Representatives — [USLM XML release points](https://uscode.house.gov/download/download.shtml) | USLM 1.0 XML |
| Code of Federal Regulations | Office of the Federal Register / GPO — [eCFR bulk data on GovInfo](https://www.govinfo.gov/bulkdata/ECFR) | eCFR XML |

**United States Code currency.** The corpus is the OLRC "prelim" online edition at release
point **119-102not101** (current through Public Law 119-102 of 2026-07-12, except Public Law 119-101,
per the OLRC naming convention). Exceptions:

- Title 36: release point **119-36** (newest intact archived copy; see Gaps).
- Title 50: release point **119-59** (newest intact archived copy; see Gaps).

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
| 1 | [Title 1—GENERAL PROVISIONS](usc/title-01-general-provisions/) | yes | 3 | 39 | 4 | 119-102not101 |
| 2 | [Title 2—THE CONGRESS](usc/title-02-the-congress/) | no | 54 | 1612 | 55 | 119-102not101 |
| 3 | [Title 3—THE PRESIDENT](usc/title-03-the-president/) | yes | 5 | 64 | 6 | 119-102not101 |
| 4 | [Title 4—FLAG AND SEAL, SEAT OF GOVERNMENT, AND THE STATES](usc/title-04-flag-and-seal-seat-of-government-and-the-states/) | yes | 5 | 47 | 6 | 119-102not101 |
| 5 | [Title 5—GOVERNMENT ORGANIZATION AND EMPLOYEES](usc/title-05-government-organization-and-employees/) | yes | 63 | 1163 | 64 | 119-102not101 |
| 5A | [Title 5—APPENDIX FEDERAL ADVISORY COMMITTEE ACT](usc/title-05a-appendix/) | no | 4 | 19 | 5 | 119-102not101 |
| 6 | [Title 6—DOMESTIC SECURITY](usc/title-06-domestic-security/) | no | 6 | 569 | 7 | 119-102not101 |
| 7 | [Title 7—AGRICULTURE](usc/title-07-agriculture/) | no | 130 | 2926 | 131 | 119-102not101 |
| 8 | [Title 8—ALIENS AND NATIONALITY](usc/title-08-aliens-and-nationality/) | no | 16 | 376 | 17 | 119-102not101 |
| 9 | [Title 9—ARBITRATION](usc/title-09-arbitration/) | yes | 4 | 33 | 5 | 119-102not101 |
| 10 | [Title 10—ARMED FORCES](usc/title-10-armed-forces/) | yes | 350 | 4033 | 351 | 119-102not101 |
| 11 | [Title 11—BANKRUPTCY](usc/title-11-bankruptcy/) | yes | 9 | 280 | 10 | 119-102not101 |
| 11A | [Title 11—APPENDIX BANKRUPTCY RULES](usc/title-11a-appendix/) | no | 1 | 0 | 2 | 119-102not101 |
| 12 | [Title 12—BANKS AND BANKING](usc/title-12-banks-and-banking/) | no | 62 | 1996 | 63 | 119-102not101 |
| 13 | [Title 13—CENSUS](usc/title-13-census/) | yes | 6 | 70 | 7 | 119-102not101 |
| 14 | [Title 14—COAST GUARD](usc/title-14-coast-guard/) | yes | 17 | 449 | 18 | 119-102not101 |
| 15 | [Title 15—COMMERCE AND TRADE](usc/title-15-commerce-and-trade/) | no | 153 | 2701 | 154 | 119-102not101 |
| 16 | [Title 16—CONSERVATION](usc/title-16-conservation/) | no | 153 | 5095 | 154 | 119-102not101 |
| 17 | [Title 17—COPYRIGHTS](usc/title-17-copyrights/) | yes | 15 | 153 | 16 | 119-102not101 |
| 18 | [Title 18—CRIMES AND CRIMINAL PROCEDURE](usc/title-18-crimes-and-criminal-procedure/) | yes | 141 | 1399 | 142 | 119-102not101 |
| 18A | [Title 18—APPENDIX UNLAWFUL POSSESSION OR RECEIPT OF FIREARMS](usc/title-18a-appendix/) | no | 4 | 27 | 5 | 119-102not101 |
| 19 | [Title 19—CUSTOMS DUTIES](usc/title-19-customs-duties/) | no | 30 | 1111 | 31 | 119-102not101 |
| 20 | [Title 20—EDUCATION](usc/title-20-education/) | no | 86 | 2029 | 87 | 119-102not101 |
| 21 | [Title 21—FOOD AND DRUGS](usc/title-21-food-and-drugs/) | no | 31 | 757 | 32 | 119-102not101 |
| 22 | [Title 22—FOREIGN RELATIONS AND INTERCOURSE](usc/title-22-foreign-relations-and-intercourse/) | no | 128 | 3485 | 129 | 119-102not101 |
| 23 | [Title 23—HIGHWAYS](usc/title-23-highways/) | yes | 6 | 172 | 7 | 119-102not101 |
| 24 | [Title 24—HOSPITALS AND ASYLUMS](usc/title-24-hospitals-and-asylums/) | no | 11 | 162 | 12 | 119-102not101 |
| 25 | [Title 25—INDIANS](usc/title-25-indians/) | no | 58 | 2400 | 59 | 119-102not101 |
| 26 | [Title 26—INTERNAL REVENUE CODE](usc/title-26-internal-revenue-code/) | no | 72 | 2161 | 99 | 119-102not101 |
| 27 | [Title 27—INTOXICATING LIQUORS](usc/title-27-intoxicating-liquors/) | no | 10 | 45 | 11 | 119-102not101 |
| 28 | [Title 28—JUDICIARY AND JUDICIAL PROCEDURE](usc/title-28-judiciary-and-judicial-procedure/) | yes | 79 | 806 | 80 | 119-102not101 |
| 28A | [Title 28—APPENDIX JUDICIAL PERSONNEL FINANCIAL DISCLOSURE REQUIREMENTS](usc/title-28a-appendix/) | no | 5 | 0 | 6 | 119-102not101 |
| 29 | [Title 29—LABOR](usc/title-29-labor/) | no | 36 | 844 | 37 | 119-102not101 |
| 30 | [Title 30—MINERAL LANDS AND MINING](usc/title-30-mineral-lands-and-mining/) | no | 34 | 626 | 35 | 119-102not101 |
| 31 | [Title 31—MONEY AND FINANCE](usc/title-31-money-and-finance/) | yes | 31 | 498 | 32 | 119-102not101 |
| 32 | [Title 32—NATIONAL GUARD](usc/title-32-national-guard/) | yes | 5 | 78 | 6 | 119-102not101 |
| 33 | [Title 33—NAVIGATION AND NAVIGABLE WATERS](usc/title-33-navigation-and-navigable-waters/) | no | 57 | 1569 | 58 | 119-102not101 |
| 34 | [Title 34—CRIME CONTROL AND LAW ENFORCEMENT](usc/title-34-crime-control-and-law-enforcement/) | no | 36 | 795 | 37 | 119-102not101 |
| 35 | [Title 35—PATENTS](usc/title-35-patents/) | yes | 25 | 175 | 26 | 119-102not101 |
| 36 | [Title 36—PATRIOTIC AND NATIONAL OBSERVANCES, CEREMONIES, AND ORGANIZATIONS](usc/title-36-patriotic-and-national-observances-ceremonies-and/) | yes | 132 | 1173 | 133 | 119-36 |
| 37 | [Title 37—PAY AND ALLOWANCES OF THE UNIFORMED SERVICES](usc/title-37-pay-and-allowances-of-the-uniformed-services/) | yes | 12 | 234 | 13 | 119-102not101 |
| 38 | [Title 38—VETERANS’ BENEFITS](usc/title-38-veterans-benefits/) | yes | 47 | 1198 | 48 | 119-102not101 |
| 39 | [Title 39—POSTAL SERVICE](usc/title-39-postal-service/) | yes | 22 | 181 | 23 | 119-102not101 |
| 40 | [Title 40—PUBLIC BUILDINGS, PROPERTY, AND WORKS](usc/title-40-public-buildings-property-and-works/) | yes | 45 | 459 | 46 | 119-102not101 |
| 41 | [Title 41—PUBLIC CONTRACTS](usc/title-41-public-contracts/) | yes | 27 | 241 | 28 | 119-102not101 |
| 42 | [Title 42—THE PUBLIC HEALTH AND WELFARE](usc/title-42-the-public-health-and-welfare/) | no | 195 | 8465 | 255 | 119-102not101 |
| 43 | [Title 43—PUBLIC LANDS](usc/title-43-public-lands/) | no | 59 | 1464 | 60 | 119-102not101 |
| 44 | [Title 44—PUBLIC PRINTING AND DOCUMENTS](usc/title-44-public-printing-and-documents/) | yes | 23 | 356 | 24 | 119-102not101 |
| 45 | [Title 45—RAILROADS](usc/title-45-railroads/) | no | 22 | 294 | 23 | 119-102not101 |
| 46 | [Title 46—SHIPPING](usc/title-46-shipping/) | yes | 108 | 1032 | 109 | 119-102not101 |
| 47 | [Title 47—TELECOMMUNICATIONS](usc/title-47-telecommunications/) | no | 16 | 432 | 17 | 119-102not101 |
| 48 | [Title 48—TERRITORIES AND INSULAR POSSESSIONS](usc/title-48-territories-and-insular-possessions/) | no | 21 | 661 | 22 | 119-102not101 |
| 49 | [Title 49—TRANSPORTATION](usc/title-49-transportation/) | yes | 114 | 1371 | 115 | 119-102not101 |
| 50 | [Title 50—WAR AND NATIONAL DEFENSE](usc/title-50-war-and-national-defense/) | no | 62 | 1425 | 63 | 119-59 |
| 50A | [Title 50—APPENDIX WAR AND NATIONAL DEFENSE [ELIMINATED] Current through 114–86u1](usc/title-50a-appendix/) | no | 0 | 0 | 1 | 119-102not101 |
| 51 | [Title 51—NATIONAL AND COMMERCIAL SPACE PROGRAMS](usc/title-51-national-and-commercial-space-programs/) | yes | 35 | 249 | 36 | 119-102not101 |
| 52 | [Title 52—VOTING AND ELECTIONS](usc/title-52-voting-and-elections/) | no | 10 | 171 | 11 | 119-102not101 |
| 54 | [Title 54—NATIONAL PARK SERVICE AND RELATED PROGRAMS](usc/title-54-national-park-service-and-related-programs/) | yes | 56 | 366 | 57 | 119-102not101 |

### Code of Federal Regulations titles

| Title | Heading | Parts | Sections | Files | Last amended |
|---|---|---|---|---|---|
| 1 | [Title 1—General Provisions](cfr/title-01-general-provisions/) | 28 | 288 | 29 | 2022-12-29 |
| 2 | [Title 2—Federal Financial Assistance](cfr/title-02-federal-financial-assistance/) | 107 | 1522 | 108 | 2026-08-17 |
| 3 | [Title 3—The President](cfr/title-03-the-president/) | 3 | 27 | 4 | 2015-03-17 |
| 4 | [Title 4—Accounts](cfr/title-04-accounts/) | 18 | 222 | 19 | 2024-07-18 |
| 5 | [Title 5—Administrative Personnel](cfr/title-05-administrative-personnel/) | 286 | 5383 | 287 | 2026-10-05 |
| 6 | [Title 6—Domestic Security](cfr/title-06-domestic-security/) | 24 | 584 | 25 | 2026-07-06 |
| 7 | [Title 7—Agriculture](cfr/title-07-agriculture/) | 440 | 17174 | 441 | 2026-10-08 |
| 8 | [Title 8—Aliens and Nationality](cfr/title-08-aliens-and-nationality/) | 126 | 985 | 127 | 2026-10-01 |
| 9 | [Title 9—Animals and Animal Products](cfr/title-09-animals-and-animal-products/) | 145 | 2440 | 146 | 2026-07-20 |
| 10 | [Title 10—Energy](cfr/title-10-energy/) | 176 | 5239 | 177 | 2026-10-07 |
| 11 | [Title 11—Federal Elections](cfr/title-11-federal-elections/) | 53 | 587 | 54 | 2025-02-20 |
| 12 | [Title 12—Banks and Banking](cfr/title-12-banks-and-banking/) | 396 | 7199 | 397 | 2026-10-02 |
| 13 | [Title 13—Business Credit and Assistance](cfr/title-13-business-credit-and-assistance/) | 47 | 1707 | 48 | 2026-09-29 |
| 14 | [Title 14—Aeronautics and Space](cfr/title-14-aeronautics-and-space/) | 198 | 6363 | 199 | 2026-09-29 |
| 15 | [Title 15—Commerce and Foreign Trade](cfr/title-15-commerce-and-foreign-trade/) | 138 | 2237 | 139 | 2026-09-24 |
| 16 | [Title 16—Commercial Practices](cfr/title-16-commercial-practices/) | 220 | 2136 | 221 | 2026-10-01 |
| 17 | [Title 17—Commodity and Securities Exchanges](cfr/title-17-commodity-and-securities-exchanges/) | 121 | 3528 | 122 | 2026-10-08 |
| 18 | [Title 18—Conservation of Power and Water Resources](cfr/title-18-conservation-of-power-and-water-resources/) | 124 | 2048 | 125 | 2026-08-24 |
| 19 | [Title 19—Customs Duties](cfr/title-19-customs-duties/) | 76 | 3172 | 77 | 2026-08-26 |
| 20 | [Title 20—Employees' Benefits](cfr/title-20-employees-benefits/) | 146 | 5634 | 147 | 2026-09-30 |
| 21 | [Title 21—Food and Drugs](cfr/title-21-food-and-drugs/) | 263 | 8421 | 264 | 2026-10-06 |
| 22 | [Title 22—Foreign Relations](cfr/title-22-foreign-relations/) | 215 | 3408 | 216 | 2026-10-01 |
| 23 | [Title 23—Highways](cfr/title-23-highways/) | 64 | 987 | 65 | 2026-09-23 |
| 24 | [Title 24—Housing and Urban Development](cfr/title-24-housing-and-urban-development/) | 152 | 4877 | 153 | 2026-08-20 |
| 25 | [Title 25—Indians](cfr/title-25-indians/) | 154 | 4747 | 155 | 2025-12-01 |
| 26 | [Title 26—Internal Revenue](cfr/title-26-internal-revenue/) | 83 | 6163 | 84 | 2026-10-06 |
| 27 | [Title 27—Alcohol, Tobacco Products and Firearms](cfr/title-27-alcohol-tobacco-products-and-firearms/) | 42 | 3952 | 43 | 2026-09-25 |
| 28 | [Title 28—Judicial Administration](cfr/title-28-judicial-administration/) | 148 | 3080 | 149 | 2026-09-30 |
| 29 | [Title 29—Labor](cfr/title-29-labor/) | 290 | 7259 | 291 | 2026-10-06 |
| 30 | [Title 30—Mineral Resources](cfr/title-30-mineral-resources/) | 206 | 5954 | 207 | 2026-09-24 |
| 31 | [Title 31—Money and Finance: Treasury](cfr/title-31-money-and-finance-treasury/) | 188 | 5398 | 189 | 2026-10-06 |
| 32 | [Title 32—National Defense](cfr/title-32-national-defense/) | 230 | 3640 | 231 | 2026-08-17 |
| 33 | [Title 33—Navigation and Navigable Waters](cfr/title-33-navigation-and-navigable-waters/) | 140 | 4652 | 141 | 2026-10-07 |
| 34 | [Title 34—Education](cfr/title-34-education/) | 108 | 3259 | 109 | 2026-10-08 |
| 36 | [Title 36—Parks, Forests, and Public Property](cfr/title-36-parks-forests-and-public-property/) | 164 | 3120 | 165 | 2026-10-07 |
| 37 | [Title 37—Patents, Trademarks, and Copyrights](cfr/title-37-patents-trademarks-and-copyrights/) | 63 | 1331 | 64 | 2026-08-26 |
| 38 | [Title 38—Pensions, Bonuses, and Veterans' Relief](cfr/title-38-pensions-bonuses-and-veterans-relief/) | 54 | 2953 | 55 | 2026-08-27 |
| 39 | [Title 39—Postal Service](cfr/title-39-postal-service/) | 99 | 1129 | 100 | 2026-09-25 |
| 40 | [Title 40—Protection of Environment](cfr/title-40-protection-of-environment/) | 363 | 24651 | 364 | 2026-10-02 |
| 41 | [Title 41—Public Contracts and Property Management](cfr/title-41-public-contracts-and-property-management/) | 174 | 3085 | 175 | 2026-09-22 |
| 42 | [Title 42—Public Health](cfr/title-42-public-health/) | 152 | 7312 | 153 | 2026-10-08 |
| 43 | [Title 43—Public Lands: Interior](cfr/title-43-public-lands-interior/) | 178 | 5436 | 179 | 2026-08-12 |
| 44 | [Title 44—Emergency Management and Assistance](cfr/title-44-emergency-management-and-assistance/) | 64 | 943 | 65 | 2026-06-22 |
| 45 | [Title 45—Public Welfare](cfr/title-45-public-welfare/) | 309 | 5694 | 310 | 2026-10-06 |
| 46 | [Title 46—Shipping](cfr/title-46-shipping/) | 210 | 8430 | 211 | 2026-09-25 |
| 47 | [Title 47—Telecommunication](cfr/title-47-telecommunication/) | 66 | 5165 | 67 | 2026-10-06 |
| 48 | [Title 48—Federal Acquisition Regulations System](cfr/title-48-federal-acquisition-regulations-system/) | 836 | 11544 | 837 | 2026-10-01 |
| 49 | [Title 49—Transportation](cfr/title-49-transportation/) | 371 | 9004 | 372 | 2026-10-05 |
| 50 | [Title 50—Wildlife and Fisheries](cfr/title-50-wildlife-and-fisheries/) | 93 | 3217 | 94 | 2026-10-06 |

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
