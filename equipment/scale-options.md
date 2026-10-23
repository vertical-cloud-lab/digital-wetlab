# Scale Options — 1 mg Resolution, Higher Capacity

> **Context:** The current A&D HR-100A analytical balance (102 g × 0.1 mg) cannot
> accommodate stock-solution containers that exceed 102 g. We need a balance with
> at least 1 mg (0.001 g) readability and a capacity well above 102 g.
> Preference is to stay within the A&D product line.
>
> See [issue #9](https://github.com/vertical-cloud-lab/digital-wetlab/issues/9)
> and the originating
> [comment](https://github.com/vertical-cloud-lab/digital-wetlab/issues/1#issuecomment-4006372713).

## Current Balance

| Spec | Value |
|------|-------|
| Model | A&D HR-100A (Galaxy series) |
| Capacity | 102 g |
| Readability | 0.1 mg (0.0001 g) |
| Repeatability | 0.1 mg |
| Linearity | ±0.2 mg |
| Pan size | 90 mm diameter |
| Interface | RS-232C |
| Calibration | External |

The HR-100A is an analytical-grade balance ideal for sub-milligram work, but its
102 g capacity is too low for weighing stock-solution tubes/bottles that include
the container weight plus 15+ mL of solution.

## Recommended Option

### A&D FX-300iWP ⭐

**Why this model:** 320 g capacity with 1 mg readability — more than 3× the
current capacity while maintaining the precision needed for stock-solution
preparation. IP65-rated (waterproof/dustproof) is a plus for wet-lab
environments. This is the model suggested in the issue.

| Spec | Value |
|------|-------|
| Model | A&D FX-300iWP |
| Capacity | 320 g |
| Readability | 1 mg (0.001 g) |
| Repeatability | 1 mg |
| Linearity | ±2 mg |
| Pan size | 130 mm (5.12 in) diameter |
| Stabilization | ~1 second |
| Interface | RS-232C (standard); optional USB, Ethernet |
| IP rating | IP65 (waterproof / dustproof) |
| Calibration | External |
| Dimensions | 193 × 262.5 × 84.5 mm |
| Weight | ~2.5 kg |
| Warranty | 5 years |
| Approx. price | $1,500–$2,800 (varies by distributor) |
| Product page | <https://www.and-store.com/products/balances/details/?productid=3641> |

**Action:** @swcharles to request a quote from A&D for the FX-300iWP.

## Alternative Options (A&D FX-iWP Series)

All models in this family share the same compact form factor, IP65 rating, ~1 s
stabilization, RS-232C interface, and 5-year warranty.

| Model | Capacity | Readability | Pan size | Approx. price | Notes |
|-------|----------|-------------|----------|---------------|-------|
| FX-120iWP | 122 g | 0.001 g | 130 mm | ~$1,200–$1,800 | Only 20 g more than current; likely not enough |
| FX-200iWP | 220 g | 0.001 g | 130 mm | ~$1,050–$1,850 | Viable if 220 g is sufficient |
| **FX-300iWP** | **320 g** | **0.001 g** | **130 mm** | **~$1,500–$2,800** | **Recommended** |
| FX-1200iWP | 1,220 g | 0.01 g | 150 mm | ~$1,050–$1,450 | 10× readability sacrifice (10 mg) |
| FX-2000iWP | 2,200 g | 0.01 g | 150 mm | ~$1,200–$1,600 | Same 10 mg readability |
| FX-3000iWP | 3,200 g | 0.01 g | 150 mm | ~$1,300–$1,700 | Same 10 mg readability |

### Non-Waterproof Variant

If IP65 protection is not required, the standard **FX-300i** (same capacity and
readability, no waterproofing) is available at a lower price point (~$780–$1,600).

## Comparison with Current Balance

| | HR-100A (current) | FX-300iWP (recommended) |
|-|--------------------|------------------------|
| Capacity | 102 g | 320 g |
| Readability | 0.0001 g | 0.001 g |
| Waterproof | No | Yes (IP65) |
| Stabilization | ~2 s | ~1 s |
| Pan size | 90 mm | 130 mm |

**Trade-off:** We sacrifice one decimal place of resolution (0.1 mg → 1 mg) but
gain 3× the weighing capacity and IP65 protection. For stock-solution preparation
where target masses are in the gram range (e.g., 2.131 g Na₂SO₄, 3.664 g
BaCl₂·2H₂O, 4.383 g NaCl), 1 mg readability is more than adequate. The HR-100A
remains available for any sub-milligram work.

## Next Steps

- [ ] Get a quote from A&D for the FX-300iWP ([@swcharles](https://github.com/swcharles))
- [ ] Confirm whether 320 g capacity is sufficient for all anticipated containers
- [ ] Evaluate whether IP65 (waterproof) is needed or if the cheaper FX-300i suffices
- [ ] Purchase and integrate into lab workflow
