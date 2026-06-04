# MSmaster Scientific Usage Guide

**MSmaster** is an integrated metabolomics analysis platform centered on building **Fusion Molecular Networks (FMN)** and **Metabolic Reaction Fusion Molecular Networks (MR-FMN)**—within a *traceable* workflow from MS/MS input to exportable network evidence.

The same tool also provides **auxiliary** capabilities for **MS/MS spectral annotation (identification)** and **metabolomics analysis** (e.g., batch differential/statistical workflows and feature-table–driven filters) that prepare, annotate, or constrain data before FMN/MR-FMN. For a scientist audience, navigation stays minimal: each main entry is a chapter auto-generated from `Manual.docx`.

<div class="hero-banner hero-banner--fmn">
  <div class="hero-banner__inner">
    <p class="hero-eyebrow">Core deliverable</p>
    <h1>Build FMN &amp; MR-FMN with MSmaster</h1>
    <p>
      <strong>Fusion Molecular Networks (FMN)</strong> combine cosine, neutral-loss, and DNN-based edges in one hierarchical graph.
      <strong>MR-FMN</strong> extends an exported FMN with metabolic reaction annotation and expert-level verification—start FMN first, then import the project folder for reaction analysis.
      <span class="hero-aside">Auxiliary:</span> MS/MS annotation and metabolomics modules support identification, feature tables, and filters upstream of the network workflows.
    </p>
    <div class="workflow-path" aria-label="Recommended network workflow">
      <span class="workflow-path__step workflow-path__step--active">FMN</span>
      <span class="workflow-path__arrow" aria-hidden="true">→</span>
      <span class="workflow-path__step">Export results</span>
      <span class="workflow-path__arrow" aria-hidden="true">→</span>
      <span class="workflow-path__step workflow-path__step--active">MR-FMN</span>
    </div>
    <div class="hero-actions">
      <a class="md-button md-button--primary" href="manual/section_05/">Fusion Molecular Networks (FMN)</a>
      <a class="md-button md-button--primary" href="manual/section_06/">MR-FMN</a>
      <a class="md-button" href="https://github.com/houzigegege/MSmaster-docs-users/releases/download/v1.0.0/MSmaster_V1.0.0.7z">Download v1.0.0</a>
      <a class="md-button" href="manual/section_04/">Quick Start</a>
    </div>
    <div class="hero-meta">
      <span class="hero-pill">Hierarchical fusion graph</span>
      <span class="hero-pill">Traceable parameters</span>
      <span class="hero-pill">Exportable network evidence</span>
      <span class="hero-pill">Reaction-aware MR-FMN</span>
      <span class="hero-pill hero-pill--aux">Auxiliary: MS/MS annotation</span>
      <span class="hero-pill hero-pill--aux">Auxiliary: metabolomics analysis</span>
    </div>
  </div>
</div>

<figure class="home-figure">
  <img src="Figures/figure%201.png" alt="Figure 1 — MSmaster overview with FMN and MR-FMN as central outputs" loading="lazy" />
  <figcaption class="home-figure__caption">Figure 1. <strong>FMN</strong> and <strong>MR-FMN</strong> are the primary network outputs; MS/MS annotation and metabolomics analysis are auxiliary modules that feed filters, labels, and evidence into those workflows (see Modules &amp; Quick Start).</figcaption>
</figure>

## Core workflows (start here)

<div class="grid cards cards--core" markdown>
  <a href="manual/section_05/" class="card card--featured">
    <div class="card__badge">Step 1</div>
    <div class="card__title">Fusion Molecular Networks (FMN)</div>
    <div class="card__subtitle">Unified graph: cosine → neutral loss → Standard DNN → Transformer DNN. Configure hierarchical fusion, run analysis, and export all results.</div>
  </a>
  <a href="manual/section_06/" class="card card--featured">
    <div class="card__badge">Step 2</div>
    <div class="card__title">Metabolic Reaction Fusion Molecular Networks (MR-FMN)</div>
    <div class="card__subtitle">Requires completed FMN exports. Import the project folder, define reaction rules, annotate reactions, and verify predictions before export.</div>
  </a>
</div>

## Auxiliary analysis (MS annotation & metabolomics)

These modules are **supporting** workflows—not substitutes for FMN/MR-FMN—but they are often used to identify spectra, build feature tables, or apply metabolomics filters before network construction.

<div class="grid cards cards--aux" markdown>
  <a href="manual/section_03/" class="card card--aux">
    <div class="card__badge card__badge--aux">Auxiliary</div>
    <div class="card__title">MS/MS spectral annotation</div>
    <div class="card__subtitle">MS Identification, AI database search, and node-level annotation linked to Molecular Networks / FMN exports.</div>
  </a>
  <a href="manual/section_03/" class="card card--aux">
    <div class="card__badge card__badge--aux">Auxiliary</div>
    <div class="card__title">Metabolomics analysis</div>
    <div class="card__subtitle">Batch metabolomics, differential/statistical outputs, and MetaboResult tables—usable in FMN metabolomics filters and downstream interpretation.</div>
  </a>
  <a href="manual/section_04/" class="card card--aux">
    <div class="card__badge card__badge--aux">Auxiliary</div>
    <div class="card__title">Quick Start (by input type)</div>
    <div class="card__subtitle">Choose entry points for MGF-only, feature-table, or combined pipelines before opening the FMN chapter.</div>
  </a>
</div>

## Foundation chapters (install, modules, quick start)

<div class="grid cards" markdown>
  <a href="manual/section_01/" class="card">
    <div class="card__title">About MSmaster</div>
    <div class="card__subtitle">Scope, outputs, and intended use</div>
  </a>
  <a href="manual/section_02/" class="card">
    <div class="card__title">Install MSmaster</div>
    <div class="card__subtitle">Download v1.0.0 · setup &amp; first launch</div>
  </a>
  <a href="manual/section_03/" class="card">
    <div class="card__title">MSmaster modules</div>
    <div class="card__subtitle">Full UI map: annotation, metabolomics, Molecular Networks, FMN inputs</div>
  </a>
  <a href="manual/section_04/" class="card">
    <div class="card__title">Quick Start</div>
    <div class="card__subtitle">Prepare MGF / project path before FMN</div>
  </a>
</div>

!!! warning
    Identification and network results are *computational predictions*.
    For research use, conclusions still require independent validation within your experimental system (e.g., standards, confirmatory MS/MS evidence, literature/database cross-checking, and experimental verification).

## Recommended reading order (FMN → MR-FMN)

1. [Install MSmaster](manual/section_02.md) — download, extract, first launch
2. [MSmaster modules](manual/section_03.md) — auxiliary annotation & metabolomics modules, plus Molecular Networks / FMN inputs
3. [Quick Start](manual/section_04.md) — inputs by data type (MGF, filters, project folder)
4. **[Fusion Molecular Networks (FMN)](manual/section_05.md)** — build and export the fusion graph
5. **[Metabolic Reaction Fusion Molecular Networks (MR-FMN)](manual/section_06.md)** — reaction analysis on exported FMN
6. [Parameters & output interpretation](parameters.md)
7. [Reproducibility & validation](reproducibility.md)
8. [FAQ & troubleshooting](faq.md)
