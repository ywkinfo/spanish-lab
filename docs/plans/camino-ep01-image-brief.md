# Español en el Camino — Ep01 "La idea" · Image-Generation Brief

> **Who executes this:** a human or external image model.
> **Who wrote this:** the designer agent.
> **Do not modify** any Python, Makefile, or pipeline files to act on this brief.

---

## Art style reference

Match the existing channel art exactly as seen in `assets/story/lucia_scene_*.png`:

- **Medium:** warm comic/graphic-novel illustration. Clean linework, soft cell shading, moderate detail in backgrounds, slightly painterly but never photorealistic.
- **Palette:** warm amber and terracotta mid-tones in interiors; cool blue-grey for metro/evening; rich warm gold for lamp/café light. Skin tones naturalistic within the illustration style.
- **Rendering:** well-defined but not harsh outlines; subtle rim lighting; backgrounds have enough detail to read as a real place without cluttering the foreground characters.
- **NOT:** anime, manga, watercolour sketch, photorealistic render, flat cartoon, pixel art.

The existing `lucia_scene_01_morning.png` (woman at balcony, terracotta tones, Madrid buildings) is the single clearest style target. Reference it for every prompt.

---

## Technical spec (all scenes)

- **Resolution:** 1920×1080 px
- **Aspect:** native 16:9 — compose FOR this ratio, do not generate square and crop
- **Format:** PNG
- **Safe area:** keep all plot-critical faces, props, and expressions in the **top ~65% of the frame** (top 702 px of 1080). The subtitle/caption panel occupies the bottom center. Nothing important below that line.
- **No baked-in text:** zero letters, words, or symbols drawn into the art. No credencial text, no journal handwriting, no signs with readable words. All text comes from captions.
- **Output folder:** `assets/images/camino_a2_ep01_la_idea/`

---

## Part 1 — Character reference sheets

Generate one reference sheet per character before producing any scene images. These sheets establish the canonical look that must remain consistent across all 42 episodes of the series. Each sheet should show the character from multiple angles (front, 3/4, back) against a neutral background in the series illustration style.

---

### REF-A: Lucía

**Prompt:**

Character reference sheet, three views (front, 3/4 turn, back), neutral warm-cream background. Illustration style matching warm comic graphic-novel art with soft cell shading and clean linework, same style as the provided reference image of a woman at a Madrid balcony.

Subject: Lucía, a Spanish woman, late 20s, medium build. Warm brown eyes, dark chestnut hair worn in a loose low bun — a few strands fall around her face. Expressive face with a thoughtful, slightly melancholic quality at rest; lights up when she smiles. Light olive complexion.

Wardrobe on the Camino: faded cornflower-blue lightweight hiking shirt (button-up, sleeves often rolled to elbows), charcoal grey hiking trousers, worn tan leather hiking boots. Slim black shoulder strap of a small water bottle visible. No hat in base reference.

Identifying prop: a small **burnished copper-orange enamel lapel pin** shaped like a vieira (scallop shell), worn on the left chest of her shirt. This pin appears in every scene she appears in — it is her consistent identifier.

Backpack: medium slate-blue hiking pack, about 40 L, worn on her back; visible in back view. Side pocket holds a reusable water bottle.

Show the character at roughly half-body (waist and above) in front and 3/4 views; show the backpack clearly in the back view. No background scenery — neutral cream or very light warm-grey.

Operator label — do NOT include in the generation prompt or render into the image; this is only a filing tag for you: "Lucía — referencia de personaje". (The sheet art itself must contain zero text, per the negative list.)

---

### REF-B: Diego

**Prompt:**

Character reference sheet, three views (front, 3/4 turn, back), neutral warm-cream background. Same illustration style: warm comic graphic-novel, soft cell shading, clean linework.

Subject: Diego, a Mexican man, early 30s, lean and slightly taller than average. Dark curly hair, kept short on the sides and a bit longer on top, often wind-tousled. Dark stubble. Warm dark brown eyes. Square jaw, easy smile. A natural ease in his posture — the outsider-insider guide archetype without being smug.

Wardrobe on the Camino: olive-green lightweight long-sleeve shirt (often with the collar open and sleeves pushed up), dark navy hiking trousers, sturdy dark brown leather boots well-worn at the toe. A small brass compass on a cord around his neck — visible at the open collar.

Identifying prop: the **brass compass on a cord** at his neck. This is his consistent identifier across all scenes.

Backpack: large burnt-sienna/rust-orange hiking pack, about 55 L — distinctly warmer in tone than Lucía's slate-blue pack. This colour difference is critical for identifying characters from behind.

Show half-body front and 3/4 views; full back view showing the rust-orange pack clearly. Neutral cream background.

