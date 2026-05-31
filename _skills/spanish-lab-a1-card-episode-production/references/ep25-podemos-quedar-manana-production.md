# Ep.25 production reference — `¿Podemos quedar mañana?`

Use this reference for Spanish Lab A2-entry episodes that continue from a refusal/reason episode into polite rescheduling or proposing an alternative time.

## Learning design
- Episode: Ep.25
- Level: A2 entry / A1→A2 bridge
- One learning point: `¿Podemos + infinitivo + time expression?` to propose another option politely.
- Scenario: After Jin cannot meet today, he proposes another time for coffee.
- Core sentence: `¿Podemos quedar mañana?`
- Complete polite sentence: `Lo siento, hoy no puedo. ¿Podemos quedar mañana?`
- Useful substitutions: `¿Podemos hablar más tarde?`, `¿Podemos tomar café el viernes?`

## Thumbnail-first workflow used
- Peter approved the Ep.25 candidate and first asked for thumbnail production.
- Thumbnail source-art prompt reused the Ep.24 A2 pattern: direct 16:9/landscape source art, Jin on the right, warm café/study setting, clean left negative space, no readable fake text/logos.
- Finished overlay used Ep.7-style layout with:
  - badge: `Español A2 · Ep.25`
  - main: `¿Podemos quedar mañana?`
  - Korean pill: `내일 만날 수 있을까요?`
  - teal callout: `quedar mañana`
- Save both repo and publish thumbnail copies:
  - `thumbs/a2-ep25-podemos-quedar-manana.jpg`
  - `output/thumbs/frases-a2-ep25-podemos-quedar-manana.jpg`
- Preserve source art as `thumbs/a2-ep25-podemos-quedar-manana-source.png` and copy it to `images/ep25-podemos-quedar-manana-source.png` for the project intro visual.
- Record the image prompt under `/opt/data/prompts/image-generation/` when producing the thumbnail first.

## Production artifacts used
- Project module: `projects/podemos_quedar_manana_a2.py`
- Source script: `a2-podemos-quedar-manana/descrip.md`
- Source image: `images/ep25-podemos-quedar-manana-source.png`
- Final local render: `output/publish/frases-a2-ep25-podemos-quedar-manana-16x9-v2.mp4`
- Metadata: `output/meta/frases-a2-ep25-podemos-quedar-manana-16x9-v2.md` and `.json`
- Short Korean-facing description materials: `output/meta/frases-a2-ep25-podemos-quedar-manana-description-materials-ko.md`
- Thumbnail: `output/thumbs/frases-a2-ep25-podemos-quedar-manana.jpg`
- QA frames: `output/qa/podemos-quedar-manana/contact-sheet-v2.jpg`, `frame-intro-v2.png`, `frame-long-sentence-v2.png`

## Script / language QA lessons
- Keep Spanish-facing `text_es` Spanish-only. During production, two lines initially mixed Korean into Spanish display text and were patched before final v2:
  - avoid `Naturalmente: 내일 만날 수 있을까요?`; use Spanish display such as `Naturalmente, suena como una propuesta amable.` and put the Korean explanation in `text_ko`.
  - avoid `Mañana significa: 내일.`; use Spanish display such as `Mañana es el día después de hoy.` and put the Korean meaning in `text_ko`.
- For complete rescheduling frames, extract the longest sentence frame and verify the two-line Spanish sentence plus Korean caption fit without portrait overlap:
  - `Lo siento, hoy no puedo. ¿Podemos quedar mañana?`
- Keep the dialogue label as `Conversación A2` via `DESIGN["conversation_label"]`; check the contact sheet for stale `Conversación A1` labels.

## Commands / validation chain
```sh
python3 -m py_compile projects/podemos_quedar_manana_a2.py
PROJECT=podemos_quedar_manana_a2 PYTHON=.venv/bin/python make check
PROJECT=podemos_quedar_manana_a2 PYTHON=.venv/bin/python make test
PROJECT=podemos_quedar_manana_a2 PYTHON=.venv/bin/python make lint-spanish
PROJECT=podemos_quedar_manana_a2 PYTHON=.venv/bin/python make tts
PROJECT=podemos_quedar_manana_a2 PYTHON=.venv/bin/python make publish-cards
PROJECT=podemos_quedar_manana_a2 PYTHON=.venv/bin/python make verify
PROJECT=podemos_quedar_manana_a2 PYTHON=.venv/bin/python .venv/bin/python checks/probe_output.py \
  output/publish/frases-a2-ep25-podemos-quedar-manana-16x9-v2.mp4
```

If copy is patched after a first render, bump `RENDER_VERSION` (Ep.25 moved from v1 to v2 after Spanish-only display fixes), rerun TTS/check/publish/verify, and regenerate QA frames/contact sheet.

## QA frame extraction pattern
```sh
mkdir -p output/qa/podemos-quedar-manana
ffmpeg -y -loglevel error \
  -i output/publish/frases-a2-ep25-podemos-quedar-manana-16x9-v2.mp4 \
  -vf "select='eq(n,0)+eq(n,450)+eq(n,900)+eq(n,1800)+eq(n,2700)+eq(n,3900)+eq(n,5200)+eq(n,6900)+eq(n,8500)',scale=320:180,tile=3x3" \
  -frames:v 1 output/qa/podemos-quedar-manana/contact-sheet-v2.jpg
ffmpeg -y -loglevel error -ss 00:00:00 \
  -i output/publish/frases-a2-ep25-podemos-quedar-manana-16x9-v2.mp4 \
  -frames:v 1 output/qa/podemos-quedar-manana/frame-intro-v2.png
ffmpeg -y -loglevel error -ss 00:03:06 \
  -i output/publish/frases-a2-ep25-podemos-quedar-manana-16x9-v2.mp4 \
  -frames:v 1 output/qa/podemos-quedar-manana/frame-long-sentence-v2.png
```

## Short upload/description-materials shape
Use Peter's current 7-section format:
1. 추천 제목
2. 제목 후보
3. 한국어 중심 설명문
4. 챕터
5. Spanish description block
6. 고정 댓글 후보
7. 해시태그

Omit tags/settings/asset paths unless Peter asks for the full pack.

## Handoff note
Final package was local-only and approval-gated: no external upload/posting performed.
