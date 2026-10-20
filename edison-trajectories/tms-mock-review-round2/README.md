# Edison mock review, round 2 — organizer-persona panel + full flyer + talk-vs-poster

Round-2 Edison ANALYSIS task for the TMS 2027 abstract (v3), requested in
[digital-wetlab-private PR 60](https://github.com/vertical-cloud-lab/digital-wetlab-private/pull/60).
Differences from round 1 (`../tms-mock-review/`):

- Reviewer personas are modeled on the **four actual symposium organizers** (Moats, Reddy, Free, Anderson),
  using researched public profiles in `bundle/organizer-profiles.md`.
- The abstract is judged against the **full flyer / ProgramMaster call content** (`bundle/symposium-flyer.md`),
  including the honoree biography and the seven Technical Focus Areas.
- Adds an explicit **talk (oral) vs. poster** recommendation question, including the oral-slot proceedings
  manuscript obligation and the chance an oral request is assigned as a poster anyway.

Contents:

- `bundle/` — exact files uploaded to Edison (v3 abstract + context, full flyer text, organizer profiles)
- `tms-mock-review-round2-SUBMITTED.json` — task id + uploaded bundle URI
- `tms-mock-review-round2-<task_id>.md` / `.json` — fetched answer and full task dump (task
  `a15d214b-ee8b-4aed-aea6-818876128c6a`, status **success**; no notebook figures were produced)

**Outcome:** the organizer panel would likely program the work as a **poster** (request Poster, not oral — the
oral proceedings-manuscript obligation is not worth it at proposal stage). The panel's revised title and
abstract were adopted as v4 in `drafts/tms2027_poster_materials.md`.

Scripts: `scripts/edison/submit_tms_mock_review_round2.py`, `scripts/edison/fetch_tms_mock_review_round2.py`.
