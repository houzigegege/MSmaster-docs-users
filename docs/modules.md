# Modules Reference (UI & workflow)

This page uses the interface as an entry point, but it focuses on the scientific task behind each module: what the input represents, what the output is intended to answer, and what should be validated independently in your research.

## Core modules overview

From the auto-generated manual, the tool covers the following core modules (which can be combined depending on your research path):

- `Batch Metabolomics Analysis`: between-group statistics, fold change (FC), visualizations, and optional reaction product prediction/annotation
- `MS Identification`: candidate identification using spectral similarity (`Basic Search`) or AI fingerprints/models (`AI Search`)
- `Molecular Networks`: builds molecular network components from similarity metrics and supports metabolomics-statistics-driven filtering/interpretation
- `Advanced Analysis`: network-file integration, visualization, multi-omics integration, embedding, and reaction-related analysis
- `AI DatabaseGen`: generates NPZ fingerprint databases required for AI identification/embedding workflows
- `Advanced Analysis – Auto-Import`: imports a complete experiment folder to create a reproducible integrated analysis environment

## Why this UI organization helps reproducibility

Taking `Batch Metabolomics Analysis` as an example, the interface follows a structured flow:

- Left side: inputs such as `Project Path`, the feature table folder, and analysis parameters (and advanced settings for preprocessing/statistics/reaction annotation when enabled)
- Right side: results such as batch summaries, per-sample outputs, and plots/tables

This layout supports a reproducible workflow: define parameters first, run batch analysis, and rely on the on-disk project directory structure for outputs and later cross-checks.

## Step-by-step operations (auto-generated manual)

For click-by-click guidance, go to:

- `manual/section_03.md` (overview, interface layout, and output logic)
- `manual/section_04.md` (quick workflows by data type)

