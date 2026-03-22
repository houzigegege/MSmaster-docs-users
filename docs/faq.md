# FAQ & Troubleshooting (inputs & run order)

This page summarizes common issues you are likely to face in real projects, especially:
1) input format mismatches, and
2) incorrect run order.

## 1) How should I prepare the feature table (CSV)?

`MSmaster` expects a feature table with:

- One row per metabolite/feature (e.g., `RT_MZ` or compound label)
- One column per sample or group (e.g., `Group1`, `Group1.1`, `Group2`)
- Intensity values in the cells

Group information is inferred from column names. For example, `Group1` and `Group1.1` may be treated as the same group depending on the naming convention.

## 2) What should the MGF file contain?

MGF is used to carry MS/MS spectral information, typically including:

- Precursor-ion related metadata (e.g., precursor `m/z`)
- Retention time (`RT`)
- Fragment peak lists, etc.

## 3) Why does reaction product prediction/annotation return no results?

A frequent reason is run order. Annotation usually depends on the per-sample directories and on `MetaboResult.csv`.

Recommended sequence:

1. Run `Batch Metabolomics Analysis` first to generate differential results and the expected folder structure.
2. Then run reaction product prediction/annotation in the appropriate location. The tool will write/update `MSFindResult.csv`.

## 4) What is the difference between `Basic Search` and `AI Search`?

- `Basic Search`: relies on spectral similarity and database/settings for candidate identification.
- `AI Search`: relies on NPZ fingerprint databases and DNN model configuration (model type/checkpoint, mass quality tolerance, minimum DNN similarity, etc.).

If you want to emphasize model-driven consistency, `AI Search` is often preferred. If you want more traditional/spectral-similarity behavior for cross-checking, start with `Basic Search`.

## 5) Where should I start troubleshooting?

Suggested checklist order:

- Confirm the input files match the expected format requirements.
- Confirm that group column names are inferred the way you intended.
- Confirm that you are using the correct output from the previous step in the correct module (for example, reaction annotation depends on differential outputs).

