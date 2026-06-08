---
hide:
  - title
---

**MSmaster** is an integrated metabolomics platform for **FMN** and **MR-FMN**, with auxiliary **MS/MS annotation** and **metabolomics analysis** in the same traceable workflow. Navigation follows chapters from `Manual.docx`—minimal tabs, defensible exports.

<div class="hero-banner hero-banner--fmn">
  <div class="hero-banner__inner">
    <p class="hero-eyebrow">Scientific usage guide</p>
    <p class="hero-tagline">
      <span class="hero-tagline__lead">Traceable fusion networks for metabolomics MS/MS</span>
      <span class="hero-tagline__with">with</span>
      <span class="hero-tagline__rotate" aria-live="polite">
        <span class="hero-tagline__word">FMN</span>
        <span class="hero-tagline__word">MR-FMN</span>
        <span class="hero-tagline__word">MS/MS annotation</span>
        <span class="hero-tagline__word">metabolomics analysis</span>
      </span>
    </p>
    <h1>Build exportable FMN &amp; MR-FMN evidence</h1>
    <p class="hero-lead">
      <strong>Fusion Molecular Networks (FMN)</strong> unify cosine, neutral-loss, and DNN edges in one hierarchical graph.
      <strong>MR-FMN</strong> adds metabolic reaction annotation on exported FMN projects—complete FMN first, then import the folder in Advanced Analysis.
    </p>
    <div class="workflow-path" aria-label="Best-practice network workflow">
      <span class="workflow-path__label">Best practice</span>
      <span class="workflow-path__step workflow-path__step--active">FMN</span>
      <span class="workflow-path__arrow" aria-hidden="true">→</span>
      <span class="workflow-path__step">Export all results</span>
      <span class="workflow-path__arrow" aria-hidden="true">→</span>
      <span class="workflow-path__step workflow-path__step--active">MR-FMN</span>
    </div>
    <div class="hero-actions">
      <a class="md-button md-button--primary hero-cta-primary" href="manual/section_05/">Start with FMN</a>
      <div class="hero-actions-secondary">
        <a class="md-button" href="manual/section_06/">MR-FMN guide</a>
        <a class="md-button" href="https://github.com/houzigegege/MSmaster-docs-users/releases/download/v1.0.0/MSmaster_V1.0.0.7z">Download v1.0.0</a>
        <a class="md-button" href="manual/section_04/">Quick Start</a>
      </div>
    </div>
  </div>
</div>

<div class="pillars" markdown="0">
  <div class="pillar">
    <div class="pillar__icon" aria-hidden="true">①</div>
    <h3 class="pillar__title">From MS/MS to FMN</h3>
    <p class="pillar__text">Hierarchical fusion (cosine → neutral loss → DNN), optional metabolomics/reactant filters, and <strong>Export All Results</strong> for reproducible network files.</p>
    <a class="pillar__link" href="manual/section_05/">FMN chapter →</a>
  </div>
  <div class="pillar">
    <div class="pillar__icon" aria-hidden="true">②</div>
    <h3 class="pillar__title">From FMN to MR-FMN</h3>
    <p class="pillar__text">Import the FMN project folder, configure reaction rules, run annotation, and verify predictions before exporting MR-FMN outputs.</p>
    <a class="pillar__link" href="manual/section_06/">MR-FMN chapter →</a>
  </div>
  <div class="pillar">
    <div class="pillar__icon" aria-hidden="true">③</div>
    <h3 class="pillar__title">Traceable &amp; defensible</h3>
    <p class="pillar__text">Documented parameters, structured exports, and explicit validation guidance—suited for supplementary materials and independent confirmation.</p>
    <a class="pillar__link" href="reproducibility/">Reproducibility →</a>
  </div>
</div>

<div class="home-video" id="overview-video">
  <div class="home-video__frame">
    <video class="home-video__player" controls preload="metadata" playsinline poster="media/fmn-mrfmn-overview-poster.jpg" title="MSmaster workflow: FMN build, export, and MR-FMN import">
      <source src="media/fmn-mrfmn-overview.mp4" type="video/mp4" />
      Your browser does not support embedded video.
      <a href="media/fmn-mrfmn-overview.mp4">Download the workflow overview (MP4)</a>.
    </video>
  </div>
  <p class="home-video__caption">Workflow overview: FMN in Molecular Networks, <strong>Export All Results</strong>, then MR-FMN import in Advanced Analysis.</p>
