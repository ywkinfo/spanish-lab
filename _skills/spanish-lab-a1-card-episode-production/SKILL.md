---
name: spanish-lab-a1-card-episode-production
description: Produce short Spanish Lab A1 card-based lesson episodes in the spanish-lab repo, including project module setup, validation, preview rendering, Hangul font handling, and Linux/Hermes environment pitfalls.
---

# Spanish Lab A1 Card Episode Production

Use this skill when creating or extending a short A1 card-based Spanish Lab episode in the `ywkinfo/spanish-lab` repo.

## When to use
- The user says to start producing a new Spanish Lab A1 episode.
- The target format is card/slide-based, not B2 Ken Burns image description.
- The episode uses `RENDER_TYPE = "cards"` and structured `PHRASES`, `BLOCKS`, and `SEGMENTS`.
- The work happens in this Hermes/Linux environment.

## Repo and environment setup
1. Work in the Spanish Lab repo, usually `/opt/data/repos/spanish-lab`.
2. If the repo is missing, clone it using the deploy-key workflow recorded in memory.
3. Python environment pitfall:
   - System Python may lack `pip` and `ensurepip`.
   - Use uv instead:
     ```sh
     uv venv .venv
     uv pip install --python .venv/bin/python -r requirements.txt
     ```
   - If a broken `.venv` exists from `python3 -m venv`, remove and recreate it.
4. Use the project prefix explicitly:
   ```sh
   PROJECT=<module_name> PYTHON=.venv/bin/python make check
   PROJECT=<module_name> PYTHON=.venv/bin/python make test
   ```

## Episode module contract
Create `projects/<module_name>.py` with at least:
- `IMAGE_PATH = ""`
- `DESCRIP_PATH = "<episode-source-dir>/descrip.md"`
- `OUTPUT_NAME`
- `PUBLIC_SLUG`
- `YOUTUBE_URL` (blank until upload if needed)
- `SERIES = "frases-a1"`
- `SERIES_TITLE = "Español A1 -- Frases útiles"`
- `EPISODE`
- `LEVEL = "A1"`
- `LANGUAGE = "es"`
- `RENDER_VERSION`
- `RENDER_TYPE = "cards"`
- `YOUTUBE_TITLE`, `DESCRIPTION_INTRO`, `DESCRIPTION_OUTRO`, `KOREAN_TEASER`
- `BASE_TAGS`, `EXTRA_TAGS`, `BASE_HASHTAGS`, `EXTRA_HASHTAGS`
- `PHRASES`, `BLOCKS`, `CHAPTERS`, `DESIGN`, `SEGMENTS`, `AUDIO`

Also create a pipe-delimited source file. For phrase-card projects, use:
```text
1 | ¿Cómo estás? | 어떻게 지내? | Hola, Peter. ¿Cómo estás?
```
For dialogue/story-card projects, `checks/validate_cards.py` still expects exactly four pipe columns, but the fourth column can be the speaker/label. Do not add Markdown headings or blank explanatory prose to `descrip.md`; non-empty non-pipe lines fail validation. Use rows like:
```text
1 | Mira la imagen, Peter. | Peter, 그림을 봐. | Diego
2 | Veo a Lucía. | 루시아가 보여. | Peter
```

## Good A1 card design defaults
- Keep short episodes around 10 core phrases when making a focused micro-lesson.
- If the user asks to see the “전체 원고” or full manuscript before production, provide the complete intro/block/dialogue/outro script first and do not create project files until they explicitly approve proceeding. For story-card episodes, include a pipe-delimited `descrip.md`-ready draft so approval can transition directly into implementation.
- When an approved story script is slightly too long (e.g. 33 lines for a 4–5 minute A1 episode), reduce to about 30 dialogue lines by removing redundant confirmation/repetition lines rather than cutting core learning functions.
- When the user asks to match the longer “previous video” level (4+ minutes), expand a story-card episode toward the established longer pattern rather than treating it as a Shorts/micro-lesson:
  - about 4 learning-function blocks,
  - roughly 30 dialogue lines,
  - dialogue durations around 8-9.5s plus 12s intro/outro,
  - target total duration around 4-5 minutes,
  - 5-6 YouTube chapters spaced well over the 10s chapter minimum.
- For full A1 story-card episodes, keep the sequence clear: the intro slide should end first, then include about a 3-second non-dialogue breathing/transition slide before the first body dialogue slide. A practical implementation is the first `block_header` segment immediately after `intro` with `duration_s: 3.0`, so the first `dialogue` segment starts at intro duration + 3s.
- For intro/first slides, use generous line spacing when there is available whitespace. Peter flagged Ep.16's first slide as having lines too tightly stacked despite ample blank space; do not revise Ep.16, but for future episodes ensure title/subtitle/body line spacing is visually relaxed rather than compressed. Peter later clarified on Ep.23 that the right-side top three divisions — main title, level/episode subtitle, and intro/body sentence — should be visually distinct with generous separation. Contact sheets can hide intro-title/body collisions; for long or wrapped intro titles, extracted user examples, or any first-slide typography concern, extract and inspect the full-size first frame. If spacing is tight, shorten the intro display title to the core learning point, make the intro sentence compact, or reduce project-level `DESIGN["font_size_title"]` so the title fits cleanly; then bump `RENDER_VERSION`, rerender, and verify both the full-size intro frame and contact sheet before handoff. Ep.26 used this lighter project-level fix (`font_size_title` 64 → 58) to make `Estoy en la estación` one clean line without renderer changes; see `references/ep26-estoy-en-la-estacion-production.md`.
- Do not turn a daily-candidate Shorts package into a standalone plain phrase-card video by default. Peter rejected the Ep.13 `Quiero + 명사` product because it did not match the existing Spanish Lab style. Before “영상제작 진행” for a daily candidate, first align it to the established channel style: usually an A1 story/scene episode with recurring characters (Jin/Lucía/Diego), Ep.7-style thumbnail direction, and the current visual grammar. If the intent is truly a short/simple card experiment, make that style deviation explicit and get approval before rendering.
- If a daily candidate includes regional vocabulary, keep exactly one learning point and put the Spain/Latin America variant as a small vocabulary note, e.g. `Spain: Quiero un billete.` / `Latin America: Quiero un boleto.` rather than introducing a second grammar point.
- Avoid the Ep.11 intro-overlap failure mode: after TTS generation, every segment's synthesized audio plus `lead_padding_s` must fit inside that segment's `duration_s`. This matters for intro/outro/block/dialogue, not only phrase cards. The repo now has `assert_tts_fits_timeline(...)` in `build/audio.py`, called by `make tts`, `render_cards`, and narration composition; `checks/validate_cards.py` also validates all segment types against the current manifest. If a new episode fails with “TTS overlaps following segment(s)”, shorten the narration or lengthen that segment before rendering/publishing. For full A1 story-card episodes, `3.5s` block headers may be safer than `3.0s` when Edge TTS reads titles like `Hace frío / calor`; verify with `make tts` before rendering.
- For image-based A1 episodes, keep the generated image as the intro visual anchor, then structure the longer lesson as: observe the image → name visible objects with `hay` → describe actions with `estar + gerundio` → 3-person mini-dialogue → learner recap.
- For A1 teaching cards, keep Spanish-facing narration/display fields (`text_es`, intro/outro Spanish text, title fields) Spanish-only. Do not put Korean explanation inside `text_es` to explain literal meanings; it renders as mixed-language Spanish display text and looks unpolished. Put literal/natural Korean explanations in `text_ko` or metadata instead. Example: use `text_es="Hace frío habla del tiempo."` with `text_ko="Hace frío는 ‘날씨가 추워요’라는 뜻이에요."`, not `text_es="Hace frío significa: 날씨가 추워요."`. Before final handoff, run a quick Hangul scan over Spanish-facing segment fields (`text_es`, `title_es`) and require an empty result; see `references/ep30-tiene-otro-color-production.md` for the exact command and v1→v2 rerender precedent.
- Build blocks around learning functions, not grammar labels.
- Include simple Korean translations and one Spanish example per card.
- Keep the story context light: Peter, Lucía, and Diego can appear in examples/teasers, but the card format should stay focused.

