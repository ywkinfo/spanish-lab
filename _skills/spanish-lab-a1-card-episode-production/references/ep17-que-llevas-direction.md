# Ep.17 `¿Qué llevas?` production direction

Use this as the preferred starting direction when Peter asks for Ep.17 production guidance and no approved Ep.17 source material exists yet.

## Recommended episode shape
- Working module: `projects/que_llevas_a1.py`
- Source text: `a1-que-llevas/descrip.md`
- Episode: `EPISODE = 17`, `LEVEL = "A1"`, `RENDER_TYPE = "cards"`
- Slug/output: `que-llevas`
- Working title: `¿Qué llevas?`
- Korean title idea: `오늘 뭐 입어요?`
- Content type: full A1 story-card episode, 16:9, Jin/Lucía/Diego continuity.
- One learning point: exactly one point — `Llevo + clothing noun` to say what someone is wearing/carrying in a simple travel-day context.

## Continuity rationale
Ep.16 taught `¿Qué tiempo hace?` / `Hace + weather`. Ep.17 should naturally connect weather to clothing choices:
- `Hace frío. Llevo una chaqueta.`
- `Hace sol. Llevo gafas de sol.`

This keeps the series practical for Korean travel learners: check the weather, choose clothes, then go out in Madrid.

## A1 vocabulary set
Keep vocabulary small and supportive of the single learning point:
- `una chaqueta`
- `una camiseta`
- `un abrigo`
- `unos zapatos`
- `unas gafas de sol`
- `un paraguas`

Avoid adding a second teaching point such as `necesito`, `me pongo`, or adjective agreement. If mentioned, keep it incidental and not as a lesson objective.

## Spanish/Korean examples
1. `¿Qué llevas?`
   - Literal Korean: `너는 무엇을 가지고/입고 있니?`
   - Natural Korean: `오늘 뭐 입었어요?`
2. `Llevo una chaqueta.`
   - Literal Korean: `나는 재킷 하나를 가지고/입고 있어요.`
   - Natural Korean: `저는 재킷을 입고 있어요.`
3. `Hace frío. Llevo un abrigo.`
   - Literal Korean: `추워요. 나는 코트 하나를 입고 있어요.`
   - Natural Korean: `추워서 코트를 입었어요.`
4. `Hace sol. Llevo gafas de sol.`
   - Literal Korean: `해가 나요. 나는 선글라스를 가지고/쓰고 있어요.`
   - Natural Korean: `햇빛이 있어서 선글라스를 써요.`

Human-review note: for Korean explanations, clarify that Spanish `llevar` can mean wear/carry depending on the object, but do not expand that into a separate grammar lesson.

## Suggested story blocks
1. Intro: connect weather to clothing.
2. Ask/answer: `¿Qué llevas?` / `Llevo...`.
3. Weather connection: `Hace frío. Llevo una chaqueta.`
4. Madrid walk/travel scene.
5. Recap with three safe `Llevo + noun` sentences.

Target production shape:
- About 4.5–5 minutes.
- Around 30 dialogue lines.
- 4 block headers.
- Intro followed by about a 3s transition before first dialogue.
- Recurring characters: Jin, Lucía, Diego.

## Visual direction
Follow the Ep.15/Ep.16 approved image workflow:
- Generate a direct 16:9 background/source image.
- Place characters/scene emphasis on the right.
- Leave clean negative space on the left for overlay.
- Avoid fake readable text, logos, clutter, or cropped heads.
- Scene idea: Madrid street or park entrance, sunny but a little cool; Jin wears a light jacket, Lucía and Diego nearby.

Thumbnail should follow the Ep.7-style pattern:
- Coral badge: `Español A1 · Ep.17`
- Main title: `¿Qué llevas?`
- Korean pill: `오늘 뭐 입어요?`
- Teal phrase pill: `Llevo una chaqueta`

## Intended artifact paths
```text
projects/que_llevas_a1.py
a1-que-llevas/descrip.md
images/ep17-que-llevas-source.png
thumbs/a1-ep17-que-llevas.jpg
output/thumbs/frases-a1-ep17-que-llevas.jpg
output/publish/frases-a1-ep17-que-llevas-16x9-v1.mp4
output/meta/frases-a1-ep17-que-llevas-16x9-v1.md
output/meta/frases-a1-ep17-que-llevas-16x9-v1.json
output/qa/que-llevas/final-contact-sheet-v1.jpg
```

## Validation chain
```sh
PROJECT=que_llevas_a1 PYTHON=.venv/bin/python make lint-spanish
PROJECT=que_llevas_a1 PYTHON=.venv/bin/python make tts
PROJECT=que_llevas_a1 PYTHON=.venv/bin/python make check
PROJECT=que_llevas_a1 PYTHON=.venv/bin/python make test
PROJECT=que_llevas_a1 PYTHON=.venv/bin/python make publish-cards
PROJECT=que_llevas_a1 PYTHON=.venv/bin/python make verify
```

## Direction draft path used in one session
A direction-only review draft was saved at:
```text
/opt/data/content/lessons/ep17-production-direction.md
```
This is not a final production artifact; use it only as a planning seed unless Peter approves or revises the direction.
