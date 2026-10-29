# P6b (point 6)

**Claim (paraphrased):** PbSO4 solubility is below 1 mmol/kg and does not rise much in other salts.

**Query** (Edison `job-futurehouse-paperqa3`, task `c8fe855a-a97f-453d-a0a3-6f79facfe93b`, status `success`):

> What is the solubility of PbSO4 (anglesite) in pure water at 25 C, and how much does it increase in NaCl and other salt solutions?

---

Question: What is the solubility of PbSO4 (anglesite) in pure water at 25 C, and how much does it increase in NaCl and other salt solutions?

## Anglesite solubility at 25 °C

In pure water at 25 °C, the critically evaluated **analytical solubility** of PbSO₄ (anglesite) is **(1.461 ± 0.035) × 10⁻⁴ mol/L**, equivalent to **44.3 ± 1.1 mg PbSO₄/L** or **30.3 ± 0.7 mg dissolved Pb/L**. This is the total amount dissolved, not the thermodynamic solubility product, which is defined using *free-ion activities* and need not equal the square of the measured molar solubility. (clever1980thesolubilityof pages 23-24, clever1980thesolubilityof pages 21-23)

The measured increase depends strongly on **which salt** is present. The following comparisons use total dissolved lead, expressed as a multiple of the pure-water value. (giordano1989anglesite(pbso4)solubility pages 2-3, clever1980thesolubilityof pages 23-24, clever1980thesolubilityof pages 21-23)

| Medium at ~25 °C | Salt/ligand concentration | Reported solubility | Equivalent dissolved PbSO₄ | Increase vs pure water¹ | Evidence/notes |
|---|---:|---:|---:|---:|---|
| Pure water | — | 1.461 × 10⁻⁴ mol L⁻¹ = 30.3 mg Pb L⁻¹ | 44.3 mg PbSO₄ L⁻¹ | 1.00× | Critically evaluated value at 25.0 °C; analytical solubility, not *K*sp (clever1980thesolubilityof pages 21-23) |
| NaClO₄ background electrolyte | Ionic strength *I* = 0.2 mol L⁻¹ | 3.02 × 10⁻⁴ mol L⁻¹ = 62.6 mg Pb L⁻¹ | 91.6 mg PbSO₄ L⁻¹ | 2.07× | Directly reported at 25.0 °C; NaClO₄ is not NaCl (clever1980thesolubilityof pages 23-24) |
| NaCH₃COO/CH₃COOH buffer | 0.005 *m* each | 47 mg Pb L⁻¹ | 68.8 mg PbSO₄ L⁻¹ | 1.55× | Equal molal concentrations; pH ≈ 4.6 (giordano1989anglesite(pbso4)solubility pages 2-3) |
| NaCH₃COO/CH₃COOH buffer | 0.010 *m* each | 57 mg Pb L⁻¹ | 83.4 mg PbSO₄ L⁻¹ | 1.88× | Equal molal concentrations; pH ≈ 4.6 (giordano1989anglesite(pbso4)solubility pages 2-3) |
| NaCH₃COO/CH₃COOH buffer | 0.025 *m* each | 106 mg Pb L⁻¹ | 155 mg PbSO₄ L⁻¹ | 3.50× | Equal molal concentrations; pH ≈ 4.7 (giordano1989anglesite(pbso4)solubility pages 2-3) |
| NaCH₃COO/CH₃COOH buffer | 0.100 *m* each | 270 mg Pb L⁻¹ | 395 mg PbSO₄ L⁻¹ | 8.91× | Equal molal concentrations; pH ≈ 4.7 (giordano1989anglesite(pbso4)solubility pages 2-3) |
| NaCH₃COO/CH₃COOH buffer | 0.250 *m* each | 584 mg Pb L⁻¹ | 855 mg PbSO₄ L⁻¹ | 19.3× | Measured at 25.9 °C; pH ≈ 4.8 (giordano1989anglesite(pbso4)solubility pages 2-3) |
| NaCl | — | No defensible measured 25 °C value recovered | — | Not quantified | Chloride complexation predicts an increase in total dissolved Pb, but the NaClO₄ and acetate factors cannot be assigned to NaCl |


*Table: Measured analytical solubilities near 25 °C, with ratios referenced to 30.3 mg dissolved Pb L⁻¹ in pure water. Here *m* means molality (mol kg⁻¹ water), while mol L⁻¹ means molarity; sulfate common-ion suppression is excluded.*

**NaCl specifically:** Chloride forms soluble lead–chloride complexes, so increasing chloride can increase total dissolved lead in equilibrium with anglesite; the amount also depends on ionic strength and sulfate activity. However, I could not verify a numerical **25 °C PbSO₄-in-NaCl solubility series** from the retrieved sources. It would be misleading to assign NaCl the **2.07-fold** increase measured in *sodium perchlorate*, or the larger increases measured in *acetate buffer*. The often-quoted maximum at 2–3 N NaCl applies to **SrSO₄**, not PbSO₄. (clever1980thesolubilityof pages 23-24, rollog2019intermobilityofbarium pages 2-3, nguyen2010galvanicleadcorrosion pages 48-52)

In contrast, adding sulfate supplies a **common ion** and can *decrease* dissolved lead rather than increase it. The acetate results are also specifically for equal molal amounts of sodium acetate and acetic acid at approximately pH 4.6—not for sodium acetate alone. (giordano1989anglesite(pbso4)solubility pages 2-3, nguyen2010galvanicleadcorrosion pages 44-48, giordano1989anglesite(pbso4)solubility media 97f55529)

