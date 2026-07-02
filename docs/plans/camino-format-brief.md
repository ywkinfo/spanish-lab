# Español en el Camino — Series Brief (v1, canonical)

> Series slug **camino-a2** · Public name **Español en el Camino** · Level **A2+/B1-low**
> Format: immersion **dialogue drama** — three friends (Lucía, Diego, Jin) walk the Camino
> Francés (Saint-Jean-Pied-de-Port → Santiago, + Finisterre coda).
> Built on existing `RENDER_TYPE = "diary"` / `STORY_SCENES`. **No new renderer, no new
> dependency, no auto hooks.** Approved plan: `~/.claude/plans/6-eager-finch.md`.
> Benchmark evidence: [camino-benchmark.md](camino-benchmark.md).

**Stage count is our editorial choice, not canon.** The Camino Francés is split differently by
pace (cf. [Pilgrim.es](https://www.pilgrim.es/en/french-way/) stage-by-stage vs
[CaminoWays](https://caminoways.com/camino-frances) ≈790 km over 4–5 weeks). We adopt a
**34-stage production itinerary**. Total series = **42 episodes** (6 prep + 34 stages + 2
epilogue), unified numbering **Ep01–Ep42** ("Preparativos / Navarra / …" are season labels).

The deliverable is a repeatable **episode machine**: one skeleton, one teaching point, one human
problem, three character arcs — built to sustain 42 episodes.

## Cast & season arcs
- **Lucía** — emotional center; standard Spanish. **Arc: letting go.** Private grief → releases
  it at **Cruz de Ferro (Ep31)** → opens up.
- **Diego** — Mexican Camino outsider-insider; culture / guide / idioms. **Arc: seeing Spain
  slowly, without pretending to own it.** Performing "expert" → lets the road teach him too
  (Atapuerca, Galicia) → vulnerable participant.
- **Jin** — Korean-learner proxy; asks back and confirms *in Spanish*. **Arc: accuracy →
  connection.** Early listening failures / "speak correctly" anxiety → by Galicia he jokes,
  comforts, leads (orders the pulpo, Ep38). He is the viewer's journey from study to use.

Recurring motifs: the **"Buen Camino"** sign-off; the **Credencial** gaining one stamp per
episode (progress bar); **Jin's Cuaderno** as the recap card.

## The episode machine (every episode, same skeleton)
1. **Cold-open** — establishing still of the etapa (place first; no faces, no text).
2. **Intro/title card first (0:00), then the café cold-open as Scene 1.** The diary builder emits
   the intro card as the first segment
   ([projects/_template_historia_diary.py:289](../../projects/_template_historia_diary.py)); we do
   **not** fight it. The intro card carries the episode title; the atmospheric "cold-open" is
   Scene 1 immediately after. (True cold-open-*before*-title would need a builder reorder —
   deferred enhancement, not v1.)
3. **Today's human problem** stated. QA bar: first 30 s shows place + the three + the problem.
4. **3–4 dialogue scenes** — the **one** grammar structure repeated in situ; lore stays
   background; **key sentence varied ≥5×**; subtitles ≤2 lines.
5. **Credencial** scene-image (day's stamp = progress bar) + **Cuaderno** scene-image (Jin's
   *next-morning* journal — past-tense reflection naturally motivating preterite/perfect) with
   the key sentence large.
6. Short **flashback / map / sign** beat.
7. **Emotional close** advancing one character's season arc.
8. End **CHAPTER "Cuaderno del peregrino"** (recap) — existing chapter capability.

## Full roadmap (Ep01–Ep42) · grammar ladder A2 → B1-low, one structure per episode

> **Grammar-column rule:** each row names **one Target structure** (the taught point). Anything
> else in a cell is a **supporting chunk** — used as known vocabulary, never a second teaching
> target. Where an early draft listed two (e.g. Ep02, Ep04, Ep05), the first is the Target and
> the second is demoted to a supporting chunk.

### Temporada 0 — Preparativos (Ep01–06) · A2 present-tense foundation
| Ep | Route / setting | Lore | Human problem | Grammar | Key sentence (≥5×) | Visual motif |
|----|-----------------|------|---------------|---------|--------------------|--------------|
| 01 *(PILOT)* | Home / café | Credencial arrives by mail; vieira shell | Each hesitates — crazy? affordable? The credencial forces a real decision | `querer`/`me gustaría` + inf | "Quiero hacer el Camino." | blank credencial, vieira, map |
| 02 | Planning | Choosing the Francés | Disagreement: too long? which way? | comparatives (`más… que`) · *support:* `hay` | "El Francés es el más largo, pero el más bonito." | route map, guidebook |
| 03 | Planning | Pilgrim calendar / season | Jin can't get enough days off | `ir a` + dates/time | "Vamos a salir en mayo." | calendar, phone messages |
| 04 | Packing | Credencial, boots, shell on pack | Lucía overpacks; bag too heavy | `tener que` + inf · *support:* `necesitar` | "Tienes que llevar menos." | backpack, boots, gear |
| 05 | Training | First training walk | Training walk goes badly: early blister, doubt | `poder` + inf · *support:* `tener miedo de` | "Tengo miedo, pero puedo." | sneakers, small blister, a hill |
| 06 | Travel to SJPdP | First credencial stamp | Delays, night-before nerves | present perfect (arrival) | "Por fin hemos llegado a Saint-Jean." | train window, first stamp |

### Temporada 1 — Navarra (Ep07–12) · present/physical → preterite introduced
| Ep | Route | Lore | Human problem | Grammar | Key sentence | Visual motif |
|----|-------|------|---------------|---------|--------------|--------------|
| 07 | SJPdP → Roncesvalles | **Roland / Song of Roland** | Brutal Pyrenees climb; someone wants to quit day one | `doler`/`estar`+adj | "Me duelen las piernas." | ridge, fog, boots, km marker |
| 08 | Roncesvalles → Zubiri | Puente de la Rabia legend | Blisters worsen; fast-vs-slow conflict | `estar`+gerundio | "Estoy caminando muy despacio." | forest path, blistered heel |
| 09 | Zubiri → Pamplona | **San Fermín / el encierro** | Albergue full; the city overwhelms | reflexive routine | "Nos levantamos antes del amanecer." | city gate, bunks, bull-run street |
| 10 | Pamplona → Puente la Reina | **Alto del Perdón** iron pilgrims | Brutal wind; exhaustion at the top | weather `hace`+noun | "Hace muchísimo viento." | iron silhouettes, wind, bridge |
| 11 | Puente la Reina → Estella | Medieval Estella; routes merge | **Jin mishears directions**, briefly separated | `gustar`-type / `me apetece` | "Me apetece parar aquí." | stone streets, wrong turn, a sign |
| 12 | Estella → Los Arcos | **Irache Wine Fountain** | Levity vs a long dry stretch ahead | preterite, regular (Cuaderno, next-morning) | "Ayer bebí vino en la fuente." | wine tap, two cups, the road |

### Temporada 2 — La Rioja → Burgos (Ep13–18) · preterite consolidation
| Ep | Route | Lore | Human problem | Grammar | Key sentence | Visual motif |
|----|-------|------|---------------|---------|--------------|--------------|
| 13 | Los Arcos → Logroño | Rioja wine; Calle Laurel tapas | Money worries vs the urge to splurge | preterite irregulars | "Anoche cenamos de tapas." | tapas bar, wine, a thin wallet |
| 14 | Logroño → Nájera | Santa María la Real | Monotony; first homesickness | food/quantity + preterite | "Comimos demasiado." | vineyards, a call home |
| 15 | Nájera → Santo Domingo | **Hen & rooster miracle** (Hugonell) | Lucía's impostor feeling — does she belong? | preterite in storytelling | "Cuentan que la gallina cantó." | cathedral coop, white feather |
| 16 | Santo Domingo → Belorado | Leaving Rioja | Rain, soaked gear, low morale | preterite vs present | "Ayer caminé bajo la lluvia." | rain capes, muddy boots, grey sky |
| 17 | Belorado → Atapuerca | **Atapuerca**, earliest Europeans | Diego drifts inward (roots); distance grows | `hace` + time (deep past) | "Aquí vivieron hace miles de años." | dig site, old stones, hands |
| 18 | Atapuerca → Burgos | **Burgos cathedral**, El Cid | Big city makes them feel small; a navigation row | superlatives | "Es la catedral más impresionante." | spires, plaza, looking up |

### Temporada 3 — La Meseta (Ep19–27) · introspective heart → imperfect, por/para, light subjunctive
The flat, monotonous Meseta is the Camino's famous mental stretch — ideal for the imperfect and
inner arcs.
| Ep | Route | Lore | Human problem | Grammar | Key sentence | Visual motif |
|----|-------|------|---------------|---------|--------------|--------------|
| 19 | Burgos → Hornillos | "Camino of the mind" begins | The empty flatness unnerves them; restlessness | imperfect (memory) | "De niña, soñaba con viajar." | wheat horizon, one lone tree |
| 20 | Hornillos → Castrojeriz | Castle ruins | Silence forces hard thoughts; **Jin can't follow group talk**, walks alone | imperfect, habitual | "Antes no sabía estar en silencio." | ruined castle, lone figure |
| 21 | Castrojeriz → Frómista | Alto de Mostelares; San Martín | A storm; sheltering, tensions air out | imperfect vs preterite | "Caminábamos cuando empezó a llover." | steep ramp, storm clouds, doorway |
| 22 | Frómista → Carrión | Roman calzada | **Lucía's grief surfaces** — the real reason she walks | past emotions (`estaba`/`me sentía`) | "Me sentía perdida." | straight road, a photo in a pocket |
| 23 | Carrión → Calzadilla | Emptiest 17 km, no village | The mental wall; someone nearly breaks | `por` / `para` | "Camino por ella." | endless horizon, water bottle |
| 24 | Calzadilla → Sahagún | Geographic midpoint | Halfway crisis: go on or go home? | `llevar` + gerundio | "Llevamos dos semanas caminando." | midpoint monument, a fork |
| 25 | Sahagún → El Burgo Ranero | The poplar senda | Reconciliation; **Diego opens up** | subjunctive intro (`espero que`) | "Espero que sigamos juntos." | poplar path, two close |
| 26 | El Burgo Ranero → Mansilla | Nearing León | Impatience; a blister-infection scare | `ojalá` + subjunctive | "Ojalá llegue pronto a León." | a foot bandaged, "León 18" sign |
| 27 | Mansilla → León | **León cathedral** stained glass; San Marcos | Rest-day splurge: guilt vs reward; spirits reunite | exclamations | "¡Cuánta luz tiene esta catedral!" | stained glass, a soft bed, boots off |

### Temporada 4 — El Bierzo & Galicia (Ep28–40) · B1: present-perfect mastery, conditional, emotion-subjunctive
| Ep | Route | Lore | Human problem | Grammar | Key sentence | Visual motif |
|----|-------|------|---------------|---------|--------------|--------------|
| 28 | León → Mazarife | Leaving the city | Post-rest reluctance to restart | present perfect (mastery) | "Hemos hecho la mitad del Camino." | city behind, open road |
| 29 | Mazarife → Astorga | **Gaudí palace**, cocido maragato | Overeating vs tomorrow's climb (comic beat) | impersonal `se` | "Aquí se come el cocido al revés." | Gaudí palace, a huge plate |
| 30 | Astorga → Rabanal | Climb begins; pick up a stone | Fear of choosing what burden to leave | future simple | "Mañana dejaré mi piedra." | a stone in a palm, mountains |
| 31 | Rabanal → Ponferrada | **CRUZ DE FERRO** → Templar castle | **Lucía finally lets go** (emotional climax) | relative `lo que` | "Aquí dejo lo que ya no necesito." | iron cross + stone mound, opening hand |
| 32 | Ponferrada → Villafranca | Bierzo valley; Puerta del Perdón | Post-catharsis lightness; wanting to linger | conditional (`me gustaría`) | "Me gustaría quedarme un día más." | castle, vineyards, arched door |
| 33 | Villafranca → O Cebreiro | **O Cebreiro Holy Grail miracle**, pallozas | Hardest climb since the Pyrenees; cold mist, doubt | preterite (retelling miracle) | "Por fin entramos en Galicia." | round pallozas, mist, a chalice |
| 34 | O Cebreiro → Triacastela | Galician mountains | Rain for days; humor as coping | weather + frequency (`a menudo`) | "En Galicia llueve a menudo." | misty green hills, dripping capes |
| 35 | Triacastela → Sarria | Ancient chestnuts | The end is near: dread + relief | `desde que` / `hace … que` | "Desde que empecé, he cambiado mucho." | old chestnuts, a worn boot |
| 36 | Sarria → Portomarín | 100 km marker; church moved stone by stone | Resentment of "tourist" newcomers vs humility | passive / `se` | "Solo quedan cien kilómetros." | the 100 km mojón, numbered stones |
| 37 | Portomarín → Palas de Rei | Eucalyptus country | Bodies hurt more as the end nears | `cada vez más` | "Cada vez estamos más cerca." | eucalyptus rows, a foot massage |
| 38 | Palas de Rei → Arzúa | **Melide pulpo a feira** | A shared meal heals a grudge; **Jin leads, orders** | recommendations / `hay que` | "Hay que probar el pulpo." | pulpo on wood, paprika, shared table |
| 39 | Arzúa → O Pedrouzo (Amenal) | Last full day | Nobody wants it to end; pre-grief of parting | subjunctive of emotion | "No quiero que esto termine." | three silhouettes, "Santiago 20" sign |
| 40 | Amenal → **Santiago** | **Monte do Gozo**, Cathedral, **botafumeiro**, Compostela | Anticlimax vs overwhelm: what now? | present perfect (sum up journey) | "Hemos llegado a Santiago." (callback Ep01) | Monte do Gozo, facade, botafumeiro |

### Epílogo — Finisterre & Muxía (Ep41–42)
*Not day-stages — treat as a **walking montage / reflective coda**: looser time, more voice-over
and landscape, the season's emotional wind-down rather than a route to complete.*
| Ep | Route | Lore | Human problem | Grammar | Key sentence | Visual motif |
|----|-------|------|---------------|---------|--------------|--------------|
| 41 | Santiago → Finisterre (km 0) | End of the world; lighthouse; burning a garment; Atlantic sunset | Journey over but they're changed — fear of normal life | reflection (`lo que aprendí`) | "Esto no es el final." | km 0 marker, sea, a small fire |
| 42 | Finisterre → Muxía / despedida | Virxe da Barca by the sea | Goodbye; will they stay friends? promises | future promises / farewell | "Algún día volveré. ¡Buen Camino!" | ocean rocks, three stacked hands, the shell |

## Production rules
- **Renderer:** reuse `RENDER_TYPE = "diary"`. No new renderer.
- **Voices (verified):** `character_voices` in `AUDIO`, resolved by `voice_for_segment()`
  ([build/audio.py:61](../../build/audio.py)); used by ~33 existing projects (e.g.
  `no_puedo_ir_a2.py`). **The diary template `AUDIO` does NOT include `character_voices` — the
  producer must add it explicitly** per module; keep `edge_voice`/`voice` as the narrator voice.
  Build a **4-voice proof** (Lucía/Diego/Jin/narrator) before the pilot.
- **Chapters after the cold-open reorder:** the template hardcodes chapter 1 = "Introducción" at
  `segment 1`. Since the cold-open scene is placed first, **chapter 1 legitimately points at the
  cold-open (YouTube 0:00) — not a bug.** Relabel it; rename the final "Repaso final" →
  "Cuaderno del peregrino".
- **Credencial / Cuaderno cards (v1):** render as **scene images** + caption; recap via the end
  CHAPTER ("Repaso final" → "Cuaderno del peregrino"). Custom animated card types are **deferred
  infra** (`build/render_diary.py:169`, `build/segment_adapter.py:33-42`,
  `build/diary_timeline.py`) — not in v1.
- **Image consistency (top risk):** no "all three facing front" every scene — use backs, boots,
  backpack colours, Jin's notebook, hands, signs, credencial close-ups. Reference sheets; faces
  in the top 65% (caption safe-area).
- **Numbering / files:** unified **Ep01–Ep42** everywhere. Pilot `projects/camino_a2_ep01_la_idea.py`
  (underscores); `OUTPUT_NAME = "la-idea"` and `PUBLIC_SLUG = "camino-a2-ep01-la-idea"`.
- **Spanish naturalness:** Peninsular present perfect for today (`hoy he bebido…`), preterite for
  `ayer`/named past (Cuaderno's next-morning framing); no flat stereotypes
  (`llueve a menudo`, not `siempre llueve`). Linguist enforces the B1-low ceiling.
- **Image sourcing (external step — the render blocker):** the repo has **no image-generation
  tool**. Real scene art (1920×1080, ~2 MB PNG) is produced by an external image model and
  committed to `assets/images/<module>/`. Per episode: ~8 scene images + reuse the 3 character
  **reference sheets**; spec in [diary-asset-sourcing.md](diary-asset-sourcing.md) (16:9,
  ≥1600×900, top-65% safe area, fixed-prop continuity). The `designer` writes the generation
  brief; a human/external step generates the art.
- **Length / pacing:** episodes run **~5 min** at ~30 lines because each `diary_line` carries a
  ~2.5 s `processing_pause_s` — **intentional A2+ comprehension time.** Do not shorten by cutting
  pauses; pacing is the audio-engineer's `AUDIO` lever.
- **Staged production:** build **Ep01 only** fully first → all gates + human preview → then
  produce in season batches. **Do not pre-author the 42 modules.**

## Content QA bar (per episode)
First 30 s shows place + the three + today's human problem · key sentence varied ≥5× · subtitles
≤2 lines · the four TTS voices instantly distinguishable · Camino atmosphere via SFX (footsteps,
wind, cathedral bells, albergue ambience).

## Gates (diary variants — this is a `RENDER_TYPE = "diary"` series)
`make check → debug → test → lint-spanish → tts → **preview-diary** → preview-qa-pack →
preview-qa` → human preview → `make **publish-diary** → verify`. Use the diary targets
([Makefile](../../Makefile) `preview-diary` / `render-diary` / `publish-diary`), **not** the
generic Ken Burns `preview` / `render` / `publish`. **From a worktree there is no local `.venv`;
pass the absolute interpreter: `PYTHON=/Users/peter/spanish-lab/.venv/bin/python`** (has PIL,
edge_tts, numpy, moviepy).

## Ep01 preview-review decision log (2026-07-02, showrunner-approved)

Frame-level review of the first Ep01 bundle (watch-skill, 80 frames + focused passes) against
diario ep51 led to these binding decisions:

- **OUTPUT_NAME rule (supersedes the naming line above):** publish prefix is
  `SERIES-epNN-OUTPUT_NAME`, so `OUTPUT_NAME` must NOT repeat the series/episode. Ep01 uses
  `OUTPUT_NAME = "la-idea"` → assets `camino-a2-ep01-la-idea-16x9-v1.*`. `PUBLIC_SLUG` stays
  `camino-a2-ep01-la-idea`.
- **Layout:** Camino adopts the diario-ep51 preview-workflow infra set (render_diary
  `center_card` intro/outro + `intro_ko`/`outro_ko`/`montage_ko`, 82px captions, Makefile
  publish-without-rerender, probe_output 12fps allowance). Worktree `checks/validate_segments.py`
  (with camino-a2 metadata validation) is kept.
- **Speaker badges:** fixed per-character colors via `DESIGN["speaker_colors"]`
  (Lucía (47,95,143) · Diego (92,111,53) · Jin (179,106,46) · Narrador (42,48,57));
  renderer falls back to scene color when unset.
- **Outro (hybrid):** keep the speak-aloud practice line (series oral-goal identity) and add the
  comment CTA `Y tú, ¿quieres hacer el Camino? Escríbelo en los comentarios.`
  — LINGUIST-APPROVED as-is 2026-07-02. `outro_ko` carries the Ep02 teaser in Korean.
- **Intro:** 17s narrated intro card kept for Ep01 (cold-open-first still deferred); intro card
  now shows a one-line Korean gist (`intro_ko`).
- **Caption fit:** Jin's grammar recap line was split into two segments at the sentence boundary
  (identical approved words) so every caption stays ≤2 lines at 82px.
- **scene_02 art:** blurred-chalkboard artifact inpainted locally (Pillow; wall interpolation +
  clean warm-slate board, x≈428–682/y≈0–224); original preserved untracked at
  `.scratch/scene_02_three_backs.orig.png`.
- **Thumbnail:** dedicated house-style draft `thumbs/camino-a2-ep01-la-idea-draft.jpg`
  (scripts/create_camino_ep01_thumbnail.py) wired via `THUMBNAIL_PATH`; the auto intro-frame
  fallback is not acceptable for this series (no Korean teaser).

## Ep01 v2 audio/canon decision log (2026-07-02, showrunner-approved)

- **Diego canon:** Diego is Mexican, not Spanish. His Camino role is outsider-insider: he can
  explain Camino vocabulary and practical culture, but he must not claim Spanish origin or say
  Spain is "my country." Avoid Mexican slang unless the showrunner approves it for a specific
  line; keep his vocabulary Camino/Peninsular-compatible.
- **Voice recast:** Diego = `es-MX-JorgeNeural`; Jin = `es-US-AlonsoNeural`; Lucía =
  `es-ES-ElviraNeural`; narrator = `es-ES-XimenaNeural`. Jin remains dialect-neutral in text.
- **BGM:** Ep01 uses the canonical Spanish Lab brand bed
  `assets/audio/spanish-lab-brand-bgm.mp3` with ducking and `bgm_volume_db = -4.0`; the previous
  `fur_elise_inspired_soft_piano.wav` bed is not used for Camino.
- **Publish version:** v1 remains as audit history; the corrected upload candidate is v2.
- **YouTube title format (series convention, follows the diario listening pattern):**
  `[스페인어 듣기 A2+] {한국어 훅} | {Spanish episode title} Camino Ep.NN` — Ep01:
  `[스페인어 듣기 A2+] 순례길을 걷고 싶어 | La idea Camino Ep.01` (module `YOUTUBE_TITLE` +
  both v2 meta JSONs updated in place; video/description unchanged).
- **Upload record:** Ep01 v2 was uploaded as a private scheduled YouTube video on 2026-07-02:
  `https://youtu.be/55HQapqptxc`. Module `YOUTUBE_URL` is the canonical repo field for
  downstream exports.
