# P7b (point 7)

**Claim (paraphrased):** Solubility data alone leave beta0 and beta1 poorly constrained, especially when both salts are very soluble.

**Query** (Edison `job-futurehouse-paperqa3`, task `895dcdbc-d6ec-4f0c-9b8a-359f983366ce`, status `success`):

> Can Pitzer binary parameters beta0 and beta1 be determined reliably from solid-solubility data alone, especially when both salts in the system are very soluble (above about 2 mol/kg)? Why did Pitzer and coworkers rely on osmotic, isopiestic and EMF data for homogeneous solutions instead?

---

Question: Can Pitzer binary parameters beta0 and beta1 be determined reliably from solid-solubility data alone, especially when both salts in the system are very soluble (above about 2 mol/kg)? Why did Pitzer and coworkers rely on osmotic, isopiestic and EMF data for homogeneous solutions instead?

**Generally, no—not reliably from solid-solubility data alone.** Solubility measurements can help constrain a Pitzer fit, but a saturated composition is a *phase-boundary condition*, not a direct measurement of how the dissolved ions’ activities vary throughout the homogeneous solution. For a simple anhydrous salt, equilibrium constrains an ion-activity product to equal a solubility constant; a hydrate also involves water activity. Consequently, changes in the fitted liquid-phase interactions can be offset by changes in the assumed solid-phase chemical potential or other interaction parameters. A phase-equilibrium-only inverse fit may therefore be non-unique. (weare1981geothermalbrinemodelingpredictionof pages 30-33, uspenskaya2011electromotiveforcemeasurements pages 1-3)

The distinction matters specifically for **β⁽⁰⁾ and β⁽¹⁾**: the Pitzer binary term has the form *B*(I) = β⁽⁰⁾ + β⁽¹⁾*g*(α√I), with an additional β⁽²⁾ term where needed. Separating β⁽⁰⁾ from β⁽¹⁾ requires observations that resolve the *ionic-strength dependence* of solution properties. Solubility observations restricted to saturated, usually concentrated compositions may instead constrain chiefly a correlated combination of parameters. When both salts are very soluble—on the order of **more than 2 mol kg⁻¹** in the question—there is no low-molality saturation boundary to supply much additional leverage on that dependence; high-concentration fits are also sensitive to other interaction terms and solid-phase assumptions. The cited studies do **not** establish 2 mol kg⁻¹ as a universal mathematical cutoff: the problem is insufficient independent information, not an absolute impossibility of using solubilities. (hovey1991thermodynamicsofaqueous pages 8-12, weare1981geothermalbrinemodelingpredictionof pages 30-33)

This is why Pitzer and coworkers emphasized measurements in **homogeneous solutions over broad concentration ranges**. Isopiestic and other osmotic measurements constrain water activity and its variation with molality; EMF measurements constrain ionic activities or activity differences. Together they test the liquid-phase model away from a solid–liquid boundary and provide substantially better leverage on its concentration-dependent parameters. Hovey, Pitzer, and Rard explicitly noted that wide-ranging isopiestic measurements made interaction parameters significant that restricted data could not reliably resolve. Weare’s Pitzer-based brine analysis generally gave solubility measurements lower weight than the typically more accurate isopiestic and cell data, reported that fitted parameters changed appreciably with weighting, and documented parameter sets that were not unique even when calculated thermodynamic properties agreed. **Solubility was useful for testing or refining the model, but not a sound sole basis for claiming independently determined β⁽⁰⁾ and β⁽¹⁾ values.** (hovey1991thermodynamicsofaqueous pages 8-12, hovey1991thermodynamicsofaqueous pages 12-15, weare1981geothermalbrinemodelingpredictionof pages 30-33)

