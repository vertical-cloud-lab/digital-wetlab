# F1b (decisive flaw 1)

**Claim (paraphrased):** The proposal assumes it knows which Pb solid precipitates.

**Query** (Edison `job-futurehouse-paperqa3`, task `2a65c565-7949-46bd-a3c0-eaaa3a84664b`, status `success`):

> Which lead solids can precipitate in aqueous Pb(II)-NaCl-sulfide-carbonate-sulfate systems at pH 4-9 and 25-90 C (galena, cotunnite PbCl2, laurionite PbOHCl, phosgenite, cerussite, hydrocerussite, anglesite)? Under what Pb, chloride, carbonate and pH conditions do chloride or carbonate lead phases form instead of, or alongside, PbS?

---

Question: Which lead solids can precipitate in aqueous Pb(II)-NaCl-sulfide-carbonate-sulfate systems at pH 4-9 and 25-90 C (galena, cotunnite PbCl2, laurionite PbOHCl, phosgenite, cerussite, hydrocerussite, anglesite)? Under what Pb, chloride, carbonate and pH conditions do chloride or carbonate lead phases form instead of, or alongside, PbS?

## Lead solids and the controlling chemistry

**All seven named solids are possible candidates, but they do not share one precipitation threshold.** Which actually forms depends on *free-ion activities*, dissolved sulfide and its redox state, carbonate/CO₂, sulfate, pH, salinity, temperature, and the order and rate of mixing. The following table gives the activity product that must exceed the phase’s solubility product to permit precipitation. Its numerical constants are selected **25 °C** values; they are not interchangeable with total analytical concentrations or directly comparable across different reaction stoichiometries. (moog2022thermodynamicdatabasefor pages 6-8, moog2022thermodynamicdatabasefor pages 8-9, moog2022thermodynamicdatabasefor pages 11-13, moog2022thermodynamicdatabasefor pages 13-14, moog2022thermodynamicdatabasefor pages 14-16)

| Phase / formula | Diagnostic activity product, \(Q\) | \(K_{sp}\) at 25 °C | Status / indicative conditions |
|---|---:|---:|---|
| Galena, PbS | \(a_{Pb^{2+}}a_{S^{2-}}\) | Not selected in the retrieved Pb database; no defensible numerical value assigned here | Expected under reducing, sulfide-bearing conditions; at pH 5–7 and anoxic \(E_h\approx-0.1\) V, PbS is favored, whereas oxidation can yield anglesite. High chloride, higher temperature, and lower pH increase PbS solubility. (keogh2019mechanismsandpreventiona pages 57-65) |
| Cotunnite, PbCl₂ | \(a_{Pb^{2+}}a_{Cl^-}^{2}\) | \(10^{-4.77}\) | Requires \(Q>K_{sp}\), hence high free Pb²⁺ and Cl⁻ activities; concentrated chloride can instead increase dissolved Pb through chloro-complexes, so total chloride alone is not predictive. (moog2022thermodynamicdatabasefor pages 6-8, moog2022thermodynamicdatabasefor pages 8-9) |
| Laurionite, PbOHCl | \(a_{Pb^{2+}}a_{OH^-}a_{Cl^-}\) | \(10^{-13.7}\) | Chloride-bearing, near-alkaline phase; the selected model gives equilibrium near pH 8.5, with substantial dissolved Pb complexation. (moog2022thermodynamicdatabasefor pages 6-8) |
| Phosgenite, Pb₂Cl₂CO₃ | \(a_{Pb^{2+}}^{2}a_{Cl^-}^{2}a_{CO_3^{2-}}\) | \(10^{-20.64}\) | Needs both chloride and carbonate. At 25 °C, 0.035 M PbCl₂ mixed with 0.035 M NaHCO₃ produced cerussite + phosgenite at final pH ≈4.7–5.8; cerussite formed first in some runs and phosgenite appeared after aging. (moog2022thermodynamicdatabasefor pages 14-16, lussier2005theinfluenceof media 16a6b50b) |
| Cerussite, PbCO₃ | \(a_{Pb^{2+}}a_{CO_3^{2-}}\) | \(10^{-13.59}\) | Broad carbonate-phase candidate over roughly pH 4–9; observed at 25 °C throughout 0.035 M Pb–carbonate experiments, alone or with phosgenite/hydrocerussite. (moog2022thermodynamicdatabasefor pages 13-14, lussier2005theinfluenceof media 16a6b50b) |
| Hydrocerussite, Pb₃(CO₃)₂(OH)₂ | \(a_{Pb^{2+}}^{3}a_{CO_3^{2-}}^{2}a_{OH^-}^{2}\) | \(10^{-46.6}\) | Favored relative to cerussite as pH rises and CO₂ activity falls; observed alongside cerussite in carbonate-fed experiments, commonly at final/aged pH ≈6.3–9.4. (moog2022thermodynamicdatabasefor pages 13-14, lussier2005theinfluenceof media 16a6b50b) |
| Anglesite, PbSO₄ | \(a_{Pb^{2+}}a_{SO_4^{2-}}\) | \(10^{-7.84}\) | Sulfate-rich or oxidizing alternative; oxidation of PbS can generate anglesite, so redox state—not sulfate concentration alone—controls competition with galena. (moog2022thermodynamicdatabasefor pages 11-13, keogh2019mechanismsandpreventiona pages 57-65) |
| **Interpretive constraint** | **Precipitation requires \(Q>K_{sp}\); equilibrium saturation is \(Q=K_{sp}\). Use free-ion activities, not analytical totals.** | **These constants have different reaction stoichiometries and therefore cannot be ranked numerically as a phase-solubility series.** | **Values apply at 25 °C. For 25–90 °C, recalculate equilibrium constants and activity coefficients at the actual temperature and salinity; the table does not imply that all phases coexist.** |


