# Ep.2 `Primer encuentro` remake production reference

Use this as a precedent when Peter asks to remake an early Spanish Lab video “our way,” especially an old phrase-list/card episode.

## Trigger/context
- Source video: `tkNs4tJunaU`, old Ep.2 `[스페인어 기초 회화] 첫 만남에 바로 쓰는 인사말 | Primer encuentro | A1 Ep.2`.
- Transcript extraction may be blocked, but the repo can contain enough canonical data. Search the repo by YouTube ID/title before relying on YouTube captions.
- The old module was `projects/primer_encuentro_a1.py`, with many phrase-list points: `Hola`, `Me llamo...`, `¿Cómo te llamas?`, `Mucho gusto`, `Igualmente`, `Soy de Corea/Madrid`, `Encantado/a`.

## Remake decision
- Do not simply reproduce the old broad phrase list.
- Narrow to exactly one A1 learning point:
  - `¿Cómo te llamas?`
  - `Me llamo + nombre`
- Treat `Hola`, `Mucho gusto`, and `Igualmente` as supporting scene phrases only.
- Exclude `Soy de Corea/Madrid` and `Encantado/a` from the main remake because they create additional learning points.
- Use current channel continuity: the Korean learner is **Jin**, not Peter, with Lucía and Diego.

## Thumbnail-first production precedent
Peter approved proceeding and thumbnail production before full video. Use Ep.7-style overlay:
- source scene: first meeting / café-language-exchange setting, three characters on the right, clean left negative space;
- badge: `Español A1 · Ep.2`;
- main title: `¿Cómo te llamas?`;
- Korean pill: `이름 묻고 답하기`;
- teal pill: `Me llamo Jin`.

Known paths from this remake:
```text
images/ep02-primer-encuentro-remake-source.png
thumbs/a1-ep02-primer-encuentro-remake.jpg
output/thumbs/frases-a1-ep02-primer-encuentro-remake.jpg
output/qa/primer-encuentro-remake/thumbnail.jpg
scripts/create_ep02_primer_encuentro_remake_thumbnail.py
```

## Full production shape
- Module: `projects/primer_encuentro_remake_a1.py`
- Source rows: `a1-primer-encuentro-remake/descrip.md`
- Series: `frases-a1`
- Episode: `2`
- Render type: `cards`
- One learning point: `¿Cómo te llamas? / Me llamo...`
- 4 blocks:
  1. `Primer encuentro`
  2. `¿Cómo te llamas?`
  3. `Me llamo...`
  4. `Mini conversación`
- 30 dialogue lines, 36 total segments, around 4m46s.
- Intro title: `¿Cómo te llamas?`; intro Korean: `첫 만남에서 이름 묻고 답하기`.
- Use brand BGM (`assets/audio/spanish-lab-brand-bgm.mp3`) and current per-character Edge voices:
  - Lucía: `es-ES-ElviraNeural`
  - Jin: `es-ES-AlvaroNeural`
  - Diego: `es-MX-JorgeNeural`

## Validation chain used
```sh
PROJECT=primer_encuentro_remake_a1 PYTHON=.venv/bin/python make check
PROJECT=primer_encuentro_remake_a1 PYTHON=.venv/bin/python make test
PROJECT=primer_encuentro_remake_a1 PYTHON=.venv/bin/python make lint-spanish
PROJECT=primer_encuentro_remake_a1 PYTHON=.venv/bin/python make tts
PROJECT=primer_encuentro_remake_a1 PYTHON=.venv/bin/python make publish-cards
PROJECT=primer_encuentro_remake_a1 PYTHON=.venv/bin/python make verify
```

`lint-spanish` may warn on `actual` inside `Spanish Lab estilo actual`; this is a false-positive warning, not a render blocker when there are no errors.

## QA precedent
Create both a contact sheet and a full-size intro frame:
```text
output/qa/primer-encuentro-remake/contact-sheet-v1.jpg
output/qa/primer-encuentro-remake/intro-frame-v1.jpg
```

Verify:
- Spanish/Korean readability;
- no Hangul tofu;
- no title/body overlap on intro full-size frame;
- characters and portraits placed correctly;
- first-meeting scene remains clear;
- output verify reports exact video/audio duration match.

Known final publish paths:
```text
output/publish/frases-a1-ep02-primer-encuentro-remake-16x9-v1.mp4
output/thumbs/frases-a1-ep02-primer-encuentro-remake.jpg
output/meta/frases-a1-ep02-primer-encuentro-remake-16x9-v1.md
output/meta/frases-a1-ep02-primer-encuentro-remake-16x9-v1.json
```
