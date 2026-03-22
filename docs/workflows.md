# Workflows (choose by data type)

The first step in scientific analysis is to match your “data type” to your “research question/hypothesis”. This page recommends workflows based on the data you have, and highlights which key parameters and outputs you should focus on. For step-by-step UI operations, see the auto-generated manual pages in the navigation.

## Decision table (quick path selection)

| Your data | Main modules | Core scientific outputs |
| --- | --- | --- |
| Multi-sample feature tables (CSV) | `Batch Metabolomics Analysis` | Between-group statistical tests, fold change (FC), volcano/heatmap, PCA/HCA, and optional reaction product prediction/annotation |
| MS/MS spectra (MGF) | `MS Identification`; `Molecular Networks` | Candidate compound identification and molecular networking driven by similarity metrics |
| Feature tables + MGF | `Batch Metabolomics Analysis + Molecular Networks` or `Molecular Networks + Advanced Analysis` | Metabolomics-filtered networks and integration of networks with statistics/visualization |
| Network files (XGMML/CSV) | `Advanced Analysis` | Network visualization, multi-omics integration, embedding, and reaction-related analysis |
| SMILES list (CSV) | `AI DatabaseGen` | Generation of NPZ fingerprint databases for later AI identification/embedding |
| Reactant MGF | `Advanced Analysis – Reaction Analysis` | Product–reactant matching and reaction type statistics |
| A complete experiment folder | `Advanced Analysis – Auto-Import` | Fully integrated environment via automatic detection/import of network, MGF, metabolomics, and AI results |

## Typical scientific workflows

### 1) Statistics from feature tables, then use statistics to filter/interpret networks

Best when your research focuses on group-differential metabolites/features and you want to interpret candidate relationships in a network context.

Recommended path:

1. Use `Batch Metabolomics Analysis` to run differential analysis and generate visualizations (volcano plot, PCA/HCA, etc.).
2. Optionally provide a molecular weight list for reaction product prediction/annotation (depends on the already computed per-sample differential outputs).
3. If you want metabolomics-filtered networks, use the metabolomics filter option in `Molecular Networks` to apply your experiment/control ratio rules during network construction or interpretation.

For the scientific meaning of each key parameter, see `parameters.md`.

### 2) Spectra-based identification and networking, then integrate via advanced analysis

Best when you are primarily interested in similarity-driven molecular family relationships, and you later want to connect identification results with statistics, embedding, or reaction-related analysis.

Recommended path:

1. Use `MS Identification` with `Basic Search` (spectral similarity) or `AI Search` (fingerprints + DNN).
2. Use `Molecular Networks` with your chosen similarity method and thresholds to build network components.
3. In `Advanced Analysis`, run network visualization, embedding, and reaction-related analysis depending on the imported file types.

### 3) Network files / full experiment folder integration (more reproducible)

Best for cross-team collaboration and for repeating analyses or doing secondary interpretation on the same experiment.

Recommended path:

1. Export network and related outputs into a “complete experiment folder”.
2. In `Advanced Analysis – Auto-Import`, set the experiment folder; the tool automatically imports network, MGF, metabolomics, and AI results.
3. Later, you can reproduce or compare different interpretation versions by adjusting only visualization settings or a small set of key parameters.

## Next

To read parameters and plots more scientifically, continue with:

- `parameters.md` (parameter meaning and output interpretation)
- `reproducibility.md` (how to record settings and validate results)

