# Research Question & Core Hypothesis — ACS PRF DNI

> Brainstormed from the [Edison Precedent Search](EDISON_PRECEDENT_SEARCH.md) findings.
> Scope: Pitzer-model validation for sulfide-scale precipitation in produced-water brines.

---

## Fundamental Research Question

**How accurately do Pitzer activity-coefficient models predict sulfide-scale (FeS mackinawite, PbS galena) precipitation boundaries in compositionally complex produced-water brines, and what specific ion–ion interactions cause deviations at high ionic strength?**

### Why this question is fundamental

Pitzer models are the accepted thermodynamic framework for predicting mineral solubility in concentrated electrolytes. For *sulfate* scales (especially BaSO₄ barite), Pitzer parameters are well-characterized and predict saturation indices to ±0.1 SI in high-TDS brines (Kan et al. 2019). However, for *sulfide* scales — FeS and PbS — the situation is markedly different:

- **FeS (mackinawite):** Published Ksp values vary by orders of magnitude; Fe–S speciation is complicated by FeHS⁺ and other complexes; the practical pH threshold for precipitation (~6.5) depends on brine composition in ways that current models do not fully capture (Wylde 2014, Wang et al. 2020).
- **PbS (galena):** Extremely insoluble (Ksp ~10⁻²⁹), but solubility increases with temperature and salinity in real brines. Pitzer interaction parameters for Pb²⁺–HS⁻ in the presence of major brine cations (Na⁺, Ca²⁺, Mg²⁺) and anions (Cl⁻) have not been systematically validated (Al-Harbi et al. 2017, Keogh 2019).
- **Higher-order mixing parameters** (θ and ψ terms in the Pitzer formalism) for Fe²⁺ and Pb²⁺ with major brine ions are sparse or absent from standard databases (Wang et al. 2020).

This creates a clear gap: the models used by petroleum engineers to predict sulfide scaling are built on interaction parameters derived from simple binary/ternary electrolyte systems, but produced waters contain 5–10+ major dissolved species simultaneously. The question asks whether — and where — this simplification breaks down.

### Why this is not applied research

The question targets the **fundamental thermodynamic accuracy** of an electrolyte theory (Pitzer formalism), not a device, method, or engineering solution. The deliverable is new knowledge about ion–ion interactions, not a treatment technology.

---

## Core Hypothesis

> **Pitzer-model predictions for FeS and PbS precipitation boundaries will systematically deviate from experimental observations in multi-component brines at ionic strengths above ~2 molal, and these deviations can be resolved by fitting higher-order mixing parameters (θ_{ij} and ψ_{ijk}) for Fe²⁺ and Pb²⁺ with major produced-water ions (Na⁺, Ca²⁺, Cl⁻).**

### Hypothesis unpacked

1. **Testable prediction:** At ionic strengths typical of produced waters (I ≈ 2–6 molal), existing Pitzer models will *overpredict* sulfide-scale supersaturation — that is, they will predict precipitation at conditions where experiments show the solution remains undersaturated. The expected mechanism is that unmeasured repulsive higher-order interactions between the scale-forming cation (Fe²⁺ or Pb²⁺) and abundant matrix cations (Na⁺, Ca²⁺) effectively increase FeS/PbS solubility beyond what current parameters capture.

2. **Measurable outcome:** Systematic precipitation screening across a factorial matrix of [Fe²⁺ or Pb²⁺] × [HS⁻] × [NaCl] × [CaCl₂] × pH × temperature will produce experimental precipitation boundaries (Q = Ksp curves) that can be quantitatively compared to Pitzer-model predictions using existing literature parameters.

3. **Falsifiable:** If experimental boundaries agree with current Pitzer predictions to within ±0.2 SI across the full parameter space, the hypothesis is falsified — the existing parameters are adequate, and the gap identified in the literature is smaller than believed.

4. **Resolvable:** Where deviations exceed ±0.2 SI, new θ and ψ parameters can be regressed from the experimental data and their physical significance interpreted in terms of specific ion–ion interactions.