</div>

<figure class="home-figure">
  <img src="Figures/figure%201.png" alt="Figure 1 — MSmaster overview with FMN and MR-FMN as central outputs" loading="lazy" />
  <figcaption class="home-figure__caption">Figure 1. <strong>FMN</strong> and <strong>MR-FMN</strong> are the primary network outputs; MS/MS annotation and metabolomics analysis are auxiliary modules upstream (Modules &amp; Quick Start).</figcaption>
</figure>

<div class="trust-strip" markdown="0">
  <div class="trust-item">
    <span class="trust-item__label">License</span>
    <span class="trust-item__value"><a href="manual/section_01/">MIT</a></span>
  </div>
  <div class="trust-item">
    <span class="trust-item__label">Developed at</span>
    <span class="trust-item__value">Max Planck Institute for Chemical Ecology · KIB/CAS</span>
  </div>
  <div class="trust-item">
    <span class="trust-item__label">Reading path</span>
    <span class="trust-item__value">Install → Modules → Quick Start → FMN → MR-FMN</span>
  </div>
</div>

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

Supporting workflows—not substitutes for FMN/MR-FMN—often used for identification, feature tables, or filters before network construction.

<div class="grid cards cards--aux" markdown>
  <a href="manual/section_03/" class="card card--aux">
    <div class="card__badge card__badge--aux">Auxiliary</div>
    <div class="card__title">MS/MS spectral annotation</div>
    <div class="card__subtitle">MS Identification, AI database search, and node-level annotation linked to Molecular Networks / FMN exports.</div>
  </a>
  <a href="manual/section_03/" class="card card--aux">
    <div class="card__badge card__badge--aux">Auxiliary</div>
    <div class="card__title">Metabolomics analysis</div>
    <div class="card__subtitle">Batch metabolomics, differential/statistical outputs, and MetaboResult tables—usable in FMN metabolomics filters.</div>
  </a>
  <a href="manual/section_04/" class="card card--aux">
    <div class="card__badge card__badge--aux">Auxiliary</div>
    <div class="card__title">Quick Start (by input type)</div>
    <div class="card__subtitle">MGF-only, feature-table, or combined pipelines before the FMN chapter.</div>
  </a>
</div>

## Foundation chapters

<div class="grid cards" markdown>
  <a href="manual/section_01/" class="card">
    <div class="card__title">About MSmaster</div>
    <div class="card__subtitle">Scope, outputs, license, affiliations</div>
  </a>
  <a href="manual/section_02/" class="card">
    <div class="card__title">Install MSmaster</div>
    <div class="card__subtitle">Download v1.0.0 · setup &amp; first launch</div>
  </a>
  <a href="manual/section_03/" class="card">
    <div class="card__title">MSmaster modules</div>
    <div class="card__subtitle">Annotation, metabolomics, Molecular Networks, FMN inputs</div>
  </a>
  <a href="manual/section_04/" class="card">
    <div class="card__title">Quick Start</div>
    <div class="card__subtitle">Prepare MGF / project path before FMN</div>
  </a>
</div>

!!! warning
    Identification and network results are *computational predictions*.
    For research use, conclusions still require independent validation within your experimental system (e.g., standards, confirmatory MS/MS evidence, literature/database cross-checking, and experimental verification).

## Recommended reading order

1. [Install MSmaster](manual/section_02.md) — download, extract, first launch
2. [MSmaster modules](manual/section_03.md) — auxiliary annotation & metabolomics, plus FMN inputs
3. [Quick Start](manual/section_04.md) — inputs by data type
4. **[Fusion Molecular Networks (FMN)](manual/section_05.md)** — build and export the fusion graph
5. **[Metabolic Reaction Fusion Molecular Networks (MR-FMN)](manual/section_06.md)** — reaction analysis on exported FMN
6. [Parameters & output interpretation](parameters.md)
7. [Reproducibility & validation](reproducibility.md)
8. [FAQ & troubleshooting](faq.md)
