# Reviewer B's claims checked against the literature

> Written 2026-10-29. I split the review into 48 claims and sent one low-effort Edison `LITERATURE`
> (paperqa3) query per claim. Each query is an open question, not the reviewer's conclusion
> restated. The queries, answers and full task dumps are in
> [`edison-trajectories/review-b-claims/`](../../edison-trajectories/review-b-claims/); each claim ID
> below links to its answer. I then compared each claim with what our earlier searches had said,
> using an inventory of 15 earlier queries and reviews found on this branch, the other branches and
> the git history. The review is paraphrased throughout, as in [`REVIEW_2026.md`](REVIEW_2026.md).

**How much to trust this.** These were low-effort searches.
- "Not found" means a lead to chase, not proof of absence. In one case today's search missed a
  source that the February high-effort search had found (P1e below).
- Edison often quotes a primary paper through a later compilation. Where it said it could not
  reach the primary, the verdict says so.
- None of the numbers below have been checked against the primary papers yet.

## Short version

- **The core of the review holds up.** Edison supports it on the points that sank the proposal:
  - trace-ion Pitzer terms can't be measured;
  - FeS and PbS solubility can be modeled with solubility products, complex constants and the
    background salt's Pitzer terms;
  - precipitation onset is not equilibrium;
  - the solid has to be identified;
  - pH₂S has to be controlled;
  - mixing terms come from pairs of concentrated salts that share an ion.
- **Of 48 claims:** 29 are supported, 14 hold in substance but are off in a detail or number, 1 is
  not corroborated, and 4 could not be checked because Edison couldn't reach the primary paper.
- **The one claim Edison does not back** is that the solid in Kendall and Sloan's (1925) PbCl₂–NaCl
  experiments was misidentified (P4c). Two evaluations find nothing wrong with their NaCl data.
  One of them (Clever and Johnston 1980) lists the data without criticism. The other, THEREDA's
  2022 Pb review, finds only cotunnite and halite in that system. The criticism Edison did find is
  aimed at Kendall and Sloan's MgCl₂ and CaCl₂ data. Ask the reviewer, or read the cited studies,
  before repeating the point.
- **Our earlier searches and this review barely overlap:**
  - They anticipated 13 of the 48 claims. Two of those came only after submission, in the October
    bench checks.
  - They said the opposite on 17 claims, never touched 16, and were mixed on 2. The October checks
    later reversed two of the 17 (F1b, P9a).
  - Today's answers cite about 145 sources. Only about 7 of them appear anywhere in the repo before
    the review arrived.
- **The main reason is how we asked.** Every earlier Pitzer query asked which parameters had been
  published. None asked whether those parameters could be measured, or what a solution chemist
  would do instead. Asked neutrally, Edison returned that classical approach within minutes: the
  constant-ionic-medium method (P2a), and galena solubility in 5 m NaCl modeled without any
  Pb–HS⁻ terms (P1c).

## Where the earlier searches went wrong, and what they missed

1. **The gap was assumed, never tested.**
   - The 2026-02-28 query ([`EDISON_PITZER_PARAMETER_SEARCH.md`](EDISON_PITZER_PARAMETER_SEARCH.md))
     asked which Fe²⁺/Pb²⁺–HS⁻ parameters had been published. It found none and labeled that "the
     gap this proposal fills" (line 25).
   - The high-effort hypothesis check ([`HYPOTHESIS_EVALUATION.md`](HYPOTHESIS_EVALUATION.md),
     line 28) recommended growing the set to 40–50 parameters.
   - The scope update ([`edison-scientific-scope-update-petroleum-relevance.md`](edison-scientific-scope-update-petroleum-relevance.md),
     line 35) took it to about 50.
   - The review argues the opposite (F3, P1, P6), and today's neutral queries support the review.
