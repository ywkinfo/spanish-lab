# Español en el Camino — Ep02 "La ruta" · editorial brief + script

> Series **Español en el Camino** · slug `camino-a2` · Level **A2+/B1-low** ·
> Format: `RENDER_TYPE = "diary"` (multi-scene stills + Ken Burns + per-speaker TTS + captions).
> Canonical source: [camino-format-brief.md](camino-format-brief.md). Structural pattern:
> [camino-ep01-la-idea-brief.md](camino-ep01-la-idea-brief.md).
> **Status: LINGUIST-APPROVED (2 fixes: Scene 8·line 3 word order naturalness; intro_ko
> duplicate-draft conflict resolved to the DESIGN-table canonical value) — ready for producer.**
> Spanish is on-screen/spoken. Korean is translation + teaser only, never on-screen Spanish.

---

## 1. Episode brief

**Logline.** Ya han decidido hacer el Camino; ahora tienen que elegir la ruta. Una tarde en el
piso de Lucía, con un gran mapa sobre la mesa, Diego presenta las opciones y empieza la primera
discusión de verdad: ¿el Francés, el Norte o el Portugués? Jin teme que el Francés sea demasiado
largo; Lucía, en silencio, quiere justo el más largo.

**The one grammar focus (only this).** Comparaciones con **`más… que` / `menos… que`**, que
culminan de forma natural en el superlativo **`el más …`** de la frase clave. Supporting chunk
(vocabulario conocido, NO se enseña): **`hay`** ("Hay muchos caminos…"). We do **not** teach
`ir a` + fechas (that is Ep03), `tener que` (Ep04), preterite, or subjunctive. `querer` + inf.
may recur as **known vocabulary** ("quiero ir por el Francés"), never as a second taught target.

**Key sentence (recurs ≥5× with natural variation).** → **"El Francés es el más largo, pero el
más bonito."** Explicit hits in the compressed script (**6**, all natural, distributed, and now
factually airtight — length comparatives run Francés vs Portugués; the Norte is set aside on
difficulty):
1. "El Camino Francés es más largo que el Portugués." — Diego, laying out the map (Scene 3). *(comparativo)*
2. "¿Más largo que el Portugués? Entonces son más días." — Jin, worried ask-back (Scene 3).
3. "El Norte es más duro que el Francés. Hay más subidas." — Diego, setting the Norte aside (Scene 4). *(comparativo)*
4. "Para mí, el Francés es el más bonito de los dos." — Lucía, quiet pull, Norte already out (Scene 5). *(superlativo)*
5. "El Francés es el más largo, pero el más bonito." — Diego, naming it (Scene 6). *(la frase, verbatim)*
6. "Es el más largo, pero también el más bonito." — Lucía, sealing the choice (Scene 7) +
   written callback in Jin's Cuaderno: "El Francés es el más largo, pero el más bonito." (Scene 8, verbatim).

The exact locked wording **"El Francés es el más largo, pero el más bonito."** appears verbatim
twice (Scene 6 Diego + Scene 8 Cuaderno). Because the Norte (~825 km, the truly longest route) is
discarded on difficulty grounds in Scene 4 *before* any superlative, every "el más largo" is true
of the remaining shortlist (Francés ~780 km vs Portugués ~620/240 km). The comparative→superlative
structure is built across four more lines so the climax lands earned, not repeated.

**Human problem.** They agree they're walking, but not *which way*. The disagreement is concrete:
Jin fears the Francés is too long (more days, maybe more expensive); Diego weighs the Norte
(shorter-feeling but harder, more climbs, fewer albergues) and sets it aside; comparisons fly
across the map. QA bar: the problem (which route?) lands inside the first 30 s of runtime.

**Flashback / arc seeds (plant lightly, pay off later).**
- **Lucía — letting go / private grief.** Implied only: she quietly wants the **longest** route
  because "necesito más tiempo… para pensar" — echoing Ep01's seed. No photo, no name, no
  explanation. (Pays off Ep22, Ep31.)
