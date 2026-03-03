# Experiment 003: PbS Vial Tests (Lead Sulfide Precipitation)

> **Reaction:** Pb²⁺ (aq) + S²⁻ (aq) → PbS (s) ↓
>
> **Observable:** Black precipitate — rapid formation (<5 minutes), visible at sub-millimolar concentrations

## Objective

Confirm that lead sulfide (PbS) black precipitates form rapidly and are clearly visible at low concentrations (0.5 mM Pb²⁺) in the presence of NaCl ionic strength modifier (1 molal). These small-scale vial tests serve as a **complementary validation** to the BaSO₄ 96-well plate experiment ([Experiment 002](../002-baso4-precipitation/README.md)), providing:

1. A robust visual signal (black vs. white) for validating detection optics and camera settings
2. Confirmation that sub-millimolar concentrations produce strong contrast
3. Evidence supporting the choice of time points and detection strategy for the full platform
4. Representative images for inclusion in the project proposal

## Expected Results

- **Black precipitate** forms **rapidly (<5 minutes)** upon mixing Pb²⁺ and S²⁻ solutions
- Precipitate is **clearly visible at 0.5 mM Pb²⁺** in 1 molal NaCl
- Strong visual contrast (black solid against clear/slightly yellow solution) validates that the target sulfide phase produces robust signal at sub-millimolar concentrations
- Results align the detection strategy with the thermodynamic regimes identified computationally

## Experimental Design

### Conditions

These are small-scale vial tests (not a full well-plate experiment). Run in glass vials or small test tubes.

| Vial | Pb²⁺ (mM) | S²⁻ (mM) | NaCl (molal) | Total Vol (mL) | Expected Result |
|------|-----------|-----------|--------------|-----------------|-----------------|
| 1 | 0.5 | 1.0 | 1.0 | 5 | Black precipitate, rapid (<5 min) |
| 2 | 1.0 | 1.0 | 1.0 | 5 | Black precipitate, rapid, denser |
| 3 | 5.0 | 5.0 | 1.0 | 5 | Strong black precipitate, immediate |
| 4 | 0.5 | 1.0 | 0.0 | 5 | Black precipitate (no NaCl control) |
| 5 | 0.5 | 0.0 | 1.0 | 5 | Clear — no precipitate (negative control) |
| 6 | 0.0 | 1.0 | 1.0 | 5 | Clear — no precipitate (negative control) |

> **Key test:** Vial 1 (0.5 mM Pb²⁺, 1 mM S²⁻, 1 m NaCl) is the primary validation condition. If black PbS is clearly visible here within 5 minutes, the detection strategy is confirmed for sub-millimolar concentrations.

### Reagent Sources

| Reagent | Stock Concentration | Source Chemical | Notes |
|---------|-------------------|-----------------|-------|
| Pb²⁺ | 10 mM stock | Pb(NO₃)₂ (lead nitrate) | **Toxic, carcinogen** — handle with extreme care |
| S²⁻ | 10 mM stock | Na₂S·9H₂O (sodium sulfide nonahydrate) | **Corrosive, releases H₂S** — use fume hood |
| NaCl | 5 M stock | NaCl (sodium chloride) | Low hazard |
| DI water | — | — | For dilutions |

### Stock Solution Preparation

**Pb(NO₃)₂ stock (10 mM):**
- MW of Pb(NO₃)₂ = 331.2 g/mol
- Dissolve 0.0331 g in 10 mL DI water
- **Caution:** Toxic — weigh in fume hood, wear gloves

**Na₂S·9H₂O stock (10 mM):**
- MW of Na₂S·9H₂O = 240.18 g/mol
- Dissolve 0.0240 g in 10 mL DI water
- **⚠️ Must prepare in fume hood** — Na₂S releases H₂S gas on contact with water/acid
- Prepare fresh (Na₂S solutions oxidize over time)

**NaCl stock (5 M):**
- MW = 58.44 g/mol; dissolve 2.922 g in 10 mL DI water

### Per-Vial Preparation (5 mL Total)

For each vial, calculate volumes of Pb²⁺ stock (10 mM), S²⁻ stock (10 mM), NaCl stock (5 M), and DI water to reach target concentrations. Example for Vial 1:

| Component | Stock (mM/M) | Target | Volume |
|-----------|-------------|--------|--------|
| Pb(NO₃)₂ stock | 10 mM | 0.5 mM | 0.25 mL |
| Na₂S stock | 10 mM | 1.0 mM | 0.50 mL |
| NaCl stock | 5 M | 1.0 m (~1.0 M) | 1.00 mL |
| DI water | — | — | 3.25 mL |
| **Total** | | | **5.00 mL** |

