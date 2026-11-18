# P1d (point 1)

**Claim (paraphrased):** Na+-HS- interactions can be measured in NaHS solutions.

**Query** (Edison `job-futurehouse-paperqa3`, task `3cbafdb5-d250-4f65-a19c-32dbe5edccdc`, status `success`):

> What Pitzer parameters have been published for Na+-HS- and other major cation-bisulfide interactions, and from what data were they derived (NaHS solutions, H2S dissociation constants in ionic media, H2S solubility in salt solutions)?

---

Question: What Pitzer parameters have been published for Na+-HS- and other major cation-bisulfide interactions, and from what data were they derived (NaHS solutions, H2S dissociation constants in ionic media, H2S solubility in salt solutions)?

## Published cation–bisulfide parameters

The clearest published set is Millero’s **25 °C Pitzer parameterization of HS⁻ interactions with major seawater cations**. Its β⁽⁰⁾ and β⁽¹⁾ values were inferred chiefly from measurements of the *first dissociation of H₂S in ionic media*, rather than from activity measurements on the corresponding pure bisulfide salts. Millero’s Table V does **not** report Cφ values. (millero1986thethermodynamicsand pages 5-8, millero1986thethermodynamicsand media f3e8f829)

| Salt / cation–HS⁻ pair | β⁽⁰⁾ | β⁽¹⁾ | Data basis and fitting constraint |
|---|---:|---:|---|
| NaHS (Na⁺–HS⁻) | −0.103 | 0.884 | Fitted to Almgren et al. (1976) measurements of the **first H₂S dissociation constant in NaCl media**, not to NaHS-only activity data; reported uncertainties are ±0.020 and ±0.050, respectively. |
| KHS (K⁺–HS⁻) | −0.337 | 0.884 | Derived from Goldhaber and Kaplan (1975) first-dissociation measurements in seawater/chloride media, including 0.67 M KCl; β⁽¹⁾ was constrained equal to the NaHS value. |
| Mg(HS)₂ (Mg²⁺–HS⁻) | 0.466 | 2.264 | Inferred from Almgren et al. (1976) H₂S first-dissociation measurements in NaCaCl and seawater mixed media, rather than from binary Mg(HS)₂ activity data. |
| Ca(HS)₂ (Ca²⁺–HS⁻) | 0.069 | 2.264 | Inferred from the mixed-media Almgren et al. data; β⁽¹⁾ was constrained equal to the Mg²⁺–HS⁻ value. |
| Scope of table | — | — | Millero’s 25 °C **binary Pitzer ion-interaction terms**; no numerical C⁽φ⁾ term was reported in Table V. (millero1986thethermodynamicsand pages 5-8, millero1986thethermodynamicsand media f3e8f829) |


*Table: Millero’s 1986 Table V parameters at 25 °C and the ionic-medium dissociation data used to infer them. These are binary Pitzer β terms—not direct binary-salt measurements—and the source reports no Cφ values.*

For Na⁺–HS⁻, Millero fitted Almgren and co-workers’ NaCl-medium dissociation measurements and reported β⁽⁰⁾ = −0.103 ± 0.020 and β⁽¹⁾ = 0.884 ± 0.050, alongside an infinite-dilution pK₁ = 6.976 ± 0.005. The Mg²⁺ and Ca²⁺ entries were inferred from Almgren’s mixed chloride and seawater measurements. Millero assigned K⁺–HS⁻ using Goldhaber and Kaplan’s measurements, **setting β⁽¹⁾(K⁺–HS⁻) equal to the Na⁺ value**; β⁽¹⁾(Ca²⁺–HS⁻) was likewise set equal to the Mg²⁺ value. Those equalities are fitting constraints, not independent determinations. Millero cautioned that more concentrated NaCl measurements were needed to constrain higher-order terms and Cl⁻–HS⁻ interactions. (millero1986thethermodynamicsand pages 5-8, millero1986thethermodynamicsand media f3e8f829)

## What the three experimental routes measure

**NaHS solutions.** Herr and Helz (1976) directly measured *mean stoichiometric activity coefficients of NaHS* by junction-free potentiometry, over approximately 0.003–0.2 mol kg⁻¹ and 12–83 °C, both with negligible dissolved H₂S and under H₂S gas. For H₂S-free NaHS at 25 °C, they reported mean activity coefficients of 0.757 at 0.1 m and 0.700 at 0.2 m. They fitted a Guggenheim-type activity equation whose empirical coefficient **B = 0.017 kg mol⁻¹** near 25 °C under H₂S-free conditions. **B is not a Pitzer β⁽⁰⁾ or β⁽¹⁾**, and their paper does not supply a corresponding Pitzer Cφ. Adding H₂S changed the measured NaHS activity coefficients, so the gas-containing and H₂S-free data are not interchangeable. These measurements provide a direct *potential check or refitting dataset* for Na⁺–HS⁻ behavior; they are not the data Millero identifies as the basis of his Table V fit. (herr1976measurementofthe pages 1-4, herr1976measurementofthe pages 7-10, herr1976measurementofthe pages 15-18, millero1986thethermodynamicsand pages 5-8)

