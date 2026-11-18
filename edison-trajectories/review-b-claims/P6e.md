# P6e (point 6)

**Claim (paraphrased):** The Rice group fitted barite solubility with only beta2 for Ba-SO4.

**Query** (Edison `job-futurehouse-paperqa3`, task `507f853a-dc07-421c-af18-0d52ec4f6844`, status `success`):

> In the Rice University (Tomson, Kan and coworkers) Pitzer models for barite solubility in brines, which Ba2+-SO42- Pitzer parameters were used (for example only beta(2) without beta0 or beta1), and could an explicit BaSO4 association constant fit the same data?

---

Question: In the Rice University (Tomson, Kan and coworkers) Pitzer models for barite solubility in brines, which Ba2+-SO42- Pitzer parameters were used (for example only beta(2) without beta0 or beta1), and could an explicit BaSO4 association constant fit the same data?

## Ba²⁺–SO₄²⁻ parameters and aqueous association

**The Rice parameter choice cannot be established from the sources I could inspect.** The relevant work includes Shi, Kan, Fan and Tomson’s 2012 study of barite solubility in up to 6 molal NaCl at high temperature and pressure. An accessible paper discussing that study confirms the importance of pressure-dependent Pitzer coefficients, but does not reproduce its Ba²⁺–SO₄²⁻ parameter table. I therefore cannot verify the proposed characterization—*β⁽²⁾ only, with neither β⁽⁰⁾ nor β⁽¹⁾*—or state whether its Ba²⁺–SO₄²⁻ interaction included Cφ. Treating an unlisted coefficient as zero would also require checking the model’s conventions and supplementary information. (habibi2020alaboratoryworkflow pages 3-5)

There **is** direct precedent for fitting barite-solubility behavior with an explicit neutral aqueous pair. Vicum’s independent analysis combines a Pitzer activity model with Ba²⁺ + SO₄²⁻ ⇌ BaSO₄(aq); adding the pair improves agreement with measured solubility in **aqueous Na₂SO₄**, especially at higher concentrations. Its reported 25 °C values, log₁₀ K_IP = −2.72 or −2.26, use the *dissociation* definition K_IP = a(Ba²⁺)a(SO₄²⁻)/a[BaSO₄(aq)]. For the reverse, association reaction, these correspond to log₁₀ K_assoc = +2.72 or +2.26, respectively. They are literature alternatives, not fitted constants for the Rice data. (lars2005investigationofthe pages 80-83, lars2005investigationofthe pages 83-89, lars2005investigationofthe pages 105-111)

| Model/data set | Ba²⁺–SO₄²⁻ treatment established by accessible evidence | What can be concluded |
|---|---|---|
| Rice—Shi, Kan, Fan & Tomson (2012), barite in NaCl to 250 °C, 1500 bar, and 6 molal NaCl | The exact selection of $\beta^{(0)}$, $\beta^{(1)}$, $\beta^{(2)}$, and $C^\phi$ was **not verifiable** because the primary parameter table was inaccessible. Therefore, the available evidence does **not** justify saying that they used “only $\beta^{(2)}$.” A later source confirms the study’s high-$T$, high-$P$, 6 m NaCl scope and the importance of pressure-dependent virial coefficients, but does not reproduce that table. (habibi2020alaboratoryworkflow pages 3-5) | Parameter usage must be checked directly in the article/SI (DOI: 10.1021/ie2020558); no unsupported beta-only assignment should be made. |
| Vicum (2005), independent Na₂SO₄–BaSO₄ modeling | Pitzer calculations explicitly included neutral $\mathrm{BaSO_4(aq)}$. Adding the pair improved agreement with solubility data, especially at higher sulfate concentration. Reported $\log_{10}K_{IP}=-2.72$ or $-2.26$ uses $K_{IP}=a_{Ba^{2+}}a_{SO_4^{2-}}/a_{BaSO_4}$—a **dissociation** convention—so the corresponding association values are $\log_{10}K_{assoc}=+2.72$ or $+2.26$. (lars2005investigationofthe pages 80-83, lars2005investigationofthe pages 83-89) | Explicit association can fit barite-solubility behavior in a related electrolyte system, but this is **not** a demonstrated refit of the Rice NaCl–temperature–pressure data. |


