# P3d (point 3)

**Claim (paraphrased):** Freezing-point depression would work, and the platform could be adapted to measure it.

**Query** (Edison `job-futurehouse-paperqa3`, task `59d6190d-b206-4d24-be97-ca7e7fdffb2f`, status `success`):

> How are freezing-point depression measurements used to derive osmotic coefficients and Pitzer parameters for electrolyte solutions, and have automated, small-volume or multi-well freezing-point or osmometry methods reached the accuracy needed for this?

---

Question: How are freezing-point depression measurements used to derive osmotic coefficients and Pitzer parameters for electrolyte solutions, and have automated, small-volume or multi-well freezing-point or osmometry methods reached the accuracy needed for this?

## From freezing point to Pitzer parameters

**Freezing-point depression measures solvent activity, not an ion-specific parameter directly.** For a solution whose measured equilibrium freezing temperature is \(T_f<T_0\), equality of the chemical potentials of ice and liquid-solution water gives

\[
\ln a_w(T_f)=\frac{\mu_w^{\mathrm{ice},*}(T_f)-\mu_w^{\mathrm{liquid},*}(T_f)}{RT_f}.
\]

Using the enthalpy and heat-capacity differences between pure ice and liquid water converts the measured depression \(T_0-T_f\) into \(a_w\). The electrolyte’s molal osmotic coefficient then follows from \(\phi=-\ln a_w/(M_w\nu m)\), where \(m\) is salt molality, \(\nu\) is the number of ions per formula unit on complete dissociation, and \(M_w=0.01801528\) kg mol⁻¹. For a 1:1 salt, \(\nu=2\). In the dilute, small-depression limit this reduces to \(\Delta T_f\simeq K_f\nu m\phi\), with water’s \(K_f\simeq1.858\) K kg mol⁻¹. For concentrated solutions, use the ice–water equilibrium calculation rather than treating that linear approximation as exact. (pitzer1986theoreticalconsiderationsof pages 1-3, vilcu2010differentialcryoscopyin pages 1-4, beyer2002vapourpressuremeasurements pages 4-7, partanen2020traceablevaluesfor pages 2-3)

At each known composition, the resulting \(\phi(m,T_f)\) constrains a Pitzer model. For a 1:1 binary electrolyte, one published convention writes \(\phi-1=f^\phi+mB^\phi+m^2C^\phi\), where \(f^\phi=-A_\phi\sqrt I/(1+b\sqrt I)\), \(I=m\), \(b=1.2\) in the corresponding molality units, and \(B^\phi=\beta^{(0)}+\beta^{(1)}\exp(-\alpha\sqrt I)\) in the usual two-\(\beta\) version. Weighted fitting across *multiple molalities* estimates the salt-specific \(\beta^{(0)},\beta^{(1)},C^\phi\); some salts or broader ranges need an additional \(\beta^{(2)}\) term. Published prefactors depend on the convention used for \(C^\phi\). A freezing series samples different temperatures as concentration changes, so parameters intended for one reference temperature also require temperature-dependent fitting or independent thermal data; a fit at the freezing curve alone must not be presented unqualified as a 25 °C parameter set. Pitzer advises omitting the third-virial \(C\) term if data do not extend above ionic strength 2 mol kg⁻¹. Mixed-salt interaction parameters require mixture data, not merely separate binary freezing curves. (pitzer1986theoreticalconsiderationsof pages 3-5, pitzer1986theoreticalconsiderationsof pages 5-7, beyer2002vapourpressuremeasurements pages 7-10, beyer2002vapourpressuremeasurements pages 10-12)

This is an established route rather than a hypothetical conversion: a sodium-acetate Pitzer study converted literature freezing temperatures to osmotic coefficients and fitted them jointly with isopiestic, vapour-pressure, and calorimetric data. Its near-freezing cryoscopic series had osmotic-coefficient fit standard deviations of about **0.004** at 265–273 K, while the colder 255–259 K series had **0.075**. Thus the useful accuracy depends on the concentration and temperature range and on which parameters must be resolved; there is no single universal thermometer specification for every Pitzer fit. (beyer2002vapourpressuremeasurements pages 10-12)

## Have small-volume or multi-well methods met that standard?

The methods cannot be judged by throughput or repeatability alone: the required observable is the **equilibrium ice–solution temperature**, with sufficiently small *systematic* error in osmolality and weighed molality. As a scale illustration, in the dilute approximation a 0.01 K freezing-point error corresponds to roughly 5.4 mOsm kg⁻¹; at 0.1 mol kg⁻¹ of a 1:1 salt, that alone would shift \(\phi\) by approximately 0.027. This is a calculation from \(K_f\), not a measured specification for any instrument. (vilcu2010differentialcryoscopyin pages 1-4, beyer2002vapourpressuremeasurements pages 4-7)

