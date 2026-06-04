# Home page video assets

The home page (`docs/index.md`) includes a **video placeholder** until a workflow clip is ready.

## Recommended clip

- **Length:** ~30–60 seconds  
- **Content:** FMN run in Molecular Networks → **Export All Results** → import project folder in Advanced Analysis → MR-FMN preview  
- **Format:** MP4 (H.264), 1280×720 or 1920×1080, keep file **under ~15 MB** for GitHub Pages  

## Files to add

| File | Purpose |
|------|---------|
| `fmn-mrfmn-overview.mp4` | Embedded demo on the home page |
| `fmn-mrfmn-poster.jpg` | Optional poster frame before play |

## Enable on the home page

1. Copy `fmn-mrfmn-overview.mp4` (and optional poster) into this folder (`docs/media/`).  
2. In `docs/index.md`, inside the `home-video` block:  
   - Remove or hide the `home-video__placeholder` div  
   - Uncomment the `<video>...</video>` block  
3. Run `python -m mkdocs serve` and confirm playback locally before pushing.

## Hosting large videos elsewhere

If the file is too large for the repo, host on GitHub Release or a lab server and replace the `<source src="...">` URL with the direct link. Keep the placeholder caption updated with a “Watch demo” link.
