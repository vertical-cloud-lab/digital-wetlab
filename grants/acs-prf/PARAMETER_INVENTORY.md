# Pitzer Parameter Inventory (~48 Target Parameters)

> **Project:** Pitzer Ion-Interaction Framework for Sulfide-Mineral Precipitation in Produced-Water Brines
>
> **Source:** Enumerated from proposal text (drafts/main_proposal_final.tex), Edison Scientific searches, and Pitzer formalism conventions.
>
> **Key references:** Pitzer & Mayorga (1973), Kan et al. (2019), Wang (2024), Woosley & Millero (2013), Felmy et al. (2000), Mgaidi et al. (1991)

---

## Summary

| Category                                  | Count   | Prior Estimates            | To Measure |
| ----------------------------------------- | ------- | -------------------------- | ---------- |
| Inorganic binary (β⁰, β¹, Cᶲ)             | 6       | 3 (Wang 2024: Fe²⁺–HS⁻)    | 3          |
| Inorganic cation–cation mixing (θ, ψ)     | 8       | 0                          | 8          |
| Neutral-species (λ, ζ) for FeS⁰ₐq, PbS⁰ₐq | 8       | 0                          | 8          |
| Pb²⁺–Cl⁻ temperature-dependent            | 3       | 3 (Woosley & Millero 2013) | 0 (refine) |
| Metal–hydroxide corrections               | 2       | 0                          | 2          |
| Pb²⁺–SO₄²⁻ binary                         | 3       | 0                          | 3          |
| PbCl₂⁰ neutral-species                    | 4       | 0                          | 4          |
| **Inorganic subtotal**                    | **34**  | **6**                      | **28**     |
| Organic acid–metal binary (β⁰, β¹, Cᶲ)    | 12      | 0                          | 12         |
| Sulfide–carboxylate mixing (θ)            | ~2      | 0                          | ~2         |
| **Organic acid subtotal**                 | **~14** | **0**                      | **~14**    |
| **Grand total**                           | **~48** | **6**                      | **~42**    |

---

## A. Inorganic Metal–Sulfide Parameters (34)

### A1. Binary parameters (β⁰, β¹, Cᶲ) — 6 parameters

These describe direct cation–anion interactions in solution.

| #   | Parameter    | Ion Pair | Status                     | Notes                                                |
| --- | ------------ | -------- | -------------------------- | ---------------------------------------------------- |
| 1   | β⁰(Fe²⁺–HS⁻) | Fe²⁺–HS⁻ | Prior estimate (Wang 2024) | Wang fit to 154 data points, 0–5 mol/kg, 23–125 °C   |
| 2   | β¹(Fe²⁺–HS⁻) | Fe²⁺–HS⁻ | Prior estimate (Wang 2024) | Will be used as initial values and benchmarked       |
| 3   | Cᶲ(Fe²⁺–HS⁻) | Fe²⁺–HS⁻ | Prior estimate (Wang 2024) | Mean SI error ±0.015 in Wang's framework             |
| 4   | β⁰(Pb²⁺–HS⁻) | Pb²⁺–HS⁻ | **Unmeasured**             | No Pb²⁺ parameters of any kind in PHREEQC pitzer.dat |
| 5   | β¹(Pb²⁺–HS⁻) | Pb²⁺–HS⁻ | **Unmeasured**             | Most critical gap — Pb²⁺ system entirely absent      |
| 6   | Cᶲ(Pb²⁺–HS⁻) | Pb²⁺–HS⁻ | **Unmeasured**             |                                                      |

### A2. Cation–cation mixing parameters (θ, ψ) — 8 parameters

These describe how metal cations interact with matrix cations (Na⁺, Ca²⁺) in the presence of anions.

