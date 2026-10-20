# TMS 2027 poster abstract draft (v2) — digital wet lab / sulfide-brine chemistry

- **Meeting:** TMS 2027 Annual Meeting & Exhibition, Orlando, FL, March 14–18, 2027
- **Format:** poster; plain-text abstract body ≤150 words, submitted via ProgramMaster (due July 15, 2026)
- **Target symposium:** From Mine to Refinery: An EPD Symposium Honoring Shijie Wang (see symposium-scope.md)

## Project context (not part of the abstract)

The underlying project (ACS PRF DNI proposal, Panel 3 Inorganic Chemistry) determines missing Pitzer
ion-interaction parameters for sulfide-mineral solubility in concentrated brines. Petroleum-derived H₂S reacts
with dissolved Fe²⁺ and Pb²⁺ in produced waters to deposit FeS and PbS scale; petroleum-derived organic acids
(acetic, propionic) modify precipitation via pH buffering and metal complexation. Binary Pitzer parameters for
Fe²⁺–HS⁻ and Pb²⁺–HS⁻, and metal–acetate/propionate parameters, are absent from standard databases (~48
unmeasured parameters). The experimental platform is a low-cost Opentrons OT-2-based digital wet lab
(autonomous liquid handling, pH measurement, image-based precipitate detection) running a ~30,000-experiment
campaign over ionic strength 0.5–5 molal, pH 4–9, and 25–90 °C, with Latin hypercube coverage plus staged
active learning near precipitation boundaries; deviations from PHREEQC Pitzer predictions beyond ±0.2
saturation-index units trigger nonlinear least-squares regression of new parameters. At poster time (March
2027) the platform and early campaign results are expected; the full parameter set is a project deliverable,
not yet a completed result.

## Title (v2 draft)

Closed-Loop Mapping of Iron and Lead Sulfide Precipitation in Concentrated Brines Using a Low-Cost Autonomous
Digital Wet Lab

## Abstract (v2 draft, 143/150 words)

Iron and lead sulfide precipitation governs impurity control and metal recovery in hydrometallurgical circuits
and causes flow-restricting scale during petroleum production, yet thermodynamic models cannot rigorously
predict sulfide solubility in concentrated brines: Pitzer parameters for Fe²⁺–HS⁻, Pb²⁺–HS⁻, and
metal–organic-acid interactions are absent from standard databases. We present a low-cost digital wet
laboratory that addresses this gap through autonomous, closed-loop experimentation. Built on an Opentrons
liquid-handling robot with automated pH measurement and image-based precipitate detection, the platform maps
FeS and PbS precipitation boundaries across ionic strength (0.5–5 molal), pH (4–9), temperature (25–90 °C), and
organic-acid concentration in a ~30,000-experiment campaign. Latin hypercube sampling provides broad coverage;
active learning adaptively targets conditions near precipitation boundaries. Deviations from PHREEQC Pitzer
predictions drive regression of the missing parameters. The result is a validated framework for sulfide-scale
and solution-chemistry prediction, and a replicable template for autonomous extractive-metallurgy-relevant
experimentation.