## Card renderer customization
If the card renderer still has hard-coded text from an older episode (for example `50 frases útiles`), generalize it through `DESIGN` keys instead of hard-coding a new title:
- `intro_title`
- `intro_subtitle`
- `intro_ko`
- `thumbnail_title`
- `thumbnail_subtitle`
- `thumbnail_ko`
- `outro_ko`

Use those in `build/render_cards.py` so future episodes can reuse the renderer.

### Character portrait support for story-card episodes
For A1 story episodes using recurring characters, set canonical paths in the project:
```python
CHARACTERS = {
    "Peter": "assets/characters/peter-profile.png",
    "Lucía": "assets/characters/lucia-profile.png",
    "Diego": "assets/characters/diego-profile.png",
}
DESIGN = {
    ...,
    "character_images": CHARACTERS,
    "show_character_portraits": True,
}
```
Then add `"character": "Peter"` / `"Lucía"` / `"Diego"` to phrase segments and `"characters": ["Peter", "Lucía", "Diego"]` to intro/outro segments.

A proven minimal renderer extension in `build/render_cards.py`:
- add helpers to load/crop portraits into circular frames from `DESIGN["character_images"]`
- intro/outro: draw a 3-character lineup between title and narration text
- phrase cards: when `segment["character"]` exists, reserve the right side for a circular portrait and draw text in a left-side centered text box
- thumbnail: optionally include the three-character lineup above the title

Keep the layout conservative: text box about 70px to 70% width, portrait center around `(1045, 305)`, portrait size around `190`, and keep the repeat pill centered under the text box. After patching, run `py_compile`, `make check`, `make test`, render/publish, extract QA frames, and inspect a contact sheet.

## Validator pitfall: old 50-phrase assumption
Older `checks/validate_cards.py` expected exactly 50 phrases and 8-10 block headers. For focused short A1 episodes, validation should instead:
- parse `DESCRIP_PATH`
- compare phrase numbers in `SEGMENTS` with the phrase numbers from the descrip file
- allow a smaller block count, e.g. 1-10 headers

This preserves validation without forcing every card episode to be a 50-phrase video.

## Character asset intake from Telegram ZIP
When Peter sends character portrait PNGs through Telegram, direct `.png` document uploads may fail with `Unsupported document type '.png'`; ask him to send a `.zip` instead. After receiving a ZIP such as `main-character-assets.zip`:
1. Inspect contents using Python `zipfile` because `unzip` may be unavailable in Hermes/Linux:
   ```sh
   python3 - <<'PY'
   import zipfile
   z = '/opt/data/cache/documents/<file>.zip'
   with zipfile.ZipFile(z) as f:
       for info in f.infolist():
           print(f'{info.file_size:>10}  {info.filename}')
   PY
   ```
2. Extract to a temp folder with `zipfile.extractall`, then copy canonical files into:
   ```text
   assets/characters/peter-profile.png
   assets/characters/lucia-profile.png
   assets/characters/diego-profile.png
   assets/characters/LICENSE.md
   ```
3. Use `.venv/bin/python` + Pillow to verify image dimensions/modes. In the first imported set, all three portraits were `1254x1254 RGB`.
4. Create a quick contact sheet for visual QA and deliver it back to Peter:
   ```text
   assets/characters/character-contact-sheet.jpg
   ```
5. Verify the contact sheet with `vision_analyze` to confirm three distinct labeled portraits and no obvious rendering problems.
6. Report `git status --short -- assets/characters`; do not imply commit/push unless actually done.

Known canonical recurring characters for A1 story cards:
- Jin: Korean learner / audience proxy from Ep.8 onward. If legacy assets or older modules still say `Peter`, treat that as the same learner persona and rename visible dialogue/script references to Jin for new episodes.
- Lucía: Spanish café/story protagonist.
- Diego: guide/teacher persona.
- Existing portrait assets may still use legacy filenames such as `assets/characters/peter-profile.png`; do not rename asset files unless intentionally migrating the repo, but use the display name `Jin` in new user-facing Spanish/Korean copy.


## Hangul font pitfall
On Linux, default fallback fonts may not render Korean/Hangul correctly; the preview may show square tofu glyphs.

Fix:
1. Add Korean-capable fonts under `assets/fonts/`, for example Noto Sans KR Regular/Bold.
2. Add `assets/fonts/LICENSE.md` with source, download date, license, and intended use.
3. Set project design fonts to repo-relative paths:
   ```python
   "font_path": "assets/fonts/NotoSansKR-Bold.ttf",
   "font_path_ko": "assets/fonts/NotoSansKR-Regular.ttf",
   ```
4. Verify a frame visually with `vision_analyze`.

## Spanish TTS on Hermes/Linux
The old card preview/final render path can fail if `AUDIO` is configured because it calls macOS `say`, which is absent on Linux:
```text
FileNotFoundError: [Errno 2] No such file or directory: 'say'
```

For final Spanish Lab channel quality, prefer a real Spanish neural TTS over the robotic Linux fallback. A proven option in Hermes/Linux is `edge-tts`:
1. Add dependency:
   ```txt
   edge-tts>=7,<8
   ```