## Safety Considerations

### ⚠️ This Experiment Requires a Fume Hood

Unlike Experiments 001 (Variant A) and 002, this experiment involves **sodium sulfide (Na₂S)** which releases **hydrogen sulfide (H₂S) gas** — a highly toxic gas that is **potentially lethal at high concentrations**. Additionally, **lead nitrate** is a toxic heavy metal compound and probable carcinogen.

**All preparation and mixing must be done inside a certified chemical fume hood.**

### Lead Nitrate — Pb(NO₃)₂ — **TOXIC, CARCINOGEN**

| Hazard | Detail |
|--------|--------|
| GHS classifications | Acute toxicity (oral, Category 4); Carcinogen (Category 1B); Reproductive toxin (Category 1A); Oxidizer; Aquatic toxicity (Category 1) |
| Signal word | **Danger** |
| Skin/eye contact | Irritant; causes serious eye irritation |
| Ingestion | **Toxic** — cumulative poison affecting nervous system, kidneys, blood |
| Inhalation | Harmful if dust is inhaled |
| Carcinogenicity | **Probable human carcinogen** (IARC Group 2A for lead compounds) |
| Reproductive toxicity | May damage fertility and the unborn child |
| Environmental | Very toxic to aquatic life with long-lasting effects |

**Handling:** Wear nitrile gloves, lab coat, splash goggles. **Weigh solid in fume hood** to avoid dust inhalation. Wash hands thoroughly. Do not eat, drink, or smoke when handling. Keep away from combustible materials (oxidizer).

### Sodium Sulfide — Na₂S — **CORROSIVE, H₂S HAZARD**

| Hazard | Detail |
|--------|--------|
| GHS classifications | Corrosive (Category 1A); Acute toxicity (oral, Category 3); Aquatic toxicity |
| Signal word | **Danger** |
| Skin/eye contact | **Causes severe burns** |
| Ingestion | Toxic if swallowed |
| H₂S release | **Releases highly toxic H₂S gas** on contact with acids or in moist air |
| Incompatibilities | Acids (violent H₂S evolution), oxidizers |

**⚠️ Critical:** Na₂S + acid → H₂S (toxic gas). H₂S is:
- Detectable by smell (rotten eggs) at <1 ppm
- **Dangerous at >10 ppm** (prolonged exposure)
- **Immediately dangerous to life at >100 ppm**
- **Olfactory fatigue occurs** — at high concentrations you STOP smelling it

**Handling:** Always use in fume hood. Wear nitrile gloves, lab coat, splash goggles, and face shield. Keep Na₂S solutions at neutral or basic pH (never acidify). Prepare solutions fresh.

### Lead Sulfide — PbS — Reaction Product

| Hazard | Detail |
|--------|--------|
| GHS classifications | Toxic (as lead compound) |
| Solubility | Extremely insoluble (Ksp ~3 × 10⁻²⁸) |
| Handling | Treat as toxic heavy metal waste |

### Sodium Nitrate — NaNO₃ — Reaction Byproduct

Low hazard at dilute concentrations (mild oxidizer in concentrated form).

### PPE Summary

- Nitrile gloves (double-gloving recommended for lead compounds)
- Lab coat
- Splash goggles
- Face shield (for Na₂S handling)
- Closed-toe shoes
- **Fume hood required for all preparation and mixing**

### Emergency Equipment

- Eyewash station and safety shower must be immediately accessible
- H₂S gas detector recommended in fume hood area
- Spill kit with appropriate absorbent
- First aid: flush affected area with water for ≥20 minutes; seek immediate medical attention for any lead or Na₂S exposure

### Waste Disposal

| Waste Stream | Disposal |
|-------------|----------|
| All vial contents (PbS precipitate + supernatant) | Collect as **heavy metal waste** (lead-containing); additionally label as sulfide-containing |
| Used glassware | Triple-rinse; collect rinse water as heavy metal waste |
| Used pipette tips / disposables | Heavy metal solid waste |
| Na₂S stock solution (unused) | Do NOT pour down drain; collect as sulfide waste |

**Never acidify lead-sulfide waste** — this would release H₂S gas.

Follow BYU Environmental Health & Safety (EH&S) guidelines for all waste disposal.

## Protocol

### A. Pre-Experiment Setup (Fume Hood)

