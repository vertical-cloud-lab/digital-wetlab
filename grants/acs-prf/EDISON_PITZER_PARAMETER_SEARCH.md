# Edison Scientific Literature Search — Pitzer Parameter Database State

> Generated via [Edison Scientific](https://edisonscientific.com/platform) `LITERATURE` search on 2026-02-28.
> Query: *"What Pitzer activity-coefficient interaction parameters (binary β⁰, β¹, Cᶲ and higher-order mixing θ, ψ) have been published for Fe²⁺-HS⁻, Fe²⁺-S²⁻, Pb²⁺-HS⁻, and Pb²⁺-S²⁻ ion pairs in aqueous electrolyte solutions?"*

> **Note (2026-10-29):** the 2026 review argues that Fe²⁺–HS⁻ and Pb²⁺–HS⁻ terms are missing
> because they cannot be measured, not because no one tried. The Pb²⁺–Cl⁻ row below matches the
> ZnCl₂ values that Millero and Byrne (1984) used in place of PbCl₂, except that Woosley (2012)
> gives Cφ as −0.08798. See [`REVIEW_2026_LITERATURE_CHECK.md`](REVIEW_2026_LITERATURE_CHECK.md).

---

## Key Finding

**The Pitzer parameter database is effectively incomplete for Fe(II)/Pb(II)–sulfide (HS⁻/S²⁻) ion-interaction and mixing parameters** (β⁰/β¹/Cᶲ; θ/ψ) in aqueous electrolyte solutions, including in brines with Na⁺, Ca²⁺, and Cl⁻.

### What IS available

| System | Parameters | Source |
|--------|-----------|--------|
| NaHS | β⁰ = −0.103, β¹ = 0.884 | Millero 1986 |
| KHS | β⁰ = −0.337, β¹ = 0.884 | Millero 1986 |
| Mg(HS)₂ | β⁰ = 0.466, β¹ = 2.264 | Millero 1986 |
| Ca(HS)₂ | β⁰ = 0.069, β¹ = 2.264 | Millero 1986 |
| Pb²⁺–Cl⁻ | b⁰ = 0.26, b¹ = 1.64, Cᶲ = 0.088 | Felmy et al. 2000 |
| Na⁺–PbCl₃⁻ | b⁰ = 0.092, b¹ = −0.65 | Felmy et al. 2000 |
| Ca²⁺–PbCl₃⁻ | b⁰ = 0.016, b¹ = 1.26 | Felmy et al. 2000 |
| Mg²⁺–PbCl₃⁻ | b⁰ = 0.21, b¹ = 1.08 | Felmy et al. 2000 |

### What is MISSING (the gap this proposal fills)

| System | Status |
|--------|--------|
| Fe²⁺–HS⁻ | **No published Pitzer β/Cᶲ found** |
| Fe²⁺–S²⁻ | **No published Pitzer β/Cᶲ found** |
| Pb²⁺–HS⁻ | **No published Pitzer β/Cᶲ found** |
| Pb²⁺–S²⁻ | **No published Pitzer β/Cᶲ found** |
| Any θ/ψ mixing terms for Fe/Pb sulfide with Na⁺/Ca²⁺/Cl⁻ | **Not found** |

### Turner & Clegg (2023/2024) check

Turner et al. (2024) focuses on Fe(III) hydrolysis modeling (MarChemSpec), not Fe(II)/Pb(II) sulfide chemistry. No Fe(II)–sulfide or Pb(II)–sulfide mixing parameters are provided. **There is no indication that Turner/Clegg has filled the Fe/Pb–sulfide Pitzer parameter gap.**

### Important nuance

- HS⁻ interactions with major cations (Na⁺, K⁺, Mg²⁺, Ca²⁺) ARE parameterized (Millero 1986, Hershey et al. 1988) — these support H₂S speciation modeling
- Pb(II) in chloride brines IS parameterized (Felmy et al. 2000) — but NOT with sulfide
- The gap is specifically in **metal–sulfide cross-interactions** and **higher-order mixing** involving Fe²⁺/Pb²⁺ with HS⁻ in the presence of major brine ions

---

## References

1. Millero, F.J. (1986). The thermodynamics and kinetics of the hydrogen sulfide system in natural waters. *Marine Chemistry*, 18, 121–147. doi:10.1016/0304-4203(86)90003-4 (372 citations)
2. Hershey, J.P.; Plese, T.; Millero, F.J. (1988). The pK₁* for the dissociation of H₂S in various ionic media. *Geochimica et Cosmochimica Acta*, 52, 2047–2051. doi:10.1016/0016-7037(88)90183-4 (76 citations)
3. Felmy, A.R.; Onishi, L.M.; Foster, N.S.; et al. (2000). An aqueous thermodynamic model for the Pb²⁺–Na⁺–K⁺–Ca²⁺–Mg²⁺–H⁺–Cl⁻–SO₄²⁻–H₂O system to high concentration. *Geochimica et Cosmochimica Acta*, 64, 3615–3628. doi:10.1016/s0016-7037(00)00454-3 (25 citations)
4. Turner, D.R.; Gledhill, M.; Clegg, S.L. (2024). Modelling the inorganic complexation of the GEOTRACES core elements, with a focus on Fe(III) hydrolysis. MarChemSpec.
5. Luther, G.W.; Rickard, D.T.; Theberge, S.; Olroyd, A. (1996). Determination of metal (bi)sulfide stability constants. *Environ. Sci. Technol.*, doi:10.1021/es950417i (243 citations)
