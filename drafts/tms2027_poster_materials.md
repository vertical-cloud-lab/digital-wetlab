# TMS 2027 poster planning for digital wet labs

**Status:** v4 — title and abstract revised per the round-2 Edison organizer-panel mock review (see
`edison-trajectories/tms-mock-review-round2/`), which judged v3 against the full symposium flyer using personas
of the four actual organizers and recommended requesting **Poster** rather than oral. The round-1 review
(`edison-trajectories/tms-mock-review/`) had returned "revise, then likely accept" for the From Mine to
Refinery symposium. v2 re-targeted toward chemistry / petroleum / extractive-metallurgy symposia using the verified
TMS 2027 symposium data (all 108 call-for-abstracts scraped from ProgramMaster) and Edison analyses from
[vertical-cloud-lab/byu-vcl#159](https://github.com/vertical-cloud-lab/byu-vcl/issues/159) /
[vertical-cloud-lab/byu-vcl#160](https://github.com/vertical-cloud-lab/byu-vcl/pull/160)
(`edison-trajectories/tms-symposium-top10/` and `edison-trajectories/tms-symposium-electrochem/` on branch
`claude/issue-159-20260710-2247`). The v1 shortlist below this section used plausible-sounding but unverified
symposium themes; the v2 list uses only real TMS 2027 symposium titles.

**Deadline:** TMS 2027 abstracts are due **July 15, 2026** (Orlando, FL, March 14–18, 2027; ≤150-word
abstract body via ProgramMaster).

## Recommended target symposium (v2)

**From Mine to Refinery: An EPD Symposium Honoring Shijie Wang**
(TMS Extraction and Processing Division; Hydrometallurgy and Electrometallurgy Committee; Pyrometallurgy Committee.
Organizers: Michael Moats, Ramana Reddy, Michael Free, Corby Anderson.)

Why this is the top chemistry-leaning pick for *this* project:

- The scope explicitly welcomes "leaching behavior, **solution chemistry**, reagent optimization, kinetic and
  **thermodynamic modeling** … including the potential use of **AI** in these areas" — the ACS PRF project *is*
  solution chemistry plus thermodynamic modeling plus AI-guided experimentation.
- Metal-sulfide chemistry of Fe and Pb sits squarely in extractive metallurgy: sulfide precipitation is used for
  impurity control and metal recovery in hydrometallurgical circuits, and Pitzer-model electrolyte thermodynamics
  in concentrated brines is a core hydrometallurgy modeling tool. The same FeS/PbS precipitation and missing
  Pitzer parameters that govern oilfield scale govern sulfide behavior in process waters — that is the
  petroleum ↔ metallurgy bridge.
- Organizer receptiveness: Michael Free (Univ. of Utah) publicly describes leaching experiments where pH and flow
  are "monitored and controlled by automated equipment" — an organizer who already runs automated solution
  chemistry. The prior Edison sweep flagged this symposium as the highest-acceptance-likelihood venue overall
  for an application-forward (solution-chemistry) reframing.
- Poster-friendly: the manuscript requirement applies to authors seeking an **oral** slot; posters do not require
  a proceedings paper.

Risk to manage: this is an industrial extractive-metallurgy audience honoring a hydrometallurgist, so the
abstract must lead with the solution chemistry and thermodynamics deliverable (validated Pitzer parameters,
scale/impurity prediction), not the robot. Petroleum framing should be one clause, not the headline.

## Ranked shortlist (v2, chemistry/petroleum lean with metallurgy tie-in)

Fit scores in parentheses are the prior Edison full-text-sweep scores for an SDL platform abstract
(byu-vcl context); ranks below are re-ordered for this project's sulfide/brine solution chemistry.

1. **From Mine to Refinery: An EPD Symposium Honoring Shijie Wang** (7.6) — top pick; see above.
2. **AI-Enabled Materials Processing: Integrating Accelerated Experimental Workflows and Processing-Aware
   Machine Learning** (9.5) — the best generalist AI/closed-loop home; scope names "Bayesian optimization,"
   "closed-loop experimental workflows." Strongest backup if the chemistry lean is dropped, but does not honor
   the chemistry/metallurgy angle.
3. **Rare Metal Extraction & Processing** (7.2) — same Hydrometallurgy and Electrometallurgy Committee;
   lab-scale processing and solution chemistry welcome; fit improves if critical/rare-metal sulfide systems are
   named explicitly.
4. **Next Generation Electrometallurgical Technologies for Metal Extraction, Refining, and Recycling** (6.8) —
   scope encourages "closed-loop system design," "process control," "modularization"; our brine electrolyte
   thermodynamics feeds electrolyte/leachate modeling, but the electro angle is upstream only.
5. **Advances in Recycling and Environmental Technologies** — hidden gem from the electrochem sweep: sulfide
   precipitation is a standard effluent-treatment / metal-recovery route, and produced-water chemistry is an
   environmental-performance story.
6. **Circular Metallurgy: Design, Technology, Application** (6.7) — only scope that literally lists "lab
   automation, robotics, process optimization and AI/ML," but would need a recovery/recycling use case we do not
   yet demonstrate.
7. **AI/ML/Data Informatics for Materials Discovery: Bridging Experiment, Theory, and Modeling** (8.8) — strong
   if the poster emphasizes FAIR data, provenance, and the experiment database rather than chemistry.
8. **Artificial Intelligence Applications in ICME (AI-ICME)** (8.4) — scope lists "active learning and Bayesian
   optimization" and "autonomous/closed-loop experimentation"; good methods audience.
9. **Mechanistic and Experimental Thermodynamics & Kinetics of Alloys** (6.4) — hidden gem for the *Pitzer
   parameter regression* story (high-quality experimental thermodynamic measurements, closed-loop frameworks),
   but the aqueous-electrolyte vs. alloy mismatch is real.
10. **Energy Technology 2027: Advancement in Energy Materials** — fallback tying produced-water/brine chemistry
    to energy production; weakest direct fit.

Excluded: **Hume-Rothery Symposium** (invited abstracts only), molten-salt and nanomaterials symposia
(aqueous/domain mismatch).

## Suggested poster framing (v2)

Lead with the chemistry deliverable, use the platform as the enabler:

- unmeasured Pitzer parameters (Fe²⁺–HS⁻, Pb²⁺–HS⁻, metal–acetate/propionate) block rigorous sulfide-solubility
  prediction in concentrated brines
- one chemistry, two industries: oilfield sulfide scale (petroleum) and impurity control / metal recovery /
  process-water chemistry (hydrometallurgy)
- low-cost Opentrons-based digital wet lab + active learning as the route to ~30,000 mapped conditions
- validated parameters delivered to the tools both industries use (PHREEQC, ScaleSoftPitzer, OLI)

## Title (v4, post round-2 organizer-panel review)

FeS/PbS Precipitation Boundaries for Impurity Management in Concentrated Hydrometallurgical Process Waters

## Draft abstract (v4, post round-2 organizer-panel review, ≤150 words)

Sulfide precipitation of iron and lead affects impurity management, metal recovery, and process-water
chemistry in hydrometallurgical circuits, but concentrated-solution models often lack Pitzer interactions for
Fe²⁺–HS⁻, Pb²⁺–HS⁻, and metal–organic-acid complexes. We will present an automated precipitation-mapping
platform with controlled temperature staging, high-ionic-strength pH measurement, and image-based FeS/PbS
endpoint detection. Latin hypercube sampling and active learning will map precipitation boundaries across
0.5–5 molal ionic strength, pH 4–9, 25–90 °C, and acetate/propionate concentration. Boundary shifts will be
compared with PHREEQC Pitzer predictions to identify parameter gaps relevant to Pb processing, sulfide
precipitation control, and process-water reuse. Early results will emphasize reproducibility, calibration
checks, and initial FeS/PbS boundary data rather than a completed parameter database. The approach provides
practical solution-chemistry data and a low-cost template for automated hydrometallurgical experiments.

(126 words. Adopted verbatim from the round-2 organizer-panel's revised version, with superscript ion
formatting restored.)

### Superseded title/abstract (v3, post round-1 review)

Title: *Automated FeS and PbS Precipitation Mapping to Improve Pitzer Modeling of Concentrated
Hydrometallurgical Brines*

> Iron and lead sulfide precipitation affects impurity control, metal recovery, and process-water chemistry in
> hydrometallurgical operations, but concentrated-brine thermodynamic models remain limited by missing Pitzer
> interactions for Fe²⁺–HS⁻, Pb²⁺–HS⁻, and metal–organic-acid complexes. We will present an Opentrons-based
> autonomous precipitation-mapping platform with automated pH measurement, temperature-controlled reaction
> staging, and image-based detection of FeS/PbS formation. The campaign combines Latin hypercube sampling with
> active learning to map precipitation boundaries across ionic strength (0.5–5 molal), pH 4–9, 25–90 °C, and
> acetate/propionate concentration, then compares boundary shifts with PHREEQC Pitzer predictions to identify
> parameter gaps. Early results will emphasize platform validation, reproducibility, and initial FeS/PbS
> boundary data rather than a completed parameter database. The work aims to provide practical
> solution-chemistry data for sulfide precipitation control and a low-cost template for automated
> hydrometallurgical experiments.

(129 words. Was adopted verbatim from the round-1 mock-review panel's revised version.)

## Submission information (for ProgramMaster entry)

- **Conference:** TMS 2027 Annual Meeting & Exhibition, Orlando, FL, March 14–18, 2027
- **Symposium:** From Mine to Refinery: An EPD Symposium Honoring Shijie Wang
- **Presentation type:** **Poster** (select "Poster", *not* "Student Poster") — confirmed by the round-2
  organizer-panel review: an oral request is plausible but not recommended, because the oral slot carries a
  proceedings-manuscript obligation and the work is too proposal-stage / too indirectly tied to the listed
  recovery-refining Technical Focus Areas to justify it
- **Abstract deadline:** July 15, 2026 (≤150-word abstract body; the v4 abstract above is 126 words)
- **Authors (in order), all affiliated with Brigham Young University, Department of Mechanical Engineering:**
  1. Timothy Commins (presenting author)
  2. Sam Charles
  3. Xavier Zaitzeff
  4. Finn Albiston
  5. Seth Leavitt
  6. Sterling Baird
- **Note:** posters in this symposium do not require a proceedings manuscript (that applies to oral-slot
  authors only).

## Mock reviewer feedback round 2 (Edison, organizer-persona panel) — results

Task `a15d214b-ee8b-4aed-aea6-818876128c6a` (ANALYSIS); full report and raw dump under
`edison-trajectories/tms-mock-review-round2/` (input bundle: v3 abstract + full flyer text + researched
organizer profiles). Scripts: `scripts/edison/submit_tms_mock_review_round2.py`,
`scripts/edison/fetch_tms_mock_review_round2.py`.

**Verdict: would likely be programmed as a poster** — not rejected, but not prioritized for oral. Persona
scores (fit / technical quality / audience interest out of 10): Moats 7/7/6; Reddy 6/8*/6 (*8 if
calibration/identifiability are handled, else 6); Free 8/7/7; Anderson 7/6*/6 (*7 if sulfide oxidation and pH
controls are named). The panel's single highest-impact change: move the framing from "automated Pitzer-model
improvement" to "impurity management in hydrometallurgical process waters," with explicit Pb-processing and
sulfide-precipitation-control hooks — the flyer's own Technical Focus Area language.

**Talk vs. poster:** request **Poster**. An oral slot is plausible but not strongly earned; the oral request
adds a proceedings-manuscript obligation and raises the bar to credible March-2027 results beyond platform
validation. If an oral request is ever made anyway, the abstract should explicitly name "Pb processing,"
"impurity management," and "process-water reuse," and add a concrete calibration/controlled-sulfide-chemistry
phrase.

Key changes implemented in v4 above (all from the panel's line edits / revised version):

- **Title leads with the metallurgical use case** — "FeS/PbS Precipitation Boundaries for Impurity Management
  in Concentrated Hydrometallurgical Process Waters" replaces the automation-first, methods-first v3 title
  ("Automated … Pitzer Modeling … Brines"). "Process waters" reads plant-side; "brines" read petroleum-side.
- **"Impurity management"** (the flyer's Technical Focus Area wording) replaces "impurity control";
  "hydrometallurgical circuits" replaces "operations"; "concentrated-solution models" replaces
  "concentrated-brine thermodynamic models" to avoid a petroleum-brine feel.
- **Opentrons brand name dropped from the abstract** ("automated precipitation-mapping platform") — it does not
  help these organizers and risks sounding platform-first; the brand goes on the poster instead.
- **Added "high-ionic-strength pH measurement" and "calibration checks"** to address Reddy's and Free's
  data-quality concerns at 0.5–5 molal.
- **"Image-based FeS/PbS endpoint detection"** replaces "image-based detection of FeS/PbS formation" — a
  defined measurement, not crude visual classification.
- **Explicit Technical Focus Area bridge added:** "…parameter gaps relevant to Pb processing, sulfide
  precipitation control, and process-water reuse."
- **Kept** the honest proposal-stage wording ("…rather than a completed parameter database"), which the panel
  said must remain.

Likely Technical Focus Area filings suggested by the panel: "Leaching and Chemical Extraction Science of Base
Metals" (Free, Reddy) or "Smelting, Electrowinning and Refining Technologies, Impurity Management, and
Cell-house Practices" (Moats), with "Novel Methods of Processing and Recycling Cu, Ni and Pb" as Anderson's
pick — useful if ProgramMaster asks for a focus-area selection.

## Mock reviewer feedback round 1 (Edison) — results

Task `eecd8120-0614-4bd4-8dfb-75a7b945284e` (ANALYSIS); full report and raw dump under
`edison-trajectories/tms-mock-review/`. Scripts: `scripts/edison/submit_tms_mock_review.py`,
`scripts/edison/fetch_tms_mock_review.py`.

**Verdict: revise, then likely accept** as a poster in From Mine to Refinery. Panel scores (fit / quality /
interest out of 10): industrial hydrometallurgist 7/7/6; academic extractive metallurgist 8/8/7;
thermodynamics skeptic 6/6/6. Key changes implemented in v3 (now the superseded version quoted above):

- **De-claimed proposal-stage work** — "The result is a validated framework…" read as completed validation;
  replaced with "Early results will emphasize platform validation, reproducibility, and initial boundary data."
  This was flagged as the single most important edit.
- **Dropped petroleum-first framing** — oilfield-scale language in the opening sentence made the work look
  adjacent to, not inside, extractive metallurgy for this audience.
- **Chemistry leads, robot follows** — "low-cost autonomous digital wet lab" removed from the title;
  "digital wet laboratory / closed-loop" jargon replaced with "autonomous precipitation-mapping platform" and
  "Latin hypercube sampling with active learning."
- **Softened "governs" → "affects"** for FeS/PbS's role in impurity control and metal recovery.
- **Added temperature-control credibility** ("temperature-controlled reaction staging") since 25–90 °C on a
  standard liquid handler is a known reviewer red flag.
- **Dropped the ~30,000-experiment and 48-parameter claims** from the abstract; the skeptic reviewer flagged
  parameter identifiability from boundary-only data as a major concern to address on the poster itself.

Remaining red flags to prepare for on the poster (not abstract blockers): high-ionic-strength pH calibration
and junction potentials, sulfide oxidation/atmosphere control, image-detection thresholds vs. quantitative
fitting, and Pitzer parameter identifiability. Backup venues re-checked by the panel: AI-Enabled Materials
Processing (better methods-novelty score but chemistry may feel narrow), Rare Metal Extraction & Processing,
and Advances in Recycling — the panel kept From Mine to Refinery as the best target after revision.

---

# v1 planning note (superseded — symposium titles below were unverified placeholders)

This draft is based on publicly available TMS-style symposium themes and the fit for a self-driving-lab /
digital-wet-lab poster. Because the full official program flyers were not readily accessible in this
environment, the shortlist should be treated as a strong first-pass targeting document rather than a final
submission decision.

## Recommended target symposium (v1)

The best first-pass fit is the broad AI/ML/data-informatics track for materials discovery and autonomous
experimentation. A poster framed around "digital wet labs," "self-driving laboratories," and "closed-loop
experimental design" should be a strong fit for a general materials-science audience, while still being
specific enough to stand out.

Suggested target title:
- AI/ML/Data Informatics for Materials Discovery: Bridging Experiment, Theory, and Modeling

## Draft abstract (v1)

Digital wet laboratories promise to compress the time between hypothesis, experiment, and insight by
integrating low-cost liquid handling, automated sensing, and machine-guided decision making. Here we present a
modular self-driving wet-lab platform that couples an Opentrons-based robotic liquid handler with
active-learning experiment selection and reusable software interfaces for materials-relevant aqueous chemistry.
The platform autonomously plans and executes plate-based experiments, ingests observations, and updates
subsequent experiments in real time using Bayesian optimization and rule-based feedback. We demonstrate the
approach in a representative inorganic precipitation workflow and show that closed-loop operation improves
information gain and reduces trial count relative to manual design. By lowering the barrier to entry for
autonomous experimentation, this work provides a practical route toward democratized digital wet labs for
accelerated discovery in materials synthesis, processing, and process-chemistry research.
