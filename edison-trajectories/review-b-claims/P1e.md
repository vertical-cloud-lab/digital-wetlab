# P1e (point 1)

**Claim (paraphrased):** Others have published unjustified metal-bisulfide Pitzer terms; that does not justify repeating them.

**Query** (Edison `job-futurehouse-paperqa3`, task `ebb0b0b8-1b1b-4433-9a31-e33086793df3`, status `success`):

> Have any researchers published Pitzer ion-interaction parameters (beta0, beta1, Cphi, theta, psi) for Fe2+-HS-, Pb2+-HS- or Zn2+-HS- interactions, for example in oilfield scale-prediction models? If so, what data were they fitted to, and have they been criticized?

---

Question: Have any researchers published Pitzer ion-interaction parameters (beta0, beta1, Cphi, theta, psi) for Fe2+-HS-, Pb2+-HS- or Zn2+-HS- interactions, for example in oilfield scale-prediction models? If so, what data were they fitted to, and have they been criticized?

## Finding

**I could not verify a published, numerically specified Pitzer parameter set for any of Fe²⁺–HS⁻, Pb²⁺–HS⁻, or Zn²⁺–HS⁻**—whether β⁽⁰⁾, β⁽¹⁾, Cφ, θ, or ψ—in the sources examined. This is a limit of the accessible literature, not proof that no proprietary database or other publication contains one. In particular, saying that a scale model *uses Pitzer equations* does not establish that it has published fitted parameters for these three specific pairs. (jang2012secondmilestonereport pages 27-32, jang2012secondmilestonereport pages 89-93, millero1998achemicalequilibrium pages 1-3)

The closest explicit attempt I found is **Jang and colleagues’ 2012 Sandia/WIPP report**, which proposed deriving Fe²⁺–HS⁻ parameters from mackinawite (FeS) solubility in sodium-sulfide solutions. Its experimental setup and measurement tables both say **“No Data to Date”**; consequently, it reports neither a completed fit nor coefficients. The same report proposed FeOH⁺–HS⁻ parameters from FeS in NaHS/Na₂S and **PbCl⁺–HS⁻** parameters from PbS in NaHS/NaCl, likewise without data. PbCl⁺–HS⁻ is **not** the requested Pb²⁺–HS⁻ pair. I found no corresponding Zn²⁺–HS⁻ determination there. The intended fitting observations were equilibrated dissolved metal and sulfide concentrations and pH across those solutions, **not an already available dataset that the report fitted**. (jang2012secondmilestonereport pages 13-19, jang2012secondmilestonereport pages 19-23, jang2012secondmilestonereport pages 27-32, jang2012secondmilestonereport pages 89-93)

## What *has* been fitted to data

Millero published Pitzer HS⁻ parameters for **Na⁺, K⁺, Mg²⁺, and Ca²⁺**, not the three metals in the question. They were inferred primarily from measurements of the **first dissociation of H₂S** in NaCl, Na–Ca–Cl, and seawater solutions at 25 °C; the KHS result drew on Goldhaber and Kaplan’s measurements. Some terms were **assigned by analogy**: β⁽¹⁾ for K⁺ was set equal to Na⁺’s, and that for Ca²⁺ equal to Mg²⁺’s. These acid-ionization measurements are not FeS, PbS, or ZnS solubility fits. Millero and Pierrot’s later Pitzer compilation likewise discusses major-ion–HS⁻ interactions and identifies additional trace-metal measurements as needed; inclusion of Fe, Pb, and Zn as minor ions in a model does not itself document fitted metal–HS⁻ binary or ternary coefficients. (millero1986thethermodynamicsand pages 5-8, millero1986thethermodynamicsand media 883f26c6, millero1998achemicalequilibrium pages 23-28, millero1998achemicalequilibrium pages 6-9)

