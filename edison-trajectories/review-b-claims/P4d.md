# P4d (point 4)

**Claim (paraphrased):** Felmy et al. added dependent parameters, including a C term for Na-PbCl4 with no matching B term.

**Query** (Edison `job-futurehouse-paperqa3`, task `84f3091f-f2d0-4f2c-9dbf-b440863d1f32`, status `success`):

> What Pitzer parameters did Felmy et al. (2000) include in their Pb-Na-K-Ca-Mg-H-Cl-SO4-H2O model, such as theta(Na,Pb), B(Na,PbCl3-) and C(Na,PbCl4 2-)? Is it considered physically justified to include a third virial coefficient for an ion pair without the corresponding second virial (beta0/beta1) terms?

---

Question: What Pitzer parameters did Felmy et al. (2000) include in their Pb-Na-K-Ca-Mg-H-Cl-SO4-H2O model, such as theta(Na,Pb), B(Na,PbCl3-) and C(Na,PbCl4 2-)? Is it considered physically justified to include a third virial coefficient for an ion pair without the corresponding second virial (beta0/beta1) terms?

### Parameters attributable to Felmy et al. (2000)

The accessible evidence verifies **θ(Na⁺, Pb²⁺) = 0.10**: a later Sandia lead-model table explicitly attributes that value to Felmy et al. It also attributes **λ(Na⁺, PbCl₂⁰) = −0.11** to Felmy; λ describes an interaction with a *neutral* complex, not a θ interaction between like-charged ions. (xiong2017apitzermodel pages 1-13)

| Interaction | Verified value | Actual attribution | Caveat |
|---|---:|---|---|
| $\theta(\mathrm{Na^+,Pb^{2+}})$ | $0.10$ | Felmy et al. (2000), as explicitly cited by Xiong et al. (2017) (xiong2017apitzermodel pages 1-13) | This is a like-charge cation-mixing parameter, not a $B$ or $C^\phi$ coefficient. |
| $\lambda(\mathrm{Na^+,PbCl_2^0})$ | $-0.11$ | Felmy et al. (2000), as explicitly cited by Xiong et al. (2017) (xiong2017apitzermodel pages 1-13) | Neutral-species interaction; it should not be labeled $\theta$. |
| $\mathrm{Na^+/PbCl_3^-}$ | $\beta^{(0)}=-0.0605$; $\beta^{(1)}=0$; $C^\phi=0.091$ | Xiong et al. (2013), as reported by Xiong et al. (2017) (xiong2017apitzermodel pages 1-13) | These values are **not** attributed to Felmy et al. (2000). |
| $\mathrm{Na^+/PbCl_4^{2-}}$ | $\beta^{(0)}=-0.0683\pm0.009$; $\beta^{(1)}=2.104\pm0.09$; no $C^\phi$ listed | Hagemann (1999), reproduced by Moog (2022) (moog2022thermodynamicdatabasefor pages 4-6, moog2022thermodynamicdatabasefor media a4017515) | These values are **not** Felmy parameters. |
| Felmy's own $B(\mathrm{Na^+,PbCl_3^-})$ and $C(\mathrm{Na^+,PbCl_4^{2-}})$ | **Unverified** | The original Felmy et al. (2000) parameter table was unavailable in the retrieved material | Neither the Xiong nor Hagemann values should be substituted or relabeled as Felmy's without checking the original article. |


*Table: Separates parameters explicitly traceable to Felmy et al. (2000) from later Xiong and Hagemann parameterizations, preventing numerical values from being misattributed.*

**The requested Felmy-specific values of B(Na⁺, PbCl₃⁻) and C(Na⁺, PbCl₄²⁻) remain unverified.** Felmy et al.’s original parameter table was not obtainable in this search. This distinction matters: the Na⁺–PbCl₃⁻ coefficients in the later Sandia table are attributed to *Xiong et al. (2013)*, whereas the Na⁺–PbCl₄²⁻ coefficients reproduced by Moog are attributed to *Hagemann (1999)*. Neither set establishes what Felmy reported, or whether Felmy omitted β⁽⁰⁾ and β⁽¹⁾ for a particular pair. (xiong2017apitzermodel pages 1-13, moog2022thermodynamicdatabasefor pages 4-6, moog2022thermodynamicdatabasefor media a4017515)