| #   | Parameter        | Interaction                  | Status         | Notes                             |
| --- | ---------------- | ---------------------------- | -------------- | --------------------------------- |
| 7   | θ(Fe²⁺–Na⁺)      | Fe²⁺/Na⁺ like-charge mixing  | **Unmeasured** | Important above I ~ 2 molal       |
| 8   | θ(Fe²⁺–Ca²⁺)     | Fe²⁺/Ca²⁺ like-charge mixing | **Unmeasured** | Relevant for CaCl₂-bearing brines |
| 9   | θ(Pb²⁺–Na⁺)      | Pb²⁺/Na⁺ like-charge mixing  | **Unmeasured** |                                   |
| 10  | θ(Pb²⁺–Ca²⁺)     | Pb²⁺/Ca²⁺ like-charge mixing | **Unmeasured** |                                   |
| 11  | ψ(Fe²⁺–Na⁺–Cl⁻)  | Fe²⁺/Na⁺/Cl⁻ ternary mixing  | **Unmeasured** |                                   |
| 12  | ψ(Fe²⁺–Ca²⁺–Cl⁻) | Fe²⁺/Ca²⁺/Cl⁻ ternary mixing | **Unmeasured** |                                   |
| 13  | ψ(Pb²⁺–Na⁺–Cl⁻)  | Pb²⁺/Na⁺/Cl⁻ ternary mixing  | **Unmeasured** |                                   |
| 14  | ψ(Pb²⁺–Ca²⁺–Cl⁻) | Pb²⁺/Ca²⁺/Cl⁻ ternary mixing | **Unmeasured** |                                   |

### A3. Neutral-species parameters (λ, ζ) for aqueous complexes — 8 parameters

These describe how uncharged aqueous complexes (FeS⁰ₐq, PbS⁰ₐq) interact with surrounding ions.

| #   | Parameter            | Species / Interaction | Status         | Notes |
| --- | -------------------- | --------------------- | -------------- | ----- |
| 15  | λ(FeS⁰ₐq, Na⁺)       | FeS⁰ₐq–Na⁺            | **Unmeasured** |       |
| 16  | λ(FeS⁰ₐq, Cl⁻)       | FeS⁰ₐq–Cl⁻            | **Unmeasured** |       |
| 17  | ζ(FeS⁰ₐq, Na⁺, Cl⁻)  | FeS⁰ₐq ternary        | **Unmeasured** |       |
| 18  | ζ(FeS⁰ₐq, Ca²⁺, Cl⁻) | FeS⁰ₐq ternary        | **Unmeasured** |       |
| 19  | λ(PbS⁰ₐq, Na⁺)       | PbS⁰ₐq–Na⁺            | **Unmeasured** |       |
| 20  | λ(PbS⁰ₐq, Cl⁻)       | PbS⁰ₐq–Cl⁻            | **Unmeasured** |       |
| 21  | ζ(PbS⁰ₐq, Na⁺, Cl⁻)  | PbS⁰ₐq ternary        | **Unmeasured** |       |
| 22  | ζ(PbS⁰ₐq, Ca²⁺, Cl⁻) | PbS⁰ₐq ternary        | **Unmeasured** |       |

### A4. Pb²⁺–Cl⁻ temperature-dependent parameters — 3 parameters

| #   | Parameter       | Ion Pair | Status                                  | Notes                     |
| --- | --------------- | -------- | --------------------------------------- | ------------------------- |
| 23  | β⁰(Pb²⁺–Cl⁻, T) | Pb²⁺–Cl⁻ | Prior estimate (Woosley & Millero 2013) | Will refine with new data |
| 24  | β¹(Pb²⁺–Cl⁻, T) | Pb²⁺–Cl⁻ | Prior estimate (Woosley & Millero 2013) |                           |
| 25  | Cᶲ(Pb²⁺–Cl⁻, T) | Pb²⁺–Cl⁻ | Prior estimate (Woosley & Millero 2013) |                           |

### A5. Metal–hydroxide corrections — 2 parameters

