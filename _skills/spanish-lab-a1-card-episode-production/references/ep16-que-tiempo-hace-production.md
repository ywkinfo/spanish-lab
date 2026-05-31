# Ep.16 `¿Qué tiempo hace?` production reference

Use this as a compact reference for future Spanish Lab A1 story-card episodes about weather / `Hace + weather`.

## Episode shape
- Module: `projects/que_tiempo_hace_a1.py`
- Source text: `a1-que-tiempo-hace/descrip.md`
- Episode: `EPISODE = 16`, `LEVEL = "A1"`, `RENDER_TYPE = "cards"`
- Slug/output: `que-tiempo-hace`
- Learning point: exactly one point — ask `¿Qué tiempo hace?` and answer with `Hace + weather expression`.
- Useful A1 expressions: `Hace sol`, `Hace frío`, `Hace calor`, `Hace viento`, `Hace buen tiempo`.
- Target length used successfully: 36 segments, 30 dialogue lines, 4 block headers, total duration `303.5s` (~5:03).

## Visual workflow
1. Generate a direct 16:9-ish source/background with right-side characters and clean left-side overlay space.
2. Persist a 16:9 crop as `images/ep16-que-tiempo-hace-source.png`.
3. Compose the Ep.7-style thumbnail with:
   - cream rounded left panel;
   - coral badge: `Español A1 · Ep.16`;
   - large white/black-stroked title: `¿Qué tiempo hace?`;
   - Korean pill: `오늘 날씨가 어때?`;
   - teal phrase pill: `Hace sol ☀️`.
4. Save both repo and publish thumbnail paths:
   - `thumbs/a1-ep16-que-tiempo-hace.jpg`
   - `output/thumbs/frases-a1-ep16-que-tiempo-hace.jpg`

## Script pitfall found in QA
Do **not** put Korean inside `text_es` / Spanish narration lines, even when explaining a literal meaning. It renders as mixed-language Spanish display text and looks wrong in final cards.

Bad:
```python
"Literalmente: hace sol, sol을 만들어요."
"Hace frío significa: 날씨가 추워요."
```
Good:
```python
"Literalmente: hace sol."
"Hace frío habla del tiempo."
```
Put Korean explanations only in `text_ko`, e.g.:
```python
"직역하면: ‘해를 만들어요’에 가까워요."
"Hace frío는 ‘날씨가 추워요’라는 뜻이에요."
```

## Timing / TTS notes
- Edge TTS fit failed when a block header was only `3.0s` (`Hace frío / calor`), because synthesized header audio plus lead padding exceeded the segment end by ~0.30s.
- Increasing all block headers to `3.5s` fixed the fit and gave the episode total `303.5s`.
- After script text changes, bump `RENDER_VERSION` instead of overwriting already-published artifacts.

## Validation chain used
```sh
PROJECT=que_tiempo_hace_a1 PYTHON=.venv/bin/python make lint-spanish
PROJECT=que_tiempo_hace_a1 PYTHON=.venv/bin/python make tts
PROJECT=que_tiempo_hace_a1 PYTHON=.venv/bin/python make check
PROJECT=que_tiempo_hace_a1 PYTHON=.venv/bin/python make publish-cards
PROJECT=que_tiempo_hace_a1 PYTHON=.venv/bin/python make verify
PROJECT=que_tiempo_hace_a1 PYTHON=.venv/bin/python .venv/bin/python checks/probe_output.py \
  output/publish/frases-a1-ep16-que-tiempo-hace-16x9-v2.mp4
```

Expected verify/probe highlights:
- MP4: `output/publish/frases-a1-ep16-que-tiempo-hace-16x9-v2.mp4`
- Duration: `303.5s`
- Resolution: `1280x720`
- Video codec: `h264`, pix_fmt `yuv420p`, faststart true
- Audio codec: `aac`, sample rate `44100`, audio duration `303.5s`

## Contact sheet QA
Use a 3x3 contact sheet with late frame `eq(n,8520)` for the outro on ~5-minute videos:
```sh
ffmpeg -y -loglevel error \
  -i output/publish/frases-a1-ep16-que-tiempo-hace-16x9-v2.mp4 \
  -vf "select='eq(n,0)+eq(n,360)+eq(n,900)+eq(n,1440)+eq(n,2160)+eq(n,2880)+eq(n,3960)+eq(n,5040)+eq(n,8520)',scale=320:180,tile=3x3" \
  -frames:v 1 output/qa/que-tiempo-hace/final-contact-sheet-v2.jpg
```

QA criteria:
- no Korean embedded in Spanish narration display lines;
- Hangul renders correctly;
- Spanish and Korean remain readable;
- portraits are not clipped/overlapped;
- outro text fits and remains readable.