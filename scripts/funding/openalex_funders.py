#!/usr/bin/env python3
"""Count who funds the Pitzer / PHREEQC / mineral-scale literature, from OpenAlex.

Writes grants/alternative-funding/openalex_funders.md: the funders most often
acknowledged by papers on each topic, and by the groups whose databases the
proposal builds on. OpenAlex takes funders from Crossref and full-text
acknowledgments, so counts are a floor, not a census.

Usage:
    python scripts/funding/openalex_funders.py
"""
from __future__ import annotations

import json
import time
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path

OUT = Path(__file__).resolve().parents[2] / "grants" / "alternative-funding" / "openalex_funders.md"
API = "https://api.openalex.org"

TOPICS = {
    "Pitzer, US institutions, 2015-2026": "title_and_abstract.search:pitzer,publication_year:2015-2026,institutions.country_code:US",
    "PHREEQC, US institutions, 2018-2026": "title_and_abstract.search:phreeqc,publication_year:2018-2026,institutions.country_code:US",
    "Mineral scale in brines, US institutions, 2015-2026": "title_and_abstract.search:mineral scale brine,publication_year:2015-2026,institutions.country_code:US",
    "Pitzer + scale + brine, any country, 2010-2026": "title_and_abstract.search:pitzer scale brine,publication_year:2010-2026",
    "Sulfide solubility in brines, any country, 2010-2026": "title_and_abstract.search:sulfide solubility brine,publication_year:2010-2026",
}

# OpenAlex author IDs for the groups behind the databases the proposal cites
GROUPS = {
    "Amy T. Kan, Rice (Brine Chemistry Consortium, ScaleSoftPitzer)": "A5054823108",
    "Yongliang Xiong, Sandia (WIPP Pitzer database)": "A5032982214",
    "Eric J. Mackay, Heriot-Watt (FAST scale modelling)": "A5086899206",
}


def get(path: str, params: dict) -> dict:
    url = f"{API}/{path}?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": "digital-wetlab funding scan"})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = json.load(r)
    time.sleep(0.2)
    return data


def funder_table(flt: str, n: int = 12) -> tuple[int, list[tuple[int, str]]]:
    total = get("works", {"filter": flt, "per_page": 1})["meta"]["count"]
    groups = get("works", {"filter": flt, "group_by": "funders.id", "per_page": 50})["group_by"]
    return total, [(g["count"], g["key_display_name"]) for g in groups[:n]]


def main() -> None:
    lines = [
        "# Who funds this niche: OpenAlex funding acknowledgments",
        "",
        f"Generated {date.today().isoformat()} by [`scripts/funding/openalex_funders.py`](../../scripts/funding/openalex_funders.py).",
        "Counts are papers that acknowledge each funder. OpenAlex misses many acknowledgments, so treat",
        "the counts as a floor.",
        "",
    ]
    for label, flt in TOPICS.items():
        total, rows = funder_table(flt)
        lines += [f"## {label} ({total} papers)", "", "| Papers | Funder |", "|---:|---|"]
        lines += [f"| {c} | {name} |" for c, name in rows]
        lines.append("")
    for label, aid in GROUPS.items():
        flt = f"authorships.author.id:{aid},publication_year:2016-2026"
        total, rows = funder_table(flt)
        lines += [f"## {label}: {total} papers, 2016-2026", "", "| Papers | Funder |", "|---:|---|"]
        lines += [f"| {c} | {name} |" for c, name in rows]
        lines.append("")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines))
    print("wrote", OUT)


if __name__ == "__main__":
    main()
