# ACS Petroleum Research Fund — Doctoral New Investigator (DNI) Grant

> **Deadline: March 6, 2026, 5:00 PM EST**
> Spring 2026 submission window: February 9 – March 6, 2026
>
> **Outcome (October 2026):** declined. The panel rated the proposal not competitive and does not
> recommend resubmission. See [REVIEW_2026.md](REVIEW_2026.md) for the review, and
> [`../alternative-funding/`](../alternative-funding/) for what comes next.

This directory contains information and materials for preparing an ACS PRF DNI grant proposal for the Digital Wetlab project (LLM-based agents for qualitative inorganic chemistry automation on Opentrons robots).

## Contents

- [**REVIEW_2026.md**](REVIEW_2026.md) — Paraphrased digest of the 2026 decline and Reviewer B's review, mapped line by line to the submitted proposal
- [**REVIEW_2026_LITERATURE_CHECK.md**](REVIEW_2026_LITERATURE_CHECK.md) — Each of Reviewer B's 48 claims checked with an Edison literature query, and compared with what our earlier searches said
- [**ACS_PRF_DNI_GUIDE.md**](ACS_PRF_DNI_GUIDE.md) — Comprehensive guide covering eligibility, budget, format, review criteria, research scope, and tips
- [**PROPOSAL_CHECKLIST.md**](PROPOSAL_CHECKLIST.md) — Quick-reference submission checklist
- [**EDISON_PRECEDENT_SEARCH.md**](EDISON_PRECEDENT_SEARCH.md) — Edison Scientific precedent search results supporting the recommended alignment angle
- [**EDISON_PITZER_PARAMETER_SEARCH.md**](EDISON_PITZER_PARAMETER_SEARCH.md) — Edison Scientific literature search (February 2026) that found no published Fe²⁺/Pb²⁺–sulfide Pitzer parameters; the 2026 review argues these terms should not exist (see the literature check)
- [**PRELIMINARY_RESULTS_PLAN.md**](PRELIMINARY_RESULTS_PLAN.md) — Recommended preliminary results (experimental + computational) achievable by March 6
- [**`preliminary_results/`**](../../preliminary_results/) — Pitzer-model gap analysis, precipitation boundary map, BaSO₄ OT-2 experiment protocol, and experimental overlay analysis script

## Key Links

| Resource | URL |
|----------|-----|
| ACS PRF Main Page | <https://www.acs.org/funding/grants/petroleum-research-fund.html> |
| DNI Program Details | <https://www.acs.org/funding/grants/petroleum-research-fund/programs/doctoral-new-investigator-grants.html> |
| Research Areas | <https://www.acs.org/funding/grants/petroleum-research-fund/about/research-areas.html> |
| For Applicants | <https://www.acs.org/funding/grants/petroleum-research-fund/applicants.html> |
| Submission Portal | <https://prfgrant.acs.org/s/> |
| FAQ | <https://www.acs.org/funding/grants/petroleum-research-fund/about/faq.html> |
| DNI Eligibility, Terms & Conditions (PDF) | <https://www.acs.org/content/dam/acsorg/funding/grants/prf/programs/dni/dni-etc-07252024.pdf> |
| Brief PRF Overview (PDF) | <https://www.acs.org/content/dam/acsorg/funding/grants/prf/about/brief-prf-overview-2023-spring-dr.pdf> |
| Writing Competitive Proposals (PDF) | <https://www.acs.org/content/dam/acsorg/funding/grants/prf/programs/information-for-applicants/Writing%20Competitive%20Proposals.pdf> |
| Proposal Submission Checklist (PDF) | <https://www.acs.org/content/dam/acsorg/funding/grants/prf/programs/information-for-applicants/Proposal%20Submission%20Checklist.pdf> |
| Checklist of Common Errors | <https://www.acs.org/funding/grants/petroleum-research-fund/applicants/checklist-of-common-errors.html> |
| Submission Instructions | <https://www.acs.org/funding/grants/petroleum-research-fund/applicants/salesforce-proposal-submission-help.html> |
| PRF Transfer Agreement (PDF) | <https://www.acs.org/content/dam/acsorg/funding/grants/prf/prf-transfer-agreement.pdf> |
| 2024 Grants Awarded (PDF) | <https://www.acs.org/content/dam/acsorg/funding/grants/prf/annual-report/annual-report-2024/grants-awarded-2024.pdf> |
| Tenure-Clock Extension Template (PDF) | <https://www.acs.org/content/dam/acsorg/funding/grants/prf/prf-exception-template-jan2026.pdf> |

