# P8c (point 8)

**Claim (paraphrased):** A temperature-dependent PbCl2 model may not be possible from existing data.

**Query** (Edison `job-futurehouse-paperqa3`, task `48d8ddf6-f476-44e7-b761-1120270dc3dd`, status `success`):

> Are there temperature-dependent Pitzer models for PbCl2 or Pb(II)-chloride systems from 25 to 90 C or higher, and what PbCl2 solubility, heat capacity or enthalpy data support them?

---

Question: Are there temperature-dependent Pitzer models for PbCl2 or Pb(II)-chloride systems from 25 to 90 C or higher, and what PbCl2 solubility, heat capacity or enthalpy data support them?

## Assessment

**Yes, temperature-dependent Pb(II)–chloride Pitzer-based speciation models exist, but a model *validated for PbCl₂(s) solubility throughout 25–90 °C* is a stronger claim than the accessible evidence supports.** Luo and Millero (2007) fitted lead–chloride complexation and Pitzer interactions using measurements at **15.1, 25, 34.7 and 44.5 °C**, including NaCl/NaClO₄ solutions. Their complex-formation-constant expressions were extended to 15–300 °C using their measurements and literature data; that range is **not** a four-temperature Pitzer fit experimentally verified through 300 °C. Turner and Clegg (2023) found the separately fitted Pitzer parameters to vary incoherently with temperature and therefore retained **only the 25 °C interaction parameters**, while fitting the measured formation constants as functions of 1/T. (turner2023sourcesofpitzer pages 9-13, woosley2012physicalchemicalproperties pages 73-79, woosley2012physicalchemicalproperties pages 79-83)

A practical high-temperature implementation is **Geodat/PHREEQC**: Regenspurg and colleagues describe Pb–chloride speciation with Pitzer activity coefficients for ionic strengths **0–6 M** and temperatures **up to 300 °C**, based on Luo–Millero stability constants. They tested related *laurionite* (PbOHCl) precipitation at **25, 80 and 133 °C**. Those tests are not measurements of PbCl₂(s) solubility or independent validation of every high-temperature Pb–Cl interaction coefficient. By contrast, Moog’s **THEREDA** Pitzer database recalculates PbCl₂ solubility in NaCl, KCl, MgCl₂ and CaCl₂ media but explicitly limits its released dataset to **298.15 K**. An earlier, directly pertinent publication is Mgaidi, Fürst and Renon (1991), *“Representation of the solubility of lead chloride in various chloride solutions with Pitzer’s model”* (*Metallurgical Transactions B* **22**, 491–498; DOI: 10.1007/BF02654287). Its full text was unavailable here, so its fitted temperatures, thermal coefficients and calorimetric inputs cannot be verified. (regenspurg2016formationandsignificance pages 5-7, regenspurg2016formationandsignificance pages 1-5, moog2022thermodynamicdatabasefor pages 1-2, moog2022thermodynamicdatabasefor pages 17-20, moog2022thermodynamicdatabasefor pages 23-25)

## Solubility evidence for evaluating a 25–90 °C model

Clever and Johnston’s evaluated **total, stoichiometric PbCl₂ solubilities in pure water** provide temperature anchors; only the 25 °C value is designated *recommended*, whereas their other tabulated temperatures are *tentative*. These are observations/evaluations, **not Pitzer-model predictions**. (clever1980thesolubilityof pages 11-13, clever1980thesolubilityof media 51f07d4e)

| Temperature (°C) | Total PbCl₂ solubility (mol kg⁻¹ H₂O) | Status |
|---:|---:|---|
| 25 | 0.03907 ± 0.00004 | Recommended stoichiometric solubility |
| 50 | 0.0601 ± 0.0024 | Tentative stoichiometric solubility |
| 75 | 0.0890 ± 0.0030 | Tentative stoichiometric solubility |
| 90 | 0.1107 | Tentative stoichiometric solubility |
| 100 | 0.1272 ± 0.0036 | Tentative stoichiometric solubility |
| 150 | 0.239 ± 0.005 | Tentative stoichiometric solubility |


*Table: Evaluated total stoichiometric PbCl₂ solubilities in pure water; these are neither Ksp values nor Pitzer-model predictions. The distinct Nriagu–Anderson observation in 3 mol kg⁻¹ NaCl at 90 °C (0.1449 mol kg⁻¹) is excluded from the table to avoid mixing pure-water and electrolyte-media results.*

Their pure-water temperature correlation is

\[\ln\!\left[m/(\mathrm{mol\,kg^{-1}})\right]=-6.40476-\frac{5.43593}{T/(100\,\mathrm K)}+3.64509\ln\!\left(\frac{T}{100\,\mathrm K}\right).\]

It spans **273.15–623 K** as an evaluated, partly extrapolated solubility correlation—not an activity-coefficient or Pitzer-parameter equation. The authors caution about possible hydrolysis at high temperature and identify one high-temperature series as approximately 20–25% low. Their tabulated **3 mol kg⁻¹ NaCl** measurements, attributed to Nriagu and Anderson, give **0.0185 mol kg⁻¹ at 28 °C, 0.0330 at 40 °C, 0.0619 at 60 °C and 0.1449 at 90 °C**: useful *chloride-brine* checks that must not be substituted for the pure-water values. (clever1980thesolubilityof pages 13-14, clever1980thesolubilityof pages 11-13)

## Enthalpy, heat capacity and limits

