# Español en el Camino — Ep02 "La ruta" · Image-Generation Brief

> **Who executes this:** a human or external image model.
> **Who wrote this:** the designer agent.
> **Do not modify** any Python, Makefile, or pipeline files to act on this brief.
> **Script source:** [camino-ep02-la-ruta-brief.md](camino-ep02-la-ruta-brief.md) (LINGUIST-APPROVED),
> §7 "Scene titles + per-scene visual one-liners" and §10 "For image sourcing".
> **Structural pattern:** [camino-ep01-image-brief.md](camino-ep01-image-brief.md).

---

## Art style reference

Match the existing channel art exactly as seen in `assets/images/camino_a2_ep01_la_idea/*.png`:

- **Medium:** warm comic/graphic-novel illustration. Clean linework, soft cell shading, moderate detail in backgrounds, slightly painterly but never photorealistic.
- **Palette:** warm amber and terracotta mid-tones in interiors; cool blue-grey for metro/evening; rich warm gold for lamp/café light. Skin tones naturalistic within the illustration style.
- **Rendering:** well-defined but not harsh outlines; subtle rim lighting; backgrounds have enough detail to read as a real place without cluttering the foreground characters.
- **NOT:** anime, manga, watercolour sketch, photorealistic render, flat cartoon, pixel art.

The existing `camino_a2_ep01_la_idea/scene_01_cafe_terrace.png` (café terrace, terracotta tones, three backpacks) and `scene_08_cuaderno_closeup.png` (blank teal notebook under lamplight) are the clearest style targets for this episode's interior-evening palette and its notebook close-up respectively. Reference both for every prompt below.

---

## Technical spec (all scenes)

- **Resolution:** 1920×1080 px
- **Aspect:** native 16:9 — compose FOR this ratio, do not generate square and crop
- **Format:** PNG
- **Safe area:** keep all plot-critical faces, props, and expressions in the **top ~65% of the frame** (top 702 px of 1080). The subtitle/caption panel occupies the bottom center. Nothing important below that line.
- **No baked-in text:** zero letters, words, or symbols drawn into the art. No map labels, no guidebook titles, no journal handwriting, no signs with readable words. All text comes from captions.
- **Output folder:** `assets/images/camino_a2_ep02_la_ruta/`

### Episode-specific technical rule — the map and guidebook must be illegible

This episode's central prop is a **large paper map of the Camino routes** plus a **guidebook**.
Both objects appear across most scenes and are near-camera, so the illegibility rule needs to be
stated explicitly and enforced every time they appear:

- The map may show: route lines in varied colors (e.g., a warm terracotta line, a cooler blue-grey line, a muted olive line for the three routes), small dots for towns, a stylised coastline, a small shell/vieira icon or two, faint decorative border flourishes, a compass rose graphic (no letters on it).
- The map must NOT show: any readable place names, any readable route names, any legible numbers or distances, any legible legend text. If small marks suggest "labels," they must read as abstract squiggles/scribble-marks, not letters — a viewer must not be able to identify or half-read a single word.
- The guidebook cover and any visible interior pages follow the same rule: cover art/texture/color is fine (e.g., a worn cloth or paper cover, a small line-drawing icon), but zero legible title text, zero legible body text. Any page texture should read as blank or as abstract fine ruled lines only.
- This rule is repeated in each relevant scene prompt below — do not skip it when generating.

---

## Part 1 — Character reference sheets

**Reuse the Ep01 reference sheets. Do not regenerate.** Ep02 uses the same three canonical
character designs already established in `docs/plans/camino-ep01-image-brief.md` Part 1
(REF-A Lucía, REF-B Diego, REF-C Jin). Generate new reference art only if an operator needs a
fresh render of the same spec — the character descriptions below are NOT new designs, they are
the required identifying anchors to repeat inside each Ep02 scene prompt so continuity holds:

