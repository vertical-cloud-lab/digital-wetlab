# Experiment 002: BaSO₄ Precipitation Boundary Mapping

> **Reaction:** Ba²⁺ (aq) + SO₄²⁻ (aq) → BaSO₄ (s) ↓
>
> **Observable:** White crystalline precipitate in supersaturated wells

## Objective

Map **precipitation intensity** for barium sulfate (BaSO₄) across a three-dimensional parameter space — Ba²⁺ concentration, SO₄²⁻ concentration, and NaCl ionic strength — using a 96-well plate with 80 Latin hypercube-sampled conditions. Time-lapse imaging at 5, 15, 60, and 240 minutes will support subsequent computer-vision analysis and validate measurement windows for the full platform.

> **Note:** PHREEQC Pitzer modeling confirms that **all 80 LHS wells are supersaturated** (SI 2.6–5.8) at the current parameter ranges (0.1–50 mM). BaSO₄'s extremely low Ksp (~1.1 × 10⁻¹⁰) means the undersaturation boundary lies near 10–140 µM (depending on NaCl), well below the minimum achievable with 1.0 M stocks and a P20 pipette. This design therefore maps **precipitation intensity and kinetics** across the supersaturated regime rather than locating a binary precipitation boundary. See [Alternative: Boundary-Crossing Design](#alternative-boundary-crossing-design) below for a modified design using 1 mM intermediate stocks that can span the actual boundary.

## Expected Results

All 80 LHS wells are predicted to be supersaturated and should display **visible white crystalline precipitate by 240 minutes**, with precipitate mass varying across wells depending on the limiting reagent concentration. Wells with low Ba²⁺ or SO₄²⁻ (~0.1 mM) may show faint or delayed precipitation despite being thermodynamically supersaturated. Time-lapse imaging should reveal a gradient of precipitation intensity and nucleation kinetics across the parameter space.

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

