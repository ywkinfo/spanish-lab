# Skill: Shipping a Historia Diary Episode (`historia-ship`)

This skill defines the turnkey workflow for rendering, packaging, verifying, and preparing a diary-type episode (`RENDER_TYPE = "diary"`) for publication.

## shipping Pipeline Checklist

Run the pipeline in the exact following chronological sequence:

### 1. Verification Gate
```bash
PROJECT=<module> make check
PROJECT=<module> make debug
PROJECT=<module> make test
PROJECT=<module> make lint-spanish
```
- Ensure there are **0 errors and 0 warnings**. The validator will catch silent audio files (peak ≤ -50 dBFS), duplicate placeholders, resolution mismatches, and layout anomalies.

### 2. Audio Synthesis
```bash
PROJECT=<module> make tts
```
- Generates the Edge TTS narration segments. Ensure that `STATUS` in the module docstring is updated to **approved** prior to shipping.

### 3. Preview Verification
```bash
PROJECT=<module> make preview-diary
```
- Renders a 12fps draft video to `output/preview.mp4`.
- **Linguist and Quality Review**: Manually inspect the preview file to verify that the dynamic caption panel adjusts smoothly and does not overlap with any Spanish/Korean text. Verify BGM ducking and sfx placement.

### 4. QA Pack and Verification
```bash
PROJECT=<module> make preview-qa-pack
PROJECT=<module> make preview-qa
```
- Generates frame contact sheets and overlays for validation.

### 5. Final 30fps Production Render
```bash
PROJECT=<module> make render-diary
```
- Renders the high-quality 30fps master video. This step will run the full Ken Burns pan/zoom rendering, subtitle overlays, and 3-Layer audio mixing.

### 6. Publish and Packaging
Do not run `make publish-diary` directly (which triggers a redundant duplicate render). Instead, run the publisher script on the existing output:
```bash
.venv/bin/python -m build.publish
```
- **Thumbnail Handling**:
  - If `THUMBNAIL_PATH` is specified in the project file, it must exist under the repository root, and will be copied over.
  - If `THUMBNAIL_PATH` is `None` or blank, the publisher automatically extracts the first segment (intro screen) as a basic fallback.
  - For premium publication, run the episode's thumbnail script (e.g. `python scripts/create_ep01_thumbnail.py`) beforehand, and set `THUMBNAIL_PATH` to point to it.

### 7. Technical Verification
```bash
PROJECT=<module> make verify
```
- Runs `probe_output.py` on the final mp4 inside `output/publish/` to ensure correct framerate, resolution (1920x1080), audio codecs, and normalized loudness targets (-14 LUFS).
- The output bundle is now ready for manual upload to YouTube.
