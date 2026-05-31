# Voice-only rerender precedent: Ep.1 50 útiles

Use this as a compact precedent when Peter asks to replace only an awkward voice in an already published Spanish Lab card episode.

## Scenario
- Published YouTube video: Ep.1 `50 frases útiles`, project `projects/frases_a1_50_utiles.py`.
- User asked whether the voice could be replaced while preserving the rest of the video.
- Goal was a local reviewable replacement bundle only; no external upload/posting.

## Durable workflow
1. Locate the canonical project by YouTube URL or title text, not by guessing the module name:
   - search for the YouTube ID in the repo;
   - inspect `projects/<module>.py` for `YOUTUBE_URL`, `OUTPUT_NAME`, `EPISODE`, and `RENDER_VERSION`.
2. Keep script/visual content unchanged unless the user asks otherwise.
3. For Linux/Hermes rerendering, switch legacy macOS voices/fonts to portable equivalents as needed:
   - `DESIGN["font_path"] = "assets/fonts/NotoSansKR-Bold.ttf"`
   - `DESIGN["font_path_ko"] = "assets/fonts/NotoSansKR-Regular.ttf"`
   - `AUDIO["tts_engine"] = "edge"`
   - `AUDIO["voice"] = AUDIO["edge_voice"] = "es-ES-ElviraNeural"`
4. Bump `RENDER_VERSION` for a new reviewable artifact instead of overwriting the published-version bundle.
5. Run `make tts` before `make check`; Edge TTS may be longer than the old voice.
6. If TTS fit fails but the user asked for voice-only replacement, prefer minimal audio timing adjustments over script edits:
   - first try a modest `edge_rate` increase;
   - then shorten `repeat_pause_s` slightly if phrase cards still overlap;
   - avoid changing Spanish/Korean copy unless necessary.
7. Long card rerenders can exceed a single foreground command timeout. Start `make publish-cards && make verify` as a background process and poll until completion rather than restarting partial renders.
8. Generate a contact sheet from the versioned publish MP4 and visually QA Korean/Hangul, Spanish readability, clipping, and overlap.
9. Handoff should state: voice changed, script/visuals unchanged, validation passed, no external publishing performed, and exact asset paths.

## Ep.1 concrete knobs that worked
- `RENDER_VERSION = 6`
- `edge_voice = "es-ES-ElviraNeural"`
- `edge_rate = "+12%"`
- `rate_wpm = 160`
- phrase `repeat_pause_s = 2.0` instead of `2.5`
- final duration remained `629.0s`

## Validation commands used
```sh
PROJECT=frases_a1_50_utiles PYTHON=.venv/bin/python make test
PROJECT=frases_a1_50_utiles PYTHON=.venv/bin/python make tts
PROJECT=frases_a1_50_utiles PYTHON=.venv/bin/python make check
PROJECT=frases_a1_50_utiles PYTHON=.venv/bin/python make publish-cards
PROJECT=frases_a1_50_utiles PYTHON=.venv/bin/python make verify
PROJECT=frases_a1_50_utiles PYTHON=.venv/bin/python .venv/bin/python checks/probe_output.py output/publish/frases-a1-ep01-50-utiles-16x9-v6.mp4
```
