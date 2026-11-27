#!/usr/bin/env python3
"""Who funds materials work done on an Opentrons robot, and how crowded each area is.

Writes grants/ot2-new-directions/ot2_funders.md. Papers come from Europe PMC,
which searches the full text of open-access articles, so it finds papers that
name the robot only in their methods. Each application area adds a title or
abstract search to "opentrons". Funders come from each paper's Crossref record.
Europe PMC holds mostly open-access, life-science-indexed journals (Nat. Commun.,
Sci. Adv., ACS and RSC open access) and publishers deposit funders unevenly, so
every count is a floor.

OpenAlex would cover more journals, but its free API budget is shared per IP
address and was used up on the GitHub runner; this needs no key.

Usage:
    python scripts/funding/ot2_funders.py
"""
from __future__ import annotations

import json
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from datetime import date
from pathlib import Path

OUT = Path(__file__).resolve().parents[2] / "grants" / "ot2-new-directions" / "ot2_funders.md"
EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
CROSSREF = "https://api.crossref.org/works/"
MAILTO = "vertical-cloud-lab@users.noreply.github.com"

AREAS = {
    "Self-driving, autonomous or closed-loop materials work": ["self-driving", "autonomous", "closed-loop", "Bayesian optimization"],
    "Nanoparticles, nanocrystals and quantum dots": ["nanoparticle", "nanoparticles", "nanocrystals", "quantum dots"],
    "Metal-halide perovskites": ["perovskite", "perovskites"],
    "Polymers and hydrogels": ["polymer", "polymers", "hydrogel", "hydrogels"],
    "Oxides, co-precipitation and high-entropy materials": ["oxide", "oxides", "coprecipitation", "co-precipitation", "high-entropy"],
    "Electrochemistry, electrodeposition and electrocatalysis": ["electrochemical", "electrochemistry", "electrodeposition", "electrocatalyst", "electrocatalysis"],
    "Batteries and electrolytes": ["battery", "batteries", "cathode", "electrolyte"],
    "Crystallization, precipitation and nucleation": ["crystallization", "nucleation", "precipitation", "crystals"],
    "Metal-organic frameworks and porous materials": ["metal-organic framework", "metal-organic frameworks", "zeolitic", "porous"],
    "Separations, sorbents and critical metals": ["solvent extraction", "adsorption", "sorbent", "lithium", "rare earth"],
    "Corrosion and coatings": ["corrosion", "coating", "coatings"],
}


def fetch(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": f"digital-wetlab funding scan (mailto:{MAILTO})"})
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return {}
            if attempt == 4:
                raise
        except urllib.error.URLError:
            if attempt == 4:
                raise
        time.sleep(2 ** attempt)
    return {}


# Clinical and omics papers that match an area's words by accident
EXCLUDE = ["patients", "clinical", "proteomics", "microbiome", "gut", "plasma", "allergen", "bacteriophage",
           "bacteriocin", "immunoassay", "sequencing", "biodegradation"]


def search(terms: list[str]) -> list[dict]:
    fields = " OR ".join(f'ABSTRACT:"{t}" OR TITLE:"{t}"' for t in terms)
    noise = " OR ".join(f'ABSTRACT:"{t}" OR TITLE:"{t}"' for t in EXCLUDE)
    query = f"opentrons AND PUB_YEAR:[2018 TO 2026] AND ({fields}) NOT ({noise})"
    papers, cursor = [], "*"
    while True:
        params = {"query": query, "format": "json", "pageSize": 1000, "resultType": "lite", "cursorMark": cursor}
        data = fetch(EPMC + "?" + urllib.parse.urlencode(params))
        papers += data.get("resultList", {}).get("result", [])
        nxt = data.get("nextCursorMark")
        if not nxt or nxt == cursor or len(papers) >= data.get("hitCount", 0):
            return papers
        cursor = nxt


_funders: dict[str, list[str]] = {}


def funders(doi: str) -> list[str]:
    if doi not in _funders:
        msg = fetch(CROSSREF + urllib.parse.quote(doi) + f"?mailto={MAILTO}").get("message", {})
        _funders[doi] = sorted({f["name"].replace("|", "/") for f in msg.get("funder", []) if f.get("name")})
        time.sleep(0.05)
    return _funders[doi]


def main() -> None:
    summary, sections = [], []
    every_paper: dict[str, dict] = {}
    for label, terms in AREAS.items():
        papers = [p for p in search(terms) if p.get("doi")]
        for p in papers:
            every_paper[p["doi"].lower()] = p
        counts = Counter(name for p in papers for name in funders(p["doi"]))
        with_funder = sum(1 for p in papers if funders(p["doi"]))
        recent = sum(1 for p in papers if int(p.get("pubYear", 0)) >= 2024)
        summary.append(f"| {label} | {len(papers)} | {recent} | {with_funder} |")
        sections += [f"## {label}", "", f"Title/abstract terms: {', '.join(terms)}. "
                     f"{len(papers)} papers, {recent} of them from 2024–2026; {with_funder} have funders on Crossref.", ""]
        sections += ["| Papers | Funder |", "|---:|---|"]
        sections += [f"| {c} | {name} |" for name, c in counts.most_common(10)] or ["| 0 | none recorded |"]
        sections += ["", "Most recent:", ""]
        for p in sorted(papers, key=lambda p: p.get("pubYear", ""), reverse=True)[:6]:
            sections.append(f"- {p.get('pubYear')}: {p.get('title', '').rstrip('.')}. "
                            f"*{p.get('journalTitle') or 'preprint'}* ([{p['doi']}](https://doi.org/{p['doi']}))")
        sections.append("")

    overall = Counter(name for doi in every_paper for name in funders(every_paper[doi]["doi"]))
    lines = [
        "# Opentrons in materials research: who funds it and how crowded each area is",
        "",
        f"Generated {date.today().isoformat()} by "
        "[`scripts/funding/ot2_funders.py`](../../scripts/funding/ot2_funders.py).",
        "",
        "Papers are 2018–2026 Europe PMC records whose full text mentions \"opentrons\" and whose title or",
        "abstract has the area's terms (clinical and omics papers are filtered out by keyword); funders",
        "are from each paper's Crossref record. Europe PMC holds mostly open-access journals and",
        "publishers deposit funders unevenly, so every count is a floor, and a paper can sit in several",
        "areas. A full-text hit means the paper mentions the robot, not that the robot made the material:",
        "the checked list is the table in",
        "[`README.md`](README.md#what-others-have-done-with-an-ot-2).",
        "",
        "| Area | Papers | 2024–2026 | With funders on Crossref |",
        "|---|---:|---:|---:|",
        *summary,
        "",
        f"## All areas together ({len(every_paper)} distinct papers)",
        "",
        "| Papers | Funder |",
        "|---:|---|",
        *[f"| {c} | {name} |" for name, c in overall.most_common(25)],
        "",
        *sections,
    ]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines))
    print("wrote", OUT, "with", len(every_paper), "papers")


if __name__ == "__main__":
    main()
