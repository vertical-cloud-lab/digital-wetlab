# P6f (point 6)

**Claim (paraphrased):** Na-Fe mixing terms should come from independent data where the ions are concentrated (Moog et al. 2004; Chou and Phan 1985).

**Query** (Edison `job-futurehouse-paperqa3`, task `08256d50-0335-4513-a989-f60b43c45a86`, status `success`):

> What Pitzer mixing parameters have been published for Na+-Fe2+ (theta(Na,Fe), psi(Na,Fe,Cl)) and from what data, for example NaCl-FeCl2-H2O solubility (Chou and Phan 1985) or isopiestic data for FeCl2 mixtures (Moog et al. 2004)?

---

Question: What Pitzer mixing parameters have been published for Na+-Fe2+ (theta(Na,Fe), psi(Na,Fe,Cl)) and from what data, for example NaCl-FeCl2-H2O solubility (Chou and Phan 1985) or isopiestic data for FeCl2 mixtures (Moog et al. 2004)?

## Published Na⁺–Fe²⁺–Cl⁻ mixing parameters

At **298.15 K**, the published isopiestic-based values are **θ(Na⁺,Fe²⁺) = 0.10945** and **ψ(Na⁺,Fe²⁺,Cl⁻) = −0.01605**. Kim et al. (2017) attribute both to Moog, Hagemann and Rumyantsev (2004); Turner and Clegg’s later parameter compilation reproduces the same values. (kim2017solubilitymodelfor pages 10-13, turner2023sourcesofpitzer pages 6-9, turner2023sourcesofpitzer pages 30-35)

| Source | Experimental basis and conditions | $\theta(\mathrm{Na^+,Fe^{2+}})$ | $\psi(\mathrm{Na^+,Fe^{2+},Cl^-})$ | Interpretation |
|---|---|---:|---:|---|
| **Chou & Phan (1985)** | Experimental solid–liquid equilibria in NaCl–FeCl₂–H₂O at 1 atm; halite and FeCl₂·4H₂O solubilities, with isotherms at 25, 50, and 70 °C | — | — | **No Pitzer mixing parameters were fitted or published**; this is a phase-solubility dataset, not the source of the later 0.08/0 parameter pair. (chou1985solubilityrelationsin pages 1-2, chou1985solubilityrelationsin pages 2-3) |
| **Nemer et al. (2011)** | Fe(OH)₂ and Fe₂Cl(OH)₃ solubility in NaCl brines; used the Pitzer (1991) Fe²⁺–Cl⁻ binary parameters, which were stated to apply only to ionic strength $I\leq2$ molal | 0.08 | 0.0 | $\theta$ was fitted jointly with mineral dissolution constants; $\psi=0$ was imposed/assumed rather than independently estimated. Kim et al. later replaced both entries. (kim2017solubilitymodelfor pages 24-26, kim2017solubilitymodelfor pages 40-48, kim2017solubilitymodelfor pages 31-35) |
| **Moog, Hagemann & Rumyantsev (2004)** | Isopiestic measurements for FeCl₂–(Na,K,Mg,Ca)Clₙ–H₂O at 298.15 K; simultaneous, internally consistent Fe²⁺–Cl⁻ binary and mixed-electrolyte parameterization | 0.10945 | −0.01605 | Published 25 °C mixing set; reported by Kim et al. as valid to $I\approx6$ molal and adopted in place of 0.08/0. Turner and Clegg independently reproduce the same values. (kim2017solubilitymodelfor pages 24-26, kim2017solubilitymodelfor pages 40-48, turner2023sourcesofpitzer pages 6-9, turner2023sourcesofpitzer pages 30-35) |


*Table: Comparison of the experimental provenance and reported Pitzer mixing parameters for Na⁺–Fe²⁺–Cl⁻. It distinguishes the Chou–Phan solubility dataset from the Nemer and Moog parameterizations.*

The provenance matters. **Chou and Phan (1985) published solubility data, not these Pitzer parameters.** Their visual-polythermal study mapped halite and FeCl₂·4H₂O saturation in NaCl–FeCl₂–H₂O at 1 atm; they calculated isothermal solubilities at 25, 50 and 70 °C. No θ(Na,Fe) or ψ(Na,Fe,Cl) fit appears in the paper. (chou1985solubilityrelationsin pages 1-2, chou1985solubilityrelationsin pages 2-3)

The earlier **θ = 0.08, ψ = 0.0** entries in Kim et al.’s comparison table instead cite **Nemer et al. (2011)**, whose measurements concerned *Fe(OH)₂ and Fe₂Cl(OH)₃ solubility in NaCl brines*—not saturation of NaCl and FeCl₂·4H₂O as in Chou and Phan. Kim et al. say Nemer derived θ alongside the two mineral-dissolution constants; the tabulated zero ψ is an earlier model setting, **not evidence of an independently measured zero interaction**. (kim2017solubilitymodelfor pages 31-35, kim2017solubilitymodelfor pages 24-26, kim2017solubilitymodelfor pages 40-48)

**Moog et al. (2004)** used isopiestic measurements on FeCl₂–(Na,K,Mg,Ca)Clₙ–H₂O at 298.15 K to obtain Fe²⁺–Cl⁻ binary parameters and the mixed-cation θ and ψ terms. Kim et al. report that this parameterization applies up to ionic strength 6 molal, versus 2 molal for the earlier Fe²⁺–Cl⁻ binary set used by Nemer; they replaced the earlier mixing entries with Moog’s values and re-derived their mineral-dissolution constants for consistency. The original Moog article was not available in full for this review, so its detailed fitting procedure and data coverage beyond these reported descriptions were not independently verified. (kim2017solubilitymodelfor pages 31-35, kim2017solubilitymodelfor pages 24-26, kim2017solubilitymodelfor pages 40-48, turner2023sourcesofpitzer pages 6-9)

