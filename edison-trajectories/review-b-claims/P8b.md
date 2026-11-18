# P8b (point 8)

**Claim (paraphrased):** Enough thermal data exist for FeCl2 to build a temperature-dependent model.

**Query** (Edison `job-futurehouse-paperqa3`, task `03df001b-bc67-4bf7-a88b-6da0ef6a30d4`, status `success`):

> Have temperature-dependent Pitzer parameters for aqueous FeCl2 been published, and what heat capacity, enthalpy of dilution, vapor pressure and solubility data exist for FeCl2 solutions above 25 C?

---

Question: Have temperature-dependent Pitzer parameters for aqueous FeCl2 been published, and what heat capacity, enthalpy of dilution, vapor pressure and solubility data exist for FeCl2 solutions above 25 C?

## Temperature-dependent Pitzer parameters

**Yes.** Muñoz and Moog published a temperature-dependent Pitzer treatment of aqueous Fe(II) chloride in *The Journal of Chemical Thermodynamics* **141**, 105977 (2020), DOI **10.1016/j.jct.2019.105977**. A subsequent compilation reproduces their temperature functions for the binary Fe²⁺–Cl⁻ interaction. This is distinct from the earlier FeCl₂ parameterizations of Moog, Hagemann and Rumyantsev (2004) and Christov (2004), which concern **298.15 K**. The compilation gives mixed-salt Fe²⁺ interaction parameters with Na⁺, K⁺, Mg²⁺ and Ca²⁺ only at 25 °C; a temperature-dependent *binary* model should therefore not be mistaken for a fully temperature-dependent mixed-brine model. (turner2023sourcesofpitzer pages 6-9, turner2023sourcesofpitzer pages 35-37, donchev2022developmentofaccurate pages 13-16)

For each parameter, the compiled expression is

\[p(T)=q_1+q_2(1/T-1/298.15)+q_3\ln(T/298.15)+q_4(T-298.15),\]

with *T* in kelvin. The reported coefficients, in the order \((q_1,q_2,q_3,q_4)\), are **β⁽⁰⁾:** (0.37324, 0.00716, 0.05840, −0.00203); **β⁽¹⁾:** (1.13499, 0.00015, −0.02341, 0.01709), with α = 2.0; and **Cφ:** (−0.0215243, 0.03714, −0.00580, 0.00016). These are coefficients as transcribed in the 2023 Turner–Clegg draft, not independently checked against the inaccessible 2020 article. In particular, the temperature interval over which the original authors validated the fit could not be verified here; the existence of a temperature equation alone is not a license to extrapolate it to arbitrary temperatures. (turner2023sourcesofpitzer pages 6-9, turner2023sourcesofpitzer pages 1-3, turner2023sourcesofpitzer pages 35-37)

## Experimental data above 25 °C

