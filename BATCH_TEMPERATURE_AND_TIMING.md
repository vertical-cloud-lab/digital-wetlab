# Batch Temperature Processing and Wait-Time Strategies

> **Context:** [digital-wetlab#11](https://github.com/vertical-cloud-lab/digital-wetlab/issues/11) raised several practical challenges around running experiments at multiple temperatures while managing time-course measurements (1, 5, 15, 60, 240 min), Bayesian optimization (BO) query times, and overall scheduling complexity.
>
> **Key constraints from the proposal:**
> - Temperature levels: 25, 60, 90 °C
> - Elevated-temperature experiments (60–90 °C) use sealed glass vials equilibrated in a heating block or oven — **not** 96-well plates on the OT-2
> - Room-temperature experiments use standard 96-well plates prepared by the OT-2
> - Time-resolved measurements at 1, 5, 15, 60, and 240 min post-mixing
> - A subset (~100 conditions) equilibrated 24–72 h in sealed glass vials to verify 240-min endpoint ≈ equilibrium
> - ~30,000 total measurements over 2 years; ~350 experimental plates + ~50 development plates
> - Bayesian optimization (SAASBO) guides adaptive follow-up after initial LHS campaign

---

## 1. Temperature Batching — "Campaign" Model

### Problem

The heater (heating block or oven) holds one temperature at a time. Running mixed-temperature experiments simultaneously is impractical.

### Proposed Strategy: Temperature Campaigns

Rather than interleaving temperatures within a day, **group all experiments at a given temperature into a "campaign."** This is already implied by the proposal timeline, where room-temperature mapping happens in Year 1 (Months 3–10) and temperature-dependent measurements in Year 2 (Months 13–18).

**Within Year 2, further organize by temperature:**

| Campaign | Temperature | Duration | Notes |
|----------|-------------|----------|-------|
| 1 (Year 1) | 25 °C | Months 3–10 | All LHS conditions at room temp; 96-well plates on OT-2 |
| 2 | 60 °C | Months 13–15 | Sealed glass vials; heating block at 60 °C |
| 3 | 90 °C | Months 15–18 | Same vials; heating block at 90 °C |

**Advantages:**
- No temperature switching during a workday — the heater stays at one setpoint
- Reduces equilibration dead time (heating block doesn't need to ramp between temperatures)
- Simplified scheduling: one temperature per campaign
- Consistent thermal environment for all samples in a batch

**Refinement — "temperature blocks" within a day:**
If a small number of conditions at multiple temperatures are needed on the same day (e.g., during BO-guided follow-up), designate morning and afternoon temperature blocks:
- **AM block:** heat to 60 °C, run that batch, measure through 240 min
- **PM block (next day or overlap):** heat to 90 °C

---

## 2. Mixing Workflow — Where Does Mixing Happen?

### Problem

Should solutions be mixed on a plate sitting on the heater, or mixed at room temperature and then transferred to the heater?

### Recommendation: Pre-Heat Reagents, Then Mix at Target Temperature (Isothermal Initiation)

> **Update:** An [Edison Scientific literature search](EDISON_HEATING_TIMING_ANALYSIS.md) found that thermal history during initial nucleation significantly affects which metastable solid phase forms, how quickly it transforms, and therefore the *apparent* Ksp and fitted Pitzer parameters — even over 4–72 h equilibration windows. Pre-heating reagents before mixing is preferred for thermodynamic parameter extraction.

For elevated-temperature experiments the proposal already specifies sealed glass vials (not 96-well plates). The recommended workflow is:

1. **Pre-heat stock solutions** in sealed bottles to the target temperature (e.g., 60 or 90 °C) in the heating block or water bath.
2. **Dispense and mix in pre-warmed vials** at the target temperature. Work quickly at the bench to minimize heat loss, or pipette inside a heated enclosure if feasible. (The OT-2 cannot pipette into a hot heating block, so elevated-temperature vial preparation is manual.)
3. **Seal the vials** with PTFE-lined screw caps immediately to contain H₂S.
4. **Return sealed vials to the heating block** at the target temperature.
5. **Start the clock** from the moment of mixing.
6. **Measure** by removing individual vials at each time point (1, 5, 15, 60, 240 min) and reading absorbance or scoring visually.

**Why this matters:** FeS precipitation proceeds through metastable phases (amorphous FeS → nanocrystalline mackinawite → greigite), following Ostwald's rule of stages. Mixing at 25 °C then heating creates a transient supersaturation ramp that can kinetically trap a different metastable phase than direct isothermal mixing at the target temperature. Since Pitzer parameter fitting assumes equilibrium with a known solid phase, trapping the wrong metastable phase biases both Ksp and interaction parameter estimates. See the [full Edison analysis](EDISON_HEATING_TIMING_ANALYSIS.md) for literature citations.

**For 25 °C experiments** (96-well plates), mixing happens directly on the plate via OT-2 aspiration/dispense cycles, and no heater is involved — thermal history is not a concern.

### Simpler Alternative: Mix at Room Temperature, Then Transfer

If pre-heating proves too complex for routine high-throughput work:
1. Dispense all components into 5 mL glass vials at 25 °C (via OT-2 or manual pipetting).
2. Seal the vials with PTFE-lined screw caps.
3. Transfer sealed vials to the pre-equilibrated heating block.
4. Allow extended equilibration (24–72 h) to ensure the system reaches true equilibrium and any metastable phases have transformed.

This approach is simpler but requires longer equilibration times to converge to the same endpoint. **Use extended equilibration times (24–72 h rather than 4 h) if mixing at room temperature.**

---

## 3. Time-Course Measurement Scheduling

### Problem

Measuring absorbance at 1, 5, 15, 60, and 240 minutes per sample creates a complex scheduling problem, especially if processing one sample at a time.

### Strategy A: Staggered-Start Batching (Recommended)

Prepare multiple samples with staggered start times so that measurement windows don't collide.

**Example schedule for a batch of 6 vials at 60 °C:**

| Vial | Mix time | 1 min | 5 min | 15 min | 60 min | 240 min |
|------|----------|-------|-------|--------|--------|---------|
| 1 | 0:00 | 0:01 | 0:05 | 0:15 | 1:00 | 4:00 |
| 2 | 0:06 | 0:07 | 0:11 | 0:21 | 1:06 | 4:06 |
| 3 | 0:12 | 0:13 | 0:17 | 0:27 | 1:12 | 4:12 |
| 4 | 0:18 | 0:19 | 0:23 | 0:33 | 1:18 | 4:18 |
| 5 | 0:24 | 0:25 | 0:29 | 0:39 | 1:24 | 4:24 |
| 6 | 0:30 | 0:31 | 0:35 | 0:45 | 1:30 | 4:30 |

With a 6-minute stagger, the early time points (1 min, 5 min) never overlap. A researcher can handle one measurement per minute comfortably. The late time points (60 min, 240 min) are spaced far enough apart that they are even easier to manage.

**Throughput:** 6 vials per 4.5-hour session → ~10–12 vials/day with two sessions.

### Strategy B: "96-Well Plate as Parallel Batch" (for 25 °C Experiments)

At room temperature, all 96 wells on a plate are prepared by the OT-2 in sequence. The sulfide (trigger reagent) is added last — well by well. The *entire plate* is then imaged at each time point:

- **t = 0 min:** Image immediately after completing sulfide dispensing
- **t = 1, 5, 15, 60, 240 min:** Image the full plate each time

This is exactly how the existing BaSO₄ protocol works (comments in `baso4_nacl_gradient_protocol.py`: "Image plate at: 0 min, 2 min, 10 min, 30 min"). **No per-well scheduling is needed** — all 96 wells start within the ~10-min dispensing window and are measured simultaneously via imaging.

For microplate reader: transfer the sealed plate to the reader at each time point. Total read time for 96 wells at 600 nm is ~30 s per plate.

### Strategy C: Simplified Time Points

If the full 5-point time course proves impractical for elevated-temperature vial experiments, simplify to fewer time points:

| Approach | Time points | Rationale |
|----------|-------------|-----------|
| Full | 1, 5, 15, 60, 240 min | Complete kinetics profile |
| Reduced | 5, 60, 240 min | Skip 1-min (hard to catch) and 15-min (interpolatable) |
| Endpoint-only | 240 min (+ 24–72 h subset) | Sufficient for equilibrium Pitzer parameters |

**Recommendation:** Use the full 5-point schedule for 96-well plates (room temp, camera imaging — nearly zero marginal cost per time point). Use the reduced or endpoint-only schedule for glass-vial experiments (elevated temp) where each measurement requires opening/removing individual vials.

---

## 4. Managing Scheduling Complexity

### Problem

Incorporating logic that constantly checks timing for when measurements need to be taken feels incredibly complex.

### Approach: Simple Timer-Based Checklists, Not Complex Software

For the scale of this project (~12 vials/day for elevated-temperature experiments), **a simple printed schedule or timer-based checklist** is more practical than custom scheduling software:

1. **Generate a printable schedule** (Python script) for each day's batch that lists exact wall-clock times for each measurement.
2. **Set phone/lab timers** for each measurement event.
3. **Record completion** by checking off the printed sheet and noting actual measurement time in the lab notebook.

**Example Python helper:**

```python
from datetime import datetime, timedelta

def generate_schedule(n_vials, stagger_min=6, time_points=[1, 5, 15, 60, 240]):
    """Print a measurement schedule for n_vials with staggered starts."""
    start = datetime.now().replace(second=0, microsecond=0) + timedelta(minutes=5)  # 5-min buffer for final setup
    for i in range(n_vials):
        mix_time = start + timedelta(minutes=i * stagger_min)
        print(f"\nVial {i+1} — mix at {mix_time.strftime('%H:%M')}")
        for tp in time_points:
            meas_time = mix_time + timedelta(minutes=tp)
            print(f"  {tp:>3d} min → measure at {meas_time.strftime('%H:%M')}")
```

For 96-well plate experiments at room temperature, scheduling is trivial: set 5 alarms after completing the plate.

### When Software Scheduling *Would* Help

If the project scales to running dozens of vials per day with overlapping time points across different temperature blocks, a simple event-driven scheduler could help. But start with the manual approach and only build software if it becomes a bottleneck.

---

## 5. Bayesian Optimization Computation Time

### Problem

Getting the next parameterization from Ax/BO with a high-dimensional search space could take a long time, creating idle periods.

### Context

- The experimental search space is 5D: [M²⁺], [HS⁻], ionic strength, pH, temperature
- The Pitzer parameter space for regression is 34D, but BO operates on the *experimental* design space, not the full parameter space
- SAASBO has been demonstrated for 23+ parameters (Baird et al., 2022)
- A single BO query on a 5D space with ~100–500 observations typically takes seconds to minutes on a standard workstation (8+ GB RAM, multi-core CPU)

### Strategies

**A. Batch BO (Recommended)**

Instead of querying BO for one experiment at a time, request a **batch of suggestions** (e.g., one plate's worth = 96 conditions). This amortizes the BO computation cost across many experiments. The Ax platform supports batch acquisition functions (e.g., q-Expected Improvement, q-Knowledge Gradient).

- Submit all previous data → request 96 new conditions → prepare one full plate → run → repeat
- BO computation for a 96-point batch on a 5D space: ~1–10 minutes
- No waiting between individual experiments for BO queries

**B. Asynchronous BO**

Run BO in the background while experiments are being measured. By the time the current plate's 240-minute measurements are complete, the next plate's conditions are already computed.

**Timeline overlap:**
```
Plate N:   [prepare]──[measure 1,5,15,60 min]────────[measure 240 min]
BO query:             [computing next batch]──[done]
Plate N+1:                                           [prepare]──...
```

The 240-minute measurement window provides ample time for BO computation.

**C. Pre-Computed Fallback Conditions**

Generate a set of quasi-random (Sobol/Halton) backup conditions in advance. If BO takes unexpectedly long, use these backup conditions rather than waiting. The proposal already mentions this fallback strategy.

**D. Decouple Temperature from BO**

The simplest approach: **fix temperature during each campaign** and run BO only over the remaining 4 experimental dimensions ([M²⁺], [HS⁻], ionic strength, pH). This:
- Reduces BO dimensionality from 5D to 4D (faster queries)
- Eliminates the need for BO to suggest different temperatures within a single plate
- Aligns with the campaign-based temperature batching (§1)

Temperature effects can be incorporated into the Pitzer regression (Aim 2) by comparing results across campaigns.

---

## 6. Putting It All Together — Recommended Workflow

### Room-Temperature Campaign (Year 1)

```
For each LHS batch (1 plate = 96 conditions):
  1. OT-2 prepares plate (~30 min dispensing)
  2. Image plate at t = 0 min (immediately after sulfide trigger)
  3. Set 4 timers: 1, 5, 15, 60 min
  4. Image plate at each timer → ~5 images per plate
  5. Set final timer: 240 min → image plate
  6. Transfer plate to microplate reader for quantitative absorbance
  7. Submit results to database
  8. While waiting for 240-min measurement: prepare next plate or run BO
```

**Throughput:** ~2 plates/day (accounting for 4-hour measurement window per plate), ~10 plates/week, ~200 plates in ~20 weeks. (Assumes 5 working days/week; adjust for holidays, equipment downtime, or shared-instrument scheduling.)

### Elevated-Temperature Campaign (Year 2)

```
Day plan:
  Morning:
    1. Set heating block to target temperature (e.g., 60 °C)
    2. Prepare 6–12 vials at room temp (OT-2 or manual)
    3. Seal vials, transfer to heating block
    4. Stagger starts by 6 min; measure at 5, 60, 240 min per vial
  
  Afternoon:
    5. Complete 240-min measurements for morning batch
    6. Prepare next day's vials or process data
    
  End of 60 °C campaign:
    7. Switch heating block to 90 °C for next campaign
```

**Throughput:** ~6–12 vials/day × ~3–4 conditions per vial = ~20–50 conditions/day. The elevated-temperature subset is smaller (~200–500 conditions total), so this is feasible within the 6-month window.

### BO Integration

```
After each batch of N plates:
  1. Upload all results to data pipeline
  2. Run batch BO (q-EI or q-KG) to suggest next 96–288 conditions
  3. While BO runs (~5–30 min), clean up and restock tips/plates
  4. Generate OT-2 protocol for next batch from BO suggestions
  5. Resume experimental cycle
```

---

## 7. Summary of Recommendations

| Challenge | Recommendation |
|-----------|---------------|
| Single-temperature heater | Temperature campaigns — run all conditions at one T before switching |
| Mixing workflow | Pre-heat reagents, mix at target temperature ([Edison analysis](EDISON_HEATING_TIMING_ANALYSIS.md)); or mix cold with extended 24–72 h equilibration |
| Time-course scheduling (96-well) | Image the whole plate at each time point — trivial scheduling |
| Time-course scheduling (vials) | Stagger starts by 6 min; use reduced time points (5, 60, 240 min) |
| Scheduling complexity | Printed timer-based checklists; no custom scheduling software needed |
| BO computation time | Batch BO (96 conditions at once); async computation during 240-min waits |
| BO dimensionality | Fix temperature per campaign → 4D BO instead of 5D |
| Dead time utilization | Prepare next batch or run BO during measurement wait periods |

---

## Open Questions

- [ ] Should we invest in a second heating block to run 60 °C and 90 °C in parallel? (Cost: ~$200–500 for a dry block heater)
- [ ] Is the 1-minute time point worth capturing for vial experiments, given the time to remove, read, and return a vial?
- [ ] For BO-guided elevated-temperature experiments, should temperature be a fixed campaign variable or an active BO dimension?
- [ ] What is the actual ramp time for our heating block from 60 °C to 90 °C? If fast (<30 min), within-day temperature switching becomes feasible.
- [ ] Should the 24–72 h equilibration subset use a separate dedicated oven to free up the primary heating block?
