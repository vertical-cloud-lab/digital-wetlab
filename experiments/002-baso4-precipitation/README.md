# Experiment 002: BaSO₄ Precipitation Boundary Mapping

> **Reaction:** Ba²⁺ (aq) + SO₄²⁻ (aq) → BaSO₄ (s) ↓
>
> **Observable:** White crystalline precipitate in supersaturated wells

## Objective

Map the precipitation boundary for barium sulfate (BaSO₄) across a three-dimensional parameter space — Ba²⁺ concentration, SO₄²⁻ concentration, and NaCl ionic strength — using a 96-well plate with 80 Latin hypercube-sampled conditions. Time-lapse imaging at 5, 15, 60, and 240 minutes will support subsequent computer-vision analysis and validate measurement windows for the full platform.

## Expected Results

All supersaturated wells should display **visible white crystalline precipitate by 240 minutes**. The Latin hypercube sampling design is expected to reveal a clear precipitation boundary separating clear (undersaturated) wells from precipitated (supersaturated) wells, consistent with the BaSO₄ Ksp (~1.1 × 10⁻¹⁰ at 25°C).

## Experimental Design

### Parameter Space

| Variable | Range | Units | Notes |
|----------|-------|-------|-------|
| Ba²⁺ concentration | 0.1–50 mM | mM | Source: BaCl₂ stock solution |
| SO₄²⁻ concentration | 0.1–50 mM | mM | Source: Na₂SO₄ stock solution |
| NaCl concentration | 0–3 | molal (m) | Ionic strength modifier |

### Latin Hypercube Sampling (LHS)

Use 80 conditions sampled via LHS across the 3 variables. This provides efficient, space-filling coverage of the parameter space without requiring a full factorial design (which would need thousands of conditions).

**Generating the design matrix (Python):**

```python
from scipy.stats import qmc
import numpy as np

sampler = qmc.LatinHypercube(d=3, seed=42)
sample = sampler.random(n=80)

# Scale to physical ranges
l_bounds = [0.1, 0.1, 0.0]    # [Ba²⁺ mM, SO₄²⁻ mM, NaCl molal]
u_bounds = [50.0, 50.0, 3.0]
conditions = qmc.scale(sample, l_bounds, u_bounds)

# conditions is an 80×3 array:
#   Column 0: Ba²⁺ (mM)
#   Column 1: SO₄²⁻ (mM)
#   Column 2: NaCl (molal)
```

### Plate Layout

- **Format:** 96-well plate (polypropylene, clear)
- **Wells 1–80:** LHS-sampled conditions (one condition per well)
- **Wells 81–84:** Negative controls (Ba²⁺ only, no SO₄²⁻)
- **Wells 85–88:** Negative controls (SO₄²⁻ only, no Ba²⁺)
- **Wells 89–92:** Blank controls (NaCl solution only, no Ba²⁺ or SO₄²⁻)
- **Wells 93–96:** Positive controls (high Ba²⁺ + high SO₄²⁻, known supersaturation)

> **Note:** A 96-well plate is preferred over a 384-well plate for this experiment because the larger well volume (~200–300 µL) better accommodates the wide concentration ranges and provides clearer imaging of white crystalline BaSO₄ precipitate against background.

## Reagents

### Stock Solutions

| Reagent | Target Stocks | Quantity Needed | Notes |
|---------|--------------|-----------------|-------|
| BaCl₂ (barium chloride) | 100 mM stock → dilute to 0.1–50 mM | ~50 mL | **Toxic** — handle with care |
| Na₂SO₄ (sodium sulfate) | 100 mM stock → dilute to 0.1–50 mM | ~50 mL | Low hazard |
| NaCl (sodium chloride) | 5 M stock → dilute to 0–3 molal | ~100 mL | Low hazard |
| DI water | For dilutions and blanks | ~200 mL | — |

### Preparation

**BaCl₂ stock (100 mM):**
- MW of BaCl₂·2H₂O = 244.26 g/mol
- Dissolve 2.443 g in 100 mL DI water
- **Caution:** BaCl₂ is toxic — wear gloves, goggles, and work in a well-ventilated area

**Na₂SO₄ stock (100 mM):**
- MW of Na₂SO₄ = 142.04 g/mol
- Dissolve 1.420 g in 100 mL DI water