A particularly easy misidentification is **HSO₄⁻ (bisulfate) versus HS⁻ (bisulfide)**. Published β coefficients for Fe²⁺–HSO₄⁻, Pb²⁺–HSO₄⁻, and Zn²⁺–HSO₄⁻ were used to describe *sulfate–sulfuric-acid* systems, including fits to solubility data. They are **not** metal–HS⁻ parameters and should not be transferred to sulfide-scale calculations. Likewise, a metal–sulfide aqueous-*complex formation constant* or an MS(s) solubility product is not a Pitzer ion-interaction coefficient. (charykova2010thermodynamicsofarsenates pages 1-2, charykova2010thermodynamicsofarsenates pages 2-4, charykova2010thermodynamicsofarsenates pages 4-5, rickard2006metalsulfidecomplexes pages 20-22)

## Criticism and its scope

I found **no documented criticism of a particular published Fe²⁺–HS⁻, Pb²⁺–HS⁻, or Zn²⁺–HS⁻ Pitzer fit** that I could first verify exists. There are, however, relevant published cautions about the measurements and models from which such a fit might be inferred. Rickard and Luther argue that fitting metal-sulfide solubility curves with assumed aqueous complexes can yield **nonunique stoichiometries and stability constants** unless independent evidence establishes the species; their criticism concerns *complexation models*, not a named Pitzer coefficient set. Millero notes that more concentrated-solution measurements were needed to constrain higher-order HS⁻ interactions and that sulfide speciation measurements suffer from inconsistent extrapolation and possible oxidation. Separately, an oilfield scale-prediction comparison by Ness and Sorbie found substantial sensitivity to the modeled partitioning of H₂S among phases; that is a critique of prediction inputs and workflows, **not** a validation or refutation of the three requested ion-pair parameters. (millero1986thethermodynamicsand pages 5-8, rickard2006metalsulfidecomplexes pages 20-22, ness2019rigorouscarbonateand pages 4-6, ness2019rigorouscarbonateand pages 1-2)

**Bottom line:** The accessible evidence supports *planned but unfinished* Fe²⁺–HS⁻ and PbCl⁺–HS⁻ parameter experiments, and *published, experimentally informed* major-ion–HS⁻ parameters. It does **not** establish published fitted coefficients, fitting data, or a coefficient-specific published critique for Fe²⁺–HS⁻, Pb²⁺–HS⁻, or Zn²⁺–HS⁻. (jang2012secondmilestonereport pages 27-32, millero1986thethermodynamicsand pages 5-8, jang2012secondmilestonereport pages 89-93, millero1986thethermodynamicsand media 883f26c6)

References

1. (jang2012secondmilestonereport pages 27-32): JH Jang, YL Xiong, and S Kim. Second milestone report on test plan tp 08-02," iron, lead, sulfide, and edta solubilities". Unknown journal, 2012.

2. (jang2012secondmilestonereport pages 89-93): JH Jang, YL Xiong, and S Kim. Second milestone report on test plan tp 08-02," iron, lead, sulfide, and edta solubilities". Unknown journal, 2012.

3. (millero1998achemicalequilibrium pages 1-3): Frank J. Millero and Denis Pierrot. A chemical equilibrium model for natural waters. Aquatic Geochemistry, 4:153-199, Dec 1998. URL: https://doi.org/10.1023/a:1009656023546, doi:10.1023/a:1009656023546. This article has 220 citations and is from a peer-reviewed journal.

4. (jang2012secondmilestonereport pages 13-19): JH Jang, YL Xiong, and S Kim. Second milestone report on test plan tp 08-02," iron, lead, sulfide, and edta solubilities". Unknown journal, 2012.

5. (jang2012secondmilestonereport pages 19-23): JH Jang, YL Xiong, and S Kim. Second milestone report on test plan tp 08-02," iron, lead, sulfide, and edta solubilities". Unknown journal, 2012.

6. (millero1986thethermodynamicsand pages 5-8): Frank J Millero. The thermodynamics and kinetics of the hydrogen sulfide system in natural waters. Marine Chemistry, 18:121-147, Mar 1986. URL: https://doi.org/10.1016/0304-4203(86)90003-4, doi:10.1016/0304-4203(86)90003-4. This article has 380 citations and is from a peer-reviewed journal.

