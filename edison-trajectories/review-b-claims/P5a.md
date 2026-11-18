# P5a (point 5)

**Claim (paraphrased):** Mixing parameters should come from two-salt common-ion systems.

**Query** (Edison `job-futurehouse-paperqa3`, task `88faeb5d-25b2-4f7c-8ccf-6ef1ff422307`, status `success`):

> From what kinds of experimental systems are Pitzer cation-cation mixing parameters (theta, psi) conventionally determined, such as two-salt common-ion mixtures like NaCl-KCl-H2O? Is it considered valid to derive theta for two cations when one or both are present only at trace concentrations?

---

Question: From what kinds of experimental systems are Pitzer cation-cation mixing parameters (theta, psi) conventionally determined, such as two-salt common-ion mixtures like NaCl-KCl-H2O? Is it considered valid to derive theta for two cations when one or both are present only at trace concentrations?

## Experimental basis

Pitzer’s cation–cation parameter **θ₍M,N₎** and cation–cation–anion parameter **ψ₍M,N,X₎** are conventionally estimated from thermodynamic measurements on *mixed electrolytes containing both salts*, especially a common-anion system MX + NX + H₂O. The pure-salt parameters are established first; mixture-specific parameters are then fitted to deviations in osmotic coefficient (or water activity), salt activity coefficients measured by suitable electrochemical cells, or other mixture-equilibrium data. Common-ion mixtures make the mixing parameters easier to constrain than more complex mixtures. Solubilities can provide additional constraints or tests; mixing enthalpies inform temperature dependence when Gibbs-energy reference data are available. (holmes1992mixingeffectsin pages 1-6, clegg1992thermodynamicsofmulticomponent pages 6-7, holmes1992mixingeffectsin pages 11-16)

**NaCl + KCl + H₂O is a documented example, not merely an analogy.** Pitzer and Kim report a fit to mixed-solution osmotic coefficients extending to ionic strength 4.8 mol kg⁻¹, with θ₍Na,K₎ = −0.012 and ψ₍Na,K,Cl₎ = −0.0018 in their formulation. These are parameters inferred from measurements on solutions containing *both* cations, rather than from either pure salt alone. (pitzer1993thermodynamicsofelectrolytes.a pages 17-21, pitzer1993thermodynamicsofelectrolytes. media 847ccda2, pitzer1993thermodynamicsofelectrolytes. media 484eb86f)

## What changes in the trace limit?

The distinction is **which property is measured and what remains abundant**. In the Pitzer osmotic-coefficient expression, the unlike-cation mixing contribution contains the product of the two cation molalities, *m*₍M₎*m*₍N₎; the ψ contribution also involves the counterion concentration. Thus, if one or both cations are trace, their contribution to a *bulk* osmotic-coefficient or water-activity measurement becomes very small. Fitting θ to such data alone is generally poorly constrained; if **both** cations are trace in another electrolyte, assigning a precise θ from bulk measurements is not justified without independent evidence. Pitzer and Kim explicitly caution that sufficiently dilute mixture data can fit well while the correct mixing parameter remains inaccurately determined. (pitzer1993thermodynamicsofelectrolytes.a pages 10-13, pitzer1993thermodynamicsofelectrolytes.a pages 17-21, pitzer1993thermodynamicsofelectrolytes.a pages 21-26)

There is **no categorical prohibition** on determining a mixing parameter when *one* cation is trace. If the other salt is present at substantial concentration and the *trace salt’s own activity coefficient* is measured selectively, its limiting activity can retain a finite mixing effect. For two 1:1 salts with a common anion, Holmes and Mesmer give the trace-sensitive relation Δln γ₍MX₎ = *m y*{θ₍M,N₎ + *m*(2 − *y*)ψ₍M,N,X₎/2}, where *m* is total salt molality and *y* is the fraction of NX. They explicitly note that mixing effects on activity coefficients can be largest for trace components, even though bulk osmotic effects are largest near equal salt fractions. Measurements over **different background concentrations**, with sufficiently well-established pure-salt behavior, are needed to distinguish θ from a possible ψ contribution; one trace measurement at one background concentration generally constrains a combination, not a unique θ. (holmes1992mixingeffectsin pages 1-6, holmes1992mixingeffectsin pages 11-16, pitzer1993thermodynamicsofelectrolytes. pages 36-41)