2. **A number in our earlier table belongs to a different salt.** That search listed
   Pb²⁺–Cl⁻ = 0.26, 1.64, 0.088 and credited it to Felmy et al. 2000
   ([line 20](EDISON_PITZER_PARAMETER_SEARCH.md)). Woosley (2012) identifies 0.26018, 1.64250 and
   −0.08798 as the ZnCl₂ parameters that Millero and Byrne (1984) substituted for PbCl₂ (P4a). This
   is the stand-in the reviewer objected to. The Cφ signs differ, so check Felmy's own table.
3. **The key compilations were missed or dismissed.**
   - Turner and Clegg's 2023 sources of Pitzer parameters for the GEOTRACES elements, which covers
     Fe(II) and Pb, came up in six of today's answers. In February we examined only their 2024
     Fe(III) paper and concluded the work did not bear on ours (line 37).
   - Moog's 2022 THEREDA Pb data selection is an evaluated Pb Pitzer model for 25 °C.
   - Clever and Johnston (1980, [10.1063/1.555628](https://doi.org/10.1063/1.555628)) critically
     evaluated the solubility of Pb salts.
   - None of the three was used.
4. **Statements in the proposal that these sources contradict:**
   - Na–Ca mixing terms "never determined" (P10a). Holmes et al. (1981) give θ(Na,Ca) = 10.7/T − 0.0316.
   - θ(Fe,Na) and ψ(Fe,Na,Cl) "unmeasured" ([`PARAMETER_INVENTORY.md`](PARAMETER_INVENTORY.md) rows 7
     and 11; P6f). Moog et al. (2004) give 0.10945 and −0.01605 from isopiestic data, valid to I ≈ 6.
   - Pitzer "fails above I ≈ 2" (proposal line 99; P10b2). The Harvie–Møller–Weare model reproduces
     seawater evaporation to I ≈ 20.
   - OLI is "Pitzer-based" (lines 71, 200; P11). Its aqueous model is Bromley–Zemaitis.
   - Fe/Pb–acetate effects need new Pitzer binaries (P0, P2b, P7a). Complex constants already exist:
     Pb–acetate to 85 °C (Giordano 1989) and Fe–acetate to 300 °C (Palmer and Drummond 1988, as
     compiled by Giordano and Kharaka 1994). Fitting both would count the same interaction twice.
5. **Papers we retrieved that pointed the right way, and dropped:**
   - Luther et al. 1996 (bisulfide stability constants) and Hershey et al. 1988 (H₂S dissociation in
     ionic media) were both retrieved in February but not used.
   - Millero 1986 (Na⁺–HS⁻ terms) was later deleted from the bibliography as uncited.
   - Manohar 1992 (NaCl–NaOAc data) was noted, but θ(Cl,OAc) and ψ(Na,Cl,OAc) were never fixed. Dorn
     (2003) had already fitted both (P3b).
6. **Points we raised but did not act on.** The mock reviews and the hypothesis check had already
   raised most of the reviewer's practical points: onset versus equilibrium, the drift in FeS
   solubility, H₂S loss, too many correlated parameters, and the need for isopiestic or EMF data
   (F2a, F2b, P7b, P12). The submitted text answered them as fitting problems (ridge regression,
   ICP-OES on 5% of wells, adhesive seals). The 24–72 h sealed-vial check in the draft
   ([`drafts/draft.tex`](../../drafts/draft.tex), line 128) was cut from the submitted version. Our
   own PHREEQC run put galena about 8 log units supersaturated at 1 mmol/kg, with Davies activities
   ([`phreeqc_si_comparison.csv`](../../preliminary_results/phreeqc_si_comparison.csv)). No one asked
   what that meant for the PbS boundary (P1b).
7. **Of the 11 papers the review cites**, only Felmy 2000 and Woosley and Millero 2013 ever came up
   in our searches. Pitzer and Mayorga 1973 was in the bibliography, but only for derivative
   formulas. Today's queries did better:
   - read directly: Pitzer and Mayorga 1973, Chou and Phan 1985;
   - reached through later papers: Millero and Byrne 1984, Felmy 2000, Kendall and Sloan 1925,
     Paige 1992, Holmes 1981, Oakes 1998, Moog 2004;
   - found but not read: Marion 2002;
   - not reached: Woosley and Millero 2013.

**For the next search:**
- Ask the question that could sink the idea: "can X be measured?" and "what would a solution chemist
  do instead?", not just "has X been published?".
- Check every parameter value against the primary paper.
- Use high effort when the answer is "nothing found".

## Where Edison disagrees with the reviewer, or adds a caveat

| ID | The reviewer's point, paraphrased | What Edison found |
|---|---|---|
| [P4c](../../edison-trajectories/review-b-claims/P4c.md) | Kendall and Sloan misidentified their solid, and Felmy et al. ignored this | Not corroborated for NaCl. Clever and Johnston (1980) and THEREDA (Moog 2022) treat the NaCl data as sound. Moog finds only cotunnite and halite in PbCl₂–NaCl–H₂O at 25 °C. Nriagu and Anderson (1971) confirmed PbCl₂ by XRD. The known problems are with the MgCl₂ data (systematically low) and the CaCl₂ data |
| [P1a](../../edison-trajectories/review-b-claims/P1a.md) | The limiting law holds to about I = 0.1 for dissociated salts | The usual limit is about 10⁻³ mol/kg for 1:1 salts. This stricter limit strengthens the reviewer's argument rather than weakening it. PbCl⁺ is about 37% of dissolved Pb at PbCl₂ saturation (Simonin 2018) |
| [P4b](../../edison-trajectories/review-b-claims/P4b.md) | PbCl₂ is much more soluble in other chloride solutions than in water | Only in concentrated chloride. At 25 °C, PbCl₂ in NaCl falls from 0.039 mol/kg in water to about 0.007 at 0.5–1 m NaCl, is 0.017 at 3 m, and reaches about 0.04 only near 4 m. It is 0.156 at 4.55 m MgCl₂, and 0.145 at 3 m NaCl at 90 °C |
| [P6b](../../edison-trajectories/review-b-claims/P6b.md) | PbSO₄ solubility barely rises in other salts | It does rise: ×2 in 0.2 M NaClO₄ and ×19 in 0.25 m acetate buffer (Giordano 1989). It stays below about 3 mmol/kg, so the conclusion that a C term is unjustified still holds |
| [P8a](../../edison-trajectories/review-b-claims/P8a.md), [P8b](../../edison-trajectories/review-b-claims/P8b.md) | The reviewer was unsure whether temperature-dependent models exist for NaOAc, Na propionate and FeCl₂ | Two exist. NaOAc: Beyer and Steiger 2002 ([10.1006/jcht.2002.0974](https://doi.org/10.1006/jcht.2002.0974)), 255–398 K and 0–25 mol/kg. FeCl₂: Muñoz and Moog 2020 ([10.1016/j.jct.2019.105977](https://doi.org/10.1016/j.jct.2019.105977)), binary terms only. Sodium propanoate has 25 °C values only |
| [P8d](../../edison-trajectories/review-b-claims/P8d.md) | Fe(OAc)₂ has essentially no thermodynamic data | Fe(II)–acetate complex constants exist from 25 to 300 °C (Palmer and Drummond 1988; Palmer and Hyde 1993). What is missing is data on the bulk solutions: no osmotic coefficients, heat capacities or solubility of the salt |
| [P5a](../../edison-trajectories/review-b-claims/P5a.md), [P9b](../../edison-trajectories/review-b-claims/P9b.md) | No θ involving a trace ion can be justified | When both cations are trace, agreed. When one is trace, its own activity coefficient in a concentrated background, measured at several background concentrations, can in principle fix θ (Holmes and Mesmer 1992). No θ(Na,Pb) has been fitted to the NaNO₃–Pb(NO₃)₂–H₂O solubilities measured in 1923 |
| [P15a](../../edison-trajectories/review-b-claims/P15a.md) | Fitting through log(Q/K_sp) is a mistake | Fits to *equilibrium* solubilities work. Zhang et al. 2016 fitted β⁽⁰⁾, β⁽¹⁾, Cφ and K_sp for Na₂WO₄ to 2.5%. Onset data only show that some nucleation threshold was crossed, so they cannot be treated as SI = 0 |
| [P3d](../../edison-trajectories/review-b-claims/P3d.md) | The platform could be adapted to measure freezing points | The route is sound: NaOAc's Pitzer fit uses cryoscopic data. But no multi-well method has shown the accuracy needed. A 0.01 K error shifts φ by about 0.03 at 0.1 m. A 96-well freezing assay that detects nucleation, not equilibrium melting, has ±0.43 K uncertainty. Classical cryometry reaches about 0.0001 °C |
| [P6d](../../edison-trajectories/review-b-claims/P6d.md) | β⁽²⁾ was a convenience, and explicit ion pairs do as well or better with fewer terms | As well, yes: for MgSO₄ the two models agree at 25 °C (Archer and Wood 1985). "Better" has not been shown. β⁽²⁾ ≈ −2K in the dilute limit |
| [P1c](../../edison-trajectories/review-b-claims/P1c.md) | FeS and PbS solubility needs no metal–HS⁻ Pitzer terms | Shown for PbS. Bourcier and Barnes (1987) matched galena solubility in 5 m NaCl + 0.5 m CaCl₂ at 100–355 °C within a factor of about 3 using constants alone, as Edison reads that zinc paper. Not yet shown for FeS |

## Openings the check turned up

These follow the review's own advice. Each is a "not found" from a low-effort search, so confirm it
before building on it.

- **FeS or PbS solubility in a fixed NaCl or NaClO₄ medium with added acetate** (P2a). No such study
  was found. Giordano chose PbSO₄ over PbS for the Pb–acetate constants because galena is too
  insoluble.
- **θ(Na,Pb) from the nitrate system** (P9b). Solubility data from 1923 exist, but no one has fitted
  them.
- **Osmotic or activity data for Pb(OAc)₂ and Fe(OAc)₂** (P3c). None were found, while NaOAc already
  has a full model (P8a). Temperature-dependent Na propanoate terms are also missing.
- **A PbCl₂ model validated from 25 to 90 °C** (P8c). Turner and Clegg kept only 25 °C terms,
  because the separate fits at each temperature disagreed with one another.
- **Sandia's 2012 test plan** (Jang, Xiong and Kim) set out to measure FeS solubility in Na₂S and PbS
  solubility in NaHS/NaCl, aiming at Fe²⁺–HS⁻ and PbCl⁺–HS⁻ terms, but reported "no data to date"
  (P1e). This matters for the Sandia entry in the [funding doc](../alternative-funding/README.md).
- **Practical limits:**
  - Galena's solubility in water is about 1 µmol/L (P1b), so Pb needs ICP-MS.
  - In 10% salt matrices, ICP-OES recoveries were 60–95% without matrix correction and 92–102% with
    an internal standard (P13).

## Claim by claim

The verdict column is Edison's evidence on the reviewer's claim:
- **S**: supported;
- **P**: the core holds, but a detail or number is off;
- **N**: not corroborated;
- **U**: Edison couldn't reach the primary paper.

The last column is how our earlier searches and reviews related to the claim:
- **anticipated**: they agreed with the reviewer;
- **contradicted**: they said the opposite;
- **silent**: they didn't cover it;
- **mixed**: different sources pointed different ways.

### The three decisive flaws and the opening paragraph

| ID | Claim (paraphrased) | Edison | Key evidence | Our earlier searches |
|---|---|---|---|---|
| [F1a](../../edison-trajectories/review-b-claims/F1a.md) | The Fe solid's identity was assumed | S | First solid is nanocrystalline mackinawite, which keeps ordering for a day (Wolthers et al. 2003, [10.2138/am-2003-11-1245](https://doi.org/10.2138/am-2003-11-1245)). Greigite, pyrrhotite, siderite and Fe(OH)₂ depend on conditions. Identify the solid by XRD or PDF analysis | Anticipated (mock reviews, hypothesis check), not acted on |
| [F1b](../../edison-trajectories/review-b-claims/F1b.md) | The Pb solid's identity was assumed | S | PbS usually forms first while sulfide lasts. Cotunnite, laurionite, cerussite, phosgenite and hydrocerussite form at high Pb/Cl or with bicarbonate (Lussier 2005; Moog 2022). Check SI for each candidate | Contradicted before submission (PbS assumed). The October checks agreed |
| [F2a](../../edison-trajectories/review-b-claims/F2a.md) | Onset within hours is not equilibrium | S | Mackinawite forms in ms–s, but equilibrium needs approach from both sides (Davison 1991, [10.1007/bf00877139](https://doi.org/10.1007/bf00877139); Hemley et al. 1992) | Anticipated (three mock personas). The 24–72 h sealed subset was cut |
| [F2b](../../edison-trajectories/review-b-claims/F2b.md) | Aging FeS drifts in solubility | S | pK 2.95 for fresh FeS versus 3.6 for mackinawite (Davison 1991) | Anticipated (hypothesis check) |
| [F3](../../edison-trajectories/review-b-claims/F3.md) | Pitzer meant a minimal set; not every term needs fitting | S | Binary terms from single salts; θ and ψ from common-ion mixtures; terms set to zero when unsupported (Pitzer and Kim 1974) | Contradicted (grow to 40–50; Kosmos: all 34 identifiable) |
| [P0](../../edison-trajectories/review-b-claims/P0.md) | Organic acids act mostly through complexes | S | Modeled through formation constants. In a modeled brine at 100 °C with 2 m Cl and 0.1 m acetate, acetate holds 16% of Fe and 5% of Pb (Giordano and Kharaka 1994, [10.1144/gsl.sp.1994.078.01.14](https://doi.org/10.1144/gsl.sp.1994.078.01.14)) | Contradicted (scope update added M–OAc Pitzer binaries) |

### Points 1–3: the trace-ion argument and the constant-medium alternative

| ID | Claim (paraphrased) | Edison | Key evidence | Our earlier searches |
|---|---|---|---|---|
| [P1a](../../edison-trajectories/review-b-claims/P1a.md) | Limiting law valid to I ≈ 0.1, lower for PbCl₂ | P | About 10⁻³ for 1:1 salts. Strong PbCl⁺ association | Silent |
| [P1b](../../edison-trajectories/review-b-claims/P1b.md) | FeS and PbS solubility is millimolal or lower | P | Galena about 0.94 µmol/L in water (Clever and Johnston 1980). Edison did not establish total Fe. Our rough check in [`REVIEW_2026.md`](REVIEW_2026.md) has mackinawite reaching saturation inside the design's concentration range, between pH 4 and 7 | Anticipated (data on file; the conclusion was never drawn) |
| [P1c](../../edison-trajectories/review-b-claims/P1c.md) | Solubility can be reproduced with no metal–HS⁻ Pitzer terms | P | PbS: yes (Bourcier and Barnes 1987, [10.2113/gsecongeo.82.7.1839](https://doi.org/10.2113/gsecongeo.82.7.1839)). FeS: not shown | Contradicted (the precedent search said better Pitzer terms were needed) |
| [P1d](../../edison-trajectories/review-b-claims/P1d.md) | Na⁺–HS⁻ can be measured in NaHS solutions | S | Herr and Helz 1976 ([10.1007/bf01167238](https://doi.org/10.1007/bf01167238)). Millero's β values came from H₂S dissociation data | Anticipated, then Millero 1986 was dropped |
| [P1e](../../edison-trajectories/review-b-claims/P1e.md) | Others published such terms; that doesn't justify them | S* | *Today's search found none. Jang et al. 2012 (Sandia) planned some but had no data. The February high-effort search had found Wang (2024) Fe²⁺–HS⁻ terms, which the proposal used as priors (line 149) | Contradicted (adopted as priors) |
| [P2a](../../edison-trajectories/review-b-claims/P2a.md) | This resembles the constant-ionic-medium method | S | Heindl and Gamsjäger 1977 (pyrrhotite, 1 m NaClO₄, fixed pH₂S); PbS in 3 m NaCl reproduced from constants. No FeS or PbS + acetate study found | Silent |
| [P2b](../../edison-trajectories/review-b-claims/P2b.md) | The complex constants are the quantities to fit | S | Pb–OAc log β₁ = 2.4, log β₂ = 3.4 at 25 °C, measured to 85 °C (Giordano 1989, [10.1016/0016-7037(89)90387-6](https://doi.org/10.1016/0016-7037(89)90387-6)). Fe–OAc known to 300 °C | Contradicted (constants noted, but Pitzer binaries were fitted instead) |
| [P3a](../../edison-trajectories/review-b-claims/P3a.md) | One salt's terms and the mixing terms must be known first | S | Fix the background binary terms. Some mixing terms can then come from ternary solubilities. Correlated parameters: van Gaans 1991 ([10.1007/bf00650718](https://doi.org/10.1007/bf00650718)) | Anticipated in part |
| [P3b](../../edison-trajectories/review-b-claims/P3b.md) | θ(Cl,OAc) and ψ(Na,Cl,OAc) need NaCl–NaOAc data | S | Already fitted (Dorn 2003). Isopiestic data: Jones and Prue 1974 ([10.1007/bf00650402](https://doi.org/10.1007/bf00650402)) | Data noted, never used |
| [P3c](../../edison-trajectories/review-b-claims/P3c.md) | No Pitzer or isopiestic data for Pb(OAc)₂ or Fe(OAc)₂ | S | None located | Anticipated (fitted from boundaries anyway) |
| [P3d](../../edison-trajectories/review-b-claims/P3d.md) | Freezing points would work on an adapted platform | P | Valid route. Multi-well accuracy not yet shown | Silent |

### Point 4: the parameter sets taken on trust

| ID | Claim (paraphrased) | Edison | Key evidence | Our earlier searches |
|---|---|---|---|---|
| [P4a](../../edison-trajectories/review-b-claims/P4a.md) | Millero and Byrne used ZnCl₂ for PbCl₂ | S | Woosley 2012: β⁽⁰⁾ = 0.26018, β⁽¹⁾ = 1.64250, Cφ = −0.08798 are the ZnCl₂ values | Silent. Our February table listed these as the Pb–Cl parameters |
| [P4b](../../edison-trajectories/review-b-claims/P4b.md) | PbCl₂ is below 0.05 m in water and more soluble in other chlorides | P | 0.03907 mol/kg in water. Higher only in concentrated chloride (see above) | Anticipated after submission (October checks) |
| [P4c](../../edison-trajectories/review-b-claims/P4c.md) | Kendall and Sloan's solid was misidentified | N | See above | Silent |
| [P4d](../../edison-trajectories/review-b-claims/P4d.md) | Felmy added dependent terms, including a C with no matching B | U | θ(Na,Pb) = 0.10 confirmed (through Xiong 2017). Felmy's B and C table not reached. A C term without B is "permissible but needs justification" | Silent (trusted) |
| [P4f](../../edison-trajectories/review-b-claims/P4f.md) | The Rice group's Pb terms have the same flaw | U | Numbers not reached. Pointers: Wang et al. 2022 ([10.2118/208616-PA](https://doi.org/10.2118/208616-PA)). PbS is not in ScaleSoftPitzer's mineral list | Contradicted (trusted) |

### Points 5–7: mixing terms, third-virial terms, and fitting from solubility

| ID | Claim (paraphrased) | Edison | Key evidence | Our earlier searches |
|---|---|---|---|---|
| [P5a](../../edison-trajectories/review-b-claims/P5a.md) | Mixing terms come from two salts that share an ion | S | Pitzer and Kim (NaCl–KCl to I = 4.8). For a single trace cation, see above | Contradicted (the hypothesis rested on Fe/Pb mixing with Na/Ca) |
| [P5b](../../edison-trajectories/review-b-claims/P5b.md) | θ(Pb,Fe) cannot come from sulfide or sulfate data | S | No θ(Pb,Fe) anywhere. Turner and Clegg treat PbSO₄ with an ion-pair constant (log K = 2.72) because the salt is too insoluble for Pitzer terms | Silent |
| [P6a](../../edison-trajectories/review-b-claims/P6a.md) | Pitzer and Mayorga used no C below about 2 m | S | Cφ was omitted when the data stopped short of 2 m | Contradicted (a Cφ planned for every trace pair) |
| [P6b](../../edison-trajectories/review-b-claims/P6b.md) | PbSO₄ is below 1 mmol/kg and barely rises in other salts | P | 0.146 mmol/L in water. It rises 2–19× (see above) | Known, but β⁽⁰⁾, β⁽¹⁾ and Cφ planned anyway |
| [P6c](../../edison-trajectories/review-b-claims/P6c.md) | Paige used β⁽²⁾ to mimic the PbSO₄ pair | P | β⁽²⁾ used, with β⁽⁰⁾ = Cφ = 0 (as tabulated by Charykova et al. 2010). Whether an explicit PbSO₄° constant was left out is unverified | Silent |
| [P6d](../../edison-trajectories/review-b-claims/P6d.md) | β⁽²⁾ was a convenience; ion pairs do as well | P | See above | Silent |
| [P6e](../../edison-trajectories/review-b-claims/P6e.md) | Rice fit barite with β⁽²⁾ alone | U | Shi et al. 2012 table not reached ([10.1021/ie2020558](https://doi.org/10.1021/ie2020558)). An explicit BaSO₄° pair has worked elsewhere (Vicum 2005) | Silent (Rice's barite model held up as the example) |
| [P6f](../../edison-trajectories/review-b-claims/P6f.md) | Na–Fe mixing terms come from concentrated data | S | Moog et al. 2004: θ = 0.10945, ψ = −0.01605. Chou and Phan 1985 published data, not parameters | Contradicted (marked "unmeasured") |
| [P7a](../../edison-trajectories/review-b-claims/P7a.md) | K(PbOAc⁺) and B(Pb,OAc) overlap | S | Overlap shown qualitatively. Giordano avoided fitting both together. A combined Pb–Cl model gave incoherent temperature trends | Contradicted (the plan fitted both) |
| [P7b](../../edison-trajectories/review-b-claims/P7b.md) | Solubility alone leaves β⁽⁰⁾ and β⁽¹⁾ loose | S | Weare 1981; Hovey, Pitzer and Rard 1991. Use isopiestic and EMF data | Anticipated (answered with ridge regression) |

### Points 8–9: temperature range and databases

| ID | Claim (paraphrased) | Edison | Key evidence | Our earlier searches |
|---|---|---|---|---|
| [P8a](../../edison-trajectories/review-b-claims/P8a.md) | The thermal data exist for NaOAc and Na propanoate | P | NaOAc model exists. Propanoate has heat capacities to 525 K but no temperature-dependent fit | Silent |
| [P8b](../../edison-trajectories/review-b-claims/P8b.md) | The thermal data exist for FeCl₂ | S | Bernarducci et al. 1979 ([10.1007/BF00648777](https://doi.org/10.1007/BF00648777)). Model: Muñoz and Moog 2020 | Anticipated loosely |
| [P8c](../../edison-trajectories/review-b-claims/P8c.md) | A temperature-dependent PbCl₂ model may not be possible | S | No validated 25–90 °C model. Turner and Clegg kept 25 °C terms only. Mgaidi et al. 1991 is unchecked | Contradicted (temperature-dependent Pb–Cl priors taken from Woosley and Millero) |
| [P8d](../../edison-trajectories/review-b-claims/P8d.md) | No temperature model for Pb(OAc)₂; no data for Fe(OAc)₂ | P | See above | Silent |
| [P9a](../../edison-trajectories/review-b-claims/P9a.md) | PHREEQC Pitzer databases vary; consistency is the work | S | pitzer.dat has no Pb; gebo, pit2010 and THEREDA 2021 do. Plummer et al. 1988 document a consistency failure. Selected PbCl₄²⁻ constants differ by more than a log unit | Contradicted before submission (gap framed as missing entries). The October checks agreed |
| [P9b](../../edison-trajectories/review-b-claims/P9b.md) | θ(Na,Pb) is better fixed from nitrate data | U | No nitrate fit exists. Glasstone and Saunders (1923) data do | Silent |

### Points 10–15: misstatements and lab practice

| ID | Claim (paraphrased) | Edison | Key evidence | Our earlier searches |
|---|---|---|---|---|
| [P10a](../../edison-trajectories/review-b-claims/P10a.md) | Na–Ca mixing terms have been measured | S | Holmes et al. 1981, 25–201 °C. Oakes et al. 1998, calorimetry to 300 °C | Silent (the proposal said "never determined") |
| [P10b](../../edison-trajectories/review-b-claims/P10b.md) | NaNO₃ fits to about 11 m with two terms | P | May et al. 2011 ([10.1021/je2009329](https://doi.org/10.1021/je2009329)): to 10.75 m, with C = −5×10⁻⁵. Marion 2002 not reached | Silent |
| [P10b2](../../edison-trajectories/review-b-claims/P10b2.md) | Pitzer doesn't fail above I ≈ 2 | S | Gypsum in 0–6 m NaCl within 3%; seawater evaporation to I ≈ 20. Failures trace to missing parameters for specific ions, not to any one ionic strength | Contradicted (the core hypothesis) |
| [P10c](../../edison-trajectories/review-b-claims/P10c.md) | Misfits come from pH₂S, constants or data errors | S | The literature value of H₂S's second dissociation constant spans 10⁻¹²–10⁻¹⁹ (Sun et al. 2008, [10.1021/ie070750i](https://doi.org/10.1021/ie070750i)); bisulfide constants aren't unique; artifacts occur. No source blamed missing mixing terms | Mixed |
| [P11](../../edison-trajectories/review-b-claims/P11.md) | OLI isn't Pitzer-based and its databanks are proprietary | S | Aqueous model is Bromley–Zemaitis. MSE has a Pitzer–Debye–Hückel long-range term; some MSE parameters are published (Lin et al. 2009, [10.1002/aic.12040](https://doi.org/10.1002/aic.12040)) | Contradicted (the proposal called OLI Pitzer-based) |
| [P12](../../edison-trajectories/review-b-claims/P12.md) | Sulfide equilibria need a fixed pH₂S | S | Continuous H₂S gas or sealed small-headspace vessels. Open wells lose H₂S and contaminate their neighbors. Galena runs kept 89 ± 11% of sulfide over 7 days, even capped | Anticipated (answered with adhesive seals) |
| [P13](../../edison-trajectories/review-b-claims/P13.md) | ICP-OES is inaccurate in brines | S | 60–95% recovery uncorrected, 92–102% with an internal standard (Krejčová et al. 2007, [10.1016/j.aca.2006.09.031](https://doi.org/10.1016/j.aca.2006.09.031)). Dilute by weight | Contradicted implicitly (ICP-OES planned as the accuracy anchor) |
| [P14](../../edison-trajectories/review-b-claims/P14.md) | Buffers add nothing, and pH isn't an independent variable | P | No blanket ban, but brine solubility studies leave buffers out. Bicarbonate is not inert. MES and HEPES bind weakly but not provably zero. Measure pH | Partly anticipated after submission |
| [P15a](../../edison-trajectories/review-b-claims/P15a.md) | Fitting through log(Q/K_sp) is a mistake | P | See above | Mixed (the hypothesis check and mock reviews agreed; Kosmos did not) |
| [P15b](../../edison-trajectories/review-b-claims/P15b.md) | Assuming a_H₂O = 1 is inconsistent | P | At 6 m NaCl, a_w ≈ 0.75. That gives SI errors of +0.25 for a dihydrate and +1.2 for a decahydrate. No direct effect on FeS + H⁺ or PbS + H⁺ | Silent |