References

1. (kim2017solubilitymodelfor pages 10-13): Sungtae Kim, Cassandra Marrs, Martin Nemer, and Jay Je-Hun Jang. Solubility model for ferrous iron hydroxide, hibbingite, siderite, and chukanovite in high saline solutions of sodium chloride, sodium sulfate, and sodium carbonate. ArXiv, 1:647-663, Nov 2017. URL: https://doi.org/10.1021/acsearthspacechem.7b00065, doi:10.1021/acsearthspacechem.7b00065. This article has 17 citations.

2. (turner2023sourcesofpitzer pages 6-9): DR Turner and SL Clegg. Sources of pitzer parameters and equilibrium constants for the geotraces core elements included in the scor working group 145 chemical speciation …. Unknown journal, 2023.

3. (turner2023sourcesofpitzer pages 30-35): DR Turner and SL Clegg. Sources of pitzer parameters and equilibrium constants for the geotraces core elements included in the scor working group 145 chemical speciation …. Unknown journal, 2023.

4. (chou1985solubilityrelationsin pages 1-2): I Ming Chou and Luong D. Phan. Solubility relations in the system sodium chloride-ferrous chloride-water between 25 and 70.degree.c at 1 atm. Journal of Chemical & Engineering Data, 30:154-156, Apr 1985. URL: https://doi.org/10.1021/je00040a027, doi:10.1021/je00040a027. This article has 17 citations and is from a peer-reviewed journal.

5. (chou1985solubilityrelationsin pages 2-3): I Ming Chou and Luong D. Phan. Solubility relations in the system sodium chloride-ferrous chloride-water between 25 and 70.degree.c at 1 atm. Journal of Chemical & Engineering Data, 30:154-156, Apr 1985. URL: https://doi.org/10.1021/je00040a027, doi:10.1021/je00040a027. This article has 17 citations and is from a peer-reviewed journal.

6. (kim2017solubilitymodelfor pages 24-26): Sungtae Kim, Cassandra Marrs, Martin Nemer, and Jay Je-Hun Jang. Solubility model for ferrous iron hydroxide, hibbingite, siderite, and chukanovite in high saline solutions of sodium chloride, sodium sulfate, and sodium carbonate. ArXiv, 1:647-663, Nov 2017. URL: https://doi.org/10.1021/acsearthspacechem.7b00065, doi:10.1021/acsearthspacechem.7b00065. This article has 17 citations.

7. (kim2017solubilitymodelfor pages 40-48): Sungtae Kim, Cassandra Marrs, Martin Nemer, and Jay Je-Hun Jang. Solubility model for ferrous iron hydroxide, hibbingite, siderite, and chukanovite in high saline solutions of sodium chloride, sodium sulfate, and sodium carbonate. ArXiv, 1:647-663, Nov 2017. URL: https://doi.org/10.1021/acsearthspacechem.7b00065, doi:10.1021/acsearthspacechem.7b00065. This article has 17 citations.

8. (kim2017solubilitymodelfor pages 31-35): Sungtae Kim, Cassandra Marrs, Martin Nemer, and Jay Je-Hun Jang. Solubility model for ferrous iron hydroxide, hibbingite, siderite, and chukanovite in high saline solutions of sodium chloride, sodium sulfate, and sodium carbonate. ArXiv, 1:647-663, Nov 2017. URL: https://doi.org/10.1021/acsearthspacechem.7b00065, doi:10.1021/acsearthspacechem.7b00065. This article has 17 citations.

### artifact-00

| Source | Experimental basis and conditions | $\theta(\mathrm{Na^+,Fe^{2+}})$ | $\psi(\mathrm{Na^+,Fe^{2+},Cl^-})$ | Interpretation |
|---|---|---:|---:|---|
| **Chou & Phan (1985)** | Experimental solid–liquid equilibria in NaCl–FeCl₂–H₂O at 1 atm; halite and FeCl₂·4H₂O solubilities, with isotherms at 25, 50, and 70 °C | — | — | **No Pitzer mixing parameters were fitted or published**; this is a phase-solubility dataset, not the source of the later 0.08/0 parameter pair. (pqac-00000029, pqac-00000028) |
| **Nemer et al. (2011)** | Fe(OH)₂ and Fe₂Cl(OH)₃ solubility in NaCl brines; used the Pitzer (1991) Fe²⁺–Cl⁻ binary parameters, which were stated to apply only to ionic strength $I\leq2$ molal | 0.08 | 0.0 | $\theta$ was fitted jointly with mineral dissolution constants; $\psi=0$ was imposed/assumed rather than independently estimated. Kim et al. later replaced both entries. (pqac-00000008, pqac-00000009, pqac-00000016) |
| **Moog, Hagemann & Rumyantsev (2004)** | Isopiestic measurements for FeCl₂–(Na,K,Mg,Ca)Clₙ–H₂O at 298.15 K; simultaneous, internally consistent Fe²⁺–Cl⁻ binary and mixed-electrolyte parameterization | 0.10945 | −0.01605 | Published 25 °C mixing set; reported by Kim et al. as valid to $I\approx6$ molal and adopted in place of 0.08/0. Turner and Clegg independently reproduce the same values. (pqac-00000008, pqac-00000009, pqac-00000021, pqac-00000027) |


*Table: Comparison of the experimental provenance and reported Pitzer mixing parameters for Na⁺–Fe²⁺–Cl⁻. It distinguishes the Chou–Phan solubility dataset from the Nemer and Moog parameterizations.*