References

1. (clever1980thesolubilityof pages 23-24): H. Lawrence Clever and Francis J. Johnston. The solubility of some sparingly soluble lead salts: an evaluation of the solubility in water and aqueous electrolyte solution. Journal of Physical and Chemical Reference Data, 9:751-784, Jul 1980. URL: https://doi.org/10.1063/1.555628, doi:10.1063/1.555628. This article has 194 citations and is from a peer-reviewed journal.

2. (clever1980thesolubilityof pages 21-23): H. Lawrence Clever and Francis J. Johnston. The solubility of some sparingly soluble lead salts: an evaluation of the solubility in water and aqueous electrolyte solution. Journal of Physical and Chemical Reference Data, 9:751-784, Jul 1980. URL: https://doi.org/10.1063/1.555628, doi:10.1063/1.555628. This article has 194 citations and is from a peer-reviewed journal.

3. (giordano1989anglesite(pbso4)solubility pages 2-3): Thomas H Giordano. Anglesite (pbso4) solubility in acetate solutions: the determination of stability constants for lead acetate complexes to 85°c. Geochimica et Cosmochimica Acta, 53:359-366, Feb 1989. URL: https://doi.org/10.1016/0016-7037(89)90387-6, doi:10.1016/0016-7037(89)90387-6. This article has 71 citations and is from a domain leading peer-reviewed journal.

4. (rollog2019intermobilityofbarium pages 2-3): Mark Rollog, Nigel J. Cook, Paul Guagliardo, Kathy Ehrig, Sarah E. Gilbert, and Matt Kilburn. Intermobility of barium, strontium, and lead in chloride and sulfate leach solutions. Geochemical Transactions, Sep 2019. URL: https://doi.org/10.1186/s12932-019-0064-0, doi:10.1186/s12932-019-0064-0. This article has 9 citations and is from a peer-reviewed journal.

5. (nguyen2010galvanicleadcorrosion pages 48-52): CK Nguyen. Galvanic lead corrosion in potable water: mechanisms, water quality impacts, and practical implications. Unknown journal, 2010.

6. (nguyen2010galvanicleadcorrosion pages 44-48): CK Nguyen. Galvanic lead corrosion in potable water: mechanisms, water quality impacts, and practical implications. Unknown journal, 2010.

7. (giordano1989anglesite(pbso4)solubility media 97f55529): Thomas H Giordano. Anglesite (pbso4) solubility in acetate solutions: the determination of stability constants for lead acetate complexes to 85°c. Geochimica et Cosmochimica Acta, 53:359-366, Feb 1989. URL: https://doi.org/10.1016/0016-7037(89)90387-6, doi:10.1016/0016-7037(89)90387-6. This article has 71 citations and is from a domain leading peer-reviewed journal.

### artifact-00

| Medium at ~25 °C | Salt/ligand concentration | Reported solubility | Equivalent dissolved PbSO₄ | Increase vs pure water¹ | Evidence/notes |
|---|---:|---:|---:|---:|---|
| Pure water | — | 1.461 × 10⁻⁴ mol L⁻¹ = 30.3 mg Pb L⁻¹ | 44.3 mg PbSO₄ L⁻¹ | 1.00× | Critically evaluated value at 25.0 °C; analytical solubility, not *K*sp (pqac-00000007) |
| NaClO₄ background electrolyte | Ionic strength *I* = 0.2 mol L⁻¹ | 3.02 × 10⁻⁴ mol L⁻¹ = 62.6 mg Pb L⁻¹ | 91.6 mg PbSO₄ L⁻¹ | 2.07× | Directly reported at 25.0 °C; NaClO₄ is not NaCl (pqac-00000005) |
| NaCH₃COO/CH₃COOH buffer | 0.005 *m* each | 47 mg Pb L⁻¹ | 68.8 mg PbSO₄ L⁻¹ | 1.55× | Equal molal concentrations; pH ≈ 4.6 (pqac-00000004) |
| NaCH₃COO/CH₃COOH buffer | 0.010 *m* each | 57 mg Pb L⁻¹ | 83.4 mg PbSO₄ L⁻¹ | 1.88× | Equal molal concentrations; pH ≈ 4.6 (pqac-00000004) |
| NaCH₃COO/CH₃COOH buffer | 0.025 *m* each | 106 mg Pb L⁻¹ | 155 mg PbSO₄ L⁻¹ | 3.50× | Equal molal concentrations; pH ≈ 4.7 (pqac-00000004) |
| NaCH₃COO/CH₃COOH buffer | 0.100 *m* each | 270 mg Pb L⁻¹ | 395 mg PbSO₄ L⁻¹ | 8.91× | Equal molal concentrations; pH ≈ 4.7 (pqac-00000004) |
| NaCH₃COO/CH₃COOH buffer | 0.250 *m* each | 584 mg Pb L⁻¹ | 855 mg PbSO₄ L⁻¹ | 19.3× | Measured at 25.9 °C; pH ≈ 4.8 (pqac-00000004) |
| NaCl | — | No defensible measured 25 °C value recovered | — | Not quantified | Chloride complexation predicts an increase in total dissolved Pb, but the NaClO₄ and acetate factors cannot be assigned to NaCl |


*Table: Measured analytical solubilities near 25 °C, with ratios referenced to 30.3 mg dissolved Pb L⁻¹ in pure water. Here *m* means molality (mol kg⁻¹ water), while mol L⁻¹ means molarity; sulfate common-ion suppression is excluded.*