- **Format:** 96-well plate (clear flat-bottom — PS recommended for imaging, PP also compatible; see [Well Plate Material](#well-plate-material))
- **Wells 1–80:** LHS-sampled conditions (one condition per well)
- **Wells 81–84:** Negative controls (Ba²⁺ only, no SO₄²⁻)
- **Wells 85–88:** Negative controls (SO₄²⁻ only, no Ba²⁺)
- **Wells 89–92:** Blank controls (NaCl solution only, no Ba²⁺ or SO₄²⁻)
- **Wells 93–96:** Positive controls (high Ba²⁺ + high SO₄²⁻, known supersaturation)

> **Note:** A 96-well plate is preferred over a 384-well plate for this experiment because the larger well volume (~200–300 µL) better accommodates the wide concentration ranges and provides clearer imaging of white crystalline BaSO₄ precipitate against background.

### Well Plate Material

**Polypropylene (PP)** is recommended:

| Property | Polypropylene (PP) | Polystyrene (PS) |
|----------|-------------------|------------------|
| Chemical resistance | Excellent — inert to all reagents (BaCl₂, Na₂SO₄, NaCl, BaSO₄) | Good — compatible with aqueous salt solutions at these concentrations |
| Optical clarity | Translucent to clear (clear PP available) | Excellent — naturally transparent |
| Temperature range | –20°C to 121°C | –20°C to 70°C |
| Solvent resistance | Resistant to most organic solvents | Attacked by organic solvents (not relevant here) |
| Cost | Moderate | Low |
| BaSO₄ adhesion | Low — precipitate stays suspended or settles loosely | Low |

**Either PP or PS works** for this experiment since all reagents are aqueous inorganic salts at moderate concentrations. The key consideration is:

- **For imaging (recommended):** Clear **PS** flat-bottom plates (e.g., Corning 3596, Greiner 655101) provide the best optical clarity for camera-based detection of white BaSO₄ precipitate. PS is fully compatible with BaCl₂, Na₂SO₄, and NaCl aqueous solutions.
- **For maximum chemical versatility:** **PP** plates (e.g., Greiner 781209-style) are the safer default if you plan to reuse plate designs across experiments that may involve organic solvents or more aggressive reagents later.
- **For the custom Formlabs clear resin v4 plate:** Compatible with all reagents in this experiment (see [Formlabs chemical compatibility chart](https://formlabs.com/materials/standard/#clear-resin) for clear resin v4). The resin's optical clarity is comparable to PS.

> **Bottom line:** If using a commercial plate, choose clear PS for best imaging. If using the custom 3D-printed plate from Experiment 001, it works here too (just note the well volume differences between 384- and 96-well formats).

## Reagents

### Stock Solutions

| Reagent | Target Stocks | Volume | Notes |
|---------|--------------|--------|-------|
| BaCl₂ (barium chloride) | 1.0 M stock → dilute to 0.1–50 mM | 15 mL | **Toxic** — handle with care |
| Na₂SO₄ (sodium sulfate) | 1.0 M stock → dilute to 0.1–50 mM | 15 mL | Low hazard |
| NaCl (sodium chloride) | 5 M stock → dilute to 0–3 molal | 15 mL | Low hazard |
| DI water | For dilutions and blanks | 15 mL | — |

> **Why 1.0 M stocks?** At 200 µL/well, reaching 50 mM Ba²⁺ from a 100 mM stock would require 100 µL, leaving insufficient volume for SO₄²⁻ and NaCl. With 1.0 M stocks, 50 mM needs only 10 µL, leaving ample room for other components. Worst case: 10 µL BaCl₂ + 10 µL Na₂SO₄ + 120 µL NaCl + 60 µL water = 200 µL.
>
> **Volume note:** All stocks are prepared in 15 mL to match the custom AC 6-tube rack (15 mL tubes) used on the OT-2 deck (slot 5). 15 mL is sufficient for a full 96-well plate at 200 µL/well (max ~2 mL of any single stock across all wells, worst case).

### Preparation

All stock solutions should be prepared in **15 mL volumes** (matching the 15 mL tube rack on the OT-2).

**BaCl₂ stock (1.0 M) — 15 mL:**
- MW of BaCl₂·2H₂O = 244.26 g/mol
- Dissolve **3.664 g** BaCl₂·2H₂O in 15 mL DI water
- Concentration: 24.426 g / 100 mL (equivalent)
- **Caution:** BaCl₂ is toxic — wear gloves, goggles, and work in a well-ventilated area

**Na₂SO₄ stock (1.0 M) — 15 mL:**
- MW of Na₂SO₄ = 142.04 g/mol
- Dissolve **2.131 g** Na₂SO₄ in 15 mL DI water
- Concentration: 14.204 g / 100 mL (equivalent)

**NaCl stock (5 M) — 15 mL:**
- MW of NaCl = 58.44 g/mol
- Dissolve **4.383 g** NaCl in 15 mL DI water
- Concentration: 29.22 g / 100 mL (equivalent)

### Solid Particulates

**All stock solutions must be fully dissolved before loading into the OT-2 tube rack.** Undissolved solids would:
1. Make the actual dissolved concentration lower than intended
2. Risk clogging pipette tips during dispensing
3. Add noise to camera-based precipitate detection

All four compounds are well within their solubility limits at 15 mL volumes and room temperature (~20–25°C):

| Stock Solution | Amount in 15 mL | Solubility at 20°C | Margin |
|---------------|-----------------|-------------------|--------|
| BaCl₂·2H₂O (1.0 M) | 3.664 g / 15 mL | ~5.6 g / 15 mL | 1.5× below limit |
| Na₂SO₄ (1.0 M) | 2.131 g / 15 mL | ~2.9 g / 15 mL | 1.4× below limit |
| NaCl (5 M) | 4.383 g / 15 mL | ~5.4 g / 15 mL | 1.2× below limit |

If any solid remains after mixing, stir or gently warm to ~30°C until fully dissolved, then cool to room temperature before use. **Do not load solutions with visible particulates into the OT-2.**

> **Na₂SO₄ note:** Anhydrous Na₂SO₄ can be slow to dissolve. Stir for 2–3 minutes. If using Na₂SO₄·10H₂O (Glauber's salt) instead, use 4.831 g in 15 mL (MW = 322.20 g/mol).

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
3. Prepare stock solutions (BaCl₂ 1.0 M, Na₂SO₄ 1.0 M, NaCl 5 M)
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

| Reagent | What to Request | Amount for 15 mL Stock |
|---------|----------------|----------------------|
| BaCl₂·2H₂O (solid) | Lab-grade barium chloride dihydrate | 3.664 g (→ 1.0 M in 15 mL) |
| Na₂SO₄ (solid) | Lab-grade anhydrous sodium sulfate | 2.131 g (→ 1.0 M in 15 mL) |
| NaCl (solid) | Lab-grade sodium chloride | 4.383 g (→ 5 M in 15 mL) |
| DI water | From Chem Stores DI tap/carboy | ~100 mL (stocks + rinse) |

## Relationship to Project Goals

This experiment maps directly to **Tier 1: Data Generation** in [opentrons-inorganic-wet-lab-agents.txt](../../opentrons-inorganic-wet-lab-agents.txt):
- **Reaction #5:** BaSO₄ formation (Ba(NO₃)₂ + H₂SO₄ → white precipitate in the project doc; this experiment uses BaCl₂ + Na₂SO₄ → BaSO₄ ↓ + 2 NaCl to avoid acid handling)
- Provides systematic precipitation data across concentration and ionic strength space
- Time-lapse images feed the computer-vision analysis pipeline
- The ionic strength (NaCl) dimension connects to activity coefficient effects relevant to Tier 3 thermodynamic modeling

## Alternative: Boundary-Crossing Design

The primary LHS design above uses 1.0 M stocks, which limits the minimum achievable well concentration to ~10 mM — far above the BaSO₄ undersaturation boundary (~12–140 µM depending on NaCl). To **actually locate the precipitation boundary**, use diluted intermediate stocks:

### PHREEQC-Predicted Boundary (SI = 0, equal [Ba²⁺] = [SO₄²⁻])

| NaCl (m) | Boundary Concentration |
|----------|----------------------|
| 0 | 12 µM (0.012 mM) |
| 1 | 102 µM (0.10 mM) |
| 3 | 140 µM (0.14 mM) |

NaCl raises the effective Ksp ~10× via activity coefficients (Pitzer model).

### 1 mM Intermediate Stocks

Dilute the 1.0 M primary stocks 1000× to create 1 mM intermediates:

| Tube | Stock | Prep (15 mL) |
|------|-------|-------------|
| A | BaCl₂ 1 mM | 15 µL of 1.0 M stock + 14.985 mL DI water |
| B | Na₂SO₄ 1 mM | 15 µL of 1.0 M stock + 14.985 mL DI water |
| C | NaCl 5 M | 4.383 g NaCl in 15 mL (same as primary design) |
| D | DI water | — |

### P20 Dispense Range with 1 mM Stocks (200 µL wells)

| P20 Dispense | Well Concentration | SI at NaCl = 0 m | SI at NaCl = 3 m |
|-------------|-------------------|-----------------|-----------------|
| 2 µL | **0.01 mM (10 µM)** | **−0.18** (undersaturated ✓) | −2.29 |
| 5 µL | 0.025 mM (25 µM) | +0.60 | −1.50 |
| 10 µL | 0.05 mM (50 µM) | +1.18 | −0.89 |
| 20 µL | **0.1 mM (100 µM)** | +1.75 | **−0.29** (undersaturated ✓) |

A 1 mM stock with P20 dispenses of 2–20 µL in 200 µL wells spans the **entire precipitation boundary** across all NaCl levels. The remaining ~180 µL is filled with NaCl stock and DI water via multiple P20 dispenses (10 × 20 µL = 200 µL total).

> **Two spare tube positions** remain in the AC 6-tube rack for higher-concentration stocks if you want to include both boundary-crossing and heavily-supersaturated conditions in the same plate.

## Next Steps

- [ ] Generate LHS design matrix and calculate per-well volumes
- [ ] Procure BaCl₂, Na₂SO₄, NaCl from BYU Chem Stores
- [ ] Prepare stock solutions
- [ ] Write OT-2 protocol script (Python, Opentrons API) for P300 + 96-well plate
- [ ] Set up camera for time-lapse imaging at 4 time points
- [ ] Run experiment and collect images
- [ ] Extract RGB data and precipitate scores from images
- [ ] Map precipitation boundary and compare to theoretical Ksp