**NaCl stock (5 M):**
- MW of NaCl = 58.44 g/mol
- Dissolve 29.22 g in 100 mL DI water

**Working solutions:** Prepare each well's working concentrations by serial dilution from stock solutions using the OT-2. The OT-2 protocol should calculate and dispense the appropriate volumes of each stock + DI water to achieve the LHS-specified concentrations in each well.

### Total Volume per Well

Use 200 µL total volume per well (standard for 96-well plate format with P300 pipette). Each well receives calculated volumes of BaCl₂ stock, Na₂SO₄ stock, NaCl stock, and DI water that sum to 200 µL while achieving the target concentrations.

## Equipment

### Required
- **OT-2 liquid handling robot** with **P300 single-channel pipette** (20–300 µL range)
- **Opentrons 300 µL tips** (standard PP tips — adequate for all reagents)
- **96-well plate** (polypropylene, clear flat-bottom)
- **Camera** (positioned above for time-lapse imaging at 5, 15, 60, 240 min)
- **Reagent reservoirs** or Eppendorf tubes for stock solutions

### Optional
- **P20 pipette** for precise small-volume additions at low concentrations
- **Plate reader** or spectrometer for quantitative turbidity measurements
- **Color calibration card** in each image frame

## Safety Considerations

### Barium Chloride (BaCl₂) — **TOXIC**

| Hazard | Detail |
|--------|--------|
| GHS classifications | Acute toxicity (oral, inhalation), Category 4 |
| Signal word | Warning |
| Skin/eye contact | Irritant; may cause redness and discomfort |
| Ingestion | **Toxic** — affects nervous system, heart, and kidneys; potentially fatal at moderate doses |
| Inhalation | Harmful if dust is inhaled |
| Environmental | Harmful to aquatic life |

**Handling:** Wear nitrile gloves, lab coat, and splash goggles. Avoid creating dust when weighing solid BaCl₂. Work in a well-ventilated area. Wash hands thoroughly after handling.

> **Fume hood:** Not strictly required for aqueous BaCl₂ solutions (no volatile components), but recommended when weighing solid BaCl₂ to avoid dust inhalation.

### Sodium Sulfate (Na₂SO₄)

| Hazard | Detail |
|--------|--------|
| GHS classifications | Not classified as hazardous (at lab concentrations) |
| Skin/eye contact | Mild irritant at high concentrations |
| Ingestion | Low toxicity |

**Handling:** Standard lab PPE. No special precautions beyond good lab practice.

### Sodium Chloride (NaCl)

Not classified as hazardous. Standard lab PPE.

### Barium Sulfate (BaSO₄) — Reaction Product

| Hazard | Detail |
|--------|--------|
| GHS classifications | Not classified as hazardous |
| Solubility | Extremely insoluble (Ksp ~1.1 × 10⁻¹⁰) |
| Toxicity | Non-toxic due to insolubility; used medically as a radiocontrast agent |

**Note:** While BaSO₄ itself is non-toxic, the unreacted Ba²⁺ remaining in solution in undersaturated wells IS toxic. All wells must be treated as barium-containing waste.

### PPE Summary

- Nitrile gloves (required — BaCl₂ is toxic)
- Lab coat
- Splash goggles
- Closed-toe shoes

### Waste Disposal

| Waste Stream | Disposal |
|-------------|----------|
| All well contents (precipitate + supernatant) | Collect as **heavy metal waste** (barium-containing) |
| Used pipette tips | If contaminated with Ba²⁺, dispose in heavy metal solid waste |
| Rinse water | Collect if potentially contaminated with Ba²⁺; do not pour down drain |

Follow BYU Environmental Health & Safety (EH&S) guidelines for all waste disposal.

## Protocol

### A. Pre-Experiment Setup

1. Generate the 80-condition LHS design matrix using the Python script above
2. Calculate required volumes of each stock solution per well to achieve target concentrations in 200 µL total
3. Prepare stock solutions (BaCl₂ 100 mM, Na₂SO₄ 100 mM, NaCl 5 M)
4. Set up OT-2 with P300 pipette, tip rack, reagent reservoirs, and 96-well plate
5. Position camera for time-lapse imaging

