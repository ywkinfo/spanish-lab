# Ep.24 production reference — `No puedo ir porque tengo que trabajar`

Use this as the precedent for Spanish Lab's A1→A2 bridge episodes after the A1+/frequency routine run started feeling repetitive.

## Learning design
- Episode: Ep.24
- Level: A2 entry / A1→A2 bridge
- One learning point: `No puedo + infinitive + porque tengo que + infinitive` to decline and give a reason.
- Scenario: Lucía invites Jin for coffee; Jin is working and politely refuses with a reason.
- Core sentence: `No puedo ir porque tengo que trabajar.`
- Polite complete sentence: `Lo siento, no puedo ir porque tengo que trabajar.`
- Useful substitutions: `tengo que estudiar`, `tengo que descansar`.

## User/context signal
Peter said the recent A1+/routine episodes felt too similar and approved moving Ep.24 up toward A2. For similar feedback, pivot away from another frequency/routine one-liner and choose a more conversational function (invitation → refusal → reason) while still keeping exactly one learning point.

## Production artifacts used
- Project module: `projects/no_puedo_ir_a2.py`
- Source script: `a2-no-puedo-ir/descrip.md`
- Source image: `images/ep24-no-puedo-ir-source.png`
- Final local render: `output/publish/frases-a2-ep24-no-puedo-ir-16x9-v1.mp4`
- Metadata: `output/meta/frases-a2-ep24-no-puedo-ir-16x9-v1.md` and `.json`
- Short Korean-facing description materials: `output/meta/frases-a2-ep24-no-puedo-ir-description-materials-ko.md`
- Thumbnail: `output/thumbs/frases-a2-ep24-no-puedo-ir.jpg`
- QA frames: `output/qa/no-puedo-ir/contact-sheet-v1.jpg`, `frame-intro-v1.png`, `frame-lo-siento-v1.png`

## Renderer / QA lessons
- The card renderer had a hard-coded `Conversación A1` dialogue label. For A2 bridge episodes, add project-level `DESIGN["conversation_label"] = "Conversación A2"` and ensure the renderer reads `design.get("conversation_label", "Conversación A1")`.
- Check the contact sheet after changing this label; it is easy to miss stale A1 wording in a full render.
- Keep Spanish-facing text Spanish-only. Avoid lines such as `No puedo significa: 할 수 없어요`; use Spanish in `text_es` and Korean explanation in `text_ko`.
- For the longest polite sentence frame, extract a full-size frame around the exact timestamp (e.g. line 23) and verify the full Spanish sentence plus Korean caption fit without portrait overlap.

## Commands / validation chain
```sh
python3 -m py_compile projects/no_puedo_ir_a2.py build/render_cards.py
PROJECT=no_puedo_ir_a2 PYTHON=.venv/bin/python make check
PROJECT=no_puedo_ir_a2 PYTHON=.venv/bin/python make lint-spanish
PROJECT=no_puedo_ir_a2 PYTHON=.venv/bin/python make tts
PROJECT=no_puedo_ir_a2 PYTHON=.venv/bin/python make publish-cards
PROJECT=no_puedo_ir_a2 PYTHON=.venv/bin/python make verify
PROJECT=no_puedo_ir_a2 PYTHON=.venv/bin/python .venv/bin/python checks/probe_output.py \
  output/publish/frases-a2-ep24-no-puedo-ir-16x9-v1.mp4
```

If script/copy is patched after rendering, delete stale output/publish/meta artifacts or bump `RENDER_VERSION`, rerun TTS/check/publish/verify, and regenerate QA frames/contact sheet.

## Short upload/description-materials shape
For Peter's current YouTube upload handoff preference, create the shortened Korean-facing description materials through section 7 only:
1. 추천 제목
2. 제목 후보
3. 한국어 중심 설명문
4. 챕터
5. Spanish description block
6. 고정 댓글 후보
7. 해시태그

Omit YouTube tags, upload-setting notes, and asset file paths unless Peter asks for them.

## Handoff note
Final package was local-only and approval-gated: no external upload/posting performed.