## Relevant Program Officer

For **Panel 3: Inorganic Chemistry** (most likely fit for this project):

**Dr. Allegra Liberman-Martin** — Manages Panels 1 (Synthetic Organic Chemistry) and 3 (Inorganic Chemistry)
Email: [a_liberman@acs.org](mailto:a_liberman@acs.org)

Grants Administrator for Panel 3: **Steven Nagle** — [s_nagle@acs.org](mailto:s_nagle@acs.org)

General Inquiries: (202) 872-4481 or [org@acs.org](mailto:org@acs.org) / [PRFsupport@acs.org](mailto:PRFsupport@acs.org)

## Alignment Strategy

ACS PRF funds **fundamental** research tied to petroleum/fossil fuels. The digital-wetlab project (LLM agents + Opentrons for inorganic chemistry) should be framed around the underlying science, **not** the automation platform itself.

### ⭐ Recommended angle: Precipitation equilibria of petroleum-produced-water metals

An [Edison Scientific precedent search](EDISON_PRECEDENT_SEARCH.md) evaluated three possible framings and found the strongest literature support for:

> **Systematic study of metal-ion precipitation equilibria (Ba²⁺, Pb²⁺, Fe²⁺/Fe³⁺) in simulated produced-water brines** — mapping solubility boundaries as functions of pH, ionic strength, temperature, and sulfide availability using automated high-throughput screening on a liquid-handling robot.

This angle works best because:

1. **Strong petroleum relevance** — Mineral scale formation (BaSO₄ barite, PbS galena, FeS mackinawite) is a major operational problem in petroleum produced water, with well-cited literature in SPE journals (Kan et al. 2019, 60 citations; Jordan et al. 2000, 63 citations)
2. **Clearly fundamental** — The core question is "How do competing equilibria govern precipitation selectivity in high-TDS brines?" — basic science, not device development
3. **Direct fit with the Opentrons platform** — Classical qualitative inorganic reactions (sulfate → BaSO₄, chromate → PbCrO₄, hydroxide → Fe(OH)₃) can be executed in 96-well plates with turbidity/color readouts
4. **Panel 3 (Inorganic Chemistry) fit** — Coordination chemistry, precipitation equilibria, and metal-ion behavior are core Panel 3 topics
5. **Gaps exist** — Pitzer-model predictions for sulfide scales (FeS, PbS) in complex brines still have significant uncertainty; systematic experimental data would fill a real gap

The other two angles (petrochemical feedstock analysis, concentration-dependent equilibria) are subsumed by this framing — they become aspects of the same study rather than standalone proposals.

### Key framing guidelines

- Emphasize **basic science questions** (e.g., "How do competing equilibria govern precipitate selectivity at varying concentrations?"), not tool-building
- Position the robot + LLM as the **method** enabling systematic exploration, not the **subject** of research
- Highlight **student training** in both chemistry fundamentals and modern research methods (≥ 60% of budget must go to student support)
- Treat this as **seed funding** for preliminary data toward a larger NSF CAREER or CHE proposal

> See [Section 9 of the DNI Guide](ACS_PRF_DNI_GUIDE.md#9-tips-for-a-competitive-proposal) for detailed proposal-writing tips.
> Full precedent search results with citations: [EDISON_PRECEDENT_SEARCH.md](EDISON_PRECEDENT_SEARCH.md)

## Related Context

- Public repo project description: [opentrons-inorganic-wet-lab-agents.txt](https://github.com/vertical-cloud-lab/digital-wetlab/blob/main/opentrons-inorganic-wet-lab-agents.txt)
- Funding opportunities overview: [FUNDING_OPPORTUNITIES.md](https://github.com/vertical-cloud-lab/digital-wetlab/blob/814b1ec9e9a0a6fa7cd33f1df0dc0bc117a0191b/FUNDING_OPPORTUNITIES.md)
- Issue tracking: [digital-wetlab#4](https://github.com/vertical-cloud-lab/digital-wetlab/issues/4)

## Instructive Videos

- [What makes a competitive proposal?](http://vimeo.com/41306667)
- [What makes a good ACS PRF grant proposal reviewer?](http://vimeo.com/64588132)
- [What Makes a Proposal a New Direction?](https://vimeo.com/132978944)
- [The PRF Program Manager as a Resource](https://vimeo.com/172902103)
- [Grant Reporting Requirements](https://vimeo.com/96719560)
