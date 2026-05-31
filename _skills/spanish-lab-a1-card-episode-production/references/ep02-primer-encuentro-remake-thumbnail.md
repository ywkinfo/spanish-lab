# Ep.2 `Primer encuentro` remake thumbnail notes

Use when remaking an older Spanish Lab A1 episode into the current story-card style, especially when the old YouTube transcript is unavailable but the repo contains the canonical project/docs.

## Source discovery pattern
- If YouTube transcript extraction is blocked, use YouTube oEmbed for basic identity and then search the Spanish Lab repo for the video ID/title.
- For `tkNs4tJunaU`, oEmbed identified: `[스페인어 기초 회화] 첫 만남에 바로 쓰는 인사말 | Primer encuentro | A1 Ep.2`.
- Canonical repo sources found:
  - `projects/primer_encuentro_a1.py`
  - `docs/lessons/a1-primer-encuentro/index.md`
- The old lesson mixed several learning functions. For the remake, narrow to one point: `¿Cómo te llamas?` / `Me llamo + nombre`.
- Use `Jin` for the Korean learner in new user-facing copy, not legacy `Peter`.

## Thumbnail concept
- Current-style A1 story-card remake, not a phrase-bank thumbnail.
- Scene: warm Madrid café / language-exchange first meeting.
- Characters on the right: Jin, Lucía, Diego; preserve full heads/hair.
- Leave clean left negative space for overlay.
- No readable generated text, logos, numbers, signs, or watermark.

Source-art prompt pattern:
> A clean, warm, modern 16:9 illustration for a Spanish Lab A1 YouTube thumbnail. Scene: a friendly first meeting at a small Spanish café / language exchange table in Madrid. Three recurring Spanish Lab characters are on the right side: Jin, a Korean beginner learner, friendly and slightly shy; Lucía, a friendly young Spanish woman smiling and greeting him; Diego, a warm Spanish guide/teacher standing nearby and encouraging them. The characters are visible from head to upper body, full heads and hair fully inside the frame, no cropping. The scene clearly suggests first meeting, greeting, and asking names. Warm beige, coral, teal, and soft terracotta palette, clean vector-like digital illustration, polished educational YouTube thumbnail style, high contrast. Leave clean empty space on the left side for large title text overlay. No text, no letters, no numbers, no logos, no watermark, no readable signs, no clutter, no distorted hands.

## Ep.7-style overlay copy
- Badge: `Español A1 · Ep.2`
- Main Spanish title: `¿Cómo te` / `llamas?`
- Korean pill: `이름 묻고 답하기`
- Teal pill: `Me llamo Jin`
- Small support note: `첫 만남 A1`

## Known-good artifact pattern
- Source image: `images/ep02-primer-encuentro-remake-source.png`
- Repo thumbnail: `thumbs/a1-ep02-primer-encuentro-remake.jpg`
- Publish thumbnail: `output/thumbs/frases-a1-ep02-primer-encuentro-remake.jpg`
- QA thumbnail: `output/qa/primer-encuentro-remake/thumbnail.jpg`
- Composition script: `scripts/create_ep02_primer_encuentro_remake_thumbnail.py`

## QA criteria
- Spanish and Korean text are readable; Hangul renders correctly.
- No text clipping in the badge, Korean pill, or teal pill.
- Character heads/hair are preserved, especially Diego on the far right.
- First-meeting/café scene remains clear even with the left panel.
- No accidental readable text/logos in generated art.
- External publishing is not performed; deliver reviewable local assets only.