2. Install with uv:
   ```sh
   uv pip install --python .venv/bin/python -r requirements.txt
   ```
3. In `build/audio.py`, support a `tts_engine="edge"` branch in `build_tts_command(...)` using:
   ```python
   [sys.executable, "-m", "edge_tts", "--voice", voice, "--text", text,
    "--write-media", str(out_path), "--rate=<value>", "--pitch=<value>", "--volume=<value>"]
   ```
   Use combined option forms like `--rate=-8%` rather than splitting `--rate`, `-8%`.
4. Use `.mp3` for Edge TTS segment outputs, `.aiff` for `say`, and `.wav` for `flite`.
5. Recommended Spain-Spanish A1 voice config:
   ```python
   "tts_engine": "edge",
   "voice": "es-ES-ElviraNeural",
   "edge_voice": "es-ES-ElviraNeural",
   "edge_rate": "-8%",
   "edge_pitch": "+0Hz",
   "edge_volume": "+0%",
   ```
6. For multi-character conversation episodes, add per-speaker voice routing in `AUDIO`. For new A1 story episodes from Ep.8 onward, use the display name `Jin` for the Korean learner even if the legacy portrait file is still named `peter-profile.png`:
   ```python
   "character_voices": {
       "Lucía": "es-ES-ElviraNeural",
       "Jin": "es-ES-AlvaroNeural",
       "Diego": "es-MX-JorgeNeural",
   }
   ```
   Legacy projects may still contain `Peter`; do not rename old episodes unless doing an intentional migration. For new episodes, make all hash validators use the resolved per-segment voice, not the global default voice. Patch `build/audio.py` with `voice_for_segment(...)` / `audio_cfg_for_segment(...)`, and import `voice_for_segment` anywhere hashes are recomputed (`checks/validate_cards.py`, `build/publish.py`). Otherwise final render can succeed but `build.publish` fails with `audio manifest text hashes do not match current project` because the manifest hash includes each speaker's voice while publish expects one global voice.
7. Edge Spanish narration can be longer than robotic fallback. If validation fails because TTS exceeds segment duration, lengthen phrase-card segments and/or shorten repeat pauses. For a 10-phrase A1 micro-lesson, `duration_s=12.0` and `repeat_pause_s=1.0` worked well.

Keep `flite` only as a functional fallback. First add unit tests in `checks/test_units.py` for `build_tts_command(...)` that verify:
- `tts_engine="edge"` uses `sys.executable -m edge_tts`, the Spanish neural voice, `--write-media`, and combined `--rate=...`
- `tts_engine="flite"` returns an `ffmpeg` command
- the flite command uses `flite=textfile=<path>:voice=<voice>` rather than raw inline text
- the output path is the final command argument

Then implement:
- `tts_engine = "auto"`: use Edge if importable, else `say` when available, otherwise `flite`
- write each narration string to `seg_NN_<hash>.txt`
- keep `probe_duration`, manifest writing, `build_narration_wav`, and muxing consistent

### Spanish Lab brand BGM / sound identity
The user wants Spanish Lab to establish a consistent background-music/sound identity and reuse it continuously across episodes. Treat BGM as a brand asset, not a one-off per episode.

Recommended A1 brand direction:
- warm, clean cafe/study atmosphere;
- soft nylon-guitar or electric-piano arpeggios, minimal shaker/percussion, discreet bass/pad;
- relaxed 80-95 BPM;
- clean beat with minimal noise/rough texture; avoid noisy claps, white-noise percussion, or gritty artifacts unless explicitly requested;
- no vocals and no attention-grabbing melody that competes with Spanish narration;
- final mix under narration around `bgm_volume_db = -22.0` to `-18.0` for normally mastered music, lowering toward `-24.0` if intelligibility suffers. If the source BGM is itself very quiet (for example a draft with mean volume around `-30 dB`), a higher setting such as `bgm_volume_db = -4.0` with ducking can still produce a subtle under-narration mix; verify with `make verify` and listening/manual checks instead of relying only on the config number.

Before adopting a track, run a quick capability/asset check from the repo root:
```sh
command -v ffmpeg && command -v ffprobe
find assets/audio -maxdepth 1 -type f \( -iname '*.mp3' -o -iname '*.wav' -o -iname '*.ogg' \) -print
.venv/bin/python - <<'PY'
import importlib.util
for m in ['torch','audiocraft','musicgen','numpy','soundfile']:
    print(f'{m}: {bool(importlib.util.find_spec(m))}')
PY
```
Do not conclude that AI music is impossible just because local packages/GPU are absent; that only means local AI generation is not ready in the current environment. For a copyright-clean draft or taste probe, use the packaged deterministic procedural fallback:
```sh
.venv/bin/python /opt/data/skills/media/spanish-lab-a1-card-episode-production/scripts/generate_spanish_lab_bgm_draft.py \
  --out assets/audio/spanish-lab-brand-bgm-draft-20s.wav
ffmpeg -y -i assets/audio/spanish-lab-brand-bgm-draft-20s.wav \
  -codec:a libmp3lame -b:a 192k assets/audio/spanish-lab-brand-bgm-draft-20s.mp3
ffmpeg -hide_banner -nostats -i assets/audio/spanish-lab-brand-bgm-draft-20s.mp3 \
  -af volumedetect -f null - 2>&1 | tail -20
```
Use the draft only for approval unless the user explicitly accepts it as the brand track. Once chosen, store the canonical asset as:
```text
assets/audio/spanish-lab-brand-bgm.mp3
```
and set episodes to:
```python
"bgm_path": "assets/audio/spanish-lab-brand-bgm.mp3",
"bgm_volume_db": -22.0,
"ducking": False,
```
If the source asset is an intentionally quiet procedural draft, start from the measured loudness rather than the nominal setting. For an asset around `mean_volume=-30 dB`, a practical episode setting is:
```python
"bgm_path": "assets/audio/spanish-lab-brand-bgm.mp3",
"bgm_volume_db": -4.0,
"narration_volume_db": 0.0,
"ducking": True,
"ducking_threshold": 0.04,
"ducking_ratio": 6,
"ducking_attack_ms": 80,
"ducking_release_ms": 450,
"fade_in_s": 0.0,
"fade_out_s": 2.0,
```
If the BGM competes with narration, lower volume first; enable or strengthen ducking only if needed. After applying a canonical BGM to an existing episode, remove stale `output/<slug>.mp4`, `output/<slug>-silent.mp4`, and versioned publish/meta artifacts (or bump `RENDER_VERSION`) before rerendering, then run `make check`, `make test`, `make lint-spanish`, `make preview-cards`, `make publish-cards`, and `make verify`.