| Data type | Direct thermodynamic quantity and identifiability implication |
|---|---|
| Saturated solid-solubility boundary | Constrains only the phase-equilibrium combination: the dissolved-ion activity product equals the solubility constant for an anhydrous salt; for a hydrated solid, water activity also enters. Thus one boundary can confound liquid-phase interaction parameters with the solid’s standard chemical potential and mixture terms. Fits can change substantially with data weighting, and solid chemical potentials have been treated as adjustable quantities, so solubility alone generally cannot identify both $\beta^{(0)}$ and $\beta^{(1)}$ uniquely (weare1981geothermalbrinemodelingpredictionof pages 30-33). |
| Unsaturated isopiestic / osmotic-coefficient data | Measure water activity, expressed through the osmotic coefficient, at many molalities and ionic strengths. Because the Pitzer binary term $B_{MX}(I)=\beta^{(0)}+\beta^{(1)}g(\alpha_1\sqrt I)+\cdots$ enters the osmotic-coefficient equations, broad concentration coverage reveals its ionic-strength dependence and separates parameter contributions far better than a saturation boundary (hovey1991thermodynamicsofaqueous pages 8-12). |
| Unsaturated EMF data | Measure ionic chemical-potential or activity differences through the Nernst relation; concentration-cell measurements across multiple compositions yield activity coefficients directly enough for Pitzer regression. EMF is described as a particularly reliable activity-coefficient method and avoids introducing an uncertain solid-phase chemical potential into each observation (uspenskaya2011electromotiveforcemeasurements pages 1-3, uspenskaya2011electromotiveforcemeasurements pages 5-6). |


*Table: Comparison of what solubility, isopiestic/osmotic, and EMF measurements constrain in a Pitzer fit. The approximately 2 mol kg⁻¹ value is not treated as a strict or universal threshold.*

References

1. (weare1981geothermalbrinemodelingpredictionof pages 30-33): JH Weare. Geothermal-brine modeling-prediction of mineral solubilities in natural waters: the na-k-mg-ca-h-cl-so sub 4-oh-hco sub 3 co sub 3-co sub 2-h sub 2 o …. Unknown journal, 1981.

2. (uspenskaya2011electromotiveforcemeasurements pages 1-3): I. Uspenskaya, N. Konstantinova, E. Veryaeva, and M. Mamontov. Electromotive force measurements and thermodynamic modelling of sodium chloride in aqueous-alcohol solvents. ArXiv, Nov 2011. URL: https://doi.org/10.5772/31247, doi:10.5772/31247. This article has 1 citations.

3. (hovey1991thermodynamicsofaqueous pages 8-12): JK Hovey, KS Pitzer, and JA Rard. Thermodynamics of aqueous sodium sulfate from 273 to 373 k and mixtures of aqueous. Unknown journal, 1991.

4. (hovey1991thermodynamicsofaqueous pages 12-15): JK Hovey, KS Pitzer, and JA Rard. Thermodynamics of aqueous sodium sulfate from 273 to 373 k and mixtures of aqueous. Unknown journal, 1991.

5. (uspenskaya2011electromotiveforcemeasurements pages 5-6): I. Uspenskaya, N. Konstantinova, E. Veryaeva, and M. Mamontov. Electromotive force measurements and thermodynamic modelling of sodium chloride in aqueous-alcohol solvents. ArXiv, Nov 2011. URL: https://doi.org/10.5772/31247, doi:10.5772/31247. This article has 1 citations.

### artifact-00

| Data type | Direct thermodynamic quantity and identifiability implication |
|---|---|
| Saturated solid-solubility boundary | Constrains only the phase-equilibrium combination: the dissolved-ion activity product equals the solubility constant for an anhydrous salt; for a hydrated solid, water activity also enters. Thus one boundary can confound liquid-phase interaction parameters with the solid’s standard chemical potential and mixture terms. Fits can change substantially with data weighting, and solid chemical potentials have been treated as adjustable quantities, so solubility alone generally cannot identify both $\beta^{(0)}$ and $\beta^{(1)}$ uniquely (pqac-00000006). |
| Unsaturated isopiestic / osmotic-coefficient data | Measure water activity, expressed through the osmotic coefficient, at many molalities and ionic strengths. Because the Pitzer binary term $B_{MX}(I)=\beta^{(0)}+\beta^{(1)}g(\alpha_1\sqrt I)+\cdots$ enters the osmotic-coefficient equations, broad concentration coverage reveals its ionic-strength dependence and separates parameter contributions far better than a saturation boundary (pqac-00000016). |
| Unsaturated EMF data | Measure ionic chemical-potential or activity differences through the Nernst relation; concentration-cell measurements across multiple compositions yield activity coefficients directly enough for Pitzer regression. EMF is described as a particularly reliable activity-coefficient method and avoids introducing an uncertain solid-phase chemical potential into each observation (pqac-00000015, pqac-00000014). |


*Table: Comparison of what solubility, isopiestic/osmotic, and EMF measurements constrain in a Pitzer fit. The approximately 2 mol kg⁻¹ value is not treated as a strict or universal threshold.*
