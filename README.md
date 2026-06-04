# MSmaster

**MSmaster** is an integrated metabolomics analysis platform centered on **Fusion Molecular Networks (FMN)** and **Metabolic Reaction Fusion Molecular Networks (MR-FMN)**, with *auxiliary* **MS/MS spectral annotation** and **metabolomics analysis** modules in the same *traceable*, evidence-oriented workflow.

| | |
|---|---|
| **Documentation** | [Scientific Usage Guide](https://houzigegege.github.io/MSmaster-docs-users/) |
| **Download** | [MSmaster_V1.0.0.7z](https://github.com/houzigegege/MSmaster-docs-users/releases/download/v1.0.0/MSmaster_V1.0.0.7z) |
| **Issues** | [GitHub Issues](https://github.com/houzigegege/MSmaster-docs-users/issues) |

---

## Overview

MSmaster is designed for researchers who need a coherent pipeline in untargeted / LC–MS–based metabolomics:

**Primary network outputs**

- **Fusion Molecular Networks (FMN)** — hierarchical fusion graph (cosine, neutral loss, DNN edges)  
- **Metabolic Reaction Fusion Molecular Networks (MR-FMN)** — reaction annotation built on exported FMN  

**Auxiliary analysis (supporting FMN/MR-FMN)**

- **MS/MS spectral annotation** — identification, AI database search, traceable parameters and exports  
- **Metabolomics analysis** — batch workflows, differential/statistical analysis, feature tables and filters used before or alongside networking  
- **Additional modules** — molecular networking UI, database generation, and advanced analysis views that connect to exported FMN data

The platform emphasizes **reproducibility**, **parameter transparency**, and **interpretable exports** suitable for supplementary materials and follow-up validation.

![MSmaster workflow overview](docs/Figures/figure%201.png)

*Figure 1. Overview of the MSmaster workflow (see the Usage Guide for details).*

---

## Quick start

1. **Install** — Download the Windows package from **[Releases](https://github.com/houzigegege/MSmaster-docs-users/releases)** (see system requirements below). Extract locally and launch the application.  
2. **Read the guide** — Open the **[FMN & MR-FMN Guide](https://houzigegege.github.io/MSmaster-docs-users/)** and follow: Install → Modules → Quick Start → **[FMN](https://houzigegege.github.io/MSmaster-docs-users/manual/section_05/)** → **[MR-FMN](https://houzigegege.github.io/MSmaster-docs-users/manual/section_06/)**.  
3. **Build networks** — Complete FMN in Molecular Networks, export all results, then run MR-FMN in Advanced Analysis on the exported project folder.

---

## System requirements

| Item | Recommendation |
|------|----------------|
| **OS** | Windows 10 / 11 (64-bit) |
| **RAM** | 8 GB minimum; **16 GB+** recommended |
| **Disk** | 4.3 GB free after extraction (plus ~1.0 GB download) |
| **Installer size** | ~1.0 GB (see Releases) |

---

## Documentation map

The full manual is published as a static site (MkDocs Material):

| Chapter | Topic |
|---------|--------|
| About MSmaster | Scope, outputs, intended use |
| Install MSmaster | Download, setup, first launch |
| MSmaster modules | UI and core workflows |
| Quick Start | Start by input type |
| FMN | Fusion Molecular Networks |
| MR-FMN | Metabolic Reaction Fusion Molecular Networks |

Source manuscript: `Manual.docx` in this repository (converted to `docs/manual/` for the website).

---

## Important notice

Identification and networking results are **computational predictions**. For research use, conclusions should be supported by independent validation (e.g., authentic standards, confirmatory MS/MS, database/literature cross-checks, and experimental verification in your system).

---

## This repository

**`MSmaster-docs-users`** hosts:

- The **Scientific Usage Guide** (built with [MkDocs](https://www.mkdocs.org/) + [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/))  
- **`Manual.docx`** and generated chapter pages under `docs/manual/`  
- **GitHub Actions** deployment to GitHub Pages  
- **Release assets** for the Windows installer (large files are **not** stored in Git history)

Maintainers: see **[WEBSITE.md](WEBSITE.md)** for regenerating the site from Word, publishing updates, and creating Releases.

---

## Citation

If you use MSmaster in published work, please cite the software and the analysis parameters you used. *(Add your preferred citation text here, e.g., manuscript DOI or Zenodo record.)*

---

## License

*(Add license information here, e.g., MIT, proprietary academic use, etc.)*

---

## Contact

*(Add contact email, lab page, or issue tracker link as appropriate.)*