### Voice-only replacement for an already published card episode
When Peter flags awkward narration in an existing/published Spanish Lab video and asks to replace only the voice, treat it as a **voice-only local rerender**, not a new content-production cycle:
1. Locate the canonical project by searching the YouTube URL/video ID or title in the repo.
2. Keep the script, Spanish/Korean copy, visuals, thumbnail direction, and metadata unchanged unless Peter explicitly asks for edits.
3. Bump `RENDER_VERSION` to produce a new reviewable bundle rather than overwriting old artifacts.
4. Swap only portable voice/font/audio settings needed for the current render environment, then run `make tts` before `make check`.
5. If Edge TTS is longer than the original voice, make minimal timing-only changes first: modest `edge_rate` increase and/or slightly shorter `repeat_pause_s`; avoid rewriting copy for a voice-only request.
6. Long full-episode rerenders can exceed foreground tool timeouts. Run `make publish-cards && make verify` in the background and poll to completion instead of restarting partial renders.
7. Generate a contact sheet from the versioned publish MP4, visually check Spanish/Korean readability and Hangul rendering, and hand off the MP4 plus QA sheet. State explicitly that no external publishing was performed.

See `references/voice-only-rerender-ep01.md` for the Ep.1 `50 frases útiles` precedent and concrete settings.

### Duration verification pitfall with BGM
If `make verify` fails with final video/audio around 0.5–1.0s shorter than the expected segment sum, probe intermediate files:
```sh
ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 output/audio/narration.wav
ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 output/audio/mix.wav
ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 output/<slug>.mp4
```
In one Ep.3 case, `narration.wav` was exactly 157.0s but `mix.wav`/final MP4 were 156.16s due to BGM/mixing behavior. A voice-only workaround is to set:
```python
"bgm_path": None,
```
and rerun publish/verify.

If the user explicitly wants BGM, keep the music and fix the mix duration instead. In `build/audio.py`, after the BGM/narration `amix=inputs=2:duration=first:dropout_transition=0`, force the mixed audio to the expected segment sum before resampling in both ducked and non-ducked branches:
```python
f"[ducked][nar2]amix=inputs=2:duration=first:dropout_transition=0,"
f"apad,atrim=0:{total_duration_s:.6f},aresample={sample_rate}[mix]"
```
```python
f"[bgm][nar]amix=inputs=2:duration=first:dropout_transition=0,"
f"apad,atrim=0:{total_duration_s:.6f},aresample={sample_rate}[mix]"
```
Then remove any failed versioned publish artifacts before rerendering, or bump `RENDER_VERSION`, because `make publish-cards` refuses to overwrite existing outputs. Re-run:
```sh
PROJECT=<module> PYTHON=.venv/bin/python make test
PROJECT=<module> PYTHON=.venv/bin/python make check
PROJECT=<module> PYTHON=.venv/bin/python make publish-cards
PROJECT=<module> PYTHON=.venv/bin/python make verify
```
This fixed an Ep.3 BGM render where verify failed at 156.409s vs expected 157.000s; after `apad,atrim`, verify reported video/audio duration exactly 157.0s.

Useful commands after implementation:
```sh
PROJECT=<module> PYTHON=.venv/bin/python make test
PROJECT=<module> PYTHON=.venv/bin/python make tts
PROJECT=<module> PYTHON=.venv/bin/python make check
PROJECT=<module> PYTHON=.venv/bin/python make preview-cards
PROJECT=<module> PYTHON=.venv/bin/python make publish-cards
PROJECT=<module> PYTHON=.venv/bin/python make verify
```

`make verify` should report AAC audio, 44100 Hz, audio duration close to video duration, and `ok: true`. Note that flite is a functional fallback but sounds robotic; for final channel quality, Monica/say or a higher-quality Spanish TTS may still be preferred.

## Preview rendering in Hermes/Linux
If TTS fallback has not been implemented yet, render a silent preview directly for visual QA:
```sh
PROJECT=<module> PYTHON=.venv/bin/python make check
.venv/bin/python - <<'PY'
from pathlib import Path
from build.render_cards import build_card_video_clip
from build.card_timeline import build_card_timings
from projects import <module> as p
Path('output').mkdir(exist_ok=True)
timings = build_card_timings(p.SEGMENTS, design=p.DESIGN, tts_durations=None, audio_cfg={})
clip = build_card_video_clip(p.SEGMENTS, p.DESIGN, timings)
clip.write_videofile(
    'output/<slug>-preview-silent.mp4',
    codec='libx264', audio=False, fps=12, preset='ultrafast',
    ffmpeg_params=['-pix_fmt', 'yuv420p', '-movflags', '+faststart', '-crf', '26'],
)
clip.close()
print('done')
PY
```

Then extract frames for QA:
```sh
mkdir -p output/qa/<slug>
ffmpeg -y -loglevel error -ss 00:00:30 -i output/<slug>-preview-silent.mp4 -frames:v 1 output/qa/<slug>/frame-030.png
```

Use `vision_analyze` to check:
- Spanish readability
- Korean/Hangul rendering
- clipping or overlap
- button spacing and visual hierarchy

### Per-slide vocabulary object cards
For A1 episodes where Peter asks to show a concrete object on each slide (for example clothing in Ep.17), keep the grammar/learning point singular and use object images as visual vocabulary support only. A proven approach is:
- create simple local PNG assets under `assets/generated/<topic>/` (e.g. `assets/generated/clothing/chaqueta.png`, `abrigo.png`, `camiseta.png`, `zapatos.png`, `gafas.png`, `paraguas.png`);
- add a project-level mapping such as `CLOTHING_IMAGES` and expose it in `DESIGN["clothing_images"]`;
- add `"clothing_items": [...]` to intro, block headers, dialogue, and outro segments;
- renderer support should draw small rounded white object cards in the unused right/bottom area so they do not cover Spanish/Korean text, focus pills, or character portraits;
- validate with a contact sheet that the object cards are visible, labels do not clip, and the visual objects remain vocabulary aids rather than a second lesson.

