# Home page video assets

The home page (`docs/index.md`) embeds **`fmn-mrfmn-overview.mp4`** in the workflow overview section.

## Recommended clip

- **Length:** ~30–60 seconds  
- **Content:** FMN run in Molecular Networks → **Export All Results** → import project folder in Advanced Analysis → MR-FMN preview  
- **Format:** MP4 (H.264), 1280×720 or 1920×1080, keep file **under ~15 MB** for GitHub Pages  

## Files to add

| File | Purpose |
|------|---------|
| `fmn-mrfmn-overview.mp4` | Embedded demo on the home page |
| `fmn-mrfmn-poster.jpg` | Optional poster frame before play |

## Update the clip

1. Replace `fmn-mrfmn-overview.mp4` in this folder (keep the same filename, or update the `<source src="...">` in `docs/index.md`).  
2. Optional: add `fmn-mrfmn-poster.jpg` and set `poster="media/fmn-mrfmn-poster.jpg"` on the `<video>` tag.  
3. Run `python -m mkdocs serve` and confirm playback before pushing.

## Hosting large videos elsewhere

If the file is too large for the repo, host on GitHub Release or a lab server and replace the `<source src="...">` URL with the direct link. Keep the placeholder caption updated with a “Watch demo” link.
