# Español en el Camino — Ep01 "La idea" (PILOT) · editorial brief + script

> Series **Español en el Camino** · slug `camino-a2` · Level **A2+/B1-low** ·
> Format: `RENDER_TYPE = "diary"` (multi-scene stills + Ken Burns + per-speaker TTS + captions).
> Canonical source: [camino-format-brief.md](camino-format-brief.md).
> **Status: LINGUIST-APPROVED (with 3 TTS punctuation fixes applied) — ready for producer once art exists. See §7.**
> Spanish is on-screen/spoken. Korean is translation + teaser only, never on-screen Spanish.

---

## 1. Episode brief

**Logline.** Tres amigos — Lucía, Diego y Jin — reciben por correo la credencial del
peregrino. Tenerla en las manos vuelve real un sueño, y cada uno tiene que decidir, de verdad,
si quiere hacer el Camino de Santiago.

**The one grammar focus (only this).** `querer` + infinitivo and `me gustaría` + infinitivo
(wishes/intentions). We do **not** teach preterite, subjunctive, comparatives, or `ir a`; any
other verb (`hay`, `ha llegado`, `se puede`) is known vocabulary, not a taught structure.

**Key sentence (recurs ≥5× with natural variation).** → **"Quiero hacer el Camino."**
Explicit hits in the compressed script (6, all natural):
1. "Quiero hacer el Camino." — Lucía, the seed (Scene 4).
2. "¿De verdad quieres hacerlo?" — Diego, testing (Scene 4).
3. "Yo también quiero hacerlo." — Diego, committing (Scene 5).
4. "Me gustaría hacer el Camino con vosotros." — Jin, tentative wish (Scene 5).
5. "Quiero hacer el Camino con vosotros." — Lucía, warming the group (Scene 6).
6. "Queremos hacer el Camino juntos." — the decision (Scene 7) + written callback in Jin's
   Cuaderno "Quiero hacer el Camino." (Scene 8).

**Human problem.** Each hesitates for a concrete reason: *Is this crazy? Can we afford the time
and money? Who commits first?* The credencial in the envelope forces the decision.

**Flashback seeds (plant lightly, pay off later).**
- **Lucía — letting go / private grief.** Implied only: "quiero empezar algo nuevo / necesito
  tiempo para pensar." No photo, no name. (Pays off Ep22, Ep31.)
- **Diego — outsider-insider.** "Soy mexicano y nunca he hecho el Camino. Quiero ver España a pie."
  (Pays off Ep17, Galicia.)
- **Jin — using Spanish, not just studying it.** "Quiero hablar español de verdad." (Pays off
  across the season: accuracy → connection.)

**Length (realistic).** 8 STORY_SCENES, **~31 spoken lines → ≈ 4:30–5:30 finished (~5 min).**
The timeline floors each `diary_line` at `max(duration_for_text, …)` where
`duration_for_text` itself floors at **4.5 s**, then adds `lead 0.25 + tail 0.4 +
processing_pause 2.5` → **~7.65 s/line minimum** ([build/timeline.py:32](../../build/timeline.py),
[build/diary_timeline.py:46](../../build/diary_timeline.py)). **~5 min is the intended pilot
length — do NOT cut `processing_pause_s` below ~2.0 s to shorten it: that pause is A2+
comprehension time (the pedagogy), and pacing is the audio-engineer's `AUDIO` lever, not a length
hack.** (The earlier 57-line draft ran ≈9 min-class and delayed the problem past the 30-s bar;
31 lines fixes the front-loading while keeping learner-friendly pacing.)