**H₂S dissociation in ionic media.** The relevant equilibrium is H₂S ⇌ H⁺ + HS⁻: converting a measured concentration-based K₁ to a thermodynamic constant requires the activity-coefficient ratio γH⁺γHS⁻/γH₂S. Consequently, fitting pK₁ across salt media can constrain HS⁻ interaction terms *conditional on the other activity corrections in the model*. Almgren et al.’s measurements in NaCl, mixed calcium-chloride media and seawater underpin Millero’s Na⁺, Mg²⁺ and Ca²⁺ entries. Goldhaber and Kaplan (1975) measured first-dissociation constants spectrophotometrically in seawater/chloride media and also list **pK₁′ = 6.686 in 0.67 M KCl**; that is a dissociation measurement, not a KHS activity measurement. Their separate potentiometric KCl experiments on the *second* dissociation, HS⁻ ⇌ H⁺ + S²⁻, must not be mistaken for the source of a directly measured K⁺–HS⁻ binary parameter. The studies also used different pH scales and definitions of apparent or stoichiometric constants. (millero1986thethermodynamicsand pages 5-8, millero1986thethermodynamicsand pages 8-11, goldhaber1975apparentdissociationconstants pages 1-4, goldhaber1975apparentdissociationconstants pages 4-7, goldhaber1975apparentdissociationconstants pages 7-11)

**H₂S solubility in salts.** Solubility experiments primarily constrain *neutral dissolved H₂S* and its salting-out or gas–ion interactions, **not β⁽⁰⁾ or β⁽¹⁾ for ionic HS⁻**. Millero summarizes Douabul and Riley’s water/seawater solubility measurements over 2–30 °C and salinities 0–40 with a Setschenow-type relation, ln(C⁰/C) = kS. He separately gives, for H₂S in seawater, a salting coefficient k′ = 0.020 in the convention log(C⁰/C) = k′I and γgas ≈ 1.03. Neither number should be inserted as a Na⁺–HS⁻ Pitzer coefficient. Millero noted that binary-salt solubility measurements were sparse and high-ionic-strength solubility data lacking. Solubility can inform an HS⁻ parameter only indirectly, if ionization/speciation and the neutral-H₂S contribution are independently accounted for. (millero1986thethermodynamicsand pages 1-5, millero1986thethermodynamicsand pages 5-8)

**Practical interpretation.** Millero’s four β pairs are useful published *25 °C, model-dependent* cation–HS⁻ estimates. The available source table establishes neither measured Cφ coefficients nor a temperature-dependent or concentrated-brine parameterization for these pairs; assigning zero to an unreported Cφ is a modeling choice, not an experimental result. (millero1986thethermodynamicsand pages 5-8, millero1986thethermodynamicsand media f3e8f829)

References

1. (millero1986thethermodynamicsand pages 5-8): Frank J Millero. The thermodynamics and kinetics of the hydrogen sulfide system in natural waters. Marine Chemistry, 18:121-147, Mar 1986. URL: https://doi.org/10.1016/0304-4203(86)90003-4, doi:10.1016/0304-4203(86)90003-4. This article has 380 citations and is from a peer-reviewed journal.

2. (millero1986thethermodynamicsand media f3e8f829): Frank J Millero. The thermodynamics and kinetics of the hydrogen sulfide system in natural waters. Marine Chemistry, 18:121-147, Mar 1986. URL: https://doi.org/10.1016/0304-4203(86)90003-4, doi:10.1016/0304-4203(86)90003-4. This article has 380 citations and is from a peer-reviewed journal.

3. (herr1976measurementofthe pages 1-4): F. L. Herr and G. R. Helz. Measurement of the activity coefficient of aqueous nahs to 80°c and 0.2m in the system nahs−h2s−h2o. Journal of Solution Chemistry, 5:833-852, Dec 1976. URL: https://doi.org/10.1007/bf01167238, doi:10.1007/bf01167238. This article has 10 citations and is from a peer-reviewed journal.

