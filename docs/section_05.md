# Metabolic Reaction Fusion Molecular Network Analysis

## 4.4 I Have Molecular Network Files

Data format: network_edges.csv (source, target, weight), network_nodes.csv (node_id, precursor_mz, rt), optional network_components.csv.

Available features:

• Interactive network visualization and m/z-based component search

• Integrate MGF, metabolomics, and AI identification results; click nodes to view spectra, structures, and box plots

• Embedding analysis (requires DNN fingerprints)

• Reaction analysis (requires reactant MGF)

Module: Advanced Analysis

Quick steps:

① Set Experiment Folder and click Auto-Import Files (if the folder already contains network and related files); or manually set Network Edges, Network Nodes, Network Components and click Import Network

② (Optional) Load MGF Data, Load Metabolomics Data, Load Annotation Data, Load DNN Fingerprints

③ In Network Visualization on the right, select components, adjust Plot Parameters, and click nodes for details

④ (Optional) View fingerprint heatmap in Embedding Analysis; view reaction statistics in Reaction Details (requires Reaction Visualization to be completed first)

## 4.6 I Have Reactant MGF (Raw Material Spectra)

Data format: MGF file containing MS/MS spectra of raw materials/reactants.

Available features:

• Match products to reactants in Advanced Analysis and annotate reaction types (e.g. glycosylation, methylation)

• Reaction visualization, reaction type statistics, product/reactant intensity ranking, product-reactant network graph

Module: Advanced Analysis (Reaction Analysis)

Quick steps:

① Import network in Advanced Analysis first (see section 4)

② In Reaction Analysis, set Reactant MGF File and click Load Reactant MGF Data

③ Set RT Tolerance, MZ Tolerance, Min Cosine Similarity, Reaction MW Tolerance; use Manage Reaction Types to configure reaction types

④ In Reaction Visualization, choose Similarity Method (cosine, neutral_loss, dnn_fingerprint, Transformer_DNN, or fusion) and set thresholds

⑤ Click Generate Reaction Visualization

⑥ View reaction network and statistics in the Reaction Visualization and Reaction Details sub-tabs

## 4.7 I Have a Complete Experiment Folder (Network + MGF + Metabolomics + AI Results, etc.)

Data format: A folder containing network_edges.csv, network_nodes.csv, network_components.csv, MGF, DNN fingerprints, FeatureTable.csv, MetaboResult.csv, AI identification results, etc. (typically from Molecular Networks Export All Results and Batch Metabolomics output).

Available features:

• Integrated analysis: network, spectra, metabolomics, structures, embeddings, and reaction analysis in one place

Module: Advanced Analysis (Auto-Import)

Quick steps:

① Set Experiment Folder to this experiment folder

② Click Auto-Import Files; the tool auto-detects and fills paths for network, MGF, metabolomics, AI results, etc.

③ If network files are detected, Import Network may run automatically

④ Browse Network Visualization, Embedding Analysis, Reaction Visualization, Reaction Details, Batch Experiments Visualization, etc. in the right panel

## 4.8 Common Combined Workflows

Workflow A: From Raw Data to Identification and Network

Feature tables → Batch Metabolomics (differential analysis) → MetaboResult, FeatureTable

MGF → Molecular Networks (optional Metabolomics Filter) → Build network, Export All Results

→ Advanced Analysis Auto-Import → Integrate network, metabolomics, AI identification

Workflow B: From MGF to Compound Identification

MGF → MS Identification (Basic Search or AI Search) → Candidate compounds

(Optional) MGF → Molecular Networks (with AI Search enabled) → Build network and identify nodes

Workflow C: Custom Database + AI Identification

SMILES CSV → AI DatabaseGen → Generate NPZ

MGF → MS Identification AI Search (load the NPZ) → Identification

Workflow D: Reactant-Product Analysis

Network + Reactant MGF → Advanced Analysis Reaction Analysis → Reaction visualization, reaction type statistics, product/reactant intensity ranking.