*Table: Activity-based precipitation tests and selected 25 °C solubility products for the seven candidate lead solids. The criteria show why pH, redox state, ligand activities, salinity, and temperature must be evaluated together.*

**With available reduced sulfide, PbS is usually the first phase to consider.** At 25 °C, dissolved sulfide is predominantly H₂S below about pH 7 and increasingly HS⁻ as pH rises; S²⁻ remains a minor species throughout most of pH 4–9. Nevertheless, PbS precipitated in direct experiments while the solution was at pH 4–6. In a separate anoxic, H₂S-fed brine experiment buffered at pH 5.2, solutions containing **100 mg/L or 1,000 mg/L Pb** were calculated to be strongly supersaturated with PbS; the higher-Pb experiment used approximately **0.5 M KCl**, and the combined PbS/CaCO₃ experiment approximately **1.07 M chloride**. Those experiments demonstrate that chloride and carbonate do **not** by themselves exclude PbS when reactive sulfide remains available. The reported PbS saturation ratios are model estimates, not measured boundaries against every other lead solid. (keogh2019mechanismsandpreventiona pages 57-65, sten2000precipitationoflead pages 3-6, sten2000precipitationoflead pages 11-13, keogh2019mechanismsandprevention pages 101-107, keogh2019mechanismsandprevention pages 107-112)

### When chloride or carbonate phases appear

