# TMS 2027 poster abstract (v3, post round-1 mock review) — FeS/PbS precipitation mapping

- **Meeting:** TMS 2027 Annual Meeting & Exhibition, Orlando, FL, March 14–18, 2027
- **Submission:** plain-text abstract body ≤150 words via ProgramMaster (due July 15, 2026)
- **Target symposium:** From Mine to Refinery: An EPD Symposium Honoring Shijie Wang (see symposium-flyer.md)
- **Currently planned presentation type:** Poster (not Student Poster). An open question for this review is
  whether to request an oral presentation instead — see the query.

## Title (v3)

Automated FeS and PbS Precipitation Mapping to Improve Pitzer Modeling of Concentrated Hydrometallurgical
Brines

## Abstract (v3, 129/150 words)

Iron and lead sulfide precipitation affects impurity control, metal recovery, and process-water chemistry in
hydrometallurgical operations, but concentrated-brine thermodynamic models remain limited by missing Pitzer
interactions for Fe²⁺–HS⁻, Pb²⁺–HS⁻, and metal–organic-acid complexes. We will present an Opentrons-based
autonomous precipitation-mapping platform with automated pH measurement, temperature-controlled reaction
staging, and image-based detection of FeS/PbS formation. The campaign combines Latin hypercube sampling with
active learning to map precipitation boundaries across ionic strength (0.5–5 molal), pH 4–9, 25–90 °C, and
acetate/propionate concentration, then compares boundary shifts with PHREEQC Pitzer predictions to identify
parameter gaps. Early results will emphasize platform validation, reproducibility, and initial FeS/PbS
boundary data rather than a completed parameter database. The work aims to provide practical
solution-chemistry data for sulfide precipitation control and a low-cost template for automated
hydrometallurgical experiments.

## Project context (not part of the abstract)

The underlying project (ACS PRF DNI proposal, Panel 3 Inorganic Chemistry) determines missing Pitzer
ion-interaction parameters for sulfide-mineral solubility in concentrated brines. Petroleum-derived H₂S reacts
with dissolved Fe²⁺ and Pb²⁺ in produced waters to deposit FeS and PbS scale; petroleum-derived organic acids
(acetic, propionic) modify precipitation via pH buffering and metal complexation. Binary Pitzer parameters for
Fe²⁺–HS⁻ and Pb²⁺–HS⁻, and metal–acetate/propionate parameters, are absent from standard databases (~48
unmeasured parameters). The experimental platform is a low-cost Opentrons OT-2-based digital wet lab
(autonomous liquid handling, pH measurement, image-based precipitate detection) running a large mapping
campaign (~30,000 experiments targeted) over ionic strength 0.5–5 molal, pH 4–9, and 25–90 °C, with Latin
hypercube coverage plus staged active learning near precipitation boundaries; deviations from PHREEQC Pitzer
predictions beyond ±0.2 saturation-index units trigger nonlinear least-squares regression of new parameters.
At presentation time (March 2027) the platform and early campaign results are expected; the full parameter
set is a project deliverable, not yet a completed result. Authors are six mechanical-engineering researchers
at Brigham Young University (presenting author: Timothy Commins).

## Round-1 mock-review changes already implemented in v3

A prior three-persona mock review (industrial hydrometallurgist; academic extractive metallurgist;
Pitzer/PHREEQC skeptic) produced verdict "revise, then likely accept" and these changes, all implemented:
de-claimed proposal-stage work ("Early results will emphasize…" instead of "The result is a validated
framework…"); removed petroleum/oilfield framing from the abstract body; demoted the robot to enabler
("autonomous precipitation-mapping platform," not "digital wet lab"; "Latin hypercube sampling with active
learning," not "closed-loop"); added temperature-control credibility ("temperature-controlled reaction
staging"); softened "governs" to "affects"; dropped the ~30,000-experiment and ~48-parameter counts from the
abstract. Known red flags to address on the poster/talk itself: high-ionic-strength pH calibration and
junction potentials; sulfide oxidation/atmosphere control; image-detection thresholds vs. quantitative
fitting; Pitzer parameter identifiability from boundary-only data.