### Is a third-virial term without second-virial terms justified?

**It is mathematically permissible, but it needs empirical and physical justification; it is not automatically forbidden by Pitzer theory.** In the excess-Gibbs-energy expansion, the pair-interaction contribution is quadratic in ion amounts, while the triplet contribution is cubic. The conventional binary-electrolyte pair coefficient *B* is parameterized with β⁽⁰⁾ and β⁽¹⁾ (sometimes β⁽²⁾); *C* represents the distinct, higher-order contribution. Thus setting both β terms to zero while fitting a nonzero *C* gives a model whose fitted short-range effect appears at higher concentration, without implying that a nonzero pair coefficient is a mathematical prerequisite. Conversely, such a fit alone does **not** demonstrate that pair interactions are physically absent: the omitted terms and the model’s predictive behavior, particularly outside the fitted concentration range, warrant scrutiny. This is a methodological assessment, **not** a verified description of Felmy’s unexamined parameter table. (batch2008documenthistory pages 27-29, lassin2015athermodynamicmodel pages 10-14)

References

1. (xiong2017apitzermodel pages 1-13): Y Xiong, LD Kirkes, J Knox, C Marrs, and HL Burton. A pitzer model for hydrolysis of lead to high ionic strength: applications to low temperature geochemical processes. ArXiv, Jan 2017. URL: https://doi.org/10.1130/abs/2017am-296210, doi:10.1130/abs/2017am-296210. This article has 0 citations.

2. (moog2022thermodynamicdatabasefor pages 4-6): H Moog. Thermodynamic database for pb and its compounds-data selection. revision. Unknown journal, 2022.

3. (moog2022thermodynamicdatabasefor media a4017515): H Moog. Thermodynamic database for pb and its compounds-data selection. revision. Unknown journal, 2022.

4. (batch2008documenthistory pages 27-29): ID Batch. Document history. Unknown journal, 2008.

5. (lassin2015athermodynamicmodel pages 10-14): A. Lassin, C. Christov, L. André, and M. Azaroual. A thermodynamic model of aqueous electrolyte solution behavior and solid-liquid equilibrium in the li-h-na-k-cl-oh-h2o system to very high concentrations (40 molal) and from 0 to 250 c. American Journal of Science, 315:204-256, Mar 2015. URL: https://doi.org/10.2475/03.2015.02, doi:10.2475/03.2015.02. This article has 73 citations and is from a peer-reviewed journal.

### artifact-00

| Interaction | Verified value | Actual attribution | Caveat |
|---|---:|---|---|
| $\theta(\mathrm{Na^+,Pb^{2+}})$ | $0.10$ | Felmy et al. (2000), as explicitly cited by Xiong et al. (2017) (pqac-00000019) | This is a like-charge cation-mixing parameter, not a $B$ or $C^\phi$ coefficient. |
| $\lambda(\mathrm{Na^+,PbCl_2^0})$ | $-0.11$ | Felmy et al. (2000), as explicitly cited by Xiong et al. (2017) (pqac-00000019) | Neutral-species interaction; it should not be labeled $\theta$. |
| $\mathrm{Na^+/PbCl_3^-}$ | $\beta^{(0)}=-0.0605$; $\beta^{(1)}=0$; $C^\phi=0.091$ | Xiong et al. (2013), as reported by Xiong et al. (2017) (pqac-00000019) | These values are **not** attributed to Felmy et al. (2000). |
| $\mathrm{Na^+/PbCl_4^{2-}}$ | $\beta^{(0)}=-0.0683\pm0.009$; $\beta^{(1)}=2.104\pm0.09$; no $C^\phi$ listed | Hagemann (1999), reproduced by Moog (2022) (pqac-00000003, pqac-00000017) | These values are **not** Felmy parameters. |
| Felmy's own $B(\mathrm{Na^+,PbCl_3^-})$ and $C(\mathrm{Na^+,PbCl_4^{2-}})$ | **Unverified** | The original Felmy et al. (2000) parameter table was unavailable in the retrieved material | Neither the Xiong nor Hagemann values should be substituted or relabeled as Felmy's without checking the original article. |


*Table: Separates parameters explicitly traceable to Felmy et al. (2000) from later Xiong and Hagemann parameterizations, preventing numerical values from being misattributed.*