- **High Pb + chloride, with little effective sulfide:** Cotunnite requires saturation with PbCl₂; it is not the expected default merely because NaCl is present. As a scale check, measured PbCl₂ saturation in chloride-containing solutions involves dissolved Pb on the order of **millimoles to hundredths of a mole per kilogram**. Increasing chloride can first lower PbCl₂ solubility through the common-ion effect, but concentrated chloride also makes soluble Pb–Cl complexes and can raise *total* dissolved Pb. The latter also tends to increase PbS solubility. Thus, neither a single NaCl cutoff nor total Pb alone establishes that cotunnite will replace galena. (moog2022thermodynamicdatabasefor pages 6-8, moog2022thermodynamicdatabasefor pages 8-9, moog2022thermodynamicdatabasefor pages 17-20, moog2022thermodynamicdatabasefor pages 25-28, keogh2019mechanismsandprevention pages 65-69)
- **Chloride + higher pH:** Laurionite, PbOHCl, becomes a candidate as OH⁻ activity increases; the selected equilibrium assessment discusses conditions around **pH 8.5**, although that is **not** a universal pH boundary at arbitrary Pb and chloride concentrations. (moog2022thermodynamicdatabasefor pages 6-8)
- **Chloride + inorganic carbon:** Phosgenite requires *both* chloride and carbonate activities. In **sulfide-free**, 25 °C experiments, mixing **0.035 M PbCl₂** with **0.035 M NaHCO₃** produced XRD-identified **cerussite plus phosgenite**. When PbCl₂ was injected into bicarbonate, fresh solids were cerussite and phosgenite appeared after **8–16 days**; reversing the addition order yielded both in fresh solids. Reported fresh final pH values spanned approximately **4.3–5.8**, and aged chloride–bicarbonate mixtures were about **pH 4.6**. These are demonstrated formation conditions, *not* a claim that phosgenite outcompetes PbS at those concentrations if sulfide is added. (lussier2005theinfluenceof pages 1-6, lussier2005theinfluenceof pages 36-39, lussier2005theinfluenceof pages 58-63, lussier2005theinfluenceof media 16a6b50b)
- **Carbonate, especially as pH rises:** Cerussite can form even in moderately acidic mixed solutions; hydrocerussite becomes a candidate at greater alkalinity and depends sensitively on CO₂ availability. In the same **sulfide-free, 0.035 M** Pb/C experiments, using **Na₂CO₃ rather than NaHCO₃** yielded XRD-identified **cerussite plus hydrocerussite** in several mixing sequences. Fresh mixture pH ranged approximately **6.3–9.5**, and aged PbCl₂–Na₂CO₃ mixtures were about **pH 9.3–9.4**. Mixing sequence matters: Na₂CO₃ added to Pb(NO₃)₂ yielded **cerussite alone** even near pH 9, so pH alone cannot specify the hydrocerussite assemblage. Hydrocerussite’s relative equilibrium stability also changes with CO₂ pressure; an approximately pH 7 transition reported for a *closed* system should not be applied to all open waters. (moog2022thermodynamicdatabasefor pages 13-14, lussier2005theinfluenceof pages 58-63, lussier2005theinfluenceof pages 26-31, lussier2005theinfluenceof media 16a6b50b)
- **Sulfate or sulfide oxidation:** Anglesite is the PbSO₄ candidate where its saturation condition is met. Oxidation of existing galena can generate anglesite; in an Eh–pH assessment cited for pH **5.2**, shifting from anoxic conditions near **−0.1 V** toward approximately **+0.2 V** changes the expected product from PbS toward PbSO₄. Carbonate-bearing oxidizing water can instead yield cerussite. These are redox-dependent alternatives, not consequences of sulfate concentration alone. (moog2022thermodynamicdatabasefor pages 11-13, keogh2019mechanismsandpreventiona pages 57-65, salter1984naturalalterationofa pages 33-38, keogh2019mechanismsandprevention pages 73-78)

**Practical decision rule.** Calculate aqueous speciation and the saturation index of *each* candidate at the actual temperature, pH, salinity, dissolved Pb, reduced-sulfur inventory, inorganic carbon/CO₂, sulfate, and redox conditions. Low or exhausted/oxidized sulfide permits chloride and carbonate solids to persist **instead of** PbS; continuing sulfide supply permits PbS to form **alongside** other solids where local saturation and incomplete reaction allow it. The cited carbonate-precipitation experiments contained **no added sulfide**, so they cannot establish a universal Pb-versus-NaCl-versus-carbonate crossover with PbS. Moreover, the selected database constants and most direct phase-comparison experiments are at **25 °C**: the evidence does not justify carrying their pH or concentration boundaries unchanged through **90 °C**. (moog2022thermodynamicdatabasefor pages 1-2, lussier2005theinfluenceof pages 1-6, keogh2019mechanismsandprevention pages 65-69, keogh2019mechanismsandprevention pages 107-112, lussier2005theinfluenceof pages 39-46)

References

1. (moog2022thermodynamicdatabasefor pages 6-8): H Moog. Thermodynamic database for pb and its compounds-data selection. revision. Unknown journal, 2022.