### B. Dispensing Protocol (OT-2)

1. **Dispense NaCl and DI water first** to all 96 wells (sets ionic strength background)
2. **Add Ba²⁺ (BaCl₂ stock)** to wells 1–80, 81–84, and 93–96 using fresh tips for each well
3. **Add SO₄²⁻ (Na₂SO₄ stock)** to wells 1–80, 85–88, and 93–96 using fresh tips — **this triggers precipitation**
4. Start timer immediately after SO₄²⁻ addition is complete

> **Tip:** Add Na₂SO₄ to all wells in rapid succession (minimize time between first and last well) so the time-lapse reference point is consistent across wells.

### C. Imaging Protocol

Capture full-plate images at the following time points:

| Time Point | Minutes | Purpose |
|-----------|---------|---------|
| T1 | 5 min | Early nucleation — detect fast-precipitating (highly supersaturated) wells |
| T2 | 15 min | Growth phase — precipitation boundary becoming visible |
| T3 | 60 min | Most supersaturated wells should show precipitate |
| T4 | 240 min | Final state — all supersaturated wells expected to show visible white crystalline precipitate |

**Camera settings:**
- Fixed position, consistent lighting for all time points
- Include color calibration card in frame
- Save images with timestamps in filenames

### D. Data Collection

For each well at each time point, record:
- **Binary precipitate score:** 0 = clear, 1 = visible precipitate
- **Precipitate intensity:** 0 = none, 1 = faint/turbid, 2 = moderate, 3 = strong crystalline
- **RGB values** from standardized ROI in each well
- **Well conditions** from the LHS design matrix (Ba²⁺, SO₄²⁻, NaCl concentrations)

### E. Analysis

1. **Precipitation boundary mapping:** Plot Ba²⁺ vs. SO₄²⁻ (colored by precipitate/no-precipitate) at each time point, with NaCl as a third dimension
2. **Compare to Ksp:** The theoretical boundary is [Ba²⁺][SO₄²⁻] = Ksp. NaCl ionic strength shifts the effective Ksp via activity coefficients — the experimental boundary should show this shift
3. **Computer vision pipeline:** Train/validate image classifiers on the T4 (240 min) images as ground truth, then test on earlier time points
4. **Time-resolved kinetics:** Track which wells precipitate at T1 vs. T2 vs. T3 vs. T4 to map nucleation kinetics

## Procurement

All reagents should be procured through **BYU Chem Stores** (see [Experiment 001](../001-agcl-formation/README.md#procurement) for contact details).

| Reagent | What to Request | Approx. Quantity |
|---------|----------------|------------------|
| BaCl₂·2H₂O (solid) | Lab-grade barium chloride dihydrate | 5–10 g |
| Na₂SO₄ (solid) | Lab-grade anhydrous sodium sulfate | 5–10 g |
| NaCl (solid) | Lab-grade sodium chloride | 50 g |
| DI water | From Chem Stores DI tap/carboy | ~500 mL |

## Relationship to Project Goals

This experiment maps directly to **Tier 1: Data Generation** in [opentrons-inorganic-wet-lab-agents.txt](../../opentrons-inorganic-wet-lab-agents.txt):
- **Reaction #5:** BaSO₄ formation (Ba(NO₃)₂ + H₂SO₄ → white precipitate in the project doc; this experiment uses BaCl₂ + Na₂SO₄ → BaSO₄ ↓ + 2 NaCl to avoid acid handling)
- Provides systematic precipitation data across concentration and ionic strength space
- Time-lapse images feed the computer-vision analysis pipeline
- The ionic strength (NaCl) dimension connects to activity coefficient effects relevant to Tier 3 thermodynamic modeling

## Next Steps

- [ ] Generate LHS design matrix and calculate per-well volumes
- [ ] Procure BaCl₂, Na₂SO₄, NaCl from BYU Chem Stores
- [ ] Prepare stock solutions
- [ ] Write OT-2 protocol script (Python, Opentrons API) for P300 + 96-well plate
- [ ] Set up camera for time-lapse imaging at 4 time points
- [ ] Run experiment and collect images
- [ ] Extract RGB data and precipitate scores from images
- [ ] Map precipitation boundary and compare to theoretical Ksp
