# ACS PRF DNI Proposal Submission Checklist

> **Deadline: March 6, 2026, 5:00 PM EST**
> Portal: <https://prfgrant.acs.org/s/>

## Pre-Submission

- [ ] Confirm eligibility: within first 3 years of first Assistant Professor appointment
- [ ] Verify proposed research is a **new direction** (not extension of graduate/postdoc work)
- [ ] Verify research is **fundamental** (not applied, not methods/device development)
- [ ] Verify **petroleum relevance** — connects to petroleum, natural gas, coal, shale, tar sands
- [ ] Contact program officer to confirm fit (Dr. Allegra Liberman-Martin for Inorganic Chemistry — [a_liberman@acs.org](mailto:a_liberman@acs.org))
- [ ] No current active PRF grant (including grants on time extension)
- [ ] No overlap with other funded projects
- [ ] Confirm this is DNI attempt 1, 2, or 3 (max 3 career attempts)
- [ ] Review the [Brief PRF Overview PDF](https://www.acs.org/content/dam/acsorg/funding/grants/prf/about/brief-prf-overview-2023-spring-dr.pdf)
- [ ] Review the [Writing Competitive Proposals PDF](https://www.acs.org/content/dam/acsorg/funding/grants/prf/programs/information-for-applicants/Writing%20Competitive%20Proposals.pdf)
- [ ] Review the [DNI Eligibility, Terms & Conditions PDF](https://www.acs.org/content/dam/acsorg/funding/grants/prf/programs/dni/dni-etc-07252024.pdf)

## Proposal Document

- [ ] **Abstract** — 250 words (entered separately in online system)
- [ ] **Petroleum relevance statement** — 100 words (entered separately online)
- [ ] **Proposal body** — single PDF, ≤ 4,000 words
  - [ ] Double-spaced, 12-point font (Arial, Times Roman, or Courier)
  - [ ] Single focused research project with clear, testable hypothesis
  - [ ] Word count excludes abstract, figure/table captions, and references
- [ ] **Six suggested peer reviewers** — names and email addresses
- [ ] **Resubmission summary** (if resubmitting — entered online, not in proposal PDF)
- [ ] **PI biosketch/CV**

## Budget ($110,000 total over 2 years)

- [ ] Total budget = exactly $110,000
- [ ] Student support ≥ 60% of total (≥ $66,000)
  - [ ] Includes: stipends/salaries/benefits, graduate tuition, field work
- [ ] PI summer stipend ≤ $8,000/year including fringe (≤ $16,000 total)
- [ ] Conference travel ≤ $2,000/year (≤ $4,000 total)
- [ ] Capital equipment ≤ $5,000 (with justification and institutional cost-matching info)
- [ ] Publication costs ≤ $2,000 total
- [ ] **No overhead/indirect costs**
- [ ] No technicians, contractors, consultants, or visiting faculty
- [ ] Budget justification included
- [ ] Start date is first day of a month (earliest: July 1, 2026)
- [ ] Grant period ends on an August 31

## Final Checks

- [ ] Used current, dated application form
- [ ] All sections complete — no late materials accepted
- [ ] Proposal clearly distinguishes from prior graduate/postdoc research
- [ ] Research framed as fundamental science, not applied or device development
- [ ] Petroleum relevance is specific and connected to PRF Trust definition
- [ ] Institutional authorization obtained
- [ ] Submitted before 5:00 PM EST on March 6, 2026

## Project-Specific Remaining Tasks (This Proposal)

### Testing Setup Action List

- [ ] Confirm OT-2, GEN2 8-channel pipette, plate-reader access, fume hood, and N₂ glovebox availability for planned experiments
- [ ] Procure minimum reagents for setup runs: AgNO₃ + NaCl (AgCl demo), BaCl₂ + Na₂SO₄ + NaCl (BaSO₄ validation), Pb(NO₃)₂ + (NH₄)₂S (PbS experiment)
- [ ] Prepare consumables: 96-well plates, OT-2 tips, adhesive seals, DI water, and PPE
- [ ] Run a no-hazard dry run (food-coloring gradient or AgCl workflow) to verify deck layout, dispensing, and imaging pipeline
- [ ] Run `preliminary_results/baso4_nacl_gradient_protocol.py` and save plate image output as `preliminary_results/baso4_results.png`
- [ ] Run `preliminary_results/baso4_experimental_overlay.py` to generate BaSO₄ experimental-vs-model overlay figure for the proposal
- [ ] Run PbS (or FeS) precipitation imaging test and save output as `preliminary_results/pbs_photo.png` (or matching FeS filename used in LaTeX)

### Proposal Integration + Final Verification

- [ ] Insert preliminary-result figures into `drafts/draft.tex` with captions and labels
- [ ] Replace the Aim 2 placeholder box in `drafts/draft.tex` with a real workflow figure
- [ ] Compile the proposal PDF and verify all figures render correctly
- [ ] Confirm proposal body word count is ≤ 4,000 words
- [ ] Confirm bibliography compiles cleanly with no missing references
