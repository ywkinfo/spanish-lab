# Ep.9 directions thumbnail notes

Session-specific guidance for the A1 Ep.9 `¿Dónde está el metro?` thumbnail and similar directions/travel episodes.

## Scenario and character continuity
- For Ep.9 directions, a strong visual concept is a warm Madrid side street/alley after the café episode.
- Show Jin asking for directions while Lucía gestures clearly toward the route; Diego can stand nearby as the friendly guide/supporting speaker.
- If the user says “Peter” in this context, clarify only if needed; for new A1 story episodes from Ep.8 onward, prefer the display name **Jin** for the Korean learner and use **Diego** as the second guide/friend rather than adding Peter as a separate new character.

## Source art prompt pattern
Use a 16:9/landscape source image with characters on the right and clean negative space on the left:

> A clean, warm, modern illustration for a Spanish Lab A1 YouTube thumbnail. Scene: a narrow charming street in Madrid, warm afternoon light, cozy Spanish buildings and a small café entrance in the background. Three friendly young adults are standing together on the right side: Jin, a Korean learner, asks a question with a curious expression; Lucía, a friendly Spanish woman, gestures clearly to the right as if giving directions; Diego stands beside them smiling and helping. The scene suggests asking for directions to the metro in Madrid. Warm beige, terracotta, and soft blue palette, clean vector-like digital illustration, polished educational YouTube thumbnail style, high contrast. Leave clear empty space on the left for large title text. No text, no letters, no numbers, no logos, no watermark, no readable signs.

## Ep.7/Ep.8-style thumbnail composition
Recommended final overlay:
- left cream rounded panel with shadow;
- coral badge: `Español A1 · Ep.9`;
- large outlined title split into two lines: `¿Dónde está` / `el metro?`;
- Korean white pill: `길 묻기`;
- teal bottom pill: keep short enough to avoid clipping. `Todo recto · Derecha` fit better than `Todo recto · A la derecha` in one 1280x720 layout.

Known paths used in the first Ep.9 thumbnail draft:
- Source art: `assets/generated/madrid-street-directions-thumbnail-source.png`
- Repo thumbnail: `thumbs/a1-donde-esta-el-metro.jpg`
- Publish thumbnail: `output/thumbs/frases-a1-ep09-donde-esta-el-metro.jpg`
- Composition script: `scripts/make_ep09_thumbnail_ep7_style.py`

## QA criteria
- Spanish and Korean text are readable at thumbnail size; Hangul renders correctly.
- The teal bottom pill text is not clipped at the left or right edge.
- Character heads/hair and Lucía's pointing hand are not cropped in a distracting way.
- Madrid street / directions vibe is obvious.
- No readable accidental generated text, logos, numbers, or watermarks.
- The left panel should not cover the characters' faces; character bodies may be partially behind the panel if faces and gesture remain clear.
