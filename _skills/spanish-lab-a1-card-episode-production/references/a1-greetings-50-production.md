# A1 Greetings 50-Phrase Bank Production Reference

Use this as the production precedent for broad `50문장` repeat-listening specials that do not fit the regular one-learning-point episode ladder.

## Positioning
- Treat broad greetings/phrase-list ideas as an **A1 Phrase Bank / 반복 듣기 특집**, not a normal sequential story episode.
- Avoid consuming a regular roadmap episode number when the item spans many greeting/social functions. A safe internal pattern is `ep00` or another clearly special/non-roadmap production label.
- Keep external posting gated: produce a local review package only and state that no YouTube upload/publish was performed.

## Proven module/artifact pattern
- Project module: `projects/greetings_50_phrases_a1.py`
- Source rows: `a1-greetings-50-phrases/descrip.md`
- Series/output pattern: `frases-a1-ep00-greetings-50-phrases-16x9-vN`
- Final MP4: `output/publish/frases-a1-ep00-greetings-50-phrases-16x9-vN.mp4`
- Metadata: `output/meta/frases-a1-ep00-greetings-50-phrases-16x9-vN.md` and `.json`
- Thumbnail: `output/thumbs/frases-a1-ep00-greetings-50-phrases.jpg`
- QA: `output/qa/greetings-50-phrases/contact-sheet-vN.jpg`

## BGM continuity
When Peter asks to reuse the early Spanish Lab sound identity, use the canonical brand track:
```python
"bgm_path": "assets/audio/spanish-lab-brand-bgm.mp3"
```
This keeps the special aligned with Ep.1/brand continuity. Tune volume/ducking by listening and `make verify`; do not rely only on a nominal dB number if the source track was mastered quietly.

## Intro image/crop fix
For a 16:9 café/character intro scene where all three people must remain visible, prefer a `contain` foreground over a blurred/darkened cover background rather than hard-cropping the source art. Verify the first/intro frame separately if the contact sheet is too small to catch cropped heads or missing characters.

## Validation chain used
From the repo root:
```sh
PROJECT=greetings_50_phrases_a1 PYTHON=.venv/bin/python make check
PROJECT=greetings_50_phrases_a1 PYTHON=.venv/bin/python make test
PROJECT=greetings_50_phrases_a1 PYTHON=.venv/bin/python make lint-spanish
PROJECT=greetings_50_phrases_a1 PYTHON=.venv/bin/python make tts
PROJECT=greetings_50_phrases_a1 PYTHON=.venv/bin/python make publish-cards
PROJECT=greetings_50_phrases_a1 PYTHON=.venv/bin/python make verify
```
Expected final package characteristics from the precedent: 1280x720 H.264/AAC, 30fps, faststart OK, audio/video durations aligned. The 50-greetings special rendered around 11 minutes (`~665s`), so use background execution/polling for long renders when needed.

## Handoff style
Deliver the review artifacts succinctly with `MEDIA:` paths for the MP4, thumbnail, and QA sheet. Mention:
- level/content type (`A1`, Phrase Bank / repeat-listening card video);
- BGM source applied;
- validations passed;
- key source/output paths;
- no external publishing performed.