### Slide-only correction workflow
When the user flags a specific slide/visual issue and explicitly says not to touch the video, do not rerender the episode or publish artifacts yet. Create a standalone still preview under `output/qa/<slug>/` and deliver only that image. Common fixes:
- Intro slide image crop: if the `intro_scene_image_path` panel crops a character, compose the left panel with a blurred cover background plus a contain-fit foreground image so the full body remains visible.
- Intro/title clipping: if a title reaches the right edge, measure/wrap with `ImageDraw.textbbox` and keep a safe right margin so final glyphs are not clipped.
- Character portrait cleanup: if a circular portrait is cluttered by table/card/coffee elements, make a separate centered portrait asset from the source image (for example `assets/generated/<slug>-lucia-centered-portrait.png`) and a circular QA preview under `output/qa/<slug>/`; show the candidate first before changing project `CHARACTERS` or rerendering.
- Outro overlap: long outro Spanish text can collide with the Korean outro line, especially when the last Spanish word wraps near the bottom. For a still-only fix, reduce/wrap the Spanish body to fewer lines, move it upward, or lower the font size; verify there is clear vertical separation above the Korean line.
- Verify the still with visual inspection/`vision_analyze`, then state clearly that the video was not changed. See `references/intro-slide-only-preview.md` and `references/slide-only-portrait-and-outro-fixes.md`.

### Remaking an existing Spanish Lab video from a YouTube URL
When Peter asks to remake/recreate one of our existing YouTube videos and gives only a watch URL:
1. Do not rely on transcript extraction alone; cloud IPs may be blocked by YouTube.
2. Use YouTube oEmbed to identify the canonical title/channel/thumbnail if normal watch/transcript access fails:
   ```sh
   python3 - <<'PY'
   import urllib.request
   video_id='VIDEO_ID'
   url=f'https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={video_id}&format=json'
   print(urllib.request.urlopen(url, timeout=20).read().decode())
   PY
   ```
3. Search the `spanish-lab` repo by video ID and title before drafting improvements:
   ```sh
   grep -R "VIDEO_ID\|KEY_TITLE_WORDS" -n projects docs episodes 2>/dev/null
   ```
4. Use the canonical project module/docs page to find the old CEFR, phrases, metadata, and lesson structure.
5. For an improvement plan, first diagnose against current channel conventions: one learning point, Jin/Lucía/Diego continuity, A1/A2 level fit, Ep.7-style thumbnail direction, literal+natural Korean explanations, shadowing, mini quiz, and no external publishing.
6. If the old episode contains multiple A1 functions, propose narrowing the remake to exactly one learning point and moving other functions to future episodes rather than recreating the same broad phrase list.

## Verification checklist before handoff
- `python3 -m py_compile projects/<module>.py`
- Import module and assert expected counts:
  - title
  - number of phrases
  - number of blocks
  - number of segments
  - chapters point to valid segments
- `PROJECT=<module> PYTHON=.venv/bin/python make check`
- `PROJECT=<module> PYTHON=.venv/bin/python make test`
- `PROJECT=<module> PYTHON=.venv/bin/python make lint-spanish`
- `PROJECT=<module> PYTHON=.venv/bin/python make publish-cards`
- `PROJECT=<module> PYTHON=.venv/bin/python make verify`
- If probing a versioned publish artifact directly, also set `PROJECT=<module>`; otherwise `checks/probe_output.py` may compare the video against a default project size/duration and produce a false failure. Example:
  ```sh
  PROJECT=<module> PYTHON=.venv/bin/python .venv/bin/python checks/probe_output.py output/publish/frases-a1-epNN-<slug>-16x9-vN.mp4
  ```
- If contact-sheet visual QA catches a script/copy problem after render, patch both `projects/<module>.py` and `descrip.md`, delete stale output/publish/meta artifacts or bump `RENDER_VERSION`, rerun TTS/check/publish/verify, and regenerate the contact sheet before handoff.
- YouTube chapter validation in `build.publish` requires at least three timestamps, and every chapter span must be at least 10 seconds, including the final chapter span from its timestamp to the end of the video. Do not place the last chapter on the final/outro segment if the outro is shorter than 10s; choose three earlier segment starts whose gaps and final tail are all >=10s, or lengthen/merge segments before publishing.
- If publish fails after rendering because of chapter validation or an existing versioned artifact, fix `CHAPTERS`, remove the failed/stale `output/publish/frases-a1-epNN-<slug>-16x9-vN.*` artifacts or bump `RENDER_VERSION`, then rerun `make publish-cards` and `make verify`.
- If publish emits `decision log not found: ... Publish will continue without a decision snapshot`, treat it as a warning rather than a render blocker unless the user explicitly needs decision-log archiving.
- Silent preview renders if audio/TTS is unavailable
- QA frame/contact sheet confirms Korean is visible, not tofu boxes
- For a quick final visual QA contact sheet from the published video, use representative frame numbers instead of relying only on one frame. Ensure the final selected frame actually lands in the outro/recap for that video's duration; for ~4-5 minute A1 episodes at 30fps, a late frame such as `eq(n,8520)` may be needed, while older shorter examples using `eq(n,3930)` can miss the outro. Also extract a full-size intro frame whenever the intro title is long, wraps, or looked even slightly crowded in the contact sheet; full-size inspection catches title/subtitle/body overlap that can be invisible in the 3x3 sheet.
  ```sh
  mkdir -p output/qa/<slug>
  ffmpeg -y -loglevel error \
    -i output/publish/frases-a1-epNN-<slug>-16x9-vN.mp4 \
    -vf "select='eq(n,0)+eq(n,360)+eq(n,900)+eq(n,1440)+eq(n,2160)+eq(n,2880)+eq(n,3960)+eq(n,5040)+eq(n,8520)',scale=320:180,tile=3x3" \
    -frames:v 1 output/qa/<slug>/contact-sheet.jpg
  ```
  Then run `vision_analyze` on the contact sheet to check Spanish/Korean readability, portrait placement, clipping/overlap, intro/outro readability, and tofu glyphs.