| Method | Sample volume | What is measured | Documented performance | Directly demonstrated fit-grade Pitzer accuracy? |
|---|---:|---|---|---|
| Rigorous differential cryometry, LiCl/CsCl solutions | Not stated | Equilibrium freezing-point depression; water activities and electrolyte activity coefficients derived up to 3 mol·kg⁻¹ | Temperature accuracy ≈0.0001 °C (vilcu2010differentialcryoscopyin pages 1-4) | **Potentially suitable**, but the cited work did not perform a Pitzer fit |
| Historical sodium-acetate cryoscopy incorporated into a global Pitzer fit | Not stated | Freezing temperature converted to osmotic coefficient, then fitted with other thermodynamic data | Osmotic-coefficient fit SD: 0.004 at 265–273 K; 0.075 at 255–259 K (beyer2002vapourpressuremeasurements pages 10-12) | **Yes as contributing data**, but not as a stand-alone automated method |
| Automated benchtop freezing-point osmometer | Not stated | Sample is supercooled, crystallization is mechanically induced, and the equilibrium melting plateau is recorded | Quantitative accuracy or repeatability was not reported in the cited study; one comparator instrument gave unstable results for some viscous samples (meng2026osmoticpressurecorrelation pages 3-6) | **Not demonstrated** in the cited evidence |
| Miniaturized/high-throughput alternatives: dual-plate FrESH; portable MX3 proxy | FrESH: 50 μL/well in two 96-well plates; MX3: 10 μL versus 250 μL benchtop reference | FrESH detects stochastic nucleation onset, **not** equilibrium freezing depression. MX3 is a portable strip-based proxy, **not** a freezing-point instrument | FrESH: 0.110–0.114 °C bath-to-well fit RMSE and 0.43–0.44 °C combined 1σ uncertainty (fogwill2026temperatureuncertaintycharacterisation pages 4-7, fogwill2026temperatureuncertaintycharacterisation pages 1-4, fogwill2026temperatureuncertaintycharacterisation pages 7-10). MX3: +24% bias at low, +9% at mid-range, and −25% at high osmolality versus benchtop cryoscopy (winkler2026validationofthe pages 3-4) | **No**—neither system demonstrated thermodynamic-quality osmotic coefficients or Pitzer-parameter recovery |


*Table: Comparison of classical, automated, and miniaturized freezing or osmometry approaches against the precision needed for electrolyte thermodynamics. It separates equilibrium cryoscopy from nucleation assays and non-cryoscopic portable proxies.*

Classical differential cryometry *has* reported approximately **0.0001 °C** temperature accuracy and measurements to 3 mol kg⁻¹ for LiCl/CsCl systems. An automated benchtop freezing-point osmometer can, in principle, measure the correct observable: it supercools a sample, induces ice formation, then records the temperature as it returns to ice–liquid equilibrium. But the automated-instrument study examined here did **not** establish the concentration-dependent bias and uncertainty needed to recover electrolyte Pitzer parameters. (vilcu2010differentialcryoscopyin pages 1-4, meng2026osmoticpressurecorrelation pages 3-6)

Miniaturization has not by itself supplied that validation. A dual-96-well, 50-µL-per-well freezing assay detected **ice-nucleation events**, not equilibrium melting. Its inspected calibration table reports approximately **0.11 °C** bath-to-well fit RMSE; its fuller operational uncertainty is **0.43–0.44 °C** (1σ), with substantial well-position effects—far too coarse to substitute for high-precision equilibrium cryoscopy. Separately, a portable **10-µL** saliva-osmolality device agreed imperfectly with a **250-µL** benchtop freezing-point reference: despite good within-sample repeatability, its concentration-dependent bias ranged from about **+24%** at low osmolality to **−25%** at high osmolality. That portable device is **not itself a freezing-point osmometer**, so it illustrates why low volume and repeatability do not establish thermodynamic accuracy, rather than proving a limit for all micro-osmometers. A cited fish study’s “96-well” tests were chloride/calcium assays; its freezing-point measurement was performed separately, not in the wells. (fogwill2026temperatureuncertaintycharacterisation pages 4-7, fogwill2026temperatureuncertaintycharacterisation pages 1-4, fogwill2026temperatureuncertaintycharacterisation media 48d8e047, fogwill2026temperatureuncertaintycharacterisation pages 7-10, winkler2026validationofthe pages 3-4, vargaschacoff2026disruptionofosmotic pages 4-5)