### Directional expectation

Based on the literature:
- **FeS:** Expect the largest deviations at near-neutral pH (6–7.5) in Ca²⁺-rich brines, where Ca²⁺–Fe²⁺ interactions and CaHS⁺ complexation are most significant but least constrained.
- **PbS:** Expect deviations to increase with temperature (60–90 °C) and NaCl concentration, where Pb²⁺–Cl⁻ complexation competes with Pb²⁺–HS⁻ interactions and current models lack validated high-temperature mixing parameters.

---

## How This Maps to the Proposal

| Proposal Element | Content |
|---|---|
| **Research question** | Accuracy of Pitzer models for sulfide scales in complex brines |
| **Hypothesis** | Existing parameters fail above ~2 molal I; new mixing parameters resolve deviations |
| **Method** | Automated high-throughput precipitation screening (Opentrons + 96-well plates + nephelometry/imaging) |
| **Gap filled** | Systematic experimental data on sulfide-scale boundaries validated against Pitzer predictions |
| **Petroleum relevance** | FeS/PbS scaling is a major operational problem in produced-water management |
| **Panel fit** | Panel 3 (Inorganic Chemistry) or Panel 6 (Chemical Physics/Physical Chemistry) |
| **New direction** | Automated brine-chemistry screening — not an extension of prior work |
| **Student training** | Hands-on thermodynamics, programming, data analysis, inorganic chemistry |
| **Seed funding path** | Preliminary data → NSF CAREER or CHE proposal on electrolyte thermodynamics |

---

## Specific Aims (draft sketch)

**Aim 1 — Map experimental FeS and PbS precipitation boundaries across produced-water-relevant parameter space.**
Using an Opentrons liquid-handling robot, systematically vary [metal], [sulfide], ionic strength (0.5–5 molal NaCl ± CaCl₂), pH (4–9), and temperature (25–90 °C) in 96-well plates. Detect precipitation onset via time-resolved nephelometry and imaging. Deliverable: a curated dataset of ~500–1000 experimental precipitation/no-precipitation points across the parameter space.

**Aim 2 — Quantify deviations between experimental boundaries and Pitzer-model predictions, and regress new mixing parameters where needed.**
Compute saturation indices for each experimental condition using PHREEQC (or equivalent) with published Pitzer databases. Identify systematic deviations. Where deviations exceed ±0.2 SI, regress new θ and ψ parameters using weighted least-squares fitting. Validate by predicting hold-out experimental conditions. Deliverable: a set of validated Pitzer mixing parameters for Fe²⁺–HS⁻ and Pb²⁺–HS⁻ systems in NaCl–CaCl₂ brines, published as a peer-reviewed dataset.

---

## Key References

1. Kan et al. (2019) — Pitzer models for produced-water scale; barite SI prediction. *SPE J.* [doi:10.2118/190754-pa](https://doi.org/10.2118/190754-pa)
2. Wang et al. (2020) — Sulfide-scale Pitzer model gaps. *SPE* [doi:10.2118/200699-ms](https://doi.org/10.2118/200699-ms)
3. Al-Harbi et al. (2017) — PbS precipitation kinetics in brine. *SPE* [doi:10.2118/184509-ms](https://doi.org/10.2118/184509-ms)
4. Wylde (2014) — FeS scale; pH thresholds. *SPE* [doi:10.2118/169776-ms](https://doi.org/10.2118/169776-ms)
5. Keogh (2019) — PbS nucleation/growth mechanisms.
6. Shafer-Peltier et al. (2020) — Ba removal; brine composition variability. *Env Sci: Water Res Tech* [doi:10.1039/c9ew00643e](https://doi.org/10.1039/c9ew00643e)
7. Dehring et al. (2004) — Robotic nephelometry methodology. *J Pharm Biomed Anal* [doi:10.1016/j.jpba.2004.07.022](https://doi.org/10.1016/j.jpba.2004.07.022)