| Property | Identifiable FeCl₂ evidence and scope | Important qualification |
|---|---|---|
| **Heat capacity** | Bernarducci, Morss and Miksztal (1979), *Journal of Solution Chemistry* **8**, 717–727, DOI **10.1007/BF00648777**, directly measured a **4.426 mol kg⁻¹** stock solution. At **35.73 °C**, its reported heat capacity is **911.6 ± 14.0 J K⁻¹ per mole of FeCl₂** on the authors’ solution-normalization basis. Combining their calorimetry and dilution results gave an **infinite-dilution partial molar** heat capacity at **30 °C** of **−210 ± 23 J K⁻¹ mol⁻¹**. | The 30 °C value is **derived**, not the directly measured heat capacity at 35.73 °C. The stock also contained approximately **0.108 mol kg⁻¹ HCl**, which the authors accounted for in deriving the FeCl₂ quantity. (bernarducci1979partialmolalheat pages 4-7, bernarducci1979partialmolalheat pages 7-10) |
| **Enthalpy of dilution** | The same study diluted approximately **4.43 mol kg⁻¹** stock at **35 °C**. Its four corrected molar dilution enthalpies were **−22,584, −22,732, −22,730 and −23,043 J mol⁻¹**, at final FeCl₂ molalities **0.004651, 0.008393, 0.011366 and 0.013659 mol kg⁻¹**, respectively. Extrapolation to infinite dilution gave **−22,353 ± 109 J mol⁻¹**. | These are dilutions *from the concentrated stock*, not heats of dissolving crystalline FeCl₂. The paper also measured at 15 and 25 °C, providing the temperature comparison. (bernarducci1979partialmolalheat pages 7-10, bernarducci1979partialmolalheat pages 1-4) |
| **Water-vapor pressure over solution** | Susarev, Gorelik, Toikka, Lyzlova and Ponomarev’s **“Vapor Pressure of Water over Ferrous Chloride Solutions,”** *Zhurnal Prikladnoi Khimii* **49**, 1045 (1976), is explicitly identified as an experimental source used for FeCl₂–H₂O isothermal vapor-pressure-depression fits by Chen and colleagues (1982). Separately, Bernarducci *et al.* **manometrically measured** vapor pressure over their approximately **4.43 mol kg⁻¹** solution at **35 °C** for an evaporation correction. | The retrieved accounts do **not** supply Susarev’s individual temperatures, concentrations or pressures, or Bernarducci’s measured pressure numbers. Chen’s 1982 fitted parameters are **electrolyte-NRTL/local-composition parameters, not Pitzer β coefficients**. A plot’s entire temperature axis should not be presented as the measurement range. (chen1982localcompositionmodel pages 9-9, chen1982localcompositionmodel pages 6-7, bernarducci1979partialmolalheat pages 4-7) |
| **Solubility in water** | Compilations of the binary FeCl₂–H₂O phase diagram and Chen’s **1986 electrolyte-NRTL fit** distinguish FeCl₂·6H₂O, ·4H₂O and ·2H₂O. The fit lists approximate phase-specific temperature windows of **253–285 K**, **285–350 K** and **350–390 K**, respectively. A later OLI-model comparison reports FeCl₂-in-water literature solubilities extending to about **120 °C**. | The windows are those of a **regressed phase-equilibrium model**, not a newly measured set of transition temperatures. In particular, aqueous dihydrate persistence above **120 °C** is described under **greater-than-atmospheric pressure**; do not interpret it as an atmospheric-pressure boiling-solution measurement. Original numerical solubility tables were not recovered. (chen1986representationofsolidliquid pages 8-14, carlos2013chemicalmodelingof pages 124-142, coscia2006transformationofan pages 65-70) |
| **Solubility in other chloride solutions** | Chou and Phan (1985), *Journal of Chemical & Engineering Data* **30**, 216–218, investigated **NaCl–FeCl₂–H₂O at 25–70 °C and 1 atm**; Atbir and colleagues reported **NaCl–FeCl₂–H₂O** and **KCl–FeCl₂–H₂O at 0–70 °C** (2000). Published FeCl₂–MgCl₂–H₂O isotherms include **40 °C** (Shchedrina, Krasnova and Ozerova, 1969) and **70 °C** (Shchedrina and Mel’nichenko, 1974). FeCl₂-in-HCl solubility data were also compared with a model up to **100 °C**. | These are **mixed-electrolyte** measurements, not binary FeCl₂–water solubilities. A reported FeCl₂·MgCl₂·8H₂O phase can matter in the MgCl₂ system; the OLI model’s prediction of FeCl₂·2H₂O at 70 °C was specifically noted as **not observed** in the comparison data. (carlos2013chemicalmodelingof pages 76-80, carlos2013chemicalmodelingof pages 124-142, chen1986representationofsolidliquid pages 14-18) |

**Bottom line:** Published temperature-dependent **binary** FeCl₂ Pitzer coefficients do exist. Above 25 °C, the directly verifiable calorimetry is concentrated at approximately **35 °C**; aqueous vapor-pressure measurements have identifiable primary sources but their numerical data were not accessible in the retrieved texts. Solubility evidence spans substantially higher temperatures, provided the **solid hydrate, other dissolved salts and pressure** are specified. Neither the 2020 model’s validated temperature limit nor numerical vapor-pressure and solubility tables should be inferred from the secondary fits alone. (turner2023sourcesofpitzer pages 6-9, bernarducci1979partialmolalheat pages 7-10, bernarducci1979partialmolalheat pages 4-7, chen1982localcompositionmodel pages 6-7, carlos2013chemicalmodelingof pages 124-142)

References

1. (turner2023sourcesofpitzer pages 6-9): DR Turner and SL Clegg. Sources of pitzer parameters and equilibrium constants for the geotraces core elements included in the scor working group 145 chemical speciation …. Unknown journal, 2023.