| Experimental system | Mixing signal | Can $\theta$ be determined? |
|---|---|---|
| NaCl + KCl + H₂O over broad salt ratios and total molalities | Isopiestic $\phi$ or solvent-activity data isolate mixing effects after fitting the pure salts. | **Yes.** $\theta_{\mathrm{Na,K}}$ and, when supported, $\psi_{\mathrm{Na,K,Cl}}$ are fitted jointly; the classic fit used data to $I=4.8\ \mathrm{mol\,kg^{-1}}$. (pitzer1993thermodynamicsofelectrolytes.a pages 17-21, pitzer1993thermodynamicsofelectrolytes. media 847ccda2, holmes1992mixingeffectsin pages 11-16) |
| One cation at trace level in a concentrated, fixed common-anion background | Its bulk-$\phi$ contribution tends to zero with trace molality, but its own limiting activity coefficient retains a finite $\theta$/$\psi$ contribution. | **Potentially.** Direct trace-salt activity measurements can be informative; varying background concentration is needed to separate $\theta$ from $\psi$. (holmes1992mixingeffectsin pages 11-16) |
| Both cations trace in an unrelated major electrolyte | The bulk unlike-cation term scales as $m_Mm_N$ and becomes negligible. | **Generally no from bulk observations alone.** The fit is practically unidentifiable unless selective activity measurements provide independent sensitivity. (pitzer1993thermodynamicsofelectrolytes.a pages 10-13) |


*Table: The ability to estimate Pitzer mixing parameters depends on the measured property, not merely on whether an ion is trace. Bulk solvent properties lose sensitivity in trace limits, while a selectively measured trace-component activity can remain informative.*

**Bottom line:** Deriving θ from ordinary bulk observations in which the relevant cations occur only at trace levels is generally not credible. Deriving it from carefully measured *trace-component activity in a substantial, varied background electrolyte* can be valid in principle, provided parameter identifiability and uncertainty are demonstrated. (holmes1992mixingeffectsin pages 11-16, pitzer1993thermodynamicsofelectrolytes.a pages 10-13, pitzer1993thermodynamicsofelectrolytes.a pages 17-21)

References

1. (holmes1992mixingeffectsin pages 1-6): H. F. Holmes and R. E. Mesmer. Mixing effects in aqueous solutions at elevated temperatures. Journal of Solution Chemistry, 21:713-724, Aug 1992. URL: https://doi.org/10.1007/bf00651505, doi:10.1007/bf00651505. This article has 3 citations and is from a peer-reviewed journal.

2. (clegg1992thermodynamicsofmulticomponent pages 6-7): Simon L. Clegg and Kenneth S. Pitzer. Thermodynamics of multicomponent, miscible, ionic solutions: generalized equations for symmetrical electrolytes. The Journal of Physical Chemistry, 96:3513-3520, Apr 1992. URL: https://doi.org/10.1021/j100187a061, doi:10.1021/j100187a061. This article has 393 citations.

3. (holmes1992mixingeffectsin pages 11-16): H. F. Holmes and R. E. Mesmer. Mixing effects in aqueous solutions at elevated temperatures. Journal of Solution Chemistry, 21:713-724, Aug 1992. URL: https://doi.org/10.1007/bf00651505, doi:10.1007/bf00651505. This article has 3 citations and is from a peer-reviewed journal.