1. Verify fume hood is certified and functioning
2. Set up H₂S detector if available
3. Prepare stock solutions inside fume hood (see [Stock Solution Preparation](#stock-solution-preparation))
4. Label 6 glass vials (scintillation vials or small test tubes)
5. Set up camera for photography (can photograph vials outside fume hood AFTER sealing)

### B. Mixing Protocol (Fume Hood)

**Important:** Add reagents in this order to minimize H₂S exposure:

1. **Add DI water** to each vial first
2. **Add NaCl stock** (non-hazardous)
3. **Add Pb(NO₃)₂ stock** (use fresh tip for each vial)
4. **Add Na₂S stock last** — this triggers precipitation and potential H₂S release
5. **Cap vials immediately** after adding Na₂S
6. Start timer

### C. Observation Protocol

1. Observe precipitate formation through vial walls in fume hood — note color and time
2. Record time to first visible precipitate for each vial
3. At 5 minutes, note precipitate status for all vials:
   - Color (black, gray, clear)
   - Amount (none, trace, moderate, heavy)
   - Settling behavior
4. Cap vials and remove from fume hood for photography (PbS is insoluble and non-volatile once formed)
5. Photograph all 6 vials against a white background with color calibration card
6. Photograph at additional time points if desired (15 min, 60 min) to document settling

### D. Data Collection

For each vial, record:
- **Time to first visible precipitate** (seconds)
- **5-minute precipitate score:** 0 = clear, 1 = faint/turbid, 2 = moderate, 3 = heavy black precipitate
- **Photograph** with color calibration reference
- **Visual contrast assessment:** Is the precipitate clearly distinguishable from background? (yes/no, with notes)

## Procurement

All reagents should be procured through **BYU Chem Stores** (see [Experiment 001](../001-agcl-formation/README.md#procurement) for contact details).

| Reagent | What to Request | Approx. Quantity | Special Notes |
|---------|----------------|------------------|---------------|
| Pb(NO₃)₂ (solid) | Lab-grade lead nitrate | 1–5 g | Toxic, carcinogen — request smallest amount |
| Na₂S·9H₂O (solid) | Lab-grade sodium sulfide nonahydrate | 5–10 g | Corrosive, H₂S hazard — store sealed |
| NaCl (solid) | Lab-grade sodium chloride | 10 g | May already have from Experiment 001 |
| DI water | From Chem Stores DI tap/carboy | ~100 mL | — |
| Glass vials | Scintillation vials with screw caps, ~20 mL | 6+ | For sealed observation after mixing |

## Relationship to Project Goals

This experiment maps directly to **Tier 1: Data Generation** in [opentrons-inorganic-wet-lab-agents.txt](../../opentrons-inorganic-wet-lab-agents.txt):
- **Reaction #7:** PbS formation (Pb(NO₃)₂ + (NH₄)₂S → black precipitate in the project doc; this experiment uses Pb(NO₃)₂ + Na₂S → PbS ↓ + 2 NaNO₃ as the sulfide source)
- Validates that black sulfide precipitates provide strong visual contrast at sub-millimolar concentrations
- Supports detection optics selection for the full platform
- Confirms measurement windows (precipitate visible within 5 minutes at target concentrations)
- Representative images support the project proposal
- Complements the white BaSO₄ precipitate data from Experiment 002 (black vs. white contrast range)

## Relationship to Experiment 002 (BaSO₄)

These two experiments are designed as complementary validations:

| Aspect | Experiment 002 (BaSO₄) | Experiment 003 (PbS) |
|--------|------------------------|----------------------|
| Scale | 96-well plate, 80 conditions | Small-scale vials, 6 conditions |
| Precipitate color | White | Black |
| Format | Systematic LHS design | Targeted spot checks |
| Purpose | Precipitation boundary mapping | Detection limit validation |
| Time scale | Up to 240 minutes | <5 minutes |
| Fume hood | Not required | **Required** (Na₂S / H₂S) |

Together, they validate the tractability of the measurement windows and confirm that both white and black precipitates produce strong contrast at the target concentrations, aligning the detection strategy with the thermodynamic regimes identified computationally.

## Next Steps

- [ ] Secure fume hood access
- [ ] Procure Pb(NO₃)₂ and Na₂S from BYU Chem Stores (smallest available quantities)
- [ ] Consult BYU EH&S on lead and sulfide waste disposal procedures
- [ ] Prepare stock solutions in fume hood
- [ ] Run vial tests and photograph
- [ ] Document results with representative images for proposal
- [ ] Assess whether to scale to a well-plate format based on vial test results
