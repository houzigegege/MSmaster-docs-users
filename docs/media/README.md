# Video assets for the documentation site

Embedded MP4 demos use a matching **poster** JPEG (shown before play). Posters are named `<video-basename>-poster.jpg` alongside each MP4 in this folder.

## Paths in Markdown

Pages under `docs/manual/` are built to `manual/<section>/index.html`. Media lives at `docs/media/` → site root `media/`. Use **`../../media/...`** in Quick Start (`section_04`), not `../media/` (that incorrectly points to `manual/media/`).

| Video | Poster | Used on |
|------|--------|---------|
| `fmn-mrfmn-overview.mp4` | `fmn-mrfmn-overview-poster.jpg` | Home |
| `Lib-search.mp4` | `Lib-search-poster.jpg` | Quick Start |
| `AILib-Search.mp4` | `AILib-Search-poster.jpg` | Quick Start |
| `Molecular_network.mp4` | `Molecular_network-poster.jpg` | Quick Start |

## Regenerate posters from video

After replacing an MP4, regenerate its cover frame (default: 1 s into the clip):

```powershell
pip install opencv-python-headless
python scripts/extract_video_posters.py
```

Use a custom timestamp (milliseconds):

```powershell
python scripts/extract_video_posters.py --time-ms 3000
```

## Replace a poster manually

1. Export a PNG/JPG from your editor or a video player screenshot.  
2. Save as `<video-basename>-poster.jpg` in this folder (max width ~1280 px recommended).  
3. No HTML changes needed if the filename matches the pattern above.

## Update a video clip

1. Replace the `.mp4` in this folder (keep the filename, or update `<source src="...">` and `poster="..."` in `docs/index.md` or `docs/templates/section_04_quick_start.md`).  
2. Run `python scripts/extract_video_posters.py` to refresh the poster.  
3. Preview with `python -m mkdocs serve` before pushing.

## Large files

Keep each MP4 **under ~50 MB** for GitHub. Host larger files on GitHub Releases and point `src` / `poster` to the release URL if needed.
