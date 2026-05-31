# Ep.17 `¿Qué llevas?` scenario + thumbnail reference

Use this as a reference for future Spanish Lab A1 story-card episodes that connect weather to clothing and need per-slide object imagery.

## Episode direction
- Working module/slug: `que_llevas_a1` / `que-llevas`
- Episode: `EPISODE = 17`, `LEVEL = "A1"`, `RENDER_TYPE = "cards"`
- One learning point: exactly one point — `Llevo + clothing noun`.
- Natural continuation from Ep.16 weather: `Hace frío -> Llevo una chaqueta`; `Hace sol -> Llevo gafas de sol`.
- Keep the `llevar` explanation short: for A1, explain that it can mean “wear” or “carry” depending on the object, but do not turn this into a second grammar lesson.

## Slide/object-image scenario pattern
When Peter asks to include clothing images on each slide, use object cards as visual support:
- Show one clean clothing object card per key learning slide, usually right side or lower-right.
- Use transparent/flat illustrated cutouts on a warm off-white rounded card with soft shadow.
- Do not use shopping/catalog-style visuals, brand logos, or fake readable text.
- Keep object images as vocabulary support only; the learning point remains `Llevo + noun`.

Recommended clothing set:
- `una chaqueta` — light jacket card
- `un abrigo` — coat card
- `una camiseta` — T-shirt card
- `unos zapatos` — shoes card
- `unas gafas de sol` — sunglasses card
- `un paraguas` — umbrella card

Good scenario blocks:
1. Intro: `¿Qué llevas?` / `오늘 뭐 입어요?`, small preview row of clothing.
2. Question pattern: `¿Qué llevas?`
3. Main phrase: `Llevo una chaqueta.`
4. Weather connection: `Hace frío. Llevo un abrigo/una chaqueta.`
5. Sunny connection: `Hace sol. Llevo gafas de sol.`
6. Carry example: `Llevo un paraguas.`
7. Shadowing: jacket, coat, sunglasses.
8. Mini quiz and recap.

## Thumbnail source-art prompt used
Generate a direct 16:9/landscape source image with right-side characters and left-side negative space:

```text
Spanish Lab YouTube thumbnail background, 16:9 landscape. A warm clean Madrid street in spring, bright but slightly cool weather. On the RIGHT side: three friendly recurring educational characters, a Korean beginner learner Jin wearing a light jacket and comfortable shoes, a Spanish woman Lucía wearing sunglasses, and a Spanish guide Diego holding a small folded umbrella. Leave the entire LEFT 45% as clean uncluttered negative space for title overlay. Modern friendly semi-realistic illustration, warm colors, clear clothing details, no readable text, no logos, no watermarks, no cropped heads, no clutter, high quality language-learning channel style.
```

Session source image path:
- `/opt/data/repos/spanish-lab/images/ep17-que-llevas-source.png`

## Thumbnail overlay pattern
Follow Ep.7-style layout:
- left cream rounded panel;
- coral badge: `Español A1 · Ep.17`;
- large stroked title: `¿Qué llevas?`;
- Korean pill: `오늘 뭐 입어요?`;
- teal phrase pill: `Llevo una chaqueta`;
- small note: `스페인어 A1 · 옷 표현`.

Delivered thumbnail paths:
- `/opt/data/repos/spanish-lab/thumbs/a1-ep17-que-llevas.jpg`
- `/opt/data/repos/spanish-lab/output/thumbs/frases-a1-ep17-que-llevas.jpg`

## Implementation notes
- If system Python lacks Pillow, use the repo virtualenv: `.venv/bin/python`.
- Crop generated `1536x1024` source to 16:9, then resize to `1280x720`.
- Save both source repo thumbnail and publish-output thumbnail so MEDIA delivery and repo state stay aligned.

## QA criteria used
- Spanish title and phrase pill readable.
- Korean pill readable with Noto Sans KR.
- Title panel does not overlap characters.
- Characters' heads/faces are not cropped.
- Clothing cues are visible: Jin jacket, Lucía sunglasses, Diego umbrella.
- No fake readable signs/logos/watermarks.
- Output is suitable as a YouTube thumbnail draft, pending Peter approval.