7. (millero1986thethermodynamicsand media 883f26c6): Frank J Millero. The thermodynamics and kinetics of the hydrogen sulfide system in natural waters. Marine Chemistry, 18:121-147, Mar 1986. URL: https://doi.org/10.1016/0304-4203(86)90003-4, doi:10.1016/0304-4203(86)90003-4. This article has 380 citations and is from a peer-reviewed journal.

8. (millero1998achemicalequilibrium pages 23-28): Frank J. Millero and Denis Pierrot. A chemical equilibrium model for natural waters. Aquatic Geochemistry, 4:153-199, Dec 1998. URL: https://doi.org/10.1023/a:1009656023546, doi:10.1023/a:1009656023546. This article has 220 citations and is from a peer-reviewed journal.

9. (millero1998achemicalequilibrium pages 6-9): Frank J. Millero and Denis Pierrot. A chemical equilibrium model for natural waters. Aquatic Geochemistry, 4:153-199, Dec 1998. URL: https://doi.org/10.1023/a:1009656023546, doi:10.1023/a:1009656023546. This article has 220 citations and is from a peer-reviewed journal.

10. (charykova2010thermodynamicsofarsenates pages 1-2): M. V. Charykova, V. G. Krivovichev, and W. Depmeier. Thermodynamics of arsenates, selenites, and sulfates in the oxidation zone of sulfide ores. ii. systems m1, m2//so42−-h2o (m1, m2 = fe2+, fe3+, cu2+, zn2+, pb2+, ni2+, co2+, h+) at 25°c. Geology of Ore Deposits, 52:701-710, Dec 2010. URL: https://doi.org/10.1134/s1075701510080027, doi:10.1134/s1075701510080027. This article has 9 citations and is from a peer-reviewed journal.

11. (charykova2010thermodynamicsofarsenates pages 2-4): M. V. Charykova, V. G. Krivovichev, and W. Depmeier. Thermodynamics of arsenates, selenites, and sulfates in the oxidation zone of sulfide ores. ii. systems m1, m2//so42−-h2o (m1, m2 = fe2+, fe3+, cu2+, zn2+, pb2+, ni2+, co2+, h+) at 25°c. Geology of Ore Deposits, 52:701-710, Dec 2010. URL: https://doi.org/10.1134/s1075701510080027, doi:10.1134/s1075701510080027. This article has 9 citations and is from a peer-reviewed journal.

12. (charykova2010thermodynamicsofarsenates pages 4-5): M. V. Charykova, V. G. Krivovichev, and W. Depmeier. Thermodynamics of arsenates, selenites, and sulfates in the oxidation zone of sulfide ores. ii. systems m1, m2//so42−-h2o (m1, m2 = fe2+, fe3+, cu2+, zn2+, pb2+, ni2+, co2+, h+) at 25°c. Geology of Ore Deposits, 52:701-710, Dec 2010. URL: https://doi.org/10.1134/s1075701510080027, doi:10.1134/s1075701510080027. This article has 9 citations and is from a peer-reviewed journal.

13. (rickard2006metalsulfidecomplexes pages 20-22): D Rickard and GW Luther III. Metal sulfide complexes and clusters. Reviews in Mineralogy & Geochemistry, 61:421-504, Jan 2006. URL: https://doi.org/10.2138/rmg.2006.61.8, doi:10.2138/rmg.2006.61.8. This article has 202 citations and is from a domain leading peer-reviewed journal.

14. (ness2019rigorouscarbonateand pages 4-6): Giulia Ness and Kenneth S. Sorbie. Rigorous carbonate and sulfide scale predictions: what really matters? Energy & Fuels, 33:10765-10774, Oct 2019. URL: https://doi.org/10.1021/acs.energyfuels.9b02646, doi:10.1021/acs.energyfuels.9b02646. This article has 9 citations and is from a peer-reviewed journal.

15. (ness2019rigorouscarbonateand pages 1-2): Giulia Ness and Kenneth S. Sorbie. Rigorous carbonate and sulfide scale predictions: what really matters? Energy & Fuels, 33:10765-10774, Oct 2019. URL: https://doi.org/10.1021/acs.energyfuels.9b02646, doi:10.1021/acs.energyfuels.9b02646. This article has 9 citations and is from a peer-reviewed journal.