4. (herr1976measurementofthe pages 7-10): F. L. Herr and G. R. Helz. Measurement of the activity coefficient of aqueous nahs to 80°c and 0.2m in the system nahs−h2s−h2o. Journal of Solution Chemistry, 5:833-852, Dec 1976. URL: https://doi.org/10.1007/bf01167238, doi:10.1007/bf01167238. This article has 10 citations and is from a peer-reviewed journal.

5. (herr1976measurementofthe pages 15-18): F. L. Herr and G. R. Helz. Measurement of the activity coefficient of aqueous nahs to 80°c and 0.2m in the system nahs−h2s−h2o. Journal of Solution Chemistry, 5:833-852, Dec 1976. URL: https://doi.org/10.1007/bf01167238, doi:10.1007/bf01167238. This article has 10 citations and is from a peer-reviewed journal.

6. (millero1986thethermodynamicsand pages 8-11): Frank J Millero. The thermodynamics and kinetics of the hydrogen sulfide system in natural waters. Marine Chemistry, 18:121-147, Mar 1986. URL: https://doi.org/10.1016/0304-4203(86)90003-4, doi:10.1016/0304-4203(86)90003-4. This article has 380 citations and is from a peer-reviewed journal.

7. (goldhaber1975apparentdissociationconstants pages 1-4): Martin B Goldhaber and I.R Kaplan. Apparent dissociation constants of hydrogen sulfide in chloride solutions. Marine Chemistry, 3:83-104, Jun 1975. URL: https://doi.org/10.1016/0304-4203(75)90016-x, doi:10.1016/0304-4203(75)90016-x. This article has 105 citations and is from a peer-reviewed journal.

8. (goldhaber1975apparentdissociationconstants pages 4-7): Martin B Goldhaber and I.R Kaplan. Apparent dissociation constants of hydrogen sulfide in chloride solutions. Marine Chemistry, 3:83-104, Jun 1975. URL: https://doi.org/10.1016/0304-4203(75)90016-x, doi:10.1016/0304-4203(75)90016-x. This article has 105 citations and is from a peer-reviewed journal.

9. (goldhaber1975apparentdissociationconstants pages 7-11): Martin B Goldhaber and I.R Kaplan. Apparent dissociation constants of hydrogen sulfide in chloride solutions. Marine Chemistry, 3:83-104, Jun 1975. URL: https://doi.org/10.1016/0304-4203(75)90016-x, doi:10.1016/0304-4203(75)90016-x. This article has 105 citations and is from a peer-reviewed journal.

10. (millero1986thethermodynamicsand pages 1-5): Frank J Millero. The thermodynamics and kinetics of the hydrogen sulfide system in natural waters. Marine Chemistry, 18:121-147, Mar 1986. URL: https://doi.org/10.1016/0304-4203(86)90003-4, doi:10.1016/0304-4203(86)90003-4. This article has 380 citations and is from a peer-reviewed journal.

### artifact-00

| Salt / cation–HS⁻ pair | β⁽⁰⁾ | β⁽¹⁾ | Data basis and fitting constraint |
|---|---:|---:|---|
| NaHS (Na⁺–HS⁻) | −0.103 | 0.884 | Fitted to Almgren et al. (1976) measurements of the **first H₂S dissociation constant in NaCl media**, not to NaHS-only activity data; reported uncertainties are ±0.020 and ±0.050, respectively. |
| KHS (K⁺–HS⁻) | −0.337 | 0.884 | Derived from Goldhaber and Kaplan (1975) first-dissociation measurements in seawater/chloride media, including 0.67 M KCl; β⁽¹⁾ was constrained equal to the NaHS value. |
| Mg(HS)₂ (Mg²⁺–HS⁻) | 0.466 | 2.264 | Inferred from Almgren et al. (1976) H₂S first-dissociation measurements in NaCaCl and seawater mixed media, rather than from binary Mg(HS)₂ activity data. |
| Ca(HS)₂ (Ca²⁺–HS⁻) | 0.069 | 2.264 | Inferred from the mixed-media Almgren et al. data; β⁽¹⁾ was constrained equal to the Mg²⁺–HS⁻ value. |
| Scope of table | — | — | Millero’s 25 °C **binary Pitzer ion-interaction terms**; no numerical C⁽φ⁾ term was reported in Table V. (pqac-00000006, pqac-00000010) |


*Table: Millero’s 1986 Table V parameters at 25 °C and the ionic-medium dissociation data used to infer them. These are binary Pitzer β terms—not direct binary-salt measurements—and the source reports no Cφ values.*
