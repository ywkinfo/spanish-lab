# Español en el Camino — Seed Benchmark Notes

**Status: seed benchmark.** Only **Extra ep1** has been torn down so far; the other axes are
pending (see the bottom of this file). Do not treat this as a completed benchmark.

Reference-video teardown feeding **"Español en el Camino"** — an **A2+/B1-low** immersion
dialogue drama (3 friends walk the Camino de Santiago; built on `RENDER_TYPE = "diary"`).
Canonical brief: [camino-format-brief.md](camino-format-brief.md).
Tool: `claude-video` (`/watch`) — frames + transcript teardown of reference videos.

Method: structure pass (sparse) + focused 2-min pass at `--resolution 1024` for
subtitle/text craft. Each entry lists **what they do** and **what we steal / what
we can't** given our constraint of *generated stills + Ken Burns + TTS* (no live actors).

---

## Axis ① Multi-character dialogue + embedded lesson — **Extr@ en Español, Ep.1 "La llegada de Sam"**

- Source watched: `youtube.com/watch?v=z-dx6kd5f4E` (segment 1a, 9:26), 50 frames @1024px, no captions (frames-only).
- Note: the canonical sub'd upload `NfAbVaKbQuk` is dead (account terminated) — yt-dlp fragility confirmed; keep backup URLs per target.

**What they do**
- **Cold open = establishing shot of the place** (t=00:00, exterior of the Madrid flat, blue sky), no people/text yet. Geography sets the scene before any character.
- **Episode title delivered ~1 min in**, overlaid at bottom over an *action* shot ("1: La llegada de Sam", t=01:08) — hook first, label later.
- **Expressive faces + tight two-shot blocking** carry the comedy (t=02:05 Lola reacting; t=07:22 two-hander conflict pose).
- **Register switch via B&W + props**: an imagined/fantasy beat rendered in black-and-white with a US-flag prop (t=04:21) to mark "this isn't real / daydream."
- **Signature pedagogical device — on-screen written-message cards** (t=08:52): a pink split-screen "email" card, `De: lola / Para: isa`, renders ONE key sentence as large readable Spanish text — *"Mi corresponsal Sam Scott ha llegado esta mañana."* Reinforces the spoken line AND spotlights a grammar point (present perfect *ha llegado*). One teachable sentence on screen at a time.

**What we steal**
- Etapa cold-open = **establishing still of the place** (maps perfectly to etapa-as-location). Title/etapa label drops ~45–60s in, after the hook.
- **Message/letter/postcard cards** rendering one key sentence as readable text — directly portable, aligns with our caption bar + `Cuaderno del peregrino`. Use peregrino texts, journal entries, trail signs.
- **Desaturate a still for memory/fantasy/flashback** beats — a cheap, reproducible register marker we CAN do in stills.
- **One teachable sentence on screen at a time**, slow and clear — fits our caption safe-area + A2+/B1-low ceiling.

**What we can't (the gap)**
- Extra leans on **live physical performance** (facial comedy, blocking) we can't reproduce in Ken Burns stills. We compensate with: distinct **per-speaker voices**, tighter scene cuts, and stronger dialogue writing. This raises the bar on our 3-voice TTS decision and on expressive scene-image art direction.

**Open**: no transcript pulled (no captions + no Whisper key) → could not analyze spoken
dialogue *rhythm / lesson density* precisely. Visual devices were fully readable from
frames alone. To get dialogue-level teardown, add a free Groq key (Whisper) — decision pending.

---

## Pending targets
- ② Serialized arc + difficulty ramp — **Destinos** (telenovela, 52 eps)
- ③ CI pacing + no-English scaffolding — **Dreaming Spanish** (intermediate/advanced story)
- ④ Camino travel storytelling (etapa structure, landscape-as-emotion) — Camino Francés doc/vlog series
- ⑤ Korean-audience expectation (thumbnail/teaser/subtitle conventions) — 시원스쿨 스페인어 / 스패니시마스터