4. (pitzer1993thermodynamicsofelectrolytes.a pages 17-21): Kenneth S. Pitzer and Janice J. Kim. Thermodynamics of electrolytes.: iv. activity and osmotic coefficients for mixed electrolytes. World Scientific Series in 20th Century Chemistry, pages 413-419, Dec 1993. URL: https://doi.org/10.1142/9789812795960\_0060, doi:10.1142/9789812795960\_0060. This article has 1576 citations.

5. (pitzer1993thermodynamicsofelectrolytes. media 847ccda2): Kenneth S. Pitzer and Janice J. Kim. Thermodynamics of electrolytes.: iv. activity and osmotic coefficients for mixed electrolytes. World Scientific Series in 20th Century Chemistry, pages 413-419, Dec 1993. URL: https://doi.org/10.1142/9789812795960\_0060, doi:10.1142/9789812795960\_0060. This article has 1576 citations.

6. (pitzer1993thermodynamicsofelectrolytes. media 484eb86f): Kenneth S. Pitzer and Janice J. Kim. Thermodynamics of electrolytes.: iv. activity and osmotic coefficients for mixed electrolytes. World Scientific Series in 20th Century Chemistry, pages 413-419, Dec 1993. URL: https://doi.org/10.1142/9789812795960\_0060, doi:10.1142/9789812795960\_0060. This article has 1576 citations.

7. (pitzer1993thermodynamicsofelectrolytes.a pages 10-13): Kenneth S. Pitzer and Janice J. Kim. Thermodynamics of electrolytes.: iv. activity and osmotic coefficients for mixed electrolytes. World Scientific Series in 20th Century Chemistry, pages 413-419, Dec 1993. URL: https://doi.org/10.1142/9789812795960\_0060, doi:10.1142/9789812795960\_0060. This article has 1576 citations.

8. (pitzer1993thermodynamicsofelectrolytes.a pages 21-26): Kenneth S. Pitzer and Janice J. Kim. Thermodynamics of electrolytes.: iv. activity and osmotic coefficients for mixed electrolytes. World Scientific Series in 20th Century Chemistry, pages 413-419, Dec 1993. URL: https://doi.org/10.1142/9789812795960\_0060, doi:10.1142/9789812795960\_0060. This article has 1576 citations.

9. (pitzer1993thermodynamicsofelectrolytes. pages 36-41): Kenneth S. Pitzer. Thermodynamics of electrolytes.: i. theoretical basis and general equations. World Scientific Series in 20th Century Chemistry, pages 386-395, Dec 1993. URL: https://doi.org/10.1142/9789812795960\_0057, doi:10.1142/9789812795960\_0057. This article has 5130 citations.

### artifact-00

| Experimental system | Mixing signal | Can $\theta$ be determined? |
|---|---|---|
| NaCl + KCl + H₂O over broad salt ratios and total molalities | Isopiestic $\phi$ or solvent-activity data isolate mixing effects after fitting the pure salts. | **Yes.** $\theta_{\mathrm{Na,K}}$ and, when supported, $\psi_{\mathrm{Na,K,Cl}}$ are fitted jointly; the classic fit used data to $I=4.8\ \mathrm{mol\,kg^{-1}}$. (pqac-00000023, pqac-00000027, pqac-00000019) |
| One cation at trace level in a concentrated, fixed common-anion background | Its bulk-$\phi$ contribution tends to zero with trace molality, but its own limiting activity coefficient retains a finite $\theta$/$\psi$ contribution. | **Potentially.** Direct trace-salt activity measurements can be informative; varying background concentration is needed to separate $\theta$ from $\psi$. (pqac-00000019) |
| Both cations trace in an unrelated major electrolyte | The bulk unlike-cation term scales as $m_Mm_N$ and becomes negligible. | **Generally no from bulk observations alone.** The fit is practically unidentifiable unless selective activity measurements provide independent sensitivity. (pqac-00000022) |


*Table: The ability to estimate Pitzer mixing parameters depends on the measured property, not merely on whether an ion is trace. Bulk solvent properties lose sensitivity in trace limits, while a selectively measured trace-component activity can remain informative.*
