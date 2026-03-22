# Reproducibility & Validation: make conclusions review-ready

For scientific teams, the goal is not only to “get results”, but to:
1) reproduce the analysis under the same data and parameter settings, and
2) explain why certain features/candidates are considered significant.

## 1) Record key settings (parameter versioning)

Archive at least the following:

- Input data versions (CSV / MGF file names and their source paths)
- `Project Path` (root output directory) and the generated per-sample folder structure
- Batch analysis parameters: missing value threshold, imputation method, log-transform settings (and log base), scaling method, test method, FC method, pseudo count, permutation count, etc.
- If reaction product prediction/annotation is enabled: molecular weight list, enabled reaction types, and matching tolerance (`Match Threshold`)

The UI also provides an “Analysis Log” during processing. Save these logs as part of your record for later review.

## 2) Structured outputs for secondary checking

Batch differential analysis generates corresponding outputs in each per-sample folder (for example: differential result tables and volcano plot images). This enables traceability:

input intensity matrix → statistical test/FC calculation → output plots and result tables.

## 3) Independent validation: identification & analysis are computational predictions

It is essential to state that identification and analysis results are computational predictions. For research use, results still require independent validation within your experimental system, e.g.:

- standards and retention-time checks
- confirmatory MS/MS evidence and independent algorithm re-check
- literature/database evidence chain cross-checking
- experimental replication or orthogonal evidence strengthening

## 4) Team collaboration recommendation

For efficient cross-team review, share the “complete experiment output folder” so others can import it directly via `Advanced Analysis – Auto-Import` and perform secondary interpretation.