| #   | Parameter                  | Interaction | Status         | Notes                                        |
| --- | -------------------------- | ----------- | -------------- | -------------------------------------------- |
| 26  | β⁰(Fe²⁺–OH⁻) or correction | Fe²⁺–OH⁻    | **Unmeasured** | Important at pH > 7 where OH⁻ activity rises |
| 27  | β⁰(Pb²⁺–OH⁻) or correction | Pb²⁺–OH⁻    | **Unmeasured** |                                              |

### A6. Pb²⁺–SO₄²⁻ binary parameters — 3 parameters

| #   | Parameter      | Ion Pair   | Status         | Notes                                             |
| --- | -------------- | ---------- | -------------- | ------------------------------------------------- |
| 28  | β⁰(Pb²⁺–SO₄²⁻) | Pb²⁺–SO₄²⁻ | **Unmeasured** | Mgaidi et al. (1991) partial; Felmy et al. (2000) |
| 29  | β¹(Pb²⁺–SO₄²⁻) | Pb²⁺–SO₄²⁻ | **Unmeasured** |                                                   |
| 30  | Cᶲ(Pb²⁺–SO₄²⁻) | Pb²⁺–SO₄²⁻ | **Unmeasured** |                                                   |

### A7. PbCl₂⁰ neutral-species parameters — 4 parameters

| #   | Parameter            | Species / Interaction | Status         | Notes                                              |
| --- | -------------------- | --------------------- | -------------- | -------------------------------------------------- |
| 31  | λ(PbCl₂⁰, Na⁺)       | PbCl₂⁰–Na⁺            | **Unmeasured** | PbCl₂⁰ is a significant species in Cl⁻-rich brines |
| 32  | λ(PbCl₂⁰, Cl⁻)       | PbCl₂⁰–Cl⁻            | **Unmeasured** |                                                    |
| 33  | ζ(PbCl₂⁰, Na⁺, Cl⁻)  | PbCl₂⁰ ternary        | **Unmeasured** |                                                    |
| 34  | ζ(PbCl₂⁰, Ca²⁺, Cl⁻) | PbCl₂⁰ ternary        | **Unmeasured** |                                                    |

---

## B. Petroleum-Derived Organic Acid–Metal Parameters (~14)

These parameters govern how crude-oil-derived organic acids (acetate, propionate) interact with the scale-forming metal ions. Na⁺–OAc⁻ Pitzer parameters already exist (Manohar et al. 1992), so only metal–carboxylate terms are needed.

### B1. Binary parameters (β⁰, β¹, Cᶲ) — 12 parameters

| #   | Parameter      | Ion Pair        | Status         | Notes                                                               |
| --- | -------------- | --------------- | -------------- | ------------------------------------------------------------------- |
| 35  | β⁰(Fe²⁺–OAc⁻)  | Fe²⁺–acetate    | **Unmeasured** | Acetate: dominant organic acid in produced waters (100–10,000 mg/L) |
| 36  | β¹(Fe²⁺–OAc⁻)  | Fe²⁺–acetate    | **Unmeasured** |                                                                     |
| 37  | Cᶲ(Fe²⁺–OAc⁻)  | Fe²⁺–acetate    | **Unmeasured** |                                                                     |
| 38  | β⁰(Pb²⁺–OAc⁻)  | Pb²⁺–acetate    | **Unmeasured** |                                                                     |
| 39  | β¹(Pb²⁺–OAc⁻)  | Pb²⁺–acetate    | **Unmeasured** |                                                                     |
| 40  | Cᶲ(Pb²⁺–OAc⁻)  | Pb²⁺–acetate    | **Unmeasured** |                                                                     |
| 41  | β⁰(Fe²⁺–Prop⁻) | Fe²⁺–propionate | **Unmeasured** | Propionate: second most abundant (10–1,000 mg/L)                    |
| 42  | β¹(Fe²⁺–Prop⁻) | Fe²⁺–propionate | **Unmeasured** |                                                                     |
| 43  | Cᶲ(Fe²⁺–Prop⁻) | Fe²⁺–propionate | **Unmeasured** |                                                                     |
| 44  | β⁰(Pb²⁺–Prop⁻) | Pb²⁺–propionate | **Unmeasured** |                                                                     |
| 45  | β¹(Pb²⁺–Prop⁻) | Pb²⁺–propionate | **Unmeasured** |                                                                     |
| 46  | Cᶲ(Pb²⁺–Prop⁻) | Pb²⁺–propionate | **Unmeasured** |                                                                     |

