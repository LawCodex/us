#!/usr/bin/env python3
"""Download the United States Code (USLM XML) into the raw cache.

Strategy:
1. Official: parse https://uscode.house.gov/download/download.shtml for the current release
   point and download each per-title XML zip (xml_uscNN@<rp>.zip).
2. Fallback (when uscode.house.gov is unavailable): use byte-identical copies of the official
   OLRC zips archived by the Internet Archive Wayback Machine. For each title the newest
   release point with an intact (valid zip) capture is used.

Output: <raw>/xml/uscNN.xml plus <raw>/manifest.json recording, per title, the release point
and URL actually used.

Usage: python fetch.py [--raw DIR] [--no-official] [--no-wayback]
"""
import argparse
import io
import json
import os
import re
import sys
import time
import zipfile

import requests

UA = "LawCodex/1.0 (+https://github.com/LawCodex)"
BASE = "https://uscode.house.gov/download/"
DL_PAGE = BASE + "download.shtml"
CDX = "https://web.archive.org/cdx/search/cdx"
DEFAULT_RAW = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "_raw", "us")

# 54 titles (53 is reserved and empty) plus the appendices published by the OLRC.
TITLES = [f"{n:02d}" for n in range(1, 55)] + ["05a", "11a", "18a", "28a", "50a"]

S = requests.Session()
S.headers["User-Agent"] = UA


def get(url, timeout=600, tries=5, stream=False):
    last = None
    for i in range(tries):
        try:
            r = S.get(url, timeout=timeout)
            if r.status_code == 200:
                return r
            last = f"HTTP {r.status_code}"
            if r.status_code in (404, 410):
                break
        except requests.RequestException as e:  # network / truncated
            last = str(e)
        time.sleep(min(60, 5 * 2 ** i))
    raise RuntimeError(f"{url}: {last}")


def valid_zip(data):
    try:
        z = zipfile.ZipFile(io.BytesIO(data))
        return z.testzip() is None and z
    except zipfile.BadZipFile:
        return None


def save_title(raw, t, data, meta, manifest):
    z = valid_zip(data)
    if not z:
        return False
    names = [n for n in z.namelist() if n.lower().endswith(".xml")]
    if not names:
        return False
    os.makedirs(os.path.join(raw, "xml"), exist_ok=True)
    with open(os.path.join(raw, "xml", f"usc{t}.xml"), "wb") as f:
        f.write(z.read(names[0]))
    manifest[t] = meta
    return True


def official(raw, manifest):
    try:
        page = get(DL_PAGE, timeout=60, tries=2).text
    except RuntimeError as e:
        print("official site unavailable:", e, file=sys.stderr)
        return False
    m = re.search(r'releasepoints/us/pl/(\d+)/([\w]+)/xml_uscAll@([\w-]+)\.zip', page)
    if not m:
        print("official site: no release point found (maintenance page?)", file=sys.stderr)
        return False
    cong, num, rp = m.groups()
    cur = re.search(r"Public Law (\d+-\d+) \((\d\d)/(\d\d)/(\d{4})\)", page)
    for t in TITLES:
        if t in manifest and manifest[t].get("release_point") == rp:
            continue
        url = f"{BASE}releasepoints/us/pl/{cong}/{num}/xml_usc{t}@{rp}.zip"
        try:
            data = get(url).content
        except RuntimeError as e:
            print("  ", t, e, file=sys.stderr)
            continue
        meta = {"release_point": rp, "url": url, "via": "official"}
        if cur:
            meta["current_through"] = f"Public Law {cur.group(1)} ({cur.group(4)}-{cur.group(2)}-{cur.group(3)})"
        if save_title(raw, t, data, meta, manifest):
            print("official", t, rp)
        time.sleep(1)
    return True


def rp_key(rp):
    # "119-102not101" < "119-102"; sort by congress, law number, then full over partial
    m = re.match(r"(\d+)-(\d+)(.*)", rp)
    return (int(m.group(1)), int(m.group(2)), 0 if m.group(3) else 1)


def wayback(raw, manifest):
    rows = get(CDX + "?url=uscode.house.gov/download/releasepoints/us/pl/&matchType=prefix"
               "&output=json&fl=timestamp,original&filter=statuscode:200", timeout=600).json()[1:]
    cands = {}
    for ts, url in rows:
        m = re.search(r"/xml_usc(\w+)@([\w-]+)\.zip$", url)
        if not m:
            continue
        t, rp = m.group(1).lower(), m.group(2)
        if t == "all":
            continue
        cands.setdefault(t, []).append((rp_key(rp), ts, rp, url))
    for t in TITLES:
        if t in manifest:
            continue
        for _, ts, rp, url in sorted(cands.get(t, []), reverse=True):
            wb = f"https://web.archive.org/web/{ts}id_/{url}"
            try:
                data = get(wb, tries=3).content
            except RuntimeError as e:
                print("  ", t, e, file=sys.stderr)
                continue
            meta = {"release_point": rp, "url": url, "via": "wayback", "wayback": wb}
            if save_title(raw, t, data, meta, manifest):
                print("wayback", t, rp)
                break
            print("  ", t, rp, "corrupt capture, trying older", file=sys.stderr)
            time.sleep(2)
        else:
            print("MISSING", t, file=sys.stderr)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw", default=DEFAULT_RAW)
    ap.add_argument("--no-official", action="store_true")
    ap.add_argument("--no-wayback", action="store_true")
    a = ap.parse_args()
    raw = os.path.abspath(a.raw)
    os.makedirs(raw, exist_ok=True)
    mpath = os.path.join(raw, "manifest.json")
    manifest = json.load(open(mpath)) if os.path.exists(mpath) else {}
    # keep cached files only if they still exist
    manifest = {k: v for k, v in manifest.items()
                if os.path.exists(os.path.join(raw, "xml", f"usc{k}.xml"))}
    try:
        if not a.no_official:
            official(raw, manifest)
        if not a.no_wayback:
            wayback(raw, manifest)
    finally:
        json.dump(manifest, open(mpath, "w"), indent=1, sort_keys=True)
    print(len(manifest), "titles in", raw)


if __name__ == "__main__":
    main()
