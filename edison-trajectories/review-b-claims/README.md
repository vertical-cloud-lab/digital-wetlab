# Edison check of Reviewer B's claims (2026-10-29)

These are 48 low-effort Edison `LITERATURE` (paperqa3) queries, one for each separate claim in the
2026 ACS PRF review. The review itself is not in this repo; [`REVIEW_2026.md`](../../grants/acs-prf/REVIEW_2026.md)
paraphrases it. Each query is an open question, written so that Edison is not handed the
reviewer's conclusion to confirm.

The assessment of the answers, and of what our earlier searches missed, is in
[`REVIEW_2026_LITERATURE_CHECK.md`](../../grants/acs-prf/REVIEW_2026_LITERATURE_CHECK.md).

- `_task_ids.json`: claim ID → Edison task ID, review point, paraphrased claim, query, submission time
- `<ID>.md`: the query and Edison's formatted answer with references, plus any table it produced
- `<ID>.json.gz`: the full task dump from `get_task(verbose=True)`, gzipped. To keep publisher
  content out of a public repo, the raw paper text and page images the agent read are replaced
  with `[redacted: …]` markers. The answer, references, Edison's context summaries, tool history
  and the agent's own messages are untouched. The unredacted trajectory stays on Edison under the
  task ID.
- Script: [`scripts/edison/review_b_claims.py`](../../scripts/edison/review_b_claims.py)
  (`submit`, `wait`, `fetch`)

Claim IDs follow the review's numbering. F1–F3 are the three flaws the reviewer ranked as decisive,
P0 is the opening paragraph, and P1a–P15b are the numbered points.