Operator label — do NOT include in the prompt or render into the image; filing tag only: "Diego — referencia de personaje". (Sheet art contains zero text.)

---

### REF-C: Jin

**Prompt:**

Character reference sheet, three views (front, 3/4 turn, back), neutral warm-cream background. Same illustration style: warm comic graphic-novel, soft cell shading, clean linework.

Subject: Jin, a Korean man, late 20s, slender build, slightly shorter than Diego. Round face, dark straight hair cut in a neat side-parted style. Warm brown eyes behind thin wire-frame round glasses. A careful, attentive expression — he is always listening, slightly watchful, quietly curious. Gentle manner; not awkward, just precise.

Wardrobe on the Camino: light oatmeal-cream coloured technical fleece zip-up (or light quilted vest over a white base layer depending on weather), slate-grey hiking trousers, grey trail-running shoes. A small cream fabric notebook pouch clipped to the front of his pack's chest strap.

Identifying prop: a **small A6-size hardcover notebook with a deep teal/dark green cover**, kept either in hand or tucked in the front chest-strap pouch of his pack. This is the Cuaderno del peregrino — Jin's journal. It appears in every recap scene and whenever he is reflecting or writing. It must be instantly recognisable by its teal cover and slightly battered corners.

Backpack: charcoal-grey hiking pack, about 40 L — the darkest of the three packs. Side mesh pocket holds a water bottle. The cream notebook pouch on the chest strap is always visible.

Show half-body front and 3/4 views (glasses clearly visible); full back view showing the charcoal pack and the cream chest-strap pouch with the teal notebook poking out or tucked in. Neutral cream background.

Operator label — do NOT include in the prompt or render into the image; filing tag only: "Jin — referencia de personaje". (Sheet art contains zero text.)

---

## Part 2 — Scene images

Eight images for Ep01 "La idea". Filename targets are given for each. Drop all files into `assets/images/camino_a2_ep01_la_idea/`.

---

### Scene 01 — Cold-open: "Una tarde en el café"

**Filename:** `scene_01_cafe_terrace.png`

**Script beat:** Establishing still, no dialogue. Place first; no faces. Atmosphere only.

**Prompt:**

1920×1080 illustration, warm comic graphic-novel style matching the provided reference art. Exterior terrace of a small Spanish café in a medium-sized town, late afternoon golden-hour light. Stone or stucco building facade with wrought-iron balcony railing visible above. Terrace has four or five small round tables with wooden chairs. ONE table in focus in the mid-upper frame: on it, THREE ceramic coffee cups (two espresso cups and one café con leche mug), arranged naturally as if three people have just been sitting there. A slate-blue hiking pack hangs on the back of one chair; a rust-orange pack rests against the chair leg. The table fills the upper 60% of the frame. A vieira (scallop shell) the size of a palm rests against one of the cups — prominent, clearly recognisable, in the upper half of the frame. Afternoon sun casts long warm amber shadows across the terrace. Street beyond softly out of focus. No faces, no characters in frame. No text baked into the art.

Mood: warm, anticipatory, still. A moment just before something changes.

---

### Scene 02 — Intro/title beat: "La idea · Lucía, Diego y Jin"

**Filename:** `scene_02_three_backs.png`

**Script beat:** Title-card energy. Introduce the three lightly, per image rule: backs, not faces.

**Prompt:**

1920×1080 illustration, warm comic graphic-novel style. Interior of the same small Spanish café — warm amber walls, wooden furniture, a chalkboard menu on the wall (no readable text on the board). The three characters seen from slightly behind and to the side: Lucía (left, slate-blue pack on the chair beside her, copper-orange vieira pin visible on her shirt collar from this angle), Diego (centre-right, rust-orange pack beside him, brass compass cord at neck), Jin (right, charcoal pack on the chair, teal notebook on the table in front of him). They are seated at a café table, leaning slightly toward each other in conversation — animated, close, comfortable. Three coffee cups on the table. Light pours in from a window at mid-frame, catching the table warmly. Faces are NOT the focus — this is a 3/4-back angle showing the group dynamic and the three distinct backpacks. Plot-critical prop (the three cups and the teal notebook) all in the upper 60% of the frame. No text.

Mood: warmth, friendship, energy, the moment before something arrives.

---

### Scene 03 — The credencial arrives: "El sobre"

**Filename:** `scene_03_envelope_arrival.png`

**Script beat:** Lucía holds up a white envelope; the credencial is about to be revealed. Inciting event.

**Prompt:**

1920×1080 illustration, warm comic graphic-novel style. Same café interior. Lucía (from the waist up, upper-centre of frame) is holding up a white A5 envelope, turning it to show the others. Her expression is surprised and delighted — wide eyes, slight open-mouthed smile. The envelope is prominent in the upper-middle third of the frame. Behind her we see the suggestion of Diego's shoulder and Jin's face in profile (both just partially visible at the frame edges — do not show all three faces fully). The envelope should be clearly the visual subject: white, slightly worn at the edges, with the flap sealed. No stamps, no address text baked into the art. Lucía's copper-orange vieira pin is visible on her shirt. Warm afternoon café light. No text.

Mood: surprise, the moment a door opens.

---

### Scene 04 — Hesitation + credencial close-up: "La credencial del peregrino"

**Filename:** `scene_04_credencial_closeup.png`

**Script beat:** Close-up of the blank credencial + the vieira shell. This image runs under Diego's "¿Ochocientos kilómetros a pie?" lines and Lucía's first "Quiero hacer el Camino." The blank credencial IS the visual teach-point — keep it completely empty (no stamps, no text, no marks).

**Prompt:**

1920×1080 illustration, warm comic graphic-novel style. Close-up still-life composition. A blank credencial del peregrino — a folded paper booklet about the size of an A5 passport, light buff/cream coloured card, accordion-folded, lying open to show two facing blank stamp-grid pages. The stamp boxes are visible as a faint grid but completely empty — no stamps, no writing, no text of any kind. Beside the credencial, a real vieira (scallop shell) with the characteristic ridged fan shape and ivory-cream colour, slightly weathered. Both objects rest on a rough wooden café table. A few crumbs of sugar and a coffee-cup ring stain on the table surface for texture. Warm afternoon window light from the upper left. These objects occupy the upper 65% of the frame; the lower third is just the warm wooden table surface fading to the frame edge. No text, no stamps, no markings on the credencial. No characters in frame.

Mood: quiet gravity, potential, a blank page about to be filled.

---

### Scene 05 — Each reason surfaces: "Cada uno tiene su razón"

**Filename:** `scene_05_reasons_table.png`

**Script beat:** Diego and Jin voice their reasons. The money/time worry is aired and answered. All three are present but framed to avoid all-three-facing-front.

**Prompt:**

1920×1080 illustration, warm comic graphic-novel style. Café interior, the same table. Camera angle: from one side of the table, showing Diego and Jin in 3/4 profile facing each other across the table. Diego (left side, leaning forward on his elbows, animated, the rust-orange pack visible behind his chair, brass compass at his open collar) is speaking — mid-sentence expression, hand gesture. Jin (right side, slightly leaning back, expression thoughtful/worried, his teal notebook open on the table with a pen resting in it) is listening. Lucía is partially visible at the far left edge of frame — just her arm, her sleeve, and the copper vieira pin — not her face. The teal notebook and Diego's hand gesture are the key visual anchors in the upper 60% of the frame. Warm café light. No text on the notebook or anywhere.

Mood: the real conversation — stakes, doubt, reasons coming to the surface.

---

### Scene 06 — The doubt softens: "Juntos da menos miedo"

**Filename:** `scene_06_together.png`

**Script beat:** Lucía pulls the group together — together it is less scary. Warmth of solidarity.

**Prompt:**

1920×1080 illustration, warm comic graphic-novel style. Café interior, same table, late afternoon light deepening toward early evening gold. This time Lucía is visible (3/4 angle, not full front) reaching across the table, hand open toward the centre. Diego is to her right, now leaning in, his posture open and warm. Jin is to the left, glasses catching the warm light, expression shifting from worry to quiet resolve. The three are physically closer than before — leaning toward the table's centre. The three coffee cups remain on the table. The vieira shell is also on the table, slightly more prominent than before. No face is shown in full frontal portrait — all are in 3/4 or slightly angled. The copper vieira pin on Lucía's shirt, the brass compass at Diego's collar, and Jin's teal notebook (closed, beside his cup) are all visible in the upper 60% of the frame. No text.

Mood: the group closing, warmth, the fear diminishing.

---

### Scene 07 — The decision: "Lo hacemos"

**Filename:** `scene_07_decision.png`

**Script beat:** They decide. Emotional close. First "Buen Camino." End on warmth, the moment crystallised.

**Prompt:**

1920×1080 illustration, warm comic graphic-novel style. Exterior of the café terrace (callback to Scene 01, but now early evening — warmer, lower sun, amber-orange glow). The three are standing together, seen from slightly behind and angled — backs and 3/4 profiles, all three backpacks visible and coloured distinctly: Lucía's slate-blue (left), Diego's rust-orange (centre/right), Jin's charcoal (right). They are grouped close, arms near each other — the suggestion of a group huddle or a moment of laughter and resolve. The vieira shell (the one from Scene 03) is held by Lucía — visible from the angle, held at about chest height, in the upper 60% of frame. The evening street behind them is soft and warm. No faces showing fully. No text.