**First-30-s QA.** Order is **intro card (~3 s, title "La idea") → Scene 1 café cold-open (1 line)
→ Scene 2 introduce the three (2 lines) → Scene 3 the envelope/credencial**. Place is set from the
intro card + Scene 1; the three are named by Scene 2 (~20 s); the problem (envelope) lands at the
top of Scene 3, ~26 s — within the 30-s bar. (The diary builder puts the intro card first; the
café is Scene 1 right after — see the format brief's episode-machine note.)

**Speaker / voice rules for the producer (locked).**
- `Narrador` lines → set module `speaker = ""` (empty string). Do **not** put "Narrador" in the
  `speaker` field or a narrator badge shows on screen and the voice map misses. Narration uses
  the narrator voice (default `edge_voice`).
- Character lines → `speaker` is exactly `Lucía` / `Diego` / `Jin` to match `character_voices`.
- **No shared/co-speaker lines.** Where two friends react together, write **two separate lines**
  (see Scene 7) so per-speaker TTS resolves cleanly.

---

## 2. Scene-by-scene script (compressed pilot)

Each spoken line = one diary line → `speaker` · `text_es` · `text_kr`. `Narrador` in the tables
below maps to `speaker = ""` in the module (see rule above). Lines kept ≤2 caption lines.

### Scene 1 — Cold-open · "Una tarde en el café" (atmosphere only, NO dialogue)
*Establishing still: a small café terrace in a Spanish town, late afternoon; three cups, a
backpack on a chair. No faces. Place first.*

| # | speaker | text_es | text_kr |
|---|---------|---------|---------|
| 1 | Narrador | Una tarde de primavera en un café de España. | 스페인의 어느 봄날 오후, 카페입니다. |

### Scene 2 — Intro / title beat · "La idea"
*Title-card energy over a warm still (backs/hands per image rule). Introduce the three, lightly.*

| # | speaker | text_es | text_kr |
|---|---------|---------|---------|
| 1 | Narrador | Episodio uno: "La idea". Estos son Lucía, Diego y Jin. | 1화 "그 아이디어". 이쪽은 루시아, 디에고, 진입니다. |
| 2 | Lucía | ¡Por fin estamos los tres juntos! | 드디어 우리 셋이 다 모였네! |

### Scene 3 — The credencial arrives · "El sobre"
*Inciting event by ~12 s. Envelope → close-up of the blank credencial + a small vieira.*

| # | speaker | text_es | text_kr |
|---|---------|---------|---------|
| 1 | Lucía | Mirad, ha llegado algo por correo. Es la credencial del peregrino. | 봐, 우편으로 뭔가 왔어. 순례자 여권이야. |
| 2 | Diego | ¿La credencial? ¿La del Camino de Santiago? | 크레덴시알? 산티아고 순례길 거? |
| 3 | Jin | ¿Cómo se dice "concha"? ¿Esta de aquí? | "concha"가 뭐였지? 이거 말이야? |
| 4 | Diego | Es la vieira, el símbolo del Camino. Y la credencial todavía está vacía. | 가리비(vieira)야, 순례길의 상징이지. 그리고 크레덴시알은 아직 비어 있어. |

### Scene 4 — Hesitation + Lucía's seed · "¿Estamos locos?"
*The hesitation begins. Lucía holds the blank credencial; her reason surfaces gently. Key-sentence
seed lands.*

| # | speaker | text_es | text_kr |
|---|---------|---------|---------|
| 1 | Diego | ¿Ochocientos kilómetros a pie? ¿Estamos locos? | 800킬로미터를 걸어서? 우리 미친 거 아냐? |
| 2 | Lucía | Quizá. Pero quiero hacer el Camino. | 아마도. 하지만 나는 순례길을 걷고 싶어. |
| 3 | Lucía | Quiero empezar algo nuevo. Necesito tiempo para pensar. | 새로운 걸 시작하고 싶어. 생각할 시간이 필요해. |
| 4 | Diego | ¿De verdad quieres hacerlo? | 정말 하고 싶어? |
| 5 | Lucía | Sí, de verdad. No quiero esperar más. | 응, 정말로. 더는 미루고 싶지 않아. |

### Scene 5 — Each reason surfaces · "Cada uno tiene su razón"
*Diego and Jin's seeds land; both express their own wish with the focus structure. The money/time
worry is voiced and answered.*

| # | speaker | text_es | text_kr |
|---|---------|---------|---------|
| 1 | Diego | Soy mexicano y nunca he hecho el Camino. Yo también quiero hacerlo. | 나 멕시코 사람인데 순례길을 한 번도 안 해 봤어. 나도 하고 싶어. |
| 2 | Diego | Quiero ver España a pie, despacio. | 스페인을 두 발로, 천천히 보고 싶어. |
| 3 | Jin | ¿Y el dinero? ¿Y los días libres? | 돈은? 그리고 휴가는? |
| 4 | Diego | Con poco dinero se puede. Los albergues son baratos. | 적은 돈으로도 돼. 알베르게는 싸거든. |
| 5 | Jin | Entonces… me gustaría hacer el Camino con vosotros. | 그럼… 나도 너희랑 순례길을 걷고 싶어. |
| 6 | Jin | Quiero hablar español de verdad, no solo estudiarlo. | 스페인어를 진짜로 말하고 싶어. 공부만 하는 게 아니라. |

### Scene 6 — The doubt softens · "Juntos da menos miedo"
*Together it is less scary. Lucía pulls the group close; another natural variation.*

| # | speaker | text_es | text_kr |
|---|---------|---------|---------|
| 1 | Jin | Solo, me da un poco de miedo. | 혼자라면 좀 무서워. |
| 2 | Lucía | Yo no quiero hacerlo sola. Quiero hacer el Camino con vosotros. | 나 혼자 하고 싶지 않아. 너희랑 함께 순례길을 걷고 싶어. |
| 3 | Diego | Juntos da menos miedo. Pues lo hacemos, los tres. | 같이 가면 덜 무섭지. 그럼 하는 거야, 우리 셋이서. |
| 4 | Jin | ¿De verdad? ¿Los tres juntos? | 정말? 우리 셋이 다 같이? |

### Scene 7 — The decision · emotional close · "Lo hacemos"
*They decide together. End on warmth and the first "Buen Camino". Co-reaction split into two
lines for clean per-speaker TTS.*

| # | speaker | text_es | text_kr |
|---|---------|---------|---------|
| 1 | Lucía | Entonces, ¿lo hacemos? | 그래서, 우리 하는 거지? |
| 2 | Diego | ¡Lo hacemos! | 하자! |
| 3 | Jin | ¡Lo hacemos! | 하자! |
| 4 | Lucía | Queremos hacer el Camino juntos. | 우리는 함께 순례길을 걷고 싶어. |
| 5 | Diego | Hay una frase para esto. Se dice "Buen Camino". | 이럴 때 쓰는 말이 있어. "부엔 카미노"라고 해. |

### Scene 8 — Cuaderno del peregrino · recap card · "El cuaderno de Jin"
*Jin's journal page = the recap card. On-screen large text shows the key sentence.*

| # | speaker | text_es | text_kr |
|---|---------|---------|---------|
| 1 | Narrador | Esa noche, Jin escribe en su cuaderno. | 그날 밤, 진은 공책에 씁니다. |
| 2 | Jin | La frase del día es "Quiero hacer el Camino". | 오늘의 문장: "나는 순례길을 걷고 싶어". |
| 3 | Jin | Con "querer" más infinitivo, digo lo que deseo. También, "Me gustaría hacerlo". | "querer + 동사원형"으로 바라는 걸 말한다. "Me gustaría hacerlo"라고도 한다. |
| 4 | Jin | Palabras nuevas: la credencial, el peregrino, la vieira. ¡Buen Camino! | 새 단어: 크레덴시알, 순례자, 가리비. 부엔 카미노! |

**Total spoken lines: 31** (1 + 2 + 4 + 5 + 6 + 4 + 5 + 4).

---

## 3. Vocab block (key words · ES ↔ KR)

| Español | 한국어 |
|---------|--------|
| querer (+ infinitivo) | ~하고 싶다 (동사원형과 함께) |
| me gustaría (+ infinitivo) | ~하면 좋겠다 (더 부드러운 표현) |
| la credencial (del peregrino) | 순례자 여권 |
| el peregrino / la peregrina | 순례자 |
| la vieira / la concha | 가리비 / 조개껍데기 (순례길의 상징) |
| el sello | 도장 (크레덴시알에 찍는) |
| el albergue | 알베르게 (순례자 숙소) |
| "Buen Camino" | 순례자들의 인사말 |

## 4. Cuaderno recap copy (the recap card text)

**Frase del día** → **Quiero hacer el Camino.** *(Me gustaría hacerlo. / Yo también quiero
hacerlo.)*
**Estructura:** `querer` / `me gustaría` + **infinitivo** → deseos e intenciones.
**Palabras:** la credencial · el peregrino · la vieira · el sello · **Despedida:** ¡Buen Camino!

## 5. On-screen text cards — **v1 method (no custom overlay)**

The diary renderer has **no native large-centered-text field**, and custom card segment types are
**deferred infra** (see format brief). So in v1 we do **not** overlay text. Instead:
- **Credencial beat (Scene 3 → 4):** use a **blank credencial close-up as the scene image**; the
  key sentence rides the **normal diary caption**. The empty card draws the eye to the caption.
- **Cuaderno beat (Scene 8):** use a **blank/lined journal-page image**; the key sentence + recap
  ride the normal caption. Loop still closes: heard → decided → written.

No overlay art, no English. Korean stays in the caption-translation lane only. (If we later add
`credencial_card` / `journal_card` segment types, this beat can upgrade to a true overlay — not v1.)

## 6. Handoff notes

**For the linguist**
- **DRAFT** → naturalness + A2+/B1-low ceiling before TTS.
- Grammar discipline: taught structure is strictly `querer`/`me gustaría` + infinitive; other
  verbs are known vocabulary. **Scene 3 "ha llegado" (present perfect) is deliberate scaffolding
  — keep it, but do not let present perfect proliferate** elsewhere and blur the `querer` target.
- Confirm the night-time journal reads Peninsular-natural (avoid "hoy + preterite"; the
  compressed script already avoids it).

**For image sourcing (the render blocker)**
- The repo has **no image-generation tool**; real scene art (cf. `assets/story/lucia_scene_*.png`,
  1920×1080, ~2 MB) is produced by an **external image model** and dropped into
  `assets/images/camino_a2_ep01_la_idea/`. This is a **human/external step**, not automatable by
  the designer agent (PIL-only).
- Deliverable to unblock: **8 scene images + 3 character reference sheets** per the spec in
  [diary-asset-sourcing.md](diary-asset-sourcing.md) — native 16:9, ≥1600×900 (rec 1920×1080),
  real PNG, plot-critical props/faces in the **top ~65%**, character continuity (fixed props:
  backpack colours, Jin's notebook). Ep01 is image-light and mostly avoids showing all three
  faces (envelope, blank credencial close-up, vieira, café interior, journal), which eases
  consistency.
- The `designer` agent's productive parallel task is to write the **image-generation brief**
  (per-scene prompts + reference-sheet prompts + safe-area/continuity constraints), which the
  external image step then executes.

**For the producer** (building `projects/camino_a2_ep01_la_idea.py` from `_template_historia_diary.py`)
- **Voices — the template `AUDIO` has NO `character_voices`; you must add it explicitly:**
  ```python
  "character_voices": {
      "Lucía": "es-ES-ElviraNeural",
      "Diego": "es-MX-JorgeNeural",
      "Jin":   "es-US-AlonsoNeural",
  },
  ```
  Keep `edge_voice` / `voice` as the **narrator** voice (e.g. `es-ES-XimenaNeural`). `Narrador`
  lines → `speaker = ""` (empty), never the string "Narrador".
- **CHAPTERS index after the cold-open reorder:** the template hardcodes
  `{"segment": 1, "title": "Introducción"}`. With the cold-open scene first, **chapter 1 will
  point at the cold-open — that is correct and intended (YouTube 0:00 = cold-open). Do NOT
  "fix" it as a bug.** Relabel chapter 1 accordingly (e.g. "La tarde en el café") and keep the
  final "Repaso final" → rename **"Cuaderno del peregrino"**.
- **Cards:** render Credencial/Cuaderno beats as **scene images + normal caption** (see §5) — no
  overlay field exists in v1.
- Image-consistency rule — no "all three facing front." Lean on the envelope, the blank
  credencial close-up, the vieira, three cups, hands, backs, Jin's cuaderno.
- **Diary gates** (run with `PYTHON=/Users/peter/spanish-lab/.venv/bin/python` — the worktree
  has no `.venv`): `check → debug → test → lint-spanish → tts → preview-diary → preview-qa-pack
  → preview-qa → human preview → publish-diary → verify`.

---

## 7. Linguist sign-off

**Status: APPROVED WITH CHANGES** · Linguist: Spanish Lab linguist · Date: 2026-07-01

### What was changed (3 lines, TTS punctuation only)

| Scene | Speaker | Change | Why |
|-------|---------|--------|-----|
| 7 · line 5 | Diego | `Se dice: "Buen Camino".` → `Se dice "Buen Camino".` | A colon immediately before a quoted phrase disrupts TTS prosody; the verb `se dice` already introduces the quote naturally without it. |
| 8 · line 2 | Jin | `La frase del día es: "Quiero…"` → `La frase del día es "Quiero…"` | Same reason. `es` + quote flows without a colon in spoken Spanish. |
| 8 · line 3 | Jin | `También: "Me gustaría hacerlo".` → `También, "Me gustaría hacerlo".` | A comma gives the TTS engine a natural micro-pause and avoids the colon-before-single-quote pattern. Meaning unchanged. |

### Line-by-line findings (all other lines)

**Naturalness / level (A2+/B1-low ceiling): PASS.**
Every line reads natural and warm. No line exceeds the A2+/B1-low ceiling. Camino/Peninsular-compatible markers are used correctly and consistently throughout:
- `Mirad` (Scene 3 · Lucía) — correct vosotros imperative, not Latin-American `miren`.
- `vosotros` (Scene 5 · Jin; Scene 6 · Lucía) — correct Peninsular second-person plural in both instances.
- `me da un poco de miedo` (Scene 6 · Jin) — idiomatic and natural.
- `Pues lo hacemos` (Scene 6 · Diego) — `pues` is natural for Diego's warm guide register without making him Spain-born.
- `¿lo hacemos?` (Scene 7 · Lucía) — natural colloquial commitment question, not stilted.
- Journal register (Scene 8) is telegraphic and note-like, which is intentional and appropriate. No `hoy + preterite` appears; the brief's instruction on this is satisfied.

**Grammar discipline (`querer`/`me gustaría` + infinitivo): PASS.**
Six key-sentence hits confirmed (Scenes 4, 4, 5, 5, 6, 7 + written callback in Scene 8). All occurrences are natural and none feel forced. Negative and plural variations (`No quiero esperar más`, `Queremos hacer el Camino juntos`) are well-chosen.

**Present perfect (scaffolding, not teaching target): PASS.**
Exactly two present-perfect forms appear in the pilot:
1. `ha llegado` (Scene 3 · Lucía) — Peninsular same-day relevance; deliberate scaffolding per brief.
2. `he hecho` (Scene 5 · Diego) — high-frequency fixed chunk (`nunca he hecho`); functions as known vocabulary, not a taught structure.
Neither instance competes with the `querer` focus. Present perfect does not proliferate. No further occurrences.

**`ser`/`estar` usage: PASS.** `Soy mexicano` (identity → `ser`), `la credencial todavía está vacía` (state → `estar`). Both correct.

**Gender/number agreement: PASS.** `Solo` (Diego/Jin, male) and `sola` (Lucía, female) are used correctly in Scene 6. No other agreement issues found.

**False friends / register risks: NONE DETECTED.**

### Voice-casting ruling (Diego es-MX, Jin es-US)

**APPROVED AS INTENTIONAL CHARACTER CHOICE.**

Rationale: Diego is canonically Mexican, so `es-MX-JorgeNeural` belongs to Diego. Jin remains the Korean-learner proxy whose Spanish is accurate and dialect-neutral; `es-US-AlonsoNeural` keeps him audibly distinct from Diego without adding Mexico-specific language to Jin's lines.

**Standing caveat for all future episodes:** Diego may explain Camino/Peninsular-compatible vocabulary, but he must not claim Spanish origin or frame Spain as his home country. Avoid Mexico-specific slang in Diego's lines unless the showrunner approves it for a specific beat. Jin's lines must remain dialect-neutral and pan-Hispanic/Peninsular-compatible.

### Note for the producer

The three TTS punctuation fixes above and the Diego canon fix are already applied in the script. The module can proceed to `make tts` once the producer has built `projects/camino_a2_ep01_la_idea.py` with the four-voice `character_voices` map. The lint-spanish gate (`make lint-spanish`) should pass on the corrected lines; if it flags the `"` quotation marks inside the caption field, that is a formatting-check false positive and not a Spanish language issue — escalate to the showrunner, not the linguist.
