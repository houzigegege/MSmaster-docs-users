# Quick Start

Use the table below to choose a workflow by input type. The video guides demonstrate three common MS/MS–related entry points in MSmaster.

| Data Type | Main Module | Core Features |
| --- | --- | --- |
| Feature tables (multi-sample CSV) | Batch Metabolomics Analysis | Differential analysis, volcano plots, and reaction product annotation. |
| MS/MS MGF | MS Identification; Molecular Networks | Compound identification and molecular network construction. |
| Feature tables + MGF | Batch Metabolomics + Molecular Networks; or Molecular Networks + Advanced Analysis | Metabolomics-filtered networks and integration of network and statistical analysis. |
| Network files (XGMML/CSV) | Advanced Analysis | Network visualization, multi-omics integration, embedding, and reaction analysis. |
| SMILES list (CSV) | AI DatabaseGen | Generation of NPZ fingerprint databases. |
| Reactant MGF | Advanced Analysis – Reaction Analysis | Product–reactant matching and reaction type statistics. |
| Complete experiment folder | Advanced Analysis – Auto-Import | Fully integrated analysis workflow in one interface. |

## Video guides

### MS/MS library search

Spectral library matching against an MGF reference database in **MS Identification** (Basic Search): load spectra, set tolerances and similarity options, and review ranked candidates.

<div class="home-video quick-start-video">
  <div class="home-video__frame">
    <video class="home-video__player" controls preload="metadata" playsinline poster="../media/Lib-search-poster.jpg" title="MS/MS library search in MSmaster">
      <source src="../media/Lib-search.mp4" type="video/mp4" />
      Your browser does not support embedded video.
      <a href="../media/Lib-search.mp4">Download MS/MS library search demo (MP4)</a>.
    </video>
  </div>
</div>

### Molecular fingerprint database search (AI)

AI fingerprint search against an NPZ database in **MS Identification** (AI Search): select a DNN model, set mass tolerance and similarity thresholds, and batch-annotate spectra.

<div class="home-video quick-start-video">
  <div class="home-video__frame">
    <video class="home-video__player" controls preload="metadata" playsinline poster="../media/AILib-Search-poster.jpg" title="AI molecular fingerprint database search in MSmaster">
      <source src="../media/AILib-Search.mp4" type="video/mp4" />
      Your browser does not support embedded video.
      <a href="../media/AILib-Search.mp4">Download AI library search demo (MP4)</a>.
    </video>
  </div>
</div>

### Molecular network construction with MS/MS annotation

Build a molecular network in **Molecular Networks**, optionally run database search / AI annotation on nodes, visualize components, and export results for downstream analysis (including FMN workflows).

<div class="home-video quick-start-video">
  <div class="home-video__frame">
    <video class="home-video__player" controls preload="metadata" playsinline poster="../media/Molecular_network-poster.jpg" title="Molecular network construction with MS/MS annotation in MSmaster">
      <source src="../media/Molecular_network.mp4" type="video/mp4" />
      Your browser does not support embedded video.
      <a href="../media/Molecular_network.mp4">Download molecular network demo (MP4)</a>.
    </video>
  </div>
</div>

For hierarchical fusion networks and MR-FMN, continue with the [Fusion Molecular Networks (FMN)](section_05.md) and [Metabolic Reaction Fusion Molecular Networks (MR-FMN)](section_06.md) chapters.
