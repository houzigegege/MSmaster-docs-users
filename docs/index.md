---
hide:
  - title
---

<section class="hero-banner hero-banner--platform">
  <div class="hero-banner__inner">
    <p class="hero-eyebrow">Academic metabolomics software</p>
    <h1 class="hero-wordmark"><span class="hero-wordmark__ms">MS</span><span class="hero-wordmark__master">master</span></h1>
    <p class="hero-tagline">
      A platform for fusion molecular networks, Metabolic reaction fusion molecular networks (MR-FMN), and traceable MS/MS evidence.
    </p>
    <p class="hero-lead">
      MSmaster integrates <strong>FMN</strong>, <strong>MR-FMN</strong>, MS/MS spectral annotation, and metabolomics analysis in a reproducible workflow for computational metabolomics research.
    </p>
    <div class="hero-actions">
      <a class="md-button md-button--primary hero-cta-primary" href="https://github.com/houzigegege/MSmaster-docs-users/releases/download/v1.0.0/MSmaster_V1.0.0.7z">Download v1.0.0</a>
      <a class="md-button" href="manual/section_05/">Explore FMN</a>
      <a class="md-button" href="manual/section_06/">Explore MR-FMN</a>
    </div>
    <div class="hero-metrics" aria-label="Platform scope">
      <div class="hero-metric">
        <span class="hero-metric__value">FMN</span>
        <span class="hero-metric__label">hierarchical molecular networks</span>
      </div>
      <div class="hero-metric">
        <span class="hero-metric__value">MR-FMN</span>
        <span class="hero-metric__label">Metabolic reaction fusion molecular networks</span>
      </div>
      <div class="hero-metric">
        <span class="hero-metric__value">MS/MS</span>
        <span class="hero-metric__label">spectral evidence and export</span>
      </div>
    </div>
  </div>
</section>

<section class="workflow-strip" aria-label="Recommended analysis workflow">
  <div class="workflow-strip__item">
    <span class="workflow-strip__step">01</span>
    <span class="workflow-strip__title">MS/MS data</span>
  </div>
  <div class="workflow-strip__arrow" aria-hidden="true">-></div>
  <div class="workflow-strip__item">
    <span class="workflow-strip__step">02</span>
    <span class="workflow-strip__title">FMN construction</span>
  </div>
  <div class="workflow-strip__arrow" aria-hidden="true">-></div>
  <div class="workflow-strip__item">
    <span class="workflow-strip__step">03</span>
    <span class="workflow-strip__title">Exported evidence</span>
  </div>
  <div class="workflow-strip__arrow" aria-hidden="true">-></div>
  <div class="workflow-strip__item">
    <span class="workflow-strip__step">04</span>
    <span class="workflow-strip__title">MR-FMN construction</span>
  </div>
</section>

## Platform Capabilities

<div class="pillars pillars--platform" markdown="0">
  <a class="pillar" href="manual/section_05/">
    <div class="pillar__icon" aria-hidden="true">F</div>
    <h3 class="pillar__title">Fusion Molecular Networks</h3>
    <p class="pillar__text">Construct hierarchical networks from cosine similarity, neutral-loss relationships, and DNN-derived edges.</p>
  </a>
  <a class="pillar" href="manual/section_06/">
    <div class="pillar__icon" aria-hidden="true">R</div>
    <h3 class="pillar__title">Metabolic Reaction Fusion Molecular Networks</h3>
    <p class="pillar__text">Run MR-FMN on exported FMN projects to construct metabolic reaction fusion molecular networks.</p>
  </a>
  <a class="pillar" href="manual/section_03/">
    <div class="pillar__icon" aria-hidden="true">A</div>
    <h3 class="pillar__title">MS/MS Annotation</h3>
    <p class="pillar__text">Use spectral matching, AI-assisted database search, and node-level annotation before network interpretation.</p>
  </a>
  <a class="pillar" href="reproducibility/">
    <div class="pillar__icon" aria-hidden="true">E</div>
    <h3 class="pillar__title">Exportable Evidence</h3>
    <p class="pillar__text">Document parameters, preserve analysis outputs, and prepare results for review, reuse, and validation.</p>
  </a>