- **Lucía:** dark chestnut hair in a loose low bun, a few strands loose; light olive complexion; warm brown eyes. Identifying prop: burnished **copper-orange enamel vieira (scallop-shell) lapel pin**, worn left chest. On the Camino she wears a faded cornflower-blue shirt; in this episode's indoor evening setting she may wear a casual home variant (e.g., the same cornflower-blue shirt with sleeves rolled, or a soft cream/blue house cardigan) as long as the vieira pin stays visible somewhere on her person or is resting beside her on the table.
- **Diego:** Mexican man, early 30s, dark curly hair (short sides, longer/tousled on top), dark stubble, warm dark brown eyes, square jaw. Identifying prop: **brass compass on a cord** at his neck, visible at an open collar. On the Camino he wears olive-green; indoors this evening a similar olive-green casual shirt (collar open) is correct, or a simple dark henley — keep the brass compass cord visible at the neck either way.
- **Jin:** Korean man, late 20s, slender, round face, neat side-parted dark straight hair, **thin wire-frame round glasses**. Identifying prop: **small A6 hardcover notebook, deep teal/dark-green cover, slightly battered corners** — the Cuaderno del peregrino. On the Camino he wears oatmeal-cream fleece; indoors this evening the same oatmeal-cream fleece or a similar soft cream/oatmeal knit is correct. The teal notebook must be visible in-frame whenever he appears with hands free.

Operator label — do NOT include in any generation prompt or render into the image; filing tag
only: "Referencia de personaje reutilizada de Ep01."

---

## Part 2 — Scene images

Eight images for Ep02 "La ruta." Filenames match exactly what `projects/camino_a2_ep02_la_ruta.py`
references via its `_BASE = "assets/images/camino_a2_ep02_la_ruta"` + `image_path` fields (the
producer module landed while this brief was being written — see "Filename reconciliation note" at
the end of this document for how the two were reconciled). Drop all files into
`assets/images/camino_a2_ep02_la_ruta/`.

Setting for all of Scenes 1–7: **Lucía's flat, evening**, warm lamp light (rich warm gold, matching
Ep01's lamp-light palette), a cozy small Spanish living-room/kitchen-table space. Central table
prop: the large paper Camino map spread out, the guidebook resting nearby, two ceramic mugs of
tea/coffee. The credencial from Ep01 (light buff/cream folded booklet) may appear once as a subtle
continuity nod, resting to one side of the table — not a focal prop this episode.

---

### Scene 01 — Cold-open: "El mapa sobre la mesa"

**Filename:** `scene_01_map_on_table.png`

**Script beat:** Establishing still, no dialogue. Place first; no faces. Atmosphere only.

**Prompt:**

1920×1080 illustration, warm comic graphic-novel style matching the provided reference art (interior evening palette as in `camino_a2_ep01_la_idea/scene_08_cuaderno_closeup.png`). Interior of a small, cozy Spanish flat's living room in the evening. A wooden dining table fills the lower-centre and upper-centre of the frame, seen from a three-quarter overhead angle. On the table: a LARGE paper map, unfolded and spread out, showing several colored route lines converging toward one corner (suggesting Santiago), small town dots, a faint stylised coastline, and one or two small shell/vieira icon marks — the map has NO readable place names, NO legible route labels, NO legible numbers; any label-like marks are abstract illegible squiggles only. Beside the map, a closed guidebook with a worn cloth-textured cover and a small line-drawing icon on it — no legible title text, no legible body text anywhere on it. Two ceramic mugs of tea sit near the map's edge, steam gently rising from one. A warm table lamp glows off-frame right, casting rich warm gold light across the map and table, softer amber ambient light filling the room behind (a sofa, a bookshelf, a window with evening blue-grey outside, softly out of focus). The map and guidebook occupy the upper 65% of the frame. No characters, no faces. No baked-in text anywhere in the art.

Mood: quiet, anticipatory, a decision about to be made.

---

### Scene 02 — Title beat: "La ruta"

**Filename:** `scene_02_three_backs_over_map.png`

**Script beat:** Title-card energy. Reintroduce the three lightly — backs and hands, not faces.

**Prompt:**