**Conclusion:** Freezing-point data can yield defensible osmotic coefficients and Pitzer parameters when equilibrium temperatures, compositions, temperature dependence, and regression uncertainties are controlled. The evidence examined demonstrates that for rigorous cryoscopy and shows cryoscopic data contributing to Pitzer fits. It does **not** demonstrate that an automated *small-volume or multi-well* freezing-point platform has yet reproduced fit-grade electrolyte osmotic coefficients and Pitzer parameters across concentration. That is a limitation of the documented validation here, not a claim that such a platform is physically impossible. (vilcu2010differentialcryoscopyin pages 1-4, pitzer1986theoreticalconsiderationsof pages 5-7, beyer2002vapourpressuremeasurements pages 10-12, fogwill2026temperatureuncertaintycharacterisation pages 7-10)

References

1. (pitzer1986theoreticalconsiderationsof pages 1-3): K. S. Pitzer. Theoretical considerations of solubility with emphasis on mixed aqueous electrolytes. Pure and Applied Chemistry, 58:1599-1610, Jan 1986. URL: https://doi.org/10.1351/pac198658121599, doi:10.1351/pac198658121599. This article has 70 citations and is from a peer-reviewed journal.

2. (vilcu2010differentialcryoscopyin pages 1-4): Rodica Vilcu and Florica Irinei. Differential cryoscopy in ternary systems, system cl(li‐cs) + h2o and associated binaries. Bulletin des Sociétés Chimiques Belges, 81:479-488, Sep 2010. URL: https://doi.org/10.1002/bscb.19720810145, doi:10.1002/bscb.19720810145. This article has 0 citations.

3. (beyer2002vapourpressuremeasurements pages 4-7): Roland Beyer and Michael Steiger. Vapour pressure measurements and thermodynamic properties of aqueous solutions of sodium acetate. The Journal of Chemical Thermodynamics, 34:1057-1071, Jul 2002. URL: https://doi.org/10.1006/jcht.2002.0974, doi:10.1006/jcht.2002.0974. This article has 41 citations.

4. (partanen2020traceablevaluesfor pages 2-3): Lauri J. Partanen and Jaakko I. Partanen. Traceable values for activity and osmotic coefficients in aqueous sodium chloride solutions at temperatures from 273.15 to 373.15 k up to the saturated solutions. Journal of Chemical & Engineering Data, 65:5226-5239, Oct 2020. URL: https://doi.org/10.1021/acs.jced.0c00402, doi:10.1021/acs.jced.0c00402. This article has 20 citations and is from a peer-reviewed journal.

5. (pitzer1986theoreticalconsiderationsof pages 3-5): K. S. Pitzer. Theoretical considerations of solubility with emphasis on mixed aqueous electrolytes. Pure and Applied Chemistry, 58:1599-1610, Jan 1986. URL: https://doi.org/10.1351/pac198658121599, doi:10.1351/pac198658121599. This article has 70 citations and is from a peer-reviewed journal.

6. (pitzer1986theoreticalconsiderationsof pages 5-7): K. S. Pitzer. Theoretical considerations of solubility with emphasis on mixed aqueous electrolytes. Pure and Applied Chemistry, 58:1599-1610, Jan 1986. URL: https://doi.org/10.1351/pac198658121599, doi:10.1351/pac198658121599. This article has 70 citations and is from a peer-reviewed journal.

7. (beyer2002vapourpressuremeasurements pages 7-10): Roland Beyer and Michael Steiger. Vapour pressure measurements and thermodynamic properties of aqueous solutions of sodium acetate. The Journal of Chemical Thermodynamics, 34:1057-1071, Jul 2002. URL: https://doi.org/10.1006/jcht.2002.0974, doi:10.1006/jcht.2002.0974. This article has 41 citations.

8. (beyer2002vapourpressuremeasurements pages 10-12): Roland Beyer and Michael Steiger. Vapour pressure measurements and thermodynamic properties of aqueous solutions of sodium acetate. The Journal of Chemical Thermodynamics, 34:1057-1071, Jul 2002. URL: https://doi.org/10.1006/jcht.2002.0974, doi:10.1006/jcht.2002.0974. This article has 41 citations.

9. (meng2026osmoticpressurecorrelation pages 3-6): Ling-Zi Meng, Rene Iwato, Takaichi Watanabe, and Carlos G. Lopez. Osmotic pressure, correlation lengths and viscosity of aqueous pullulan solutions beyond the overlap concentration. Polymer Bulletin, Jul 2026. URL: https://doi.org/10.1007/s00289-026-06590-4, doi:10.1007/s00289-026-06590-4. This article has 0 citations and is from a peer-reviewed journal.

