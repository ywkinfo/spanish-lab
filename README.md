# Spanish Lab

Spanish Lab is a small showrunner-style pipeline for producing narrated Spanish
learning videos from a source image, a B2 description script, and a project
configuration file. It renders Ken Burns-style 16:9 videos with Spanish TTS,
subtitle bars, optional background music, thumbnails, and YouTube metadata.

The flagship series is **Descripción de imagen B2**, aimed at Korean adult
Spanish learners who want repeatable image-description practice. The public
channel is available at
<https://www.youtube.com/channel/UCTA60roVDZYZGXtO61pUmWA>.

This repository intentionally tracks the code, scripts, source images, agent
prompts, and production recipes. Heavy generated artifacts under `output/` are
ignored; publish-ready videos should live on YouTube or GitHub Releases instead
of in git.

## Setup

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

FFmpeg is required. On macOS:

```sh
brew install ffmpeg
```

Narrated projects use the macOS `say` command for TTS. It is included with
macOS. Optional background music can be placed at `assets/audio/bgm.mp3`; if the
file is missing, the render falls back to narration only.

## Repository Layout

- `projects/` - per-episode project modules and metadata fields
- `build/` - render, audio, timeline, subtitle, and publish pipeline code
- `checks/` - validation, previews, QA helpers, and unit tests
- `images/` - source images used by project modules
- `2ndsc/` through `7thsc/`, `aea1/` - episode drafts, notes, and source text
- `.claude/agents/` and `.claude/skills/` - local showrunner agent surfaces
- `assets/audio/` - optional BGM assets with license evidence
- `docs/` - GitHub Pages-ready public lesson hub
- `scripts/export_github_pages.py` - generates the public lesson pages from a finished project
- `output/` - generated media and debug artifacts, intentionally ignored

## Public Lesson Export

The production repo stays the source of truth. When an episode is ready, export a static lesson page into `docs/` so GitHub Pages can serve it as the searchable learning hub.

Current pattern:

- YouTube = discovery channel
- docs/ = public lesson archive
- projects/ = canonical production source

See `GITHUB_WORKFLOW.md` for the branch-review-merge policy. Hermes may prepare and push content branches, but `main` merges require human review because `main` + `/docs` can publish publicly via GitHub Pages.

## Workflow

```sh
make check    # static segment validation
make debug    # overlay, contact sheet, subtitle previews
make test     # unit tests
make tts      # optional: generate/reuse narration clips and manifest
make preview  # fast 12 fps preview render
make render   # final 30 fps render
make publish  # render, then copy upload-ready video/meta/thumb assets
make publish-existing  # package an existing MP4 without chapters
make verify   # ffprobe validation for final MP4
make all      # check -> debug -> test -> render -> verify
```

For a specific project:

```sh
PROJECT=mercado make tts
PROJECT=mercado make render
PROJECT=mercado make publish
PROJECT=mercado make verify
```

Projects without an `AUDIO` config keep the existing silent-video workflow.

Outputs:

- `output/debug/segments_overlay.jpg`
- `output/debug/contact_sheet.jpg`
- `output/debug/subtitle_previews/seg_NN.png`
- `output/audio/tts/seg_NN_*.aiff`
- `output/audio/tts/manifest.json`
- `output/audio/narration.wav`
- `output/audio/mix.wav`
- `output/preview.mp4`
- `output/{OUTPUT_NAME}.mp4`
- `output/publish/{series}-epNN-{OUTPUT_NAME}-16x9-vN.mp4`
- `output/meta/{series}-epNN-{OUTPUT_NAME}-16x9-vN.json`
- `output/meta/{series}-epNN-{OUTPUT_NAME}-16x9-vN.md`
- `output/thumbs/{series}-epNN-{OUTPUT_NAME}.jpg`

`make publish` depends on `render` because `output/audio/tts/manifest.json`
is shared across projects and must match the project being published. Use
`make publish-existing` only when packaging an existing MP4 without chapter
timestamps.

## Background Music

Store optional BGM as `assets/audio/bgm.mp3`. Record the source URL, download
date, license name, author, and intended video usage in
`assets/audio/LICENSE.md`. This is required even for no-attribution sources so
license evidence stays with the project.

## Licenses

Pipeline code, tests, and build scripts are MIT licensed; see `LICENSE`.
Creative content is licensed under CC BY-NC-SA 4.0 unless noted otherwise; see
`LICENSE-content.md`, `images/LICENSE.md`, and `assets/audio/LICENSE.md`.

## Editing Segments

Update `segments.py` to adjust text, frames, or zoom values. A segment frame is
the final 16:9 camera view in the source-image coordinate system:

```python
{"x": 0, "y": 0, "w": 1024, "h": 576}
```

Frames must stay inside the source image, keep a 16:9 ratio within 2%, and meet
the validator's scaled minimum size. Current projects use either 1024x576 or
1280x720 source images.
