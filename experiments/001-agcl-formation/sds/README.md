# Safety Data Sheet (SDS) Summaries

This directory contains SDS summaries for all chemicals and reaction products
involved in Experiment 001 (AgCl precipitation). These are **summaries
extracted from manufacturer SDS documents** — always refer to the full
official SDS for complete safety information.

## Chemicals

| Chemical | CAS No. | Summary | PDF | Role in Experiment |
|----------|---------|---------|-----|--------------------|
| Silver nitrate (AgNO₃) | 7761-88-8 | [AgNO3.md](AgNO3.md) | [AgNO3_Chemos_0.1M.pdf](pdfs/AgNO3_Chemos_0.1M.pdf) | Reagent (both variants) |
| Sodium chloride (NaCl) | 7647-14-5 | [NaCl.md](NaCl.md) | [NaCl_SigmaAldrich.pdf](pdfs/NaCl_SigmaAldrich.pdf) | Reagent (Variant A) |
| Hydrochloric acid (HCl) | 7647-01-0 | [HCl.md](HCl.md) | [HCl_SigmaAldrich_1M.pdf](pdfs/HCl_SigmaAldrich_1M.pdf) | Reagent (Variant B) |
| Silver chloride (AgCl) | 7783-90-6 | [AgCl.md](AgCl.md) | [AgCl_SigmaAldrich.pdf](pdfs/AgCl_SigmaAldrich.pdf) | Reaction product (both variants) |
| Sodium nitrate (NaNO₃) | 7631-99-4 | [NaNO3.md](NaNO3.md) | [NaNO3_SigmaAldrich.pdf](pdfs/NaNO3_SigmaAldrich.pdf) | Reaction byproduct (Variant A) |
| Nitric acid (HNO₃) | 7697-37-2 | [HNO3.md](HNO3.md) | [HNO3_SigmaAldrich.pdf](pdfs/HNO3_SigmaAldrich.pdf) | Reaction byproduct (Variant B) |

## SDS PDF Downloads

The `pdfs/` subdirectory should contain the original PDF SDS documents.
Use the table below to download each PDF from its source. Save the file
with the filename shown in the "Save As" column.

| Chemical | Source | Download URL | Save As |
|----------|--------|-------------|---------|
| AgNO₃ (0.1 M) | Chemos GmbH | https://www.chemos.de/import/data/msds/GB_en/7761-88-8-A0287385-GB-en.pdf | `pdfs/AgNO3_Chemos_0.1M.pdf` |
| AgNO₃ (0.1 M) | CDH Fine Chemical | https://www.cdhfinechemical.com/images/product/msds/14_1779855659_SilverNitrate0.1M(0.1N)Solution-MSDS.pdf | `pdfs/AgNO3_CDH_0.1M.pdf` |
| NaCl | Sigma-Aldrich (S7653) | https://www.sigmaaldrich.com/US/en/sds/SIAL/S7653 | `pdfs/NaCl_SigmaAldrich.pdf` |
| HCl (1 M) | Delta College (hosted Sigma-Aldrich) | https://employees.delta.edu/facilities/_safety-data-sheets/hydrochloric-acid-solution-1m-sigma-aldrich.pdf | `pdfs/HCl_SigmaAldrich_1M.pdf` |
| AgCl | Sigma-Aldrich (227927) | https://www.sigmaaldrich.com/US/en/sds/sigald/227927 | `pdfs/AgCl_SigmaAldrich.pdf` |
| NaNO₃ | Sigma-Aldrich (S5506) | https://www.sigmaaldrich.com/US/en/sds/sigald/s5506 | `pdfs/NaNO3_SigmaAldrich.pdf` |
| HNO₃ (dilute) | Sigma-Aldrich (438073) | https://www.sigmaaldrich.com/US/en/sds/sigald/438073 | `pdfs/HNO3_SigmaAldrich.pdf` |

> **Note:** Sigma-Aldrich SDS pages generate PDFs dynamically and require
> clicking "Download" on their website. The direct PDF links above (Chemos,
> CDH, Delta College) can be downloaded directly with `curl` or a browser.

### Quick download script

```bash
cd experiments/001-agcl-formation/sds/pdfs/

# Direct PDF downloads
curl -L -o AgNO3_Chemos_0.1M.pdf "https://www.chemos.de/import/data/msds/GB_en/7761-88-8-A0287385-GB-en.pdf"
curl -L -o AgNO3_CDH_0.1M.pdf "https://www.cdhfinechemical.com/images/product/msds/14_1779855659_SilverNitrate0.1M(0.1N)Solution-MSDS.pdf"
curl -L -o HCl_SigmaAldrich_1M.pdf "https://employees.delta.edu/facilities/_safety-data-sheets/hydrochloric-acid-solution-1m-sigma-aldrich.pdf"

# For Sigma-Aldrich hosted SDSs, visit these URLs in a browser and click "Download":
# NaCl:  https://www.sigmaaldrich.com/US/en/sds/SIAL/S7653
# AgCl:  https://www.sigmaaldrich.com/US/en/sds/sigald/227927
# NaNO3: https://www.sigmaaldrich.com/US/en/sds/sigald/s5506
# HNO3:  https://www.sigmaaldrich.com/US/en/sds/sigald/438073
```

## Additional SDS Sources

| Chemical | Additional Source | URL |
|----------|------------------|-----|
| AgNO₃ (0.1 M solution) | Sigma-Aldrich (SAJ, Product 28-1350) | https://www.sigmaaldrich.com/GB/en/sds/saj/28-1350 |
| HCl (1 M solution) | Sigma-Aldrich / Merck (Product 110165) | https://www.sigmaaldrich.com/US/en/sds/mm/1.10165 |
| AgCl | Sigma-Aldrich (Product 204382) | https://www.sigmaaldrich.com/US/en/sds/aldrich/204382 |
| NaNO₃ | Sigma-Aldrich (Product 221341) | https://www.sigmaaldrich.com/US/en/sds/SIGALD/221341 |
| HNO₃ (0.1 M solution) | Sigma-Aldrich / Merck (Product 1.60236) | https://www.sigmaaldrich.com/US/en/sds/mm/1.60236 |

## Notes

- SDS documents are living documents updated by manufacturers. The summaries
  here were compiled in February 2026. Always check the manufacturer's website
  for the most current version.
- For the actual experiment, the concentrations used are dilute (0.1 M AgNO₃,
  1 M NaCl or HCl), which generally reduce hazard severity compared to
  concentrated or solid forms.
- All chemicals should be procured from BYU Chem Stores to maintain proper
  chain of custody and institutional safety compliance.
- The PDFs in `pdfs/` need to be downloaded manually — see the download
  instructions and script above.