For crystalline PbCl₂ at 25 °C, Moog reports **ΔfH° = −359.410 kJ mol⁻¹** and **S° = 136 J mol⁻¹ K⁻¹**, and selects **log₁₀K° = 4.77** for the *precipitation* reaction Pb²⁺ + 2Cl⁻ → PbCl₂(cr), derived from solubility and checked against chloride-complex/Pitzer data. The quoted ΔfH° is the **standard enthalpy of formation of the crystal**, *not* its heat of dissolution; a dissolution reaction enthalpy additionally requires the aqueous-ion formation enthalpies. The accessible sources do **not** establish a measured PbCl₂ dissolution-enthalpy series, solid or aqueous heat-capacity dataset, or ΔCₚ-derived temperature functions for Pb-specific Pitzer interactions. Solubility-versus-temperature data constrain the combined equilibrium and speciation behavior but do not alone identify each interaction parameter’s temperature derivative. (moog2022thermodynamicdatabasefor pages 8-9, turner2023sourcesofpitzer pages 9-13)

**Bottom line:** for 25–90 °C calculations, a Pb–Cl Pitzer/geochemical implementation can be used, and both pure-water and 90 °C chloride-brine solubilities offer checks. Its high-temperature output should be described as **model-dependent** unless its particular PbCl₂(s) equilibrium, aqueous complexation and temperature-dependent interaction parameters have been checked against those data. The identified 1991 PbCl₂-solubility Pitzer paper is an important next primary source for establishing whether a specific formulation meets that standard. (clever1980thesolubilityof pages 13-14, turner2023sourcesofpitzer pages 9-13, regenspurg2016formationandsignificance pages 5-7, moog2022thermodynamicdatabasefor pages 23-25)

References

1. (turner2023sourcesofpitzer pages 9-13): DR Turner and SL Clegg. Sources of pitzer parameters and equilibrium constants for the geotraces core elements included in the scor working group 145 chemical speciation …. Unknown journal, 2023.

2. (woosley2012physicalchemicalproperties pages 73-79): RJ Woosley. Physical chemical properties of trace and minor components of natural waters: solubility, speciation, and density. Unknown journal, 2012.

3. (woosley2012physicalchemicalproperties pages 79-83): RJ Woosley. Physical chemical properties of trace and minor components of natural waters: solubility, speciation, and density. Unknown journal, 2012.

4. (regenspurg2016formationandsignificance pages 5-7): Simona Regenspurg, Dejene Legesse Driba, and Carolin Zorn. Formation and significance of laurionite in geothermal brine. Environmental Earth Sciences, 75:1-10, May 2016. URL: https://doi.org/10.1007/s12665-016-5668-4, doi:10.1007/s12665-016-5668-4. This article has 12 citations and is from a peer-reviewed journal.

5. (regenspurg2016formationandsignificance pages 1-5): Simona Regenspurg, Dejene Legesse Driba, and Carolin Zorn. Formation and significance of laurionite in geothermal brine. Environmental Earth Sciences, 75:1-10, May 2016. URL: https://doi.org/10.1007/s12665-016-5668-4, doi:10.1007/s12665-016-5668-4. This article has 12 citations and is from a peer-reviewed journal.

6. (moog2022thermodynamicdatabasefor pages 1-2): H Moog. Thermodynamic database for pb and its compounds-data selection. Unknown journal, 2022.

7. (moog2022thermodynamicdatabasefor pages 17-20): H Moog. Thermodynamic database for pb and its compounds-data selection. Unknown journal, 2022.

8. (moog2022thermodynamicdatabasefor pages 23-25): H Moog. Thermodynamic database for pb and its compounds-data selection. Unknown journal, 2022.

9. (clever1980thesolubilityof pages 11-13): H. Lawrence Clever and Francis J. Johnston. The solubility of some sparingly soluble lead salts: an evaluation of the solubility in water and aqueous electrolyte solution. Journal of Physical and Chemical Reference Data, 9:751-784, Jul 1980. URL: https://doi.org/10.1063/1.555628, doi:10.1063/1.555628. This article has 194 citations and is from a peer-reviewed journal.

10. (clever1980thesolubilityof media 51f07d4e): H. Lawrence Clever and Francis J. Johnston. The solubility of some sparingly soluble lead salts: an evaluation of the solubility in water and aqueous electrolyte solution. Journal of Physical and Chemical Reference Data, 9:751-784, Jul 1980. URL: https://doi.org/10.1063/1.555628, doi:10.1063/1.555628. This article has 194 citations and is from a peer-reviewed journal.

11. (clever1980thesolubilityof pages 13-14): H. Lawrence Clever and Francis J. Johnston. The solubility of some sparingly soluble lead salts: an evaluation of the solubility in water and aqueous electrolyte solution. Journal of Physical and Chemical Reference Data, 9:751-784, Jul 1980. URL: https://doi.org/10.1063/1.555628, doi:10.1063/1.555628. This article has 194 citations and is from a peer-reviewed journal.

12. (moog2022thermodynamicdatabasefor pages 8-9): H Moog. Thermodynamic database for pb and its compounds-data selection. Unknown journal, 2022.

### artifact-00

| Temperature (°C) | Total PbCl₂ solubility (mol kg⁻¹ H₂O) | Status |
|---:|---:|---|
| 25 | 0.03907 ± 0.00004 | Recommended stoichiometric solubility |
| 50 | 0.0601 ± 0.0024 | Tentative stoichiometric solubility |
| 75 | 0.0890 ± 0.0030 | Tentative stoichiometric solubility |
| 90 | 0.1107 | Tentative stoichiometric solubility |
| 100 | 0.1272 ± 0.0036 | Tentative stoichiometric solubility |
| 150 | 0.239 ± 0.005 | Tentative stoichiometric solubility |


*Table: Evaluated total stoichiometric PbCl₂ solubilities in pure water; these are neither Ksp values nor Pitzer-model predictions. The distinct Nriagu–Anderson observation in 3 mol kg⁻¹ NaCl at 90 °C (0.1449 mol kg⁻¹) is excluded from the table to avoid mixing pure-water and electrolyte-media results.*
