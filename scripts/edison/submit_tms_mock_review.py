#!/usr/bin/env python3
"""Submit an Edison ANALYSIS task requesting mock reviewer feedback on the
TMS 2027 poster abstract (v2) targeted at "From Mine to Refinery: An EPD
Symposium Honoring Shijie Wang".

Uploads a small bundle (draft title/abstract with project context, plus the
symposium's full call-for-abstracts scope text) and writes a SUBMITTED
placeholder with the task id so fetching is resumable across sessions.

Usage:
    EDISON_PLATFORM_API_KEY=... python scripts/edison/submit_tms_mock_review.py
"""
from __future__ import annotations

import json
import os
from pathlib import Path

from edison_client import EdisonClient, JobNames, TaskRequest

HERE = Path(__file__).resolve().parents[2]
TRAJ = HERE / "edison-trajectories" / "tms-mock-review"
BUNDLE = TRAJ / "bundle"
SUBMITTED = TRAJ / "tms-mock-review-SUBMITTED.json"

QUERY = """\
Act as a mock review panel for a TMS 2027 poster abstract. The attached bundle
contains:

  - abstract.md: the draft poster title and 143-word abstract, "Closed-Loop
    Mapping of Iron and Lead Sulfide Precipitation in Concentrated Brines
    Using a Low-Cost Autonomous Digital Wet Lab," plus project context
    (an Opentrons-based autonomous wet lab measuring missing Pitzer
    parameters for Fe2+-HS-, Pb2+-HS-, and metal-organic-acid interactions
    to predict FeS/PbS solubility in concentrated brines; ~30,000-experiment
    campaign with Latin hypercube sampling plus active learning; results
    compared against PHREEQC Pitzer predictions). Note the stage of the work:
    at poster time (March 2027) the platform and early campaign results are
    expected, but the full parameter set is a deliverable, not a completed
    result.

  - symposium-scope.md: the full ProgramMaster call-for-abstracts text of the
    target symposium, "From Mine to Refinery: An EPD Symposium Honoring
    Shijie Wang" (TMS Extraction and Processing Division; Hydrometallurgy and
    Electrometallurgy Committee; Pyrometallurgy Committee; organizers Michael
    Moats, Ramana Reddy, Michael Free, Corby Anderson).

Your task: provide MOCK REVIEWER FEEDBACK on the title and abstract as if
reviewing/programming this poster submission for this specific symposium.

1. THREE REVIEWER PERSONAS, each with a short written review and a 1-10
   score for (a) fit to this symposium's scope, (b) technical quality of the
   abstract, and (c) likely audience interest at this symposium:
   - Reviewer A: an industrial hydrometallurgist (smelter/refinery or
     mining-company background, the community this symposium honors);
   - Reviewer B: an academic extractive-metallurgy professor close to the
     organizers' interests (leaching, solution chemistry, electrochemical
     processing, automated experiments);
   - Reviewer C: a methods-skeptical thermodynamics/modeling reviewer
     (Pitzer/PHREEQC expert) alert to overclaiming and to whether the
     experimental design can actually yield reliable parameters.

2. SPECIFIC LINE EDITS. Concrete wording changes to the TITLE and ABSTRACT
   that would raise acceptance likelihood at THIS symposium, keeping the body
   at or under 150 words. Flag: does the petroleum/oilfield-scale framing
   help or hurt for this extractive-metallurgy audience, and how much of it
   should remain? Should the hydrometallurgy relevance (impurity control,
   metal recovery, process-water chemistry) be made more concrete, and how,
   without overclaiming applications we have not demonstrated?

3. RED FLAGS. Anything a TMS organizer might ding: proposal-stage work
   presented as results, the robot upstaging the chemistry, missing
   temperature-control credibility for 25-90 C on a liquid handler, scope
   drift from the symposium's technical focus areas, jargon (SDL,
   "digital wet lab") unfamiliar to this audience.

4. REVISED VERSION. Provide your single best revised title and revised
   abstract (<=150 words, plain text) implementing your own feedback.

5. BOTTOM LINE. Accept/revise/reject verdict for this symposium as a poster,
   one sentence on the single highest-impact change, and whether any of these
   backups would score meaningfully better for this abstract: Rare Metal
   Extraction & Processing; AI-Enabled Materials Processing; Advances in
   Recycling and Environmental Technologies.
"""


def main() -> None:
    api_key = (os.environ.get("EDISON_PLATFORM_API_KEY") or os.environ.get("EDISON_API_KEY") or "").strip()
    if not api_key:
        raise SystemExit("No EDISON_PLATFORM_API_KEY / EDISON_API_KEY in environment")

    client = EdisonClient(api_key=api_key)

    resp = client.store_file_content(name="tms-mock-review-bundle", file_path=str(BUNDLE), as_collection=True)
    uri = f"data_entry:{resp.data_storage.id}"
    print("uploaded bundle:", uri)

    task = TaskRequest(name=JobNames.ANALYSIS, query=QUERY)
    task_id = client.create_task(task, files=[uri])
    task_id = str(task_id)
    print("submitted ANALYSIS task:", task_id)

    TRAJ.mkdir(parents=True, exist_ok=True)
    SUBMITTED.write_text(json.dumps({"task_id": task_id, "bundle_uri": uri}, indent=2))
    print("wrote", SUBMITTED)


if __name__ == "__main__":
    main()
