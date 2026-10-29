# P4a (point 4)

**Claim (paraphrased):** Millero and Byrne (1984) used ZnCl2 as a stand-in for PbCl2.

**Query** (Edison `job-futurehouse-paperqa3`, task `d250ef6b-4429-42fc-9ade-52deb4f0e4b9`, status `success`):

> What Pitzer parameters did Millero and Byrne (1984) use for Pb2+-Cl- interactions when modeling lead chloride complexation in seawater and NaCl solutions, and were these based on ZnCl2 or another analog salt?

---

Question: What Pitzer parameters did Millero and Byrne (1984) use for Pb2+-Cl- interactions when modeling lead chloride complexation in seawater and NaCl solutions, and were these based on ZnCl2 or another analog salt?

For the **Pb²⁺–Cl⁻ binary interaction**, the parameter set reported for the approach associated with Millero and Byrne (1984) is β⁽⁰⁾ = **0.26018**, β⁽¹⁾ = **1.64250**, and Cᵠ = **−0.08798**. Woosley’s later account explicitly identifies these as **ZnCl₂ parameters substituted for unavailable PbCl₂ parameters**, following Millero and Byrne—not parameters borrowed from CdCl₂. (woosley2012physicalchemicalproperties pages 68-73)

A distinction matters: those three values describe the *binary salt interaction*. According to Woosley, Millero and Byrne fitted a **single linear virial coefficient, B, for each lead–chloride complex**, rather than independently fitting β⁽⁰⁾, β⁽¹⁾, and Cᵠ for each complex. The numerical attribution above rests on that later account; the 1984 paper itself was not available for direct verification. (woosley2012physicalchemicalproperties pages 83-86, woosley2012physicalchemicalproperties pages 68-73)

References

1. (woosley2012physicalchemicalproperties pages 68-73): RJ Woosley. Physical chemical properties of trace and minor components of natural waters: solubility, speciation, and density. Unknown journal, 2012.

2. (woosley2012physicalchemicalproperties pages 83-86): RJ Woosley. Physical chemical properties of trace and minor components of natural waters: solubility, speciation, and density. Unknown journal, 2012.

### artifact-00

| Quantity | Millero–Byrne (1984) treatment |
|---|---|
| Pb²⁺–Cl⁻ binary β⁽⁰⁾ | 0.26018 |
| Pb²⁺–Cl⁻ binary β⁽¹⁾ | 1.64250 |
| Pb²⁺–Cl⁻ binary Cᵠ | −0.08798 |
| Source salt | **ZnCl₂—not CdCl₂** (pqac-00000027) |
| Important qualification | Millero and Byrne fitted a **single linear virial coefficient B** for each Pb–chloride complex; they did not separately fit β⁽⁰⁾, β⁽¹⁾, and Cᵠ for each complex. (pqac-00000030) |


*Table: Woosley (2012), Table 4.3, reports these as ZnCl₂-surrogate binary parameters for PbCl₂ and explicitly ties that substitution to Millero and Byrne (1984). The distinction between these free-ion binary parameters and the single virial B fitted for each lead–chloride complex prevents conflating two parameterizations. (pqac-00000027, pqac-00000030)*