1920×1080 illustration, warm comic graphic-novel style. Same cozy flat interior, evening, warm lamp light. Camera close to table height, looking across the spread map toward the three friends seated around it — but framed so only their hands, forearms, and the tops of their shoulders/backs are the focus, faces only partially visible at the very top edge of frame or turned away. Lucía's hand (left) rests near the map's edge, her copper-orange vieira pin just visible on her sleeve/collar at the frame's upper edge. Diego's hand (centre) is planted on the map, fingers slightly spread as if about to point; his brass compass cord is visible at his open collar, glimpsed at the upper-frame edge. Jin's hands (right) rest near his teal notebook, which lies closed beside his mug at the table edge. Two mugs of tea are visible near the map. The map itself (route lines, town dots, coastline, shell icon — no legible text of any kind) fills the centre of the frame. Warm gold lamp light pools across the table; the room behind fades into soft amber shadow. Plot-critical props (the map, the teal notebook, the mugs) occupy the upper 60% of the frame. No full faces shown. No text anywhere.

Mood: warmth, familiarity, a group settling back into each other's company.

---

### Scene 03 — Diego performs the expert: "Hay muchos caminos"

**Filename:** `scene_03_diego_points_at_routes.png`

**Script beat:** Diego leans over the map and points, laying out the three route options from the guidebook. First comparative lands.

**Prompt:**

1920×1080 illustration, warm comic graphic-novel style. Same flat interior, evening, warm lamp light. Diego is the visual anchor: seen from a 3/4 angle, leaning over the table, one hand pointing decisively at a spot on the spread map where several route lines branch apart (three visibly distinct colored lines diverging — suggesting the Francés, Norte, and Portugués routes — but with NO legible route names or labels anywhere, only abstract illegible squiggle-marks if any label-like shapes appear at all). Diego's dark curly hair, stubble, and the brass compass on its cord at his open olive-green collar are all clearly visible; his expression is animated, engaged, explaining. The open guidebook lies beside the map at his elbow, showing a spread with a faint illustrated line-drawing (e.g., a simple map or shell motif) but zero legible text, cover or interior. Lucía and Jin are present only at the frame edges — a shoulder, an arm, the suggestion of listening postures — not full faces. Diego's pointing hand and face sit in the upper 60% of frame. Warm gold lamp light catches the map and guidebook. No text baked into the art anywhere.

Mood: engaged, informative, the options laid bare — Diego enjoying his moment as the informed one.

---

### Scene 04 — Jin worries, the Norte is set aside: "¿Demasiado largo?"

**Filename:** `scene_04_jin_worried_over_map.png`

**Script beat:** Jin fears the Francés is too long/expensive; Diego sets the Norte aside on difficulty grounds.

**Prompt:**

1920×1080 illustration, warm comic graphic-novel style. Same flat interior, evening, warm lamp light. Jin is the visual anchor, framed from a 3/4 angle looking down at the map, one finger tracing along one of the illegible colored route lines — his expression is worried, brow slightly furrowed, thoughtful concern. His wire-frame round glasses catch a glint of warm lamp light; his oatmeal-cream fleece is visible at the shoulders. Diego is partially visible across the table (upper frame edge or soft focus), mid-gesture as if setting a different route line aside with an open hand — a "let's rule this one out" gesture. The map (with its illegible squiggle-marks standing in for any labels, and no readable text or numbers anywhere) remains the shared visual centre, its branching route lines clearly visible. Two mugs of tea sit nearby. Jin's tracing finger and worried expression occupy the upper 65% of frame. Warm gold lamp light, soft amber room behind. No text of any kind baked into the art.

Mood: concern surfacing, a real question on the table, warmth still present underneath the worry.

---

### Scene 05 — Lucía's quiet pull: "Yo quiero el más largo"

**Filename:** `scene_05_lucia_over_map.png`

**Script beat:** The Norte is out; between Francés and Portugués, Lucía quietly wants the longest route — grief seed, implied only.

**Prompt:**