### B2. Sulfide–carboxylate anion mixing — ~2 parameters

| #   | Parameter    | Interaction                       | Status         | Notes                                                        |
| --- | ------------ | --------------------------------- | -------------- | ------------------------------------------------------------ |
| 47  | θ(HS⁻–OAc⁻)  | HS⁻/acetate like-charge mixing    | **Unmeasured** | Governs competitive effects between sulfide and organic acid |
| 48  | θ(HS⁻–Prop⁻) | HS⁻/propionate like-charge mixing | **Unmeasured** |                                                              |

### Why organic–organic mixing parameters are excluded

Organic–organic anion mixing parameters (e.g., θ(OAc⁻–Prop⁻), ψ(OAc⁻–Prop⁻–Na⁺)) are **not** included in the target parameter set. In the Pitzer equations, like-charge mixing terms enter as the product of both anion molalities (m\_OAc × m\_Prop). In produced waters, organic acid concentrations are typically 2–4 orders of magnitude below the dominant inorganic anions: acetate is ~0.001–0.05 m while Cl⁻ is 1–5 m (Lundegard & Kharaka 1994; Bostick 2002). The organic–organic product (≲10⁻⁴) is therefore orders of magnitude smaller than the metal–organic acid cross terms (~10⁻² to 10⁻³) that govern activity-coefficient corrections. Pitzer & Kim (1974) noted that like-charge mixing parameters are "always small," and Mizera et al. (1999) explicitly set all organic–organic and ternary Pitzer parameters to zero when modeling carboxylic acid dissociation in NaCl brines. This is also standard practice in oilfield scale prediction codes such as ScaleSoftPitzer (Kan et al. 2019). An Edison Scientific literature search confirmed that no measurements of θ(acetate–propionate) exist in the published literature (see `ORGANIC_ORGANIC_EVALUATION.md`).

---

## Hierarchical Fitting Strategy

The proposal uses a phased approach based on parameter identifiability (see sensitivity analysis, Figure `fig:param_sens`):

1. **Phase 1 — Fix known values:** Hold Pb²⁺–Cl⁻ (#23–25) at Woosley & Millero (2013) values; adopt Wang (2024) Fe²⁺–HS⁻ (#1–3) as initial values. Reduces free parameters to ~42.
2. **Phase 2 — Binary parameters first:** Fit binary terms (#4–6, #28–30) which have largest ∂SI/∂p sensitivity.
3. **Phase 3 — Mixing terms:** Release mixing parameters (#7–14) as ionic-strength-dependent data accumulates.
4. **Phase 4 — Neutral-species:** Fit λ and ζ terms (#15–22, #31–34) which matter at high I where neutral complexes form.
5. **Phase 5 — Organic acid terms:** Fit acetate/propionate binary (#35–46) and mixing (#47–48) from organic-acid campaign data.

**Fallback:** If Fe²⁺ oxidation control proves difficult, prioritize PbS system first (no inert atmosphere needed), reducing active parameter set to ~24.

---

## Notes

- The "~48" count is approximate because some parameters (e.g., additional ψ ternary mixing terms for organic acids, or temperature-dependent coefficients) may be added or dropped depending on data quality and identifiability during regression.
- The sensitivity heatmap (`parameter-sensitivities-48.png`) confirms all 48 parameters have |∂SI/∂p| > 0.05, validating theoretical identifiability.
- Parameters are formatted for direct import into PHREEQC `pitzer.dat`, gebo, Thermoddem, and ScaleSoftPitzer databases.