2. (turner2023sourcesofpitzer pages 35-37): DR Turner and SL Clegg. Sources of pitzer parameters and equilibrium constants for the geotraces core elements included in the scor working group 145 chemical speciation …. Unknown journal, 2023.

3. (donchev2022developmentofaccurate pages 13-16): S Donchev, T Tsenov, and C Christov. Development of accurate chemical thermodynamic database for geochemical storage of nuclear waste. part ii: models for predicting solution properties and …. Unknown journal, 2022.

4. (turner2023sourcesofpitzer pages 1-3): DR Turner and SL Clegg. Sources of pitzer parameters and equilibrium constants for the geotraces core elements included in the scor working group 145 chemical speciation …. Unknown journal, 2023.

5. (bernarducci1979partialmolalheat pages 4-7): Ernest E. Bernarducci, Lester R. Morss, and Andrew R. Miksztal. Partial molal heat capacity of aqueous ferrous chloride from measurements of integral heats of dilution. Journal of Solution Chemistry, 8:717-727, Oct 1979. URL: https://doi.org/10.1007/bf00648777, doi:10.1007/bf00648777. This article has 9 citations and is from a peer-reviewed journal.

6. (bernarducci1979partialmolalheat pages 7-10): Ernest E. Bernarducci, Lester R. Morss, and Andrew R. Miksztal. Partial molal heat capacity of aqueous ferrous chloride from measurements of integral heats of dilution. Journal of Solution Chemistry, 8:717-727, Oct 1979. URL: https://doi.org/10.1007/bf00648777, doi:10.1007/bf00648777. This article has 9 citations and is from a peer-reviewed journal.

7. (bernarducci1979partialmolalheat pages 1-4): Ernest E. Bernarducci, Lester R. Morss, and Andrew R. Miksztal. Partial molal heat capacity of aqueous ferrous chloride from measurements of integral heats of dilution. Journal of Solution Chemistry, 8:717-727, Oct 1979. URL: https://doi.org/10.1007/bf00648777, doi:10.1007/bf00648777. This article has 9 citations and is from a peer-reviewed journal.

8. (chen1982localcompositionmodel pages 9-9): Chau‐Chyun Chen, H. I. Britt, J. F. Boston, and L. B. Evans. Local composition model for excess gibbs energy of electrolyte systems. part i: single solvent, single completely dissociated electrolyte systems. Aiche Journal, 28:588-596, Jul 1982. URL: https://doi.org/10.1002/aic.690280410, doi:10.1002/aic.690280410. This article has 1297 citations and is from a peer-reviewed journal.

9. (chen1982localcompositionmodel pages 6-7): Chau‐Chyun Chen, H. I. Britt, J. F. Boston, and L. B. Evans. Local composition model for excess gibbs energy of electrolyte systems. part i: single solvent, single completely dissociated electrolyte systems. Aiche Journal, 28:588-596, Jul 1982. URL: https://doi.org/10.1002/aic.690280410, doi:10.1002/aic.690280410. This article has 1297 citations and is from a peer-reviewed journal.

10. (chen1986representationofsolidliquid pages 8-14): Chau-Chyun Chen. Representation of solid-liquid equilibrium of aqueous electrolyte systems with the electrolyte nrtl model. Fluid Phase Equilibria, 27:457-474, Jan 1986. URL: https://doi.org/10.1016/0378-3812(86)87066-2, doi:10.1016/0378-3812(86)87066-2. This article has 60 citations and is from a peer-reviewed journal.

11. (carlos2013chemicalmodelingof pages 124-142): M Carlos. Chemical modeling of iron (ii)/(iii) solutions in hydrometallurgy using oli. Unknown journal, 2013.

12. (coscia2006transformationofan pages 65-70): C Coscia. Transformation of an aluminium-iron-magnesium-chloride solution during pyrohydrolysis. Unknown journal, 2006.

13. (carlos2013chemicalmodelingof pages 76-80): M Carlos. Chemical modeling of iron (ii)/(iii) solutions in hydrometallurgy using oli. Unknown journal, 2013.

14. (chen1986representationofsolidliquid pages 14-18): Chau-Chyun Chen. Representation of solid-liquid equilibrium of aqueous electrolyte systems with the electrolyte nrtl model. Fluid Phase Equilibria, 27:457-474, Jan 1986. URL: https://doi.org/10.1016/0378-3812(86)87066-2, doi:10.1016/0378-3812(86)87066-2. This article has 60 citations and is from a peer-reviewed journal.