- Thumbnail QA matters as much as video QA. For a new episode, create/approve the thumbnail-source image early, before full implementation, when the user asks for visual direction first. If a user flags cropped character hair/head or weak text-box placement, regenerate the thumbnail directly from the source image instead of only tweaking metadata. For 1:1 generated scene art used in a 16:9 thumbnail, a robust layout is: blurred/darkened full-bleed background, a right-side square/rounded image card showing the full uncropped character head, and a left-side light rounded text panel. For 16:9 generated source art, request the subject on the right and deliberately leave clean negative space on the left for title text. When composing the final thumbnail, size badges/pills from measured text bounds (for example with `ImageDraw.textbbox`) so labels like `Español A1 · Ep.8` do not clip at the right edge. Keep title and callout pills fully inside the panel; size rounded boxes from actual text bounds; verify with `vision_analyze` that hair/head is not cropped, Korean/Spanish text is readable, boxes do not overlap the subject, and there is no readable accidental text/logo in the generated image. If Peter approves the thumbnail and then says `영상제작 진행`, treat that as approval to produce the full reviewable episode bundle from the thumbnail direction; create the project module/source script, run the full validation chain, publish locally only, and stop for review.
- If the user asks to make a later thumbnail match Ep.7, use the Ep.7-style pattern rather than the two-card layout: blurred/darkened full-bleed image background, large cream rounded text panel on the left, coral episode badge, large white Spanish title with thick black stroke, Korean white pill, teal Spanish callout pill, and the scene image directly on the right with no separate white card frame. See `references/thumbnail-ep7-style.md` for the reusable pattern and the Ep.8 revision example.
- If the user asks to see the thumbnail first before writing/producing the full episode, generate a standalone thumbnail draft immediately and do not create or modify episode project files yet. Use source art with right-side characters and left-side negative space, then compose readable overlay text and run visual QA before handoff. See `references/ep11-time-thumbnail.md` for a time/departure station example and copy pattern; see `references/ep18-me-gusta-pero-thumbnail.md` for an A1+/A2- `Me gusta, pero…` example with duplicate-phrase correction and Ep.7-style overlay copy.
- When Peter asks to remake an early/old Spanish Lab video “our way,” first search the repo by YouTube ID/title for the canonical old module/lesson data, then narrow the remake to one current-style learning point instead of reproducing the old broad phrase list. Use current continuity (`Jin`, Lucía, Diego), generate/approve the Ep.7-style thumbnail if requested, then produce a full story-card package. See `references/ep02-primer-encuentro-remake-production.md` for the `¿Cómo te llamas? / Me llamo...` precedent.
- For A2 entry episodes that reuse the card renderer, verify the dialogue header label is not hard-coded as `Conversación A1`. Prefer a project `DESIGN["conversation_label"] = "Conversación A2"` and renderer support that reads `design.get("conversation_label", "Conversación A1")`; regenerate the contact sheet after this fix because the stale A1 label can be easy to miss in full renders.
- If Peter says recent A1+/phrase episodes feel too similar and wants to raise the level, pivot the next episode to **A2 entry / A1→A2 bridge** rather than proposing another near-identical one-sentence routine pattern. Keep exactly one learning point, but make the function more conversational (e.g. invitation → refusal → reason) and make the thumbnail clearly signal the higher level with `Español A2`. See `references/ep24-a2-no-puedo-ir-thumbnail.md` for the approved `No puedo ir porque tengo que trabajar` thumbnail-first direction.
- For broad `50문장` ideas such as greetings, do not force them into the regular one-learning-point episode ladder or a preassigned episode number. Position them as an **A1 Phrase Bank / 반복 듣기 특집** when the scope covers multiple functions, keep the regular roadmap intact, and use the Spanish Lab brand/Ep.1 BGM if Peter requests continuity. Use an `ep00`/special-style internal label when needed to avoid conflicting with the main episode roadmap. See `references/a1-greetings-50-thumbnail-special.md` for the approved `스페인어 인사 50문장` thumbnail-first precedent and `references/a1-greetings-50-production.md` for the full local-render/BGM/QA precedent.
- Peter approved the Ep.15 image-generation workflow for future Spanish Lab images: generate a direct 16:9 landscape background/thumbnail draft with a clear prompt, place characters/scene emphasis on the right, leave clean left-side space for overlay, avoid fake readable text/logos/clutter/cropped heads, then add the Ep.7-style overlay if a finished thumbnail is requested. See `references/ep15-primavera-madrid-production.md`.
- When regenerating a thumbnail manually, update both the source repo thumbnail path (for example `thumbs/<slug>.jpg`) and the publish-output thumbnail path (for example `output/thumbs/frases-a1-epNN-<slug>.jpg`) so the delivered MEDIA and publish artifacts stay in sync.
- `references/ep15-primavera-thumbnail.md` for copy/layout details and handoff expectations.
- For clothing/wardrobe episodes, use per-slide object-card imagery as vocabulary support without creating a second learning point; see `references/ep17-que-llevas-thumbnail-and-scenario.md` for the `¿Qué llevas?` / `Llevo + clothing noun` scenario and thumbnail pattern.
- `git status --short` reviewed so the user knows what files changed. Remember generated `output/` artifacts may be gitignored and therefore not appear in `git status --short`, even though they are ready to deliver with `MEDIA:` paths.

## Handoff guidance
Be explicit about what is done and what is not:
- Project module and source text created
- Validation passed
- Visual/silent preview created
- TTS/final audio may still be pending if macOS `say` is unavailable in Hermes/Linux
- Next decision is TTS strategy: run on macOS with `say`, adapt Linux TTS, or ship a silent/subtitle-first test

### Daily-candidate approval, production, and cleanup
When Peter replies to a daily candidate with approval plus a packaging constraint (for example `승인, 스페인 본토, 라틴 함께 표시`):
1. Treat it as approval to revise the internal production draft, not permission to externally publish.
2. Use session/context search to identify the candidate slug and existing package files before editing; do not recreate a parallel package unless the slug is missing.
3. Update every persistent package artifact that represents the item, typically:
   - `/opt/data/content/lessons/<slug>.md`
   - `/opt/data/youtube/shorts/<slug>.md`
   - `/opt/data/youtube/metadata/<slug>.json`
   - `/opt/data/data/lessons/<slug>.json`
   - `/opt/data/data/quizzes/<slug>.json`
4. Keep exactly one learning point. Regional vocabulary notes should be side-by-side wording, not a second grammar lesson.
5. For Spain/mainland + Latin America ticket wording, a compact A1-safe pattern is:
   - `Spain: Quiero un billete.`
   - `Latin America: Quiero un boleto.`
   Both share the same learning point: `Quiero + noun`.
6. If Peter then says “영상제작 진행,” do not assume a plain card-only Shorts rendering is acceptable. First map the approved learning point into the established Spanish Lab style (story/scene, recurring characters, and existing thumbnail/visual conventions) or ask for a style decision if the request implies a new short-form experiment.
7. Validate after writing: files exist, JSON parses, CEFR is present, one-learning-point markers remain, regional variants appear, and `external_auto_publish`/no-publish status is preserved.
8. If Peter rejects a produced video package because the style does not fit, delete the product artifacts promptly and narrowly: project module, episode source directory, rendered MP4, publish MP4, thumbnail, metadata, and QA directory for that slug. Keep upstream internal candidate/draft files unless Peter explicitly asks to delete those too. Verify no slug-specific paths remain and report that external publishing was not performed.
9. Final handoff should be concise: approval reflected or product deleted, files changed, checks passed, and no external posting performed.

