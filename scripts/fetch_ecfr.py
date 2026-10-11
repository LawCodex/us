#!/usr/bin/env python3
"""Download the Electronic Code of Federal Regulations (eCFR) bulk XML from GovInfo.

Source: https://www.govinfo.gov/bulkdata/ECFR (one XML file per title, updated daily).
Output: <raw>/ecfr/ECFR-titleN.xml and <raw>/ecfr/manifest.json (lastModified per title).

Usage: python fetch_ecfr.py [--raw DIR] [--titles 1,2,...]
"""
import argparse
import json
import os
import time

import requests

UA = "LawCodex/1.0 (+https://github.com/LawCodex)"
BULK = "https://www.govinfo.gov/bulkdata/json/ECFR"
HERE = os.path.dirname(os.path.abspath(__file__))

S = requests.Session()
S.headers["User-Agent"] = UA


def get(url, **kw):
    for i in range(5):
        try:
            r = S.get(url, timeout=900, **kw)
            if r.status_code == 200:
                return r
            if r.status_code == 404:
                return None
        except requests.RequestException:
            pass
        time.sleep(5 * 2 ** i)
    raise RuntimeError(url)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw", default=os.path.join(HERE, "..", "..", "_raw", "us"))
    ap.add_argument("--titles", default=",".join(str(i) for i in range(1, 51)))
    a = ap.parse_args()
    d = os.path.join(os.path.abspath(a.raw), "ecfr")
    os.makedirs(d, exist_ok=True)
    mpath = os.path.join(d, "manifest.json")
    manifest = json.load(open(mpath)) if os.path.exists(mpath) else {}
    for t in a.titles.split(","):
        r = get(f"{BULK}/title-{t}", headers={"Accept": "application/json"})
        if r is None:
            print("no title", t)
            continue
        files = [f for f in r.json().get("files", []) if f["name"].endswith(".xml")]
        for f in files:
            path = os.path.join(d, f["name"])
            stamp = f.get("formattedLastModifiedTime")
            if os.path.exists(path) and manifest.get(t, {}).get("modified") == stamp:
                continue
            x = get(f["link"], stream=True)
            with open(path + ".part", "wb") as out:
                for chunk in x.iter_content(1 << 20):
                    out.write(chunk)
            os.replace(path + ".part", path)
            manifest[t] = {"file": f["name"], "modified": stamp, "url": f["link"]}
            json.dump(manifest, open(mpath, "w"), indent=1, sort_keys=True)
            print(t, f["name"], stamp, flush=True)
        time.sleep(1)


if __name__ == "__main__":
    main()