</div>

## Workflow Overview

<div class="home-video" id="overview-video">
  <div class="home-video__frame">
    <video class="home-video__player" controls preload="metadata" playsinline poster="media/fmn-mrfmn-overview-poster.jpg" title="MSmaster workflow: FMN build, export, and MR-FMN import">
      <source src="media/fmn-mrfmn-overview.mp4" type="video/mp4" />
      Your browser does not support embedded video.
      <a href="media/fmn-mrfmn-overview.mp4">Download the workflow overview (MP4)</a>.
    </video>
  </div>
  <p class="home-video__caption">Recommended sequence: build FMN in Molecular Networks, export all results, then import the project folder for Metabolic reaction fusion molecular networks (MR-FMN).</p>
</div>

<figure class="home-figure">
  <img src="Figures/figure%201.png" alt="MSmaster overview with FMN and MR-FMN as central outputs" loading="lazy" />
  <figcaption class="home-figure__caption">FMN and MR-FMN are the primary network outputs; MS/MS annotation and metabolomics analysis provide supporting evidence upstream.</figcaption>
</figure>

## Documentation

<div class="grid cards cards--core" markdown>
  <a href="manual/section_05/" class="card card--featured">
    <div class="card__badge">Core workflow</div>
    <div class="card__title">FMN Analysis</div>
    <div class="card__subtitle">Configure hierarchical fusion, construct molecular networks, and export reproducible network evidence.</div>
  </a>
  <a href="manual/section_06/" class="card card--featured">
    <div class="card__badge">Core workflow</div>
    <div class="card__title">Metabolic reaction fusion molecular networks (MR-FMN)</div>
    <div class="card__subtitle">Import FMN outputs, apply reaction rules, inspect predictions, and export MR-FMN results.</div>
  </a>
</div>

<div class="grid cards cards--aux" markdown>
  <a href="manual/section_01/" class="card card--aux">
    <div class="card__badge card__badge--aux">Platform</div>
    <div class="card__title">Scope and License</div>
    <div class="card__subtitle">Scientific scope, software license, and institutional context.</div>
  </a>
  <a href="manual/section_02/" class="card card--aux">
    <div class="card__badge card__badge--aux">Release</div>
    <div class="card__title">Download and Installation</div>
    <div class="card__subtitle">Windows requirements, release archive, extraction, and first launch.</div>
  </a>
  <a href="manual/section_03/" class="card card--aux">
    <div class="card__badge card__badge--aux">Methods</div>
    <div class="card__title">Platform Capabilities</div>
    <div class="card__subtitle">Annotation, metabolomics analysis, molecular networks, and FMN inputs.</div>
  </a>
  <a href="manual/section_04/" class="card card--aux">
    <div class="card__badge card__badge--aux">Protocol</div>
    <div class="card__title">Workflow Selection</div>
    <div class="card__subtitle">Choose an analysis route based on MGF files, feature tables, or combined inputs.</div>
  </a>
</div>

<section class="trust-strip trust-strip--academic" aria-label="Research context">
  <div class="trust-item">
    <span class="trust-item__label">License</span>
    <span class="trust-item__value"><a href="manual/section_01/">MIT</a></span>
  </div>
  <div class="trust-item">
    <span class="trust-item__label">Research Context</span>
    <span class="trust-item__value">Computational metabolomics and molecular network analysis</span>
  </div>
  <div class="trust-item">
    <span class="trust-item__label">Developed at</span>
    <span class="trust-item__value">Max Planck Institute for Chemical Ecology / KIB, CAS</span>
  </div>
</section>

!!! warning "Research-use interpretation"
    Identification and network results are computational predictions. Scientific conclusions should be supported by independent validation, such as authentic standards, confirmatory MS/MS evidence, literature or database cross-checking, and experimental verification.