2. (moog2022thermodynamicdatabasefor pages 8-9): H Moog. Thermodynamic database for pb and its compounds-data selection. revision. Unknown journal, 2022.

3. (moog2022thermodynamicdatabasefor pages 11-13): H Moog. Thermodynamic database for pb and its compounds-data selection. revision. Unknown journal, 2022.

4. (moog2022thermodynamicdatabasefor pages 13-14): H Moog. Thermodynamic database for pb and its compounds-data selection. revision. Unknown journal, 2022.

5. (moog2022thermodynamicdatabasefor pages 14-16): H Moog. Thermodynamic database for pb and its compounds-data selection. revision. Unknown journal, 2022.

6. (keogh2019mechanismsandpreventiona pages 57-65): W Keogh. Mechanisms and prevention of lead sulphide (pbs) scale deposition in multiphase systems. Unknown journal, 2019.

7. (lussier2005theinfluenceof media 16a6b50b): AJ Lussier. The influence of parent-solution chemistry on the precipitation of pb-carbonates at 25⁰c, 1 bar total pressure. Unknown journal, 2005.

8. (sten2000precipitationoflead pages 3-6): Pekka Stén and Willis Forsling. Precipitation of lead sulfide for surface chemical studies. Colloids and Surfaces A: Physicochemical and Engineering Aspects, 172:17-31, Oct 2000. URL: https://doi.org/10.1016/s0927-7757(00)00588-4, doi:10.1016/s0927-7757(00)00588-4. This article has 11 citations and is from a peer-reviewed journal.

9. (sten2000precipitationoflead pages 11-13): Pekka Stén and Willis Forsling. Precipitation of lead sulfide for surface chemical studies. Colloids and Surfaces A: Physicochemical and Engineering Aspects, 172:17-31, Oct 2000. URL: https://doi.org/10.1016/s0927-7757(00)00588-4, doi:10.1016/s0927-7757(00)00588-4. This article has 11 citations and is from a peer-reviewed journal.

10. (keogh2019mechanismsandprevention pages 101-107): W Keogh. Mechanisms and prevention of lead sulphide (pbs) scale deposition in multiphase systems. Unknown journal, 2019.

11. (keogh2019mechanismsandprevention pages 107-112): W Keogh. Mechanisms and prevention of lead sulphide (pbs) scale deposition in multiphase systems. Unknown journal, 2019.

12. (moog2022thermodynamicdatabasefor pages 17-20): H Moog. Thermodynamic database for pb and its compounds-data selection. revision. Unknown journal, 2022.

13. (moog2022thermodynamicdatabasefor pages 25-28): H Moog. Thermodynamic database for pb and its compounds-data selection. revision. Unknown journal, 2022.

14. (keogh2019mechanismsandprevention pages 65-69): W Keogh. Mechanisms and prevention of lead sulphide (pbs) scale deposition in multiphase systems. Unknown journal, 2019.

15. (lussier2005theinfluenceof pages 1-6): AJ Lussier. The influence of parent-solution chemistry on the precipitation of pb-carbonates at 25⁰c, 1 bar total pressure. Unknown journal, 2005.

16. (lussier2005theinfluenceof pages 36-39): AJ Lussier. The influence of parent-solution chemistry on the precipitation of pb-carbonates at 25⁰c, 1 bar total pressure. Unknown journal, 2005.

17. (lussier2005theinfluenceof pages 58-63): AJ Lussier. The influence of parent-solution chemistry on the precipitation of pb-carbonates at 25⁰c, 1 bar total pressure. Unknown journal, 2005.

18. (lussier2005theinfluenceof pages 26-31): AJ Lussier. The influence of parent-solution chemistry on the precipitation of pb-carbonates at 25⁰c, 1 bar total pressure. Unknown journal, 2005.

19. (salter1984naturalalterationofa pages 33-38): JD Salter. Natural alteration of base-metal sulphides in broken limestone. Unknown journal, 1984.

20. (keogh2019mechanismsandprevention pages 73-78): W Keogh. Mechanisms and prevention of lead sulphide (pbs) scale deposition in multiphase systems. Unknown journal, 2019.