1920×1080 illustration, warm comic graphic-novel style. Same flat interior, evening, warm lamp light — light now a touch softer/lower, deepening the mood slightly. Lucía is the visual anchor: seen from a 3/4 angle, looking down at the map with a quiet, private expression — not sad exactly, but distant, thoughtful, a little wistful. Her dark chestnut low bun and the copper-orange vieira pin on her collar are clearly visible. She holds a mug of tea in one hand near her chest; her other hand rests lightly near the longest illegible colored route line on the map (no readable text or numbers on the map, only abstract illegible marks if any). Diego and Jin are present only as soft out-of-focus presences at the frame edges — shoulders, not faces. The map's branching lines and Lucía's contemplative expression occupy the upper 65% of frame. Warm gold lamp light catches her face gently; the room behind is soft amber shadow. No text baked into the art anywhere.

Mood: quiet, private, a small ache under a practical conversation — the moment the audience senses she wants this for a reason she hasn't said aloud.

---

### Scene 06 — The route takes shape: "El más largo, pero el más bonito"

**Filename:** `scene_06_three_closer_over_map.png`

**Script beat:** They converge; Diego names the key sentence; the group leans in warmer.

**Prompt:**

1920×1080 illustration, warm comic graphic-novel style. Same flat interior, evening, warm lamp light glowing rich and full. All three are visibly closer together over the table now than in earlier scenes — leaning in toward the map's centre, a warmer, more resolved energy in their postures. Diego (centre or left, in 3/4 profile) has one finger tapping a specific illegible colored route line on the map — decisive, pleased. Lucía (opposite or beside him, partial profile) is leaning in too, a small warm smile emerging. Jin (to one side, partial profile, glasses catching lamplight) looks more at ease than in Scene 04, his teal notebook now open beside his mug. No character shows a full frontal face — use 3/4 angles and careful staging so all three can be present without an all-facing-camera composition. The map (illegible squiggle-marks only, no readable labels/numbers/names anywhere) remains the shared visual centre with Diego's tapping finger drawing the eye. The scene's props (map, tapping hand, teal notebook, mugs) occupy the upper 60% of frame. Warm gold lamp light fills the space. No text baked into the art.

Mood: convergence, warmth, the group settling into a shared decision together.

---

### Scene 07 — The decision: "Vamos por el Francés"

**Filename:** `scene_07_marking_route_decision.png`

**Script beat:** Decision beat — a pen marking the route on the map, three hands near it, soft smiles.

**Prompt:**

1920×1080 illustration, warm comic graphic-novel style. Same flat interior, evening, warm lamp light at its fullest, golden glow. Close-mid framing on the map's surface: a hand (Diego's, holding a simple pen) is in the act of tracing/marking along one illegible colored route line — the pen tip touching the map, a small fresh mark just being made (still entirely illegible — a soft line stroke, not a word or letter). Around this focal point, the other two hands rest nearby on the table's edge — Lucía's hand with a glimpse of the copper-orange vieira pin on her cuff/sleeve, Jin's hand near his open teal notebook. All three heads/shoulders are visible at the upper frame edge in soft 3/4 or profile angles, expressions warm and settled — the suggestion of smiles, ease, a decision made together. The map's full spread (branching illegible route lines, town dots, coastline, shell icon) remains visible beneath the marking hand. Warm gold lamp light glows across the whole table. The marking hand and the three visible partial faces sit within the upper 65% of frame. No text or legible marks baked into the art anywhere — the fresh pen stroke is a plain illegible line, not a letter.

Mood: resolve, quiet celebration, the adventure becoming real and specific.

---

### Scene 08 — Jin's cuaderno: "El cuaderno de Jin"

**Filename:** `scene_08_cuaderno_closeup.png`

**Script beat:** Jin's journal = the recap card. Night-time desk framing, distinct room from Scene 08 of Ep01 but the same visual family. The notebook shows illegible handwriting squiggles only (a deliberate variation from Ep01's fully blank notebook — this is now Jin's second entry, so faint scribble marks are appropriate, but must remain completely non-readable).

