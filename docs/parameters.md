# Parameters & Output Interpretation (scientific)

This page focuses on the key statistical parameters you encounter in `Batch Metabolomics Analysis`, and explains how they can affect differential results and the corresponding visualizations. When writing reports or making scientific conclusions, it is recommended to archive: parameter versions + data versions + the relevant output files.

For UI locations and step-by-step operations, see the auto-generated manual: `manual/section_03.md`.

## Batch differential analysis: preprocessing & statistical framework

### 1) Missing values & imputation

- `Missing Value Threshold` (default `0.8`): if a feature is missing in more than this fraction of samples, the feature will be removed (`0–1`). Higher thresholds keep more features but can make later statistics more sensitive to missingness structure.
- `Imputation Method` (default `median`): missing value filling method, choose among `median`, `mean`, `zero`. Different choices change the resulting distribution and can affect statistical outcomes, so select a method consistent with your experimental context.

### 2) Transformations & scaling (for statistical stability)

- `Log Transform` (default “Checked”): whether to log-transform intensity values.
- `Log Base` (default `2`): the logarithm base used for the transform.
- `Scaling` (default `standard`): scaling method, choose among `standard`, `minmax`, `robust`, or `None`.

### 3) Statistical test & fold change (FC)

- `Test Method` (default `ttest`): between-group statistical test (`ttest`, `mannwhitney`, or `permutation`).
- `Fold Change Method` (default `log2`): fold change calculation mode (`log2`, `ratio`, or `difference`).
- `Pseudo Count` (default `1`): pseudo-count added when computing fold change to avoid division-by-zero issues.
- `Permutation Count` (default `1000`): when using `permutation`, the number of permutations determines the resolution/precision of the empirical distribution.

## Reaction product prediction & annotation (optional)

When you want to map differential features/identifications onto potential reaction processes, use reaction product prediction and annotation:

- `Input Data`: a comma-separated list of molecular weights, e.g. `228.25, 180.16, 162.05`
- `Manage Reaction Types`: inspect and enable/disable predefined reaction types (single- or multi-step); prediction only uses enabled types
- `Match Threshold` (default `0.02`): mass/time tolerance used for matching
- `Run Prediction & Annotation`: runs predictions from the molecular weight list, matches against each sample's metabolomics result, and updates/writes `MSFindResult.csv`

Important: annotation typically depends on the `MetaboResult.csv` already generated in each sample folder, so in most cases you run batch differential analysis first.

## Interpreting plots and outputs

From the auto-generated manual, the main plot types include:

- Volcano plot (`Volcano`): combines `p-value` and `FC` to show both statistical significance and effect size/direction.
- Heatmap (`Heatmap`) and RT distribution (`RT Distribution`): show patterns across samples/groups and check retention-time consistency.
- PCA: projects the merged feature matrix into lower dimensions to diagnose clustering and potential batch effects.
- HCA: hierarchical clustering visualization to inspect similarity structure between samples.