10. (fogwill2026temperatureuncertaintycharacterisation pages 4-7): Germán Perez Fogwill and André Welti. Temperature uncertainty characterisation of the fresh droplet-freezing assay. Unknown journal, Aug 2026. URL: https://doi.org/10.5194/egusphere-2026-3971, doi:10.5194/egusphere-2026-3971.

11. (fogwill2026temperatureuncertaintycharacterisation pages 1-4): Germán Perez Fogwill and André Welti. Temperature uncertainty characterisation of the fresh droplet-freezing assay. Unknown journal, Aug 2026. URL: https://doi.org/10.5194/egusphere-2026-3971, doi:10.5194/egusphere-2026-3971.

12. (fogwill2026temperatureuncertaintycharacterisation pages 7-10): Germán Perez Fogwill and André Welti. Temperature uncertainty characterisation of the fresh droplet-freezing assay. Unknown journal, Aug 2026. URL: https://doi.org/10.5194/egusphere-2026-3971, doi:10.5194/egusphere-2026-3971.

13. (winkler2026validationofthe pages 3-4): A. Maleah Winkler, Mitchell E. Zaplatosch, Caroline J. Smith, William M. Adams, Charlotte F. Willis, Skylar Bovine, M. Ryan McClure, Genesis Santos, Yana Chmunevich, Samantha J. Mitchell, Emilee O'Grady, and William Kinnaird. Validation of the portable mx3 hydration testing system for measuring saliva osmolality. Frontiers in Nutrition, Aug 2026. URL: https://doi.org/10.3389/fnut.2026.1882490, doi:10.3389/fnut.2026.1882490. This article has 1 citations.

14. (fogwill2026temperatureuncertaintycharacterisation media 48d8e047): Germán Perez Fogwill and André Welti. Temperature uncertainty characterisation of the fresh droplet-freezing assay. Unknown journal, Aug 2026. URL: https://doi.org/10.5194/egusphere-2026-3971, doi:10.5194/egusphere-2026-3971.

15. (vargaschacoff2026disruptionofosmotic pages 4-5): Luis Vargas-Chacoff, Ricardo Oyarzún-Salazar, Oscar de Lázaro, Pedro Cortés, Kurt Paschke, and José Muñoz. Disruption of osmotic balance and metabolic shifting in oncorhynchus kisutch under hypoxic stress: implications for salmon aquaculture climate resilience. Fishes, 11:420, Jul 2026. URL: https://doi.org/10.3390/fishes11070420, doi:10.3390/fishes11070420. This article has 0 citations.

### artifact-00

| Method | Sample volume | What is measured | Documented performance | Directly demonstrated fit-grade Pitzer accuracy? |
|---|---:|---|---|---|
| Rigorous differential cryometry, LiCl/CsCl solutions | Not stated | Equilibrium freezing-point depression; water activities and electrolyte activity coefficients derived up to 3 mol·kg⁻¹ | Temperature accuracy ≈0.0001 °C (pqac-00000010) | **Potentially suitable**, but the cited work did not perform a Pitzer fit |
| Historical sodium-acetate cryoscopy incorporated into a global Pitzer fit | Not stated | Freezing temperature converted to osmotic coefficient, then fitted with other thermodynamic data | Osmotic-coefficient fit SD: 0.004 at 265–273 K; 0.075 at 255–259 K (pqac-00000028) | **Yes as contributing data**, but not as a stand-alone automated method |
| Automated benchtop freezing-point osmometer | Not stated | Sample is supercooled, crystallization is mechanically induced, and the equilibrium melting plateau is recorded | Quantitative accuracy or repeatability was not reported in the cited study; one comparator instrument gave unstable results for some viscous samples (pqac-00000008) | **Not demonstrated** in the cited evidence |
| Miniaturized/high-throughput alternatives: dual-plate FrESH; portable MX3 proxy | FrESH: 50 μL/well in two 96-well plates; MX3: 10 μL versus 250 μL benchtop reference | FrESH detects stochastic nucleation onset, **not** equilibrium freezing depression. MX3 is a portable strip-based proxy, **not** a freezing-point instrument | FrESH: 0.110–0.114 °C bath-to-well fit RMSE and 0.43–0.44 °C combined 1σ uncertainty (pqac-00000011, pqac-00000012, pqac-00000029). MX3: +24% bias at low, +9% at mid-range, and −25% at high osmolality versus benchtop cryoscopy (pqac-00000030) | **No**—neither system demonstrated thermodynamic-quality osmotic coefficients or Pitzer-parameter recovery |


*Table: Comparison of classical, automated, and miniaturized freezing or osmometry approaches against the precision needed for electrolyte thermodynamics. It separates equilibrium cryoscopy from nucleation assays and non-cryoscopic portable proxies.*