### YouTube upload description handoff
When the user asks for `유튜브 게재 설명자료`, `업로드 설명`, `설명자료`, or similar for a finished card episode, do not invent from memory. Pull the canonical upload metadata from the generated project artifacts first:
- project module fields: `YOUTUBE_TITLE`, `DESCRIPTION_INTRO`, `DESCRIPTION_OUTRO`, `KOREAN_TEASER`, tags/hashtags;
- latest versioned files under `output/meta/<series>-epNN-<slug>-16x9-vN.md` and `.json`;
- upload asset paths under `output/publish/`, `output/thumbs/`, and `output/meta/` when needed for verification.

Peter currently prefers the shortened Ep.14-style YouTube description materials through section 7 only unless he explicitly asks for the full upload/settings pack:
1. 추천 제목;
2. 제목 후보;
3. 한국어 중심 설명문;
4. 챕터;
5. Spanish description block;
6. 고정 댓글 후보;
7. 해시태그.

Omit comma-separated tags, upload-setting notes, and asset file paths from the user-facing description-materials response unless requested. Keep the wording upload-ready: clean Korean labels, no Telegram table syntax, and preserve Spanish accents/chapter timestamps exactly. If Peter asks for a full operations/upload pack, then include tags, category/settings, duration/resolution/version, and exact upload file paths; a reusable starter is available at `templates/youtube-upload-description-pack.md`.