- **Diego — outsider-insider (performing "expert").** He lays out the routes from **books and
  pilgrim friends**, never from having walked them: "Lo he leído en la guía." / "Un amigo hizo el
  Norte." He explains Camino vocabulary but never claims Spain as his country. (Arc pays off
  Atapuerca / Galicia.)
- **Jin — accuracy → connection.** He asks back and confirms *in Spanish* to be sure he
  understood ("¿Más largo que el Portugués?"), and mutters the one worry nobody solved tonight —
  the days off / when to leave — left unresolved as **Ep03's problem**. (One line max.)

**Length (realistic).** 8 STORY_SCENES, **29 spoken lines → ≈ 4:30–5:30 finished (~5 min).**
Same timeline math as the pilot: each `diary_line` floors at ~7.65 s (text floor 4.5 s + lead
0.25 + tail 0.4 + processing_pause 2.5). **~5 min is intended — do NOT cut `processing_pause_s`
below ~2.0 s to shorten it: that pause is A2+ comprehension time (the pedagogy), and pacing is the
audio-engineer's `AUDIO` lever, not a length hack.**

**First-30-s QA.** Order is **intro card (~3 s, title "La ruta") → Scene 1 map cold-open (1 line)
→ Scene 2 title beat + reintroduce the three (2 lines) → Scene 3 Diego lays out the routes**. Place
(Lucía's flat, the map) is set from the intro card + Scene 1; the three are re-named by Scene 2
(~20 s); the problem (which route? too long?) lands at the top of Scene 3 / into Scene 4, within
the 30-s bar. (The diary builder puts the intro card first; the map cold-open is Scene 1 right
after — see the format brief's episode-machine note.)

**Speaker / voice rules for the producer (locked, unchanged from Ep01).**
- `Narrador` lines → set module `speaker = ""` (empty string). Do **not** put "Narrador" in the
  `speaker` field. Narration uses the narrator voice (default `edge_voice`).
- Character lines → `speaker` is exactly `Lucía` / `Diego` / `Jin` to match `character_voices`.
- **No shared/co-speaker lines.** Where two friends react together, write **two separate lines**
  (see Scene 7) so per-speaker TTS resolves cleanly.

---

## 2. Scene-by-scene script (compressed)

Each spoken line = one diary line → `speaker` · `text_es` · `text_ko`. `Narrador` in the tables
below maps to `speaker = ""` in the module (see rule above). Every `text_es` fits ≤2 caption lines
at 82px (each line ≤ ~75 chars; longer thoughts split at the sentence boundary into separate diary
lines).

### Scene 1 — Cold-open · "El mapa sobre la mesa" (atmosphere only, NO dialogue)
*Establishing still: the flat's table at evening, a big paper map of the Camino routes spread out,
a guidebook, two mugs of tea, a warm lamp. No faces. Place first, no baked-in text.*

| # | speaker | text_es | text_ko |
|---|---------|---------|---------|
| 1 | Narrador | Esa noche, en casa de Lucía, hay un gran mapa sobre la mesa. | 그날 밤, 루시아네 집, 테이블 위에 커다란 지도가 펼쳐져 있습니다. |

### Scene 2 — Title beat · "La ruta"
*Title-card energy over a warm still (hands over the map, backs, mugs per image rule). Reintroduce
the three, lightly.*

| # | speaker | text_es | text_ko |
|---|---------|---------|---------|
| 1 | Narrador | Episodio dos: "La ruta". Otra vez están Lucía, Diego y Jin. | 2화 "그 길". 다시 루시아, 디에고, 진이 모였습니다. |
| 2 | Lucía | Muy bien, ya lo decidimos. Ahora, ¿por dónde vamos? | 좋아, 이제 결정했잖아. 그럼 어느 길로 가지? |

### Scene 3 — Diego performs the expert · "Hay muchos caminos"
*Diego leans over the map and points. He lays out the three options from the guidebook. First
comparative lands. Problem is opening up.*

| # | speaker | text_es | text_ko |
|---|---------|---------|---------|
| 1 | Diego | Mirad el mapa. Hay muchos caminos a Santiago. | 지도 좀 봐. 산티아고로 가는 길이 많아. |
| 2 | Diego | El Francés, el del Norte y el Portugués. Lo he leído en la guía. | 프랑세스, 노르테, 그리고 포르투게스. 가이드북에서 읽었어. |
| 3 | Diego | El Camino Francés es más largo que el Portugués. | 카미노 프랑세스가 포르투게스보다 더 길어. |
| 4 | Jin | ¿Más largo que el Portugués? Entonces son más días. | 포르투게스보다 더 길다고? 그럼 날이 더 걸리잖아. |

### Scene 4 — Jin worries + the Norte is set aside · "¿Demasiado largo?"
*The disagreement lands. Jin fears the Francés is too long/expensive; the Norte is discarded here
on difficulty grounds (before the superlative in Scene 5). `hay` stays a supporting chunk.*

| # | speaker | text_es | text_ko |
|---|---------|---------|---------|
| 1 | Jin | Más días… ¿y más caro también? | 날이 더 걸리면… 돈도 더 드는 거 아냐? |
| 2 | Jin | ¿Y el del Norte? ¿No es más fácil? | 그럼 노르테는? 더 쉽지 않아? |
| 3 | Diego | El Norte es más duro que el Francés. Hay más subidas. | 노르테가 프랑세스보다 더 고돼. 오르막이 더 많거든. |
| 4 | Diego | Y en el Norte hay menos albergues que en el Francés. | 그리고 노르테에는 프랑세스보다 알베르게가 더 적어. |

### Scene 5 — Lucía's quiet pull · "Yo quiero el más largo"
*The Norte is out. Between the Francés and the Portugués, Lucía — who has said little — wants the
long one; she needs the time. Grief seed, implied only. Superlative appears for the first time,
true of the remaining shortlist.*

| # | speaker | text_es | text_ko |
|---|---------|---------|---------|
| 1 | Jin | Vale, el Norte no. ¿Entonces el Francés o el Portugués? | 좋아, 노르테는 아니고. 그럼 프랑세스 아니면 포르투게스야? |
| 2 | Lucía | Para mí, el Francés es el más bonito de los dos. | 나한테는 둘 중에 프랑세스가 제일 예뻐. |
| 3 | Lucía | Y quiero el más largo. Necesito más tiempo… para pensar. | 그리고 제일 긴 길로 가고 싶어. 생각할 시간이 더 필요하거든. |
| 4 | Diego | ¿El más largo? Pues el Francés es más largo que el Portugués. | 제일 긴 거? 그럼 프랑세스가 포르투게스보다 더 길어. |

### Scene 6 — The route takes shape · "El más largo, pero el más bonito"
*They converge. Diego names the sentence; the social argument (more pilgrims, more albergues) seals
it with comparatives still doing the work.*

| # | speaker | text_es | text_ko |
|---|---------|---------|---------|
| 1 | Diego | El Francés es el más largo, pero el más bonito. | 프랑세스가 제일 길지만, 제일 아름다워. |
| 2 | Diego | Y es el más popular. Hay más peregrinos que en las otras rutas. | 그리고 제일 인기 많아. 다른 길보다 순례자가 더 많거든. |
| 3 | Jin | ¿Más peregrinos? Entonces conocemos a más gente. | 순례자가 더 많다고? 그럼 사람도 더 많이 만나겠네. |
| 4 | Lucía | Sí. Solos, da un poco de miedo. Con más gente, menos. | 응. 우리끼리만 가면 좀 무섭잖아. 사람이 많으면 덜하고. |

### Scene 7 — The decision · emotional close · "Vamos por el Francés"
*They choose the Francés. End on warmth and the key sentence, sealed by Lucía. Co-reaction split
into two lines for clean per-speaker TTS. Jin plants the Ep03 worry — one line.*

| # | speaker | text_es | text_ko |
|---|---------|---------|---------|
| 1 | Diego | Entonces, ¿vamos por el Francés? | 그럼, 프랑세스로 가는 거야? |
| 2 | Jin | Por el Francés. | 프랑세스로. |
| 3 | Lucía | Por el Francés. Es el más largo, pero también el más bonito. | 프랑세스로. 제일 길지만, 그래도 제일 아름다우니까. |
| 4 | Diego | Perfecto. Mañana marcamos la ruta en el mapa. | 좋아. 내일 지도에 길을 표시하자. |
| 5 | Jin | Vale… pero ¿cuándo salimos? Yo tengo pocos días libres. | 좋아… 근데 우리 언제 출발해? 나 휴가가 별로 없는데. |

### Scene 8 — Cuaderno del peregrino · recap card · "El cuaderno de Jin"
*Jin's journal page = the recap card. On-screen large text shows the key sentence. Night-time
journal framing; present-tense/note register, no `hoy + preterite`.*

| # | speaker | text_es | text_ko |
|---|---------|---------|---------|
| 1 | Narrador | Esa noche, Jin escribe otra vez en su cuaderno. | 그날 밤, 진은 또 공책에 씁니다. |
| 2 | Jin | La frase del día es "El Francés es el más largo, pero el más bonito". | 오늘의 문장: "프랑세스가 제일 길지만, 제일 아름다워". |
| 3 | Jin | Con "más… que" y "menos… que", comparo cosas. | "más… que"와 "menos… que"로 비교한다. |
| 4 | Jin | Y "el más…" es el superlativo: el más largo, el más bonito. | 그리고 "el más…"는 최상급이다: 제일 긴, 제일 아름다운. |
| 5 | Jin | Palabras nuevas: la ruta, el mapa, la guía, el albergue. ¡Buen Camino! | 새 단어: 길, 지도, 가이드북, 알베르게. 부엔 카미노! |

**Total spoken lines: 29** (1 + 2 + 4 + 4 + 4 + 4 + 5 + 5). *(Same footprint as the pilot: 8
scenes, ~29–31 lines, ≈5 min. Two-line ceiling met on every line.)*

---

## 3. Vocab block (key words · ES ↔ KR)

| Español | 한국어 |
|---------|--------|
| la ruta / el camino | 경로 / 길 |
| el mapa | 지도 |
| la guía | 가이드북 |
| el albergue | 알베르게 (순례자 숙소) |
| el peregrino / la peregrina | 순례자 |
| más… que | ~보다 더 … (비교급) |
| menos… que | ~보다 덜 … (비교급) |
| el más … (de todos) | (그중) 가장 … (최상급) |
| hay | ~이 있다 (기존 어휘, 이번엔 안 배움) |

## 4. Cuaderno recap copy (the recap card text)

**Frase del día** → **El Francés es el más largo, pero el más bonito.**
*(Es más largo que el Portugués. / El Norte es más duro que el Francés.)*
**Estructura:** comparativo `más… que` / `menos… que` → superlativo **`el más …`**.
**Palabras:** la ruta · el mapa · la guía · el albergue · **Despedida:** ¡Buen Camino!

## 5. On-screen text cards — **v1 method (no custom overlay)**

Unchanged from the pilot. No native large-centered-text field; custom card types are deferred
infra. So we do **not** overlay text:
- **Map beat (Scenes 3–7):** use the **big paper map as the scene image**; the comparatives ride
  the **normal diary caption**. The route lines/labels on the map draw the eye to the caption.
- **Cuaderno beat (Scene 8):** use a **blank/lined journal-page image**; the key sentence + recap
  ride the normal caption. Loop closes: argued → chosen → written.

No overlay art, no English. Korean stays in the caption-translation lane only.

---

## 6. Draft narration + DESIGN text (for the producer to copy)

### Intro narration (`type: "intro"`, ~16 s card)
`text_es` (**~235 chars**):
```
Ya está decidido: van a hacer el Camino. Esta noche, con un mapa sobre la mesa, tienen que elegir la ruta. ¿El Francés, el del Norte o el Portugués? Fíjate en las comparaciones: "más… que", "menos… que" y "el más…".
```
`intro_ko` (one-liner — canonical value; matches the DESIGN table below):
```
순례길은 정했어요. 이제 어느 길로 갈까요? 프랑세스, 노르테, 포르투게스.
```
*(Showrunner decision 2026-07-03: present-tense intro adopted — no `decidieron`. `van a hacer`
is `ir a` used only as a **known chunk** here, not a taught target; the only taught surface stays
the comparatives. The narrator now carries no past tense at all.)*

### Outro narration (`type: "outro"`, ~15 s card)
`text_es` (**238 chars**):
```
Muy bien. Practica en voz alta: "El Francés es el más largo, pero el más bonito." Y tú, ¿qué camino prefieres? Escríbelo en los comentarios. En el próximo episodio, los tres eligen la fecha de salida. ¡Buen Camino!
```
`outro_ko` (Korean Ep03 teaser one-liner):
```
3화에서는 세 친구가 출발 날짜를 정해요. 여러분은 어느 길이 좋나요? 댓글로 알려 주세요!
```

### DESIGN text fields (copy into `DESIGN`)

| field | value |
|-------|-------|
| `intro_title` | `La ruta` |
| `intro_subtitle` | `Español en el Camino · Ep.2` |
| `intro_ko` | `순례길은 정했어요. 이제 어느 길로 갈까요? 프랑세스, 노르테, 포르투게스.` |
| `outro_title` | `Muy bien` |
| `outro_subtitle` | `Fin de la lección` |
| `outro_ko` | (as above) `3화에서는 세 친구가 출발 날짜를 정해요. 여러분은 어느 길이 좋나요? 댓글로 알려 주세요!` |
| `montage_title` | `La ruta` |
| `montage_subtitle` | `el episodio completo` |
| `montage_ko` | `에피소드 전체 다시 보기` |
| `montage_order_text` | `El mapa  →  Las opciones  →  ¿Demasiado largo?  →  El Francés  →  ¡Buen Camino!` |
| `thumbnail_title` | `La ruta` |
| `thumbnail_subtitle` | `Español en el Camino · A2+` |
| `thumbnail_ko` | `El más largo, pero el más bonito` |

`diary_intro_background_path` → Scene 2 still (hands over the map). `diary_outro_background_path` →
Scene 8 cuaderno close-up. `speaker_colors` unchanged from Ep01 (Lucía / Diego / Jin / Narrador).

---

## 7. Scene titles + per-scene visual one-liners (for image sourcing)

Faces (when shown) in the **top ~65%** (caption safe area). No baked-in text in the art. Fixed-prop
continuity: the paper map, the guidebook, the two mugs, Jin's cuaderno, backpack colours.

| Scene | title_es | title_ko | Visual (what the still shows) |
|-------|----------|----------|-------------------------------|
| 1 | El mapa sobre la mesa | 테이블 위의 지도 | Evening flat interior; big paper Camino map spread on a table, a guidebook, two mugs, warm lamp. **No faces.** |
| 2 | La ruta | 그 길 | Warm three-shot from behind / hands over the map; the three lean in. Backs and hands, faces top of frame. |
| 3 | Hay muchos caminos | 길은 많아 | Diego's hand pointing at the map's branching routes; the guidebook open beside it. Diego upper frame. |
| 4 | ¿Demasiado largo? | 너무 길지 않아? | Jin's worried face over the map, finger tracing a long line; Diego gesturing. Faces top 65%. |
| 5 | Yo quiero el más largo | 난 제일 긴 길이 좋아 | Lucía looking down at the map, quiet, a mug in hand; the long Francés line under her finger. |
| 6 | El más largo, pero el más bonito | 제일 길지만 제일 예뻐 | The three closer together over the map, warming; Diego tapping the Francés route. |
| 7 | Vamos por el Francés | 프랑세스로 가자 | Decision beat: a pen marking the Francés route on the map, three hands near it, soft smiles. |
| 8 | El cuaderno de Jin | 진의 공책 | Close-up of Jin's lined journal page under lamplight, pen resting; the map softly out of focus behind. **No faces.** |

---

## 8. Chapter title list (10 rows, honest to actual segment order)

The diary builder places the INTRO card first → segment 1 is the title card "La ruta" at 0:00
(**not** a bug). The map cold-open is Scene 1 right after. Final "Repaso final" → renamed
"Cuaderno del peregrino".

| # | segment | title |
|---|---------|-------|
| 1 | 1 (intro card) | La ruta |
| 2 | Scene 1 | El mapa sobre la mesa |
| 3 | Scene 2 | Los tres, otra vez |
| 4 | Scene 3 | Hay muchos caminos |
| 5 | Scene 4 | ¿Demasiado largo? |
| 6 | Scene 5 | El más largo |
| 7 | Scene 6 | El más bonito |
| 8 | Scene 7 | Vamos por el Francés |
| 9 | Scene 8 | El cuaderno de Jin |
| 10 | final | Cuaderno del peregrino |

---

## 9. MINI_QUIZ (5 items · Korean question → Spanish answer)

Exactly 5 (validated by `checks/validate_segments.py`). Focus: the comparative/superlative
structure + episode vocabulary.

```python
MINI_QUIZ = [
    ("¿Cómo dices '길 / 경로'?", "La ruta"),
    ("¿Cómo dices '지도'?", "El mapa"),
    ("¿Cómo dices '프랑세스가 포르투게스보다 더 길어'?", "El Francés es más largo que el Portugués"),
    ("¿Cómo dices '(그중) 제일 아름다운'?", "El más bonito"),
    ("¿Cómo dices '순례자 숙소'?", "El albergue"),
]
```

---

## 10. Handoff notes

**For the linguist (DRAFT → approve before TTS)**
- Grammar discipline: taught structure is strictly comparatives `más… que` / `menos… que`
  climaxing in superlative `el más …`. `hay` is a **supporting chunk** (known vocabulary), not a
  second target. `querer` + inf. recurs only as known vocabulary ("quiero el más largo") — confirm
  it does not compete with the comparative focus.
- **Narrator/intro is fully present-tense** (showrunner decision 2026-07-03): intro now opens
  "Ya está decidido: van a hacer el Camino." (`van a` = known `ir a` chunk, not taught). No
  `decidieron`, no preterite anywhere in narrator copy — please confirm the taught surface stays
  comparatives-only.
- Confirm Peninsular register among friends: `Mirad` (Scene 3, vosotros imperative), `¿por dónde
  vamos?`, `Pues…`, `Vale`. Diego stays Mexican-voiced but Camino/Peninsular-compatible; **he must
  not claim Spain as his country and his route knowledge is from books/friends** (`Lo he leído en
  la guía`), not from having walked it.
- Confirm the night-time journal (Scene 8) reads Peninsular-natural with no `hoy + preterite`.
- Check the TTS punctuation pattern from Ep01: `La frase del día es "…"` (no colon before the
  quote) is already applied in Scene 8 · line 2.

**Factual note (RESOLVED — showrunner decision 2026-07-03).** Real-world, the Camino del Norte is
*slightly* longer than the Francés (~825 km vs ~780 km), so no length claim may put the Francés
above the Norte. Binding resolution applied to the script:
- **Length comparatives run Francés vs Portugués only** (true: Francés ~780 km vs Portugués ~620 km
  from Lisbon / ~240 km from Porto). Scene 3: "El Camino Francés es más largo que el Portugués.";
  Jin's ask-back adjusts to "¿Más largo que el Portugués?".
- **The Norte is set aside on difficulty**, with comparatives intact and `hay` kept as the
  supporting chunk: Scene 4 "El Norte es más duro que el Francés. Hay más subidas." +
  "en el Norte hay menos albergues que en el Francés." (all defensible: coastal route, more
  elevation, fewer albergues).
- **Sequencing guarantees "el más largo" is true.** The Norte is discarded in Scene 4 *before* the
  first superlative in Scene 5, so every "el más largo" reads against the remaining shortlist
  (Francés vs Portugués). One non-locked hit carries "de los dos" for airtightness (Scene 5
  Lucía); the **locked sentence stays verbatim** "El Francés es el más largo, pero el más bonito."
No open flag remains; the resolution above is the showrunner ruling of record.

**For image sourcing (the render blocker)**
- Same pipeline as Ep01: real scene art produced by an **external image model**, dropped into
  `assets/images/camino_a2_ep02_la_ruta/`. Deliverable: **8 scene images** (per §7) + reuse the 3
  character **reference sheets**. Native 16:9, ≥1600×900 (rec 1920×1080), plot-critical
  props/faces in the **top ~65%**, no baked-in text.
- Ep02 is prop-anchored (the map, the guidebook, mugs, the cuaderno), which eases face-continuity
  and keeps captions clear — lean on hands-over-map and pointing shots rather than "all three
  facing front."
- The `designer` writes the image-generation brief (per-scene prompts + reference-sheet reuse +
  safe-area/continuity constraints); a human/external step executes it.

**For the producer** (building `projects/camino_a2_ep02_la_ruta.py` from the Ep01 module)
- Clone `camino_a2_ep01_la_idea.py`; set `EPISODE = 2`, `OUTPUT_NAME = "la-ruta"`,
  `PUBLIC_SLUG = "camino-a2-ep02-la-ruta"`, `DESCRIP_PATH = "camino-a2-ep02-la-ruta/descrip.md"`,
  `_BASE = "assets/images/camino_a2_ep02_la_ruta"`. **`KOREAN_TEASER` is required for ep06+ but
  recommended here too; keep it.**
- **Voices — carry the four-voice map forward unchanged:**
  ```python
  "character_voices": {
      "Lucía": "es-ES-ElviraNeural",
      "Diego": "es-MX-JorgeNeural",
      "Jin":   "es-US-AlonsoNeural",
  },
  ```
  Keep `edge_voice` / `voice` as narrator (`es-ES-XimenaNeural`). `Narrador` lines →
  `speaker = ""` (empty), never the string "Narrador".
- Paste the intro/outro narration from §6 into `_build_diary_segments()` (intro `duration_s`
  16.0, outro 15.0). Paste DESIGN text fields from §6, MINI_QUIZ from §9, CHAPTERS from §8.
- **CHAPTERS after the cold-open reorder:** chapter 1 legitimately points at the intro card /
  0:00. Do NOT "fix" it. Keep the final chapter renamed **"Cuaderno del peregrino"**.
- **Cards:** render map/cuaderno beats as **scene images + normal caption** (see §5) — no overlay
  field exists in v1.
- **Diary gates** (run with `PYTHON=/Users/peter/spanish-lab/.venv/bin/python` — the worktree has
  no `.venv`): `check → debug → test → lint-spanish → tts → preview-diary → preview-qa-pack →
  preview-qa → human preview → publish-diary → verify`.

---

## 11. Editorial judgment calls (for the showrunner)

1. **Key-sentence build, not just repeat.** The locked sentence "El Francés es el más largo, pero
   el más bonito." is a **superlative**; a raw ≥5× repetition of a superlative would feel canned at
   A2. So the 6 hits *build the grammar*: 3 comparative lines (`más largo que`, `más duro que`,
   `menos albergues que`) → 3 superlative lines (`el más bonito`, `el más largo`, the full locked
   sentence) → written callback. This teaches the comparative→superlative ladder while hitting the
   key sentence verbatim twice (Scene 6 Diego, Scene 8 Cuaderno). This is the one substantive craft
   decision.
2. **Geographic accuracy — RESOLVED (showrunner 2026-07-03).** The Norte is really the longest
   route, so length comparatives were reworked to run **Francés vs Portugués**, and the **Norte is
   discarded on difficulty grounds in Scene 4 before any superlative**. Every "el más largo" is now
   true of the remaining shortlist; the locked sentence is unchanged. Full resolution recorded in
   §10 (Factual note). No open flag remains.
3. **`querer` carried as known vocabulary.** Per greenlight, `quiero el más largo` may recur; I
   used it sparingly (Lucía, Scene 5) so it never eclipses the comparative focus.
4. **Ep03 seed is exactly one line.** Jin's closing "pero ¿cuándo salimos? Yo tengo pocos días
   libres." plants the next episode's problem (days off / departure date) without resolving it and
   without teaching `ir a` + dates here.
5. **Narrator is fully present-tense (showrunner 2026-07-03).** The earlier `decidieron` is gone;
   the intro now opens "Ya está decidido: van a hacer el Camino." (`van a` = known `ir a` chunk).
   No preterite anywhere in narrator copy. Lucía's colloquial "ya lo decidimos" (Scene 2) is a
   present-tense form (`decidimos` = present here), not a taught surface. The whole taught surface
   is comparatives-only.