21. (moog2022thermodynamicdatabasefor pages 1-2): H Moog. Thermodynamic database for pb and its compounds-data selection. revision. Unknown journal, 2022.

22. (lussier2005theinfluenceof pages 39-46): AJ Lussier. The influence of parent-solution chemistry on the precipitation of pb-carbonates at 25⁰c, 1 bar total pressure. Unknown journal, 2005.

### artifact-00

| Phase / formula | Diagnostic activity product, \(Q\) | \(K_{sp}\) at 25 °C | Status / indicative conditions |
|---|---:|---:|---|
| Galena, PbS | \(a_{Pb^{2+}}a_{S^{2-}}\) | Not selected in the retrieved Pb database; no defensible numerical value assigned here | Expected under reducing, sulfide-bearing conditions; at pH 5–7 and anoxic \(E_h\approx-0.1\) V, PbS is favored, whereas oxidation can yield anglesite. High chloride, higher temperature, and lower pH increase PbS solubility. (pqac-00000015) |
| Cotunnite, PbCl₂ | \(a_{Pb^{2+}}a_{Cl^-}^{2}\) | \(10^{-4.77}\) | Requires \(Q>K_{sp}\), hence high free Pb²⁺ and Cl⁻ activities; concentrated chloride can instead increase dissolved Pb through chloro-complexes, so total chloride alone is not predictive. (pqac-00000008, pqac-00000009) |
| Laurionite, PbOHCl | \(a_{Pb^{2+}}a_{OH^-}a_{Cl^-}\) | \(10^{-13.7}\) | Chloride-bearing, near-alkaline phase; the selected model gives equilibrium near pH 8.5, with substantial dissolved Pb complexation. (pqac-00000008) |
| Phosgenite, Pb₂Cl₂CO₃ | \(a_{Pb^{2+}}^{2}a_{Cl^-}^{2}a_{CO_3^{2-}}\) | \(10^{-20.64}\) | Needs both chloride and carbonate. At 25 °C, 0.035 M PbCl₂ mixed with 0.035 M NaHCO₃ produced cerussite + phosgenite at final pH ≈4.7–5.8; cerussite formed first in some runs and phosgenite appeared after aging. (pqac-00000012, pqac-00000071) |
| Cerussite, PbCO₃ | \(a_{Pb^{2+}}a_{CO_3^{2-}}\) | \(10^{-13.59}\) | Broad carbonate-phase candidate over roughly pH 4–9; observed at 25 °C throughout 0.035 M Pb–carbonate experiments, alone or with phosgenite/hydrocerussite. (pqac-00000011, pqac-00000071) |
| Hydrocerussite, Pb₃(CO₃)₂(OH)₂ | \(a_{Pb^{2+}}^{3}a_{CO_3^{2-}}^{2}a_{OH^-}^{2}\) | \(10^{-46.6}\) | Favored relative to cerussite as pH rises and CO₂ activity falls; observed alongside cerussite in carbonate-fed experiments, commonly at final/aged pH ≈6.3–9.4. (pqac-00000011, pqac-00000071) |
| Anglesite, PbSO₄ | \(a_{Pb^{2+}}a_{SO_4^{2-}}\) | \(10^{-7.84}\) | Sulfate-rich or oxidizing alternative; oxidation of PbS can generate anglesite, so redox state—not sulfate concentration alone—controls competition with galena. (pqac-00000010, pqac-00000015) |
| **Interpretive constraint** | **Precipitation requires \(Q>K_{sp}\); equilibrium saturation is \(Q=K_{sp}\). Use free-ion activities, not analytical totals.** | **These constants have different reaction stoichiometries and therefore cannot be ranked numerically as a phase-solubility series.** | **Values apply at 25 °C. For 25–90 °C, recalculate equilibrium constants and activity coefficients at the actual temperature and salinity; the table does not imply that all phases coexist.** |


*Table: Activity-based precipitation tests and selected 25 °C solubility products for the seven candidate lead solids. The criteria show why pH, redox state, ligand activities, salinity, and temperature must be evaluated together.*