**Prompt:**

1920×1080 illustration, warm comic graphic-novel style, matching the palette and framing family of `camino_a2_ep01_la_idea/scene_08_cuaderno_closeup.png` (night desk, warm lamp pool of light, cooler shadow outside it) but staged as a distinct room/desk arrangement — a different small corner of Jin's own room, not an identical repeat composition. Close-up still-life, night-time. Jin's teal hardcover A6 notebook lies open on a wooden desk surface, its deep teal cover visible at the spine edges, corners slightly battered/soft with wear. The two facing pages show fine horizontal ruled lines with a SMALL amount of handwriting-like content on the upper portion of the left page only — rendered strictly as abstract illegible squiggles/scribble-marks that read as "handwriting from a distance," with zero actual letters, zero legible words, zero legible numbers. The rest of both pages remain empty ruled lines. A simple pen rests across the lower right page. A warm pool of light from a desk lamp (lamp head visible at the upper corner of frame) washes warm amber light across the notebook; cooler shadow surrounds it. Beside the notebook, softly out of focus: Jin's folded wire-frame glasses and a glass of water. Very faintly, further back and out of focus in the deep background, the suggestion of the paper map rolled or folded on a shelf — a continuity nod, not a focal object. The open notebook occupies the upper 65% of frame; the desk fades to warm shadow below. No legible writing, no legible numbers, no legible words baked anywhere into the art — illegible squiggles only.

Mood: quiet night, satisfaction, a small ritual of writing down what was learned.

---

## Part 3 — Continuity checklist

| Element | Description | Must appear in |
|---|---|---|
| Lucía's vieira pin | Copper-orange enamel scallop-shell lapel pin, visible on collar/sleeve | Scenes 02, 05, 07 |
| Diego's compass | Brass compass on a cord, worn at open collar | Scenes 02, 03, 04, 06 |
| Jin's glasses | Thin wire-frame round glasses | Scenes 02, 04, 06, 08 |
| Jin's teal notebook | A6 hardcover, deep teal/dark-green cover, slightly battered | Scenes 02 (closed), 06 (open), 08 (open, close-up with illegible squiggles) |
| The paper map | Large spread map, colored illegible route lines, town dots, coastline, shell icon, NO readable text | Scenes 01–07 (central prop); faint background nod in Scene 08 |
| The guidebook | Worn cloth/paper cover, small line-drawing icon only, NO readable title/body text | Scenes 01, 03 |
| Two mugs of tea/coffee | Ceramic mugs, steam optional | Scenes 01, 02, 04, 05, 07 |
| Credencial (continuity nod) | Light buff/cream folded booklet from Ep01, resting to one side | Optional single appearance, Scene 01 or 02 (not a focal prop) |
| Flat/evening setting | Same cozy Spanish flat interior, warm gold lamp light throughout | Scenes 01–07 |

---

## Part 4 — Negative list

These things must NOT appear in any scene image.

- **No all-three-facing-front composition.** Never show Lucía, Diego, and Jin all facing directly at the camera at the same time. Use backs, 3/4 profiles, over-the-shoulder angles, hands-over-map framing.
- **No baked-in text of any kind.** No readable place names, route names, numbers, or legend text on the map. No readable title or body text on the guidebook. No legible handwriting on Jin's notebook (Scene 08's "handwriting" must be illegible squiggles only). All actual text arrives via the caption renderer.
- **No legible map or guidebook content, ever.** This is the episode's single most important negative constraint — reread the "Episode-specific technical rule" above before generating any scene that includes the map or guidebook.
- **No recognisable real-world logos or trademarks** on clothing, bags, mugs, the map, or the guidebook.
- **No English text** anywhere in the art.
- **No anime/manga stylisation.** The style is warm illustrated graphic-novel (reference: `assets/images/camino_a2_ep01_la_idea/scene_01_cafe_terrace.png` and `scene_08_cuaderno_closeup.png`), not anime.
- **No photorealism.** Do not generate photographs or photorealistic renders.
- **No faces below the caption safe area.** Any character face must sit in the top 65% of the 1080px frame height (above ~702 px from the top).

