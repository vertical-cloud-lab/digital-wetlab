# P3b (point 3)

**Claim (paraphrased):** theta(Cl,OAc) and psi(Na,Cl,OAc) need NaCl-NaOAc-H2O data.

**Query** (Edison `job-futurehouse-paperqa3`, task `4ba541af-270c-4c7f-8e5f-86b170d6a6d5`, status `success`):

> Have the Pitzer mixing parameters theta(Cl-, acetate) and psi(Na+, Cl-, acetate) been determined from isopiestic, EMF, solubility or other data on NaCl-sodium acetate-water mixtures?

---

Question: Have the Pitzer mixing parameters theta(Cl-, acetate) and psi(Na+, Cl-, acetate) been determined from isopiestic, EMF, solubility or other data on NaCl-sodium acetate-water mixtures?

**Yes.** Dorn’s 2003 study of aqueous NaCl–sodium acetate explicitly states that it determined both Pitzer mixing parameters, θ(Cl⁻, CH₃COO⁻) and ψ(Na⁺, Cl⁻, CH₃COO⁻), by least-squares fitting. The fit used ternary **solubility measurements** at 278.15, 298.15, and 323.15 K together with published activity- and osmotic-coefficient data. The accessible summary confirms the determination but does not give numerical parameter values. (dorn2003experimentellebestimmungund pages 1-2)

The relevant experimental record is worth distinguishing from that fit:

| Source | Mixture data and method | Explicit Pitzer mixing parameters fitted? |
|---|---|---|
| Dorn (2003), thesis English summary | NaOAc–NaCl–H₂O solubilities at 278.15, 298.15, and 323.15 K, combined with literature activity- and osmotic-coefficient data; least-squares fitting (dorn2003experimentellebestimmungund pages 1-2) | **Yes:** both \(\theta_{\mathrm{Cl,OAc}}\) and \(\psi_{\mathrm{Na,Cl,OAc}}\). Numerical values are not present in the accessible summary. |
| Jones & Prue (1974) | Isopiestic osmotic coefficients for NaCl–NaOAc–H₂O at 25 °C (jones1974excessgibbsenergies pages 1-4) | **No explicit Pitzer fit.** Reports the Scatchard parameter \(b_{01}=-0.0156\ \mathrm{kg\,mol^{-1}}\), which must not be identified directly as Pitzer \(\theta\) or \(\psi\) (jones1974excessgibbsenergies pages 4-7). |
| Lanier (1965) | Glass-electrode EMF measurements of NaCl activity coefficients in NaCl–NaOAc–H₂O at 25 °C and ionic strengths 1, 3, and 5 mol·kg⁻¹ (lanier1965activitycoefficientsof pages 1-2, lanier1965activitycoefficientsof pages 3-4) | **No.** Reports activity coefficients/Harned-rule behavior, not Pitzer \(\theta_{\mathrm{Cl,OAc}}\) or \(\psi_{\mathrm{Na,Cl,OAc}}\). |


*Table: The direct Pitzer determination is a combined solubility-plus-literature-activity/osmotic fit, while the earlier isopiestic and EMF studies supplied mixture thermodynamics in other parameterizations. This distinction prevents treating the Scatchard coefficient or raw EMF activities as Pitzer parameters.*

Thus, the answer is not merely that suitable data exist: **both requested Pitzer parameters have been fitted** for this mixture. Earlier isopiestic results and EMF measurements characterize the mixture, but Jones and Prue’s reported Scatchard coefficient is **not** itself θ(Cl⁻, acetate), and Lanier did **not** report either Pitzer parameter. The available summary does not establish whether Lanier’s particular EMF dataset was included in Dorn’s fit. (dorn2003experimentellebestimmungund pages 1-2, jones1974excessgibbsenergies pages 1-4, jones1974excessgibbsenergies pages 4-7, lanier1965activitycoefficientsof pages 1-2)

References

1. (dorn2003experimentellebestimmungund pages 1-2): J Dorn. Experimentelle bestimmung und thermodynamische modellierung von löslichkeitsgleichgewichten im system na+-ca2+-oac–cl–h2o. Unknown journal, 2003.

2. (jones1974excessgibbsenergies pages 1-4): R. A. Jones and J. E. Prue. Excess gibbs energies of aqueous mixtures of sodium chloride, potassium chloride, sodium acetate, and potassium acetate at 25°c. Journal of Solution Chemistry, 3:585-592, Aug 1974. URL: https://doi.org/10.1007/bf00650402, doi:10.1007/bf00650402. This article has 9 citations and is from a peer-reviewed journal.

3. (jones1974excessgibbsenergies pages 4-7): R. A. Jones and J. E. Prue. Excess gibbs energies of aqueous mixtures of sodium chloride, potassium chloride, sodium acetate, and potassium acetate at 25°c. Journal of Solution Chemistry, 3:585-592, Aug 1974. URL: https://doi.org/10.1007/bf00650402, doi:10.1007/bf00650402. This article has 9 citations and is from a peer-reviewed journal.

4. (lanier1965activitycoefficientsof pages 1-2): R. D. Lanier. Activity coefficients of nacl in aqueous three-component solutions by cation-sensitive glass electrodes. [25/sup 0/c]. The Journal of Physical Chemistry, 69:3992-3998, Nov 1965. URL: https://doi.org/10.1021/j100895a058, doi:10.1021/j100895a058. This article has 130 citations.

5. (lanier1965activitycoefficientsof pages 3-4): R. D. Lanier. Activity coefficients of nacl in aqueous three-component solutions by cation-sensitive glass electrodes. [25/sup 0/c]. The Journal of Physical Chemistry, 69:3992-3998, Nov 1965. URL: https://doi.org/10.1021/j100895a058, doi:10.1021/j100895a058. This article has 130 citations.

### artifact-00

| Source | Mixture data and method | Explicit Pitzer mixing parameters fitted? |
|---|---|---|
| Dorn (2003), thesis English summary | NaOAc–NaCl–H₂O solubilities at 278.15, 298.15, and 323.15 K, combined with literature activity- and osmotic-coefficient data; least-squares fitting (pqac-00000015) | **Yes:** both \(\theta_{\mathrm{Cl,OAc}}\) and \(\psi_{\mathrm{Na,Cl,OAc}}\). Numerical values are not present in the accessible summary. |
| Jones & Prue (1974) | Isopiestic osmotic coefficients for NaCl–NaOAc–H₂O at 25 °C (pqac-00000009) | **No explicit Pitzer fit.** Reports the Scatchard parameter \(b_{01}=-0.0156\ \mathrm{kg\,mol^{-1}}\), which must not be identified directly as Pitzer \(\theta\) or \(\psi\) (pqac-00000010). |
| Lanier (1965) | Glass-electrode EMF measurements of NaCl activity coefficients in NaCl–NaOAc–H₂O at 25 °C and ionic strengths 1, 3, and 5 mol·kg⁻¹ (pqac-00000023, pqac-00000025) | **No.** Reports activity coefficients/Harned-rule behavior, not Pitzer \(\theta_{\mathrm{Cl,OAc}}\) or \(\psi_{\mathrm{Na,Cl,OAc}}\). |


*Table: The direct Pitzer determination is a combined solubility-plus-literature-activity/osmotic fit, while the earlier isopiestic and EMF studies supplied mixture thermodynamics in other parameterizations. This distinction prevents treating the Scatchard coefficient or raw EMF activities as Pitzer parameters.*
