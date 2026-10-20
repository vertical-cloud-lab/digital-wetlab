#!/usr/bin/env python3
"""Submit round 2 of the Edison ANALYSIS mock review for the TMS 2027
abstract (v3), this time with reviewer personas modeled on the four actual
symposium organizers and judged against the full symposium flyer content.
Also asks whether to request an oral (talk) slot instead of a poster.

Uploads the round-2 bundle (v3 title/abstract + full flyer text + researched
organizer profiles) and writes a SUBMITTED placeholder with the task id so
fetching is resumable across sessions.

Usage:
    EDISON_PLATFORM_API_KEY=... python scripts/edison/submit_tms_mock_review_round2.py
"""
from __future__ import annotations

import json
import os
from pathlib import Path

from edison_client import EdisonClient, JobNames, TaskRequest

HERE = Path(__file__).resolve().parents[2]
TRAJ = HERE / "edison-trajectories" / "tms-mock-review-round2"
BUNDLE = TRAJ / "bundle"
SUBMITTED = TRAJ / "tms-mock-review-round2-SUBMITTED.json"

QUERY = """\
Act as a mock review panel for a TMS 2027 abstract submission. This is ROUND 2
of review; round-1 feedback has already been implemented. The attached bundle
contains:

  - abstract-v3.md: the current (v3) title and 129-word abstract, project
    context, and a list of the round-1 changes already implemented. Do not
    re-litigate round 1; build on it.
  - symposium-flyer.md: the FULL flyer / call-for-abstracts content of the
    target symposium, "From Mine to Refinery: An EPD Symposium Honoring
    Shijie Wang" (verbatim ProgramMaster text: honoree biography, scope,
    technical focus areas, proceedings and manuscript policy).
  - organizer-profiles.md: researched profiles of the four actual symposium
    organizers (Michael S. Moats, Ramana G. Reddy, Michael L. Free,
    Corby G. Anderson) and the honoree community context.

Your task, in five parts:

1. ORGANIZER-PERSONA REVIEWS. Four mock reviews, one per organizer, each
   modeled on that specific person's documented research emphases, industrial
   ties, and likely programming priorities (per organizer-profiles.md — do
   not invent biographical facts beyond that file plus well-established
   public knowledge). For each: a short written review of the v3 title and
   abstract AGAINST THE FULL FLYER (scope paragraphs AND the seven listed
   Technical Focus Areas), plus 1-10 scores for (a) fit to this symposium as
   programmed, (b) technical quality, (c) likely audience interest. Note
   explicitly: which Technical Focus Area, if any, would each organizer file
   this under, and does the mismatch (FeS/PbS solution chemistry vs. the
   listed recovery/refining focus areas) matter to them?

2. TALK VS. POSTER. The submission is currently planned as a Poster. TMS
   allows requesting an oral presentation instead, but (per the flyer)
   authors seeking an oral slot MUST submit a manuscript for the stand-alone
   proceedings book, and oral requests may be assigned as posters anyway if
   the program is full. As these four organizers programming this honorary
   symposium: (a) would this abstract plausibly earn an oral slot, or is it a
   clear poster? (b) Do the pros of requesting a talk (visibility, priority)
   outweigh the cons (proceedings manuscript obligation by the manuscript
   deadline, proposal-stage results by March 2027, risk of weak fit in an
   oral session honoring an industrial refining career)? (c) Give a clear
   recommendation: request "Oral" or "Poster", with one sentence of
   reasoning, and note anything the authors should do differently in the
   abstract if they request an oral slot.

3. SPECIFIC LINE EDITS. Concrete wording changes to the v3 TITLE and
   ABSTRACT (keep <=150 words) that would raise acceptance likelihood with
   THESE FOUR organizers specifically — e.g., terms from the flyer's own
   vocabulary (impurity control/management, process-water chemistry, metal
   recovery, solution chemistry, thermodynamic modeling, AI), and whether to
   name a Technical Focus Area connection (e.g., Pb processing, impurity
   management) explicitly. Flag anything in v3 that any one of the four
   would specifically dislike.

4. REVISED VERSION. Your single best revised title and abstract (<=150
   words, plain text) implementing your own round-2 feedback. If you
   recommend requesting an oral slot, make this version the oral-ready one.

5. BOTTOM LINE. One-paragraph verdict: how the four-organizer panel would
   likely program this submission (oral / poster / reject), the single
   highest-impact remaining change, and any red flags an organizer panel
   (as opposed to anonymous reviewers) would uniquely care about.
"""


def main() -> None:
    api_key = (os.environ.get("EDISON_PLATFORM_API_KEY") or os.environ.get("EDISON_API_KEY") or "").strip()
    if not api_key:
        raise SystemExit("No EDISON_PLATFORM_API_KEY / EDISON_API_KEY in environment")

    client = EdisonClient(api_key=api_key)

    resp = client.store_file_content(name="tms-mock-review-round2-bundle", file_path=str(BUNDLE), as_collection=True)
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