Mood: decision made, lightness, the adventure beginning to feel real.

---

### Scene 08 — Jin's cuaderno: "El cuaderno de Jin"

**Filename:** `scene_08_cuaderno_closeup.png`

**Script beat:** Jin's journal = the recap card. The journal page must be BLANK/LINED so the key sentence rides the caption, not baked into the art. This image runs under Jin's grammar explanation and the episode's key sentence display.

**Prompt:**

1920×1080 illustration, warm comic graphic-novel style. Close-up still-life, night-time setting. Jin's teal hardcover notebook lies open on a wooden desk. The two facing pages show clean horizontal ruled lines — completely blank, no writing, no text, no marks. The teal cover is visible at the edges of the open spine. A fine-tip pen or pencil rests across the lower right page. A small warm pool of light from a desk lamp (the lamp head just visible at the upper-right corner of frame) falls across the notebook — warm amber light on the pages, cooler shadows outside the pool. Beside the notebook, slightly out of focus: a glass of water and Jin's wire-frame glasses folded shut. The open notebook pages occupy the upper 65% of the frame. The desk surface below fades into warm shadow in the lower third. No writing, no text, no numbers baked anywhere into the art.

Mood: quiet night, reflection, anticipation — a page about to be written.

---

## Part 3 — Continuity checklist

The following elements must be identical across every image they appear in. Print this list and verify before approving any scene.

| Element | Description | Must appear in |
|---|---|---|
| Lucía's vieira pin | Copper-orange enamel scallop-shell lapel pin, left chest | Scenes 02, 03, 05, 06 |
| Lucía's pack | Slate-blue, ~40 L, medium size | Scenes 01 (on chair), 02, 07 |
| Diego's compass | Brass compass on a cord, worn at open collar | Scenes 02, 05, 06, 07 |
| Diego's pack | Rust-orange/burnt-sienna, ~55 L, larger than the others | Scenes 01 (on chair), 02, 07 |
| Jin's glasses | Thin wire-frame round/oval glasses | Scenes 02, 05, 06, 07 |
| Jin's teal notebook | A6 hardcover, deep teal/dark-green cover, slightly battered | Scenes 02 (on table), 05 (open), 06 (closed by cup), 08 (close-up) |
| Jin's pack | Charcoal grey, ~40 L with cream chest-strap pouch | Scenes 01 (implied), 02, 07 |
| Vieira shell (prop) | Ivory-cream, ridged fan, palm-sized, slightly weathered | Scenes 01 (on café table), 03/04 (close-up), 06 (table), 07 (in Lucía's hand) |
| Three coffee cups | Two small espresso, one café con leche mug | Scenes 01, 02, 05, 06 |
| Café setting | Same small warm-amber interior / terrace throughout Scenes 01–07 | Scenes 01–07 |

---

## Part 4 — Negative list

These things must NOT appear in any scene image.

- **No all-three-facing-front composition.** Never show Lucía, Diego, and Jin all facing directly at the camera at the same time. Use backs, 3/4 profiles, over-the-shoulder angles.
- **No baked-in text of any kind.** No handwriting on the credencial. No text on the notebook pages. No words on the chalkboard. No readable stamps, addresses, labels. All text arrives via the caption renderer.
- **No stamps on the credencial.** Scene 04 credencial must be completely blank — zero marks. (Stamps are the series progress motif, earned episode by episode; they cannot appear in Ep01.)
- **No recognisable real-world logos or trademarks** on clothing, bags, or objects.
- **No English text** anywhere in the art.
- **No anime/manga stylisation.** The style is warm illustrated graphic-novel (reference: `assets/story/lucia_scene_01_morning.png`), not anime.
- **No photorealism.** Do not generate photographs or photorealistic renders.
- **No faces below the caption safe area.** Any character face must sit in the top 65% of the 1080px frame height (above ~702 px from the top).

---

## Part 5 — Notes on Scenes 04 and 08

**Scene 04 (Credencial close-up, `scene_04_credencial_closeup.png`):** This image is used specifically because the diary renderer has no custom overlay type in v1. The empty stamp-grid pages draw the viewer's eye to the caption bar, where the spoken lines play. The blank credencial IS the scene's visual point. Do not add any marks, stamps, script, or even a faint "Credencial del Peregrino" title header baked into the art — the caption carries all of that.

**Scene 08 (Cuaderno close-up, `scene_08_cuaderno_closeup.png`):** Same principle. The lined but blank pages let the caption deliver the grammar recap ("Quiero hacer el Camino" / "Me gustaría hacerlo" / vocabulary list). The image's job is atmosphere and visual anchor, not information delivery. Blank ruled lines are the correct output — do not add Jin's handwriting to the art even if the prompt is interpreted that way.