*Table: Comparison of what can be verified for the Rice parameterization and the independent evidence for an explicit aqueous BaSO₄ pair. It separates demonstrated results from claims that require the inaccessible primary parameter table.*

**Conclusion:** An association-based representation is thermodynamically plausible and has reproduced related barite-solubility observations; it is **not established here** that a single explicit association constant reproduces the *same Rice NaCl–temperature–pressure dataset* with comparable accuracy. Such a claim needs a refit with specified free-ion Pitzer parameters, temperature/pressure dependence, and a treatment of the neutral pair’s activity coefficient. Total solubility alone may confound ion association with fitted ion interactions; independent speciation or activity measurements would help distinguish them. (lars2005investigationofthe pages 83-89, matyskin2016onthesolubility pages 14-17)

References

1. (habibi2020alaboratoryworkflow pages 3-5): Ali Habibi, Charles E. Fensky, Morteza Roostaei, Mahdi Mahmoudi, Vahidoddin Fattahpour, Hongbo Zeng, and Mohtada Sadrzadeh. A laboratory workflow for characterization of scaling deposits in thermal wells. Energies, 13:3184, Jun 2020. URL: https://doi.org/10.3390/en13123184, doi:10.3390/en13123184. This article has 3 citations.

2. (lars2005investigationofthe pages 80-83): Lars Vicum. Investigation of the influence of turbulent mixing on precipitation processes carried out in stirred tank reactors. ArXiv, 2005. URL: https://doi.org/10.3929/ethz-a-005069682, doi:10.3929/ethz-a-005069682. This article has 9 citations.

3. (lars2005investigationofthe pages 83-89): Lars Vicum. Investigation of the influence of turbulent mixing on precipitation processes carried out in stirred tank reactors. ArXiv, 2005. URL: https://doi.org/10.3929/ethz-a-005069682, doi:10.3929/ethz-a-005069682. This article has 9 citations.

4. (lars2005investigationofthe pages 105-111): Lars Vicum. Investigation of the influence of turbulent mixing on precipitation processes carried out in stirred tank reactors. ArXiv, 2005. URL: https://doi.org/10.3929/ethz-a-005069682, doi:10.3929/ethz-a-005069682. This article has 9 citations.

5. (matyskin2016onthesolubility pages 14-17): Artem V. Matyskin. On the solubility of radium sulfate and carbonate. Unknown, Jan 2016. URL: https://doi.org/10.13140/rg.2.1.4329.0009, doi:10.13140/rg.2.1.4329.0009. This article has 13 citations.

### artifact-00

| Model/data set | Ba²⁺–SO₄²⁻ treatment established by accessible evidence | What can be concluded |
|---|---|---|
| Rice—Shi, Kan, Fan & Tomson (2012), barite in NaCl to 250 °C, 1500 bar, and 6 molal NaCl | The exact selection of $\beta^{(0)}$, $\beta^{(1)}$, $\beta^{(2)}$, and $C^\phi$ was **not verifiable** because the primary parameter table was inaccessible. Therefore, the available evidence does **not** justify saying that they used “only $\beta^{(2)}$.” A later source confirms the study’s high-$T$, high-$P$, 6 m NaCl scope and the importance of pressure-dependent virial coefficients, but does not reproduce that table. (pqac-00000012) | Parameter usage must be checked directly in the article/SI (DOI: 10.1021/ie2020558); no unsupported beta-only assignment should be made. |
| Vicum (2005), independent Na₂SO₄–BaSO₄ modeling | Pitzer calculations explicitly included neutral $\mathrm{BaSO_4(aq)}$. Adding the pair improved agreement with solubility data, especially at higher sulfate concentration. Reported $\log_{10}K_{IP}=-2.72$ or $-2.26$ uses $K_{IP}=a_{Ba^{2+}}a_{SO_4^{2-}}/a_{BaSO_4}$—a **dissociation** convention—so the corresponding association values are $\log_{10}K_{assoc}=+2.72$ or $+2.26$. (pqac-00000008, pqac-00000009) | Explicit association can fit barite-solubility behavior in a related electrolyte system, but this is **not** a demonstrated refit of the Rice NaCl–temperature–pressure data. |


*Table: Comparison of what can be verified for the Rice parameterization and the independent evidence for an explicit aqueous BaSO₄ pair. It separates demonstrated results from claims that require the inaccessible primary parameter table.*
