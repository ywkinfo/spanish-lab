# Ep.21 `A veces me levanto temprano` thumbnail reference

Use this when Peter asks for Spanish Lab Ep.21 thumbnail/source-art continuation after the Ep.1 phrase-bank review.

## Content decision

- Episode: Ep.21
- Level: `Español A1+`
- Main title direction: `A veces me levanto temprano 🌅 가끔 일찍 일어나요 | Español A1+ · Ep.21`
- One learning point: `A veces + presente` = `가끔 ~해요`
- Continuity: Peter suggested combining `a veces` with underused phrases from Ep.1's 50-phrase bank. The recommended subset was the routine/daily-life group, especially:
  - `Me levanto temprano.`
  - `Tengo tiempo.`
  - `Voy al trabajo.`
  - `Voy a estudiar español.`
- Rationale: This recycles an underused Ep.1 routine expression without making another broad phrase list.

## Thumbnail source-art prompt pattern

Generate a direct 16:9/landscape thumbnail background with:

- warm clean morning apartment / small study corner in Madrid;
- Jin, the Korean learner, on the right side;
- early-morning study vibe with coffee and notebook;
- left 45% clean negative space for overlay;
- warm cream/coral tones and subtle teal accents;
- no text, logos, watermarks, cropped head, or clutter.

Session source image path used:

```text
/opt/data/cache/images/openai_codex_gpt-image-2-medium_20260522_111108_94bbc02c.png
```

## Composition pattern

Use the established Ep.7-style overlay:

- full-bleed blurred/darkened background;
- sharp right-side scene faded into the text area;
- cream rounded text panel on the left;
- coral badge: `Español A1+ · Ep.21`;
- main Spanish overlay:
  - `A veces`
  - `me levanto`
  - `temprano`
- Korean pill: `가끔 일찍 일어나요`;
- teal pill: `가끔 = A veces`;
- small footer note: `A veces + 현재형`.

## Delivered paths from the session

```text
/opt/data/repos/spanish-lab/images/ep21-a-veces-me-levanto-temprano-source.png
/opt/data/repos/spanish-lab/thumbs/a1-ep21-a-veces-me-levanto-temprano.jpg
/opt/data/repos/spanish-lab/output/thumbs/frases-a1-ep21-a-veces-me-levanto-temprano.jpg
/opt/data/repos/spanish-lab/output/qa/a-veces-me-levanto-temprano/thumbnail.jpg
/opt/data/repos/spanish-lab/scripts/create_ep21_thumbnail.py
```

## QA criteria

Before handoff, verify:

- Spanish and Korean text are readable at thumbnail size;
- no text clipping or overlap;
- Jin's head/face and hands are not awkwardly cropped;
- no generated fake readable text, logos, or watermarks;
- left panel and right character are visually balanced;
- no external publishing occurred.

Run `git status --short` for the source image, repo thumbnail, and script. Note that `output/` artifacts may be gitignored and not appear in status even though they are ready to deliver.