## References
- `references/ep08-la-cuenta-continuity.md`: Ep.8 café-bill scenario, Jin naming transition, brand BGM reuse, and thumbnail-source prompt/QA criteria.
- `references/ep09-directions-thumbnail.md`: Ep.9 Madrid street directions thumbnail concept, Jin/Lucía/Diego continuity, prompt, overlay text, paths, and clipping QA notes.
- `references/ep09-directions-production.md`: Ep.9 `¿Dónde está el metro?` full production details: approved script shape, module paths, chapters, validation chain, and contact-sheet QA.
- `references/ep10-ticket-thumbnail.md`: Ep.10 metro-ticket thumbnail concept, source-art prompt, Ep.7-style overlay text, paths, and QA criteria.
- `references/ep10-ticket-production.md`: Ep.10 `Un billete, por favor` production details: ticket-buying script shape, module paths, chapters, validation chain, and contact-sheet QA.
- `references/ep11-upload-description-pack.md`: Ep.11 concrete YouTube upload-description pack example: artifacts used, title, chapters, key-expression block, settings, tags, and asset paths.
- `references/ep12-travel-weekend-thumbnail.md`: Ep.12 thumbnail-first continuity pattern: connect a weekend/trip chat to Ep.11's travel teaser using `¿Qué tal el viaje?`, train/Toledo visuals, and Ep.7-style overlay.
- `references/ep12-travel-followup-production.md`: Ep.12 full production reference for the travel-aftertalk episode, including continuity decision, module/copy, 30-line story-card shape, validation chain, and handoff artifacts.
- `references/ep13-quiero-noun-shorts-production.md`: Candidate A / Ep.13 `Quiero + 명사` Shorts-style card production reference, including Spain/Latin America variant handling, TTS duration fix, validation commands, artifacts, and 73s contact-sheet QA frames. Treat this as a rejected/alternate Shorts-style path, not the default for the channel.
- `references/ep13-quiero-volver-thumbnail.md`: Ep.13 thumbnail-first direction that bridges from Ep.12 via `Quiero volver`, including Ep.7-style overlay copy, source-art prompt, draft paths, Pillow composition notes, and QA criteria.
- `references/ep13-quiero-volver-production.md`: Ep.13 full A1 story-card production reference for `Quiero volver` / `Quiero + infinitivo`, including thumbnail-first workflow, script adjustments, module settings, validation commands, and 310s QA frame picks.
- `references/ep14-voy-a-practicar-thumbnail.md`: Ep.14 thumbnail-first direction that bridges from Ep.13 `Quiero + infinitivo` to `Voy a + infinitivo`, including Ep.7-style overlay copy, source-art prompt, crop/composition notes for non-16:9 generated images, draft paths, and QA criteria.
- `references/ep14-voy-a-practicar-production.md`: Ep.14 full production reference for `Voy a + infinitivo`, including module/artifact paths, validation commands, visual-QA copy fixes, direct publish-probe pitfall, and 306s contact-sheet frame picks.
- `references/ep15-primavera-madrid-production.md`: Ep.15 full production reference for `¿Cómo es + noun/place?`, including Peter-approved 16:9 right-scene/left-overlay image workflow, Ep.7-style thumbnail composition, intro-title readability fix, and `la primavera` gender-agreement QA.
- `references/ep16-que-tiempo-hace-production.md`: Ep.16 full production reference for `¿Qué tiempo hace?` / `Hace + weather`, including the mixed Korean-in-`text_es` QA pitfall, 3.5s block-header TTS fit fix, thumbnail pattern, validation commands, and contact-sheet frame picks.
- `references/ep17-que-llevas-thumbnail-and-scenario.md`: Ep.17 direction for `¿Qué llevas?` / `Llevo + clothing noun`, including per-slide clothing object-card usage, thumbnail source-art prompt, overlay copy, delivered paths, and QA criteria.
- `references/ep18-me-gusta-pero-production.md`: Ep.18 A1+ direction for raising `gustar` difficulty with `Me gusta + noun, pero...`, duplicate-topic avoidance after `¿Cuánto cuesta?`, thumbnail-first workflow, validation chain, and artifact pattern.
- `references/ep19-prefiero-cafe-thumbnail.md`: Ep.19 thumbnail-first direction for `Prefiero + noun`, including café/coffee-vs-tea source-art prompt, Ep.7-style overlay copy, crop/composition notes, paths, and QA criteria.
- `references/ep19-prefiero-cafe-production.md`: Ep.19 A1+ `Prefiero + noun` full-production reference, including café-choice story continuity from Ep.18, validation chain, and contact-sheet frame picks.
- `references/ep20-porque-thumbnail.md`: Ep.20 thumbnail-first direction for `porque + short reason`, continuing from Ep.19 coffee preference into `Porque tengo sueño`, with café source-art prompt, Ep.7-style overlay copy, output paths, and QA criteria.
- `references/ep20-porque-tengo-sueno-production.md`: Ep.20 A1+ `porque + short reason` full-production reference, including thumbnail-first approval flow, café continuity from Ep.19, validation chain, and contact-sheet QA.
- `references/ep21-a-veces-production.md`: Ep.21 A1+ `A veces + presente` full-production reference, including the Ep.1 phrase-bank mining decision, thumbnail-first morning-routine direction, module/artifact paths, validation chain, and contact-sheet QA.
- `references/ep21-a-veces-thumbnail.md`: Ep.21 thumbnail-first direction for combining underused Ep.1 routine phrases with `A veces + presente`, including morning-study source-art prompt, Ep.7-style overlay copy, delivered paths, and QA criteria.
- `references/ep22-siempre-thumbnail.md`: Ep.22 thumbnail-first direction for continuing routine/frequency from `a veces` to `siempre + presente`, including morning coffee source-art prompt, overlay copy, complete Korean thumbnail-copy revision, paths, and QA criteria.
- `references/ep22-siempre-production.md`: Ep.22 full-production precedent for `siempre + presente`, including module/artifact paths, validation chain, v1/v2 intro spacing failure, and the full-size intro-frame QA requirement.
- `references/ep23-nunca-production.md`: Ep.23 full-production precedent for `nunca + presente`, including Peter's explicit first-slide spacing preference for visually distinct right-side title/subtitle/body divisions, validation chain, and intro-frame QA.
- `references/ep24-a2-no-puedo-ir-thumbnail.md`: Ep.24 thumbnail-first A2 bridge direction for `No puedo ir porque tengo que trabajar`, including right-side work scene, left-side overlay copy, A2 signaling, paths, and QA criteria.
- `references/ep24-a2-no-puedo-ir-production.md`: Ep.24 A2-entry production precedent, including the A1→A2 bridge decision, `Conversación A2` renderer label fix, Spanish-only display text correction, validation chain, and shortened 7-section description-materials shape.
- `references/ep25-podemos-quedar-manana-production.md`: Ep.25 A2-entry rescheduling/polite alternative precedent for `¿Podemos + infinitivo + time expression?`, including thumbnail-first workflow, Spanish-only display-text fixes, v1→v2 rerender, longest-sentence QA, and 7-section description materials.
- `references/ep26-estoy-en-la-estacion-production.md`: Ep.26 A1+ `estar en + lugar` production precedent, including station-travel scene, right-scene/left-panel thumbnail, `soy en` common-error guard, full-size intro-frame spacing fix via project `font_size_title`, and validation/QA commands.
- `references/ep27-hay-farmacia-thumbnail.md`: Ep.27 thumbnail-first precedent for `Hay + 명사`, including pharmacy/station scene direction, overlay copy, non-16:9 source crop handling, long callout clipping fix, and QA criteria.
- `references/ep27-hay-una-farmacia-cerca-production.md`: Ep.27 A1+ `hay + noun` production precedent, including the Ep.26→Ep.27 existence/location bridge, pharmacy/station thumbnail direction, Spanish-only display-text fixes for Korean quiz prompts, callout-pill clipping fix, and validation/QA commands.
- `references/ep28-para-llevar-thumbnail.md`: Ep.28 thumbnail-first precedent after Peter rejected `el/la` as too basic; practical A1+ `Quiero + noun + para llevar` café/takeaway topic, source-image prompt constraints, Ep.7-style overlay copy, paths, and QA criteria.
- `references/ep29-me-lo-llevo-thumbnail.md`: Ep.29 thumbnail-first precedent after Peter rejected repeated `para llevar` and too-basic numbers; practical A1+/A2-entry `Me lo llevo` shopping/souvenir chunk, duplicate-topic cautions, source prompt, Ep.7-style overlay copy, paths, and QA criteria.
- `references/ep28-quiero-cafe-para-llevar-production.md`: Ep.28 A1+ practical café/travel production precedent for `Quiero + product + para llevar`; includes Spanish-only display-text fixes, `producto` wording correction, intro `contain` crop fix, and final v4 validation/QA commands.
- `references/ep29-me-lo-llevo-production.md`: Ep.29 A1+ shopping/souvenir precedent after Peter rejected duplicate `para llevar` and too-basic numbers; covers `Me lo llevo` thumbnail-first workflow, duplicate-topic avoidance (`¿Cuánto cuesta?`, `¿Dónde está...?`), artifact paths, validation chain, and QA notes.
- `references/ep30-tiene-otro-color-production.md`: Ep.30 A1+ shopping-option precedent for `¿Tiene otro color?`, including thumbnail-first flow, `¿Tiene otra talla?` as a safe word-swap, v1→v2 rerender after contact-sheet QA caught Korean in Spanish-facing fields, and a reusable Hangul-in-`text_es` scan command.
- `references/ep02-primer-encuentro-remake-thumbnail.md`: Ep.2 remake thumbnail-first precedent for narrowing the old multi-point `Primer encuentro` episode to `¿Cómo te llamas?` / `Me llamo + nombre`, using oEmbed/repo search when transcripts are blocked, and composing the current Ep.7-style thumbnail with Jin/Lucía/Diego.
- `references/ep02-primer-encuentro-remake-thumbnail.md`: Ep.2 remake thumbnail-first precedent for narrowing the old multi-point `Primer encuentro` episode to `¿Cómo te llamas?` / `Me llamo + nombre`, using oEmbed/repo search when transcripts are blocked, and composing the current Ep.7-style thumbnail with Jin/Lucía/Diego.
- `references/a1-greetings-50-thumbnail-special.md`: A1 Phrase Bank / repeat-listening special precedent for `스페인어 인사 50문장`, including the decision not to force a broad 50-phrase idea into a regular one-point episode number, Ep.1/brand BGM continuity, overlay copy, artifact paths, and QA notes.
- `references/a1-greetings-50-production.md`: full local production precedent for the `스페인어 인사 50문장` A1 Phrase Bank special, including `ep00` positioning, canonical BGM use, intro contain-crop fix, validation chain, artifacts, and concise handoff pattern.
- When regenerating a thumbnail manually, update both the source repo thumbnail path
- `references/ep17-que-llevas-thumbnail-and-scenario.md`: Ep.17 direction for `¿Qué llevas?` / `Llevo + clothing noun`, including per-slide clothing object-card usage, thumbnail source-art prompt, overlay copy, delivered paths, and QA criteria.
- `references/ep18-me-gusta-pero-production.md`: Ep.18 A1+ direction for raising `gustar` difficulty with `Me gusta + noun, pero...`, duplicate-topic avoidance after `¿Cuánto cuesta?`, thumbnail-first workflow, validation chain, and artifact pattern.
- `references/ep19-prefiero-cafe-thumbnail.md`: Ep.19 thumbnail-first direction for `Prefiero + noun`, including café/coffee-vs-tea source-art prompt, Ep.7-style overlay copy, crop/composition notes, paths, and QA criteria.
- `references/ep19-prefiero-cafe-production.md`: Ep.19 A1+ `Prefiero + noun` full-production reference, including café-choice story continuity from Ep.18, validation chain, and contact-sheet frame picks.
- `references/intro-slide-only-preview.md`: still-image-only workflow for intro slide corrections when the user says not to rerender or touch the video.