---

## Part 5 — Notes on Scene 08

**Scene 08 (Cuaderno recap, `scene_08_cuaderno_closeup.png`):** Per the script brief §5, the
key sentence and grammar recap ride the normal on-screen caption, not the art. This scene is
allowed one deliberate departure from Ep01's identical beat: Ep01's `scene_08_cuaderno_closeup.png`
shows a **completely blank** notebook (Jin's first entry — nothing written yet). Ep02's Scene 08 is
Jin's **second** journal entry in the series, so a small amount of illegible squiggle "handwriting"
on the upper-left page is appropriate and reads as continuity of the running gag/motif (he's
already written something tonight) — but it must remain strictly non-readable, exactly like the
map and guidebook elsewhere in this episode. Do not let it drift into actual legible characters,
Spanish or Korean, even partially.

---

## Thumbnail plan

The dedicated Ep02 thumbnail will be built from **`scene_06_three_closer_over_map.png`** — the
scene where all three friends are visibly close together, warm, and leaning into the map with
Diego's finger on the chosen route. This mirrors the Ep01 thumbnail's choice of `scene_06_together.png`
(the analogous "group warmth" beat) for the same house-style reasons: it reads clearly at small
sizes, shows all three characters' identifying props (vieira pin, compass, glasses) without an
all-facing-camera composition, and carries the episode's emotional resolution.

At ship time, adapt `scripts/create_camino_ep01_thumbnail.py` into a new
`scripts/create_camino_ep02_thumbnail.py` (not written now, per task scope) — same house style:
full-bleed blurred background from the scene image, a sharp scene crop on the right (focus on the
three figures/hands over the map), a cream rounded text panel on the left with a colored badge, a
bold title line, and a Korean subtitle line in the established Optima-adjacent house type.

Per the Ep02 module's `DESIGN` table (`docs/plans/camino-ep02-la-ruta-brief.md` §6):

- `thumbnail_title` → `La ruta`
- `thumbnail_subtitle` → `Español en el Camino · A2+`
- `thumbnail_ko` → `El más largo, pero el más bonito`

Per the workspace brand constraint, the Korean thumbnail sublabel should stay short (four Korean
characters or fewer). `thumbnail_ko` as currently drafted in the module brief is a full Spanish
sentence rendered for a Korean-facing teaser slot, not a Korean string — flag this for the
`seo-promo` / showrunner pass at metadata time: either confirm this field is intentionally a
Spanish-language teaser line (unlike the short-Korean-sublabel convention), or supply a short
Korean equivalent (e.g., 4 characters or fewer, such as "가장 길고 예뻐" is 7 syllables/characters and
would need trimming further, something like "제일 길고 예뻐" or a shorter phrase) before the thumbnail
is finalized. This is a metadata/copy question, not an image-generation blocker, and does not stop
scene image production.

---

## Filename reconciliation note

Drafting began before `projects/camino_a2_ep02_la_ruta.py` existed, so the eight filenames were
first derived from the script brief's §7 visual one-liners and scene titles, following the Ep01
module's snake_case convention (`scene_NN_<short-description>.png`). The producer's module landed
during this brief's drafting (in parallel), and its `_BASE = "assets/images/camino_a2_ep02_la_ruta"`
+ per-scene `image_path` fields were checked at the end of this pass. Two filenames matched by
coincidence (`scene_01_map_on_table.png`, `scene_08_cuaderno_closeup.png`); the other six differed
in wording only (same scene, same numbering, different descriptive suffix — e.g. designer's
`scene_03_diego_points_routes.png` vs. producer's `scene_03_diego_points_at_routes.png`). All eight
filenames in this brief have been updated to match the producer module exactly, since the module's
`SEGMENTS`/`image_path` values are the pipeline's source of truth. No scene content, numbering, or
ordering changed as a result — only filename strings.
