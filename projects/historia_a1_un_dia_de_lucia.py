"""DRAFT v2 (diary format) -- historia-a1 Ep.1: "Un día de Lucía en Madrid".

Comprehensible-input mini-historia (SERIES "historia-a1"). v2 diary format
adds STORY_SCENES with per-scene lines, ambient SFX slots, and pause timings.
Legacy PHRASES / BLOCKS / DIALOGUE / MINI_QUIZ kept for cards fallback.

Render path v2 = diary (scene images Phase 2, ambient SFX Phase 3).

STATUS: approved -- linguist signed off the es/ko lines 2026-05-31 (lint-spanish
clean, 0 errors / 0 warnings). Cleared for render/publish (30 fps final + diary
publish). SFX/ambient + intro/montage/outro segment beds balanced 2026-05-31.
Spec: control-plane docs/plans/format-mini-story-spec.md
"""

from __future__ import annotations

IMAGE_PATH = ""
DESCRIP_PATH = "historia-a1-un-dia-de-lucia/descrip.md"
OUTPUT_NAME = "historia-un-dia-de-lucia"
PUBLIC_SLUG = "historia-a1-un-dia-de-lucia"
YOUTUBE_URL = ""
SERIES = "historia-a1"
SERIES_TITLE = "Español A1 -- Mini-historias"
EPISODE = 1
LEVEL = "A1"
LANGUAGE = "es"
RENDER_VERSION = 5
RENDER_TYPE = "diary"
THUMBNAIL_PATH = "thumbs/historia-a1-ep01-un-dia-de-lucia.jpg"
YOUTUBE_TITLE = "Un día de Lucía en Madrid 🌞 하루 일과 따라가기 | Español A1 · Historia Ep.1"
DESCRIPTION_INTRO = (
    "Sigue un día de Lucía en Madrid en español A1: por la mañana, en el metro, "
    "en la calle y en la cafetería con Diego. Una mini-historia con frases que ya "
    "conoces, para escuchar y entender sin esfuerzo."
)
DESCRIPTION_OUTRO = (
    "Vuelve a ver la historia e intenta contar el día de Lucía con primero, luego, "
    "después y al final. En la próxima historia seguimos con otra escena de su semana."
)
KOREAN_TEASER = (
    "한국어 티저: 이미 배운 표현(커피·지하철·날씨·인사)으로 만든 짧은 이야기예요. "
    "Lucía의 하루를 따라가며 primero(먼저)·luego(그다음)·después(그 후)·al final(마지막에) "
    "순서 표현을 자연스럽게 익혀요. A1 수준, 천천히 듣고 이해하기."
)
BASE_TAGS = [
    "스페인어",
    "스페인어 입문",
    "스페인어 A1",
    "Spanish A1",
    "aprender español",
    "español para principiantes",
]
EXTRA_TAGS = [
    "historia en español A1",
    "mini historia español",
    "español comprensible",
    "스페인어 이야기",
    "스페인어 듣기 연습",
    "Spanish story for beginners",
]
BASE_HASHTAGS = ["#EspañolA1", "#aprenderespañol", "#스페인어"]
EXTRA_HASHTAGS = ["#SpanishA1", "#historiaenespañol", "#스페인어이야기"]

# ---------------------------------------------------------------------------
# Legacy cards data (fallback)
# ---------------------------------------------------------------------------
PHRASES = [
    (1, "Es por la mañana. Lucía se despierta.", "아침이에요. Lucía가 일어나요.", "Lucía se despierta a las siete."),
    (2, "Primero, Lucía toma un café.", "먼저, Lucía는 커피를 마셔요.", "Primero, un café con leche."),
    (3, "Me gusta el café por la mañana.", "아침에 커피가 좋아요.", "Me gusta mucho el café."),
    (4, "Luego, Lucía va al centro en metro.", "그다음, Lucía는 지하철로 시내에 가요.", "Luego, va al centro."),
    (5, "¿Dónde está el metro? Está allí.", "지하철이 어디 있어요? 저기 있어요.", "El metro está allí, cerca."),
    (6, "Hace sol en Madrid. ¡Qué bonito!", "마드리드는 해가 나요. 정말 예뻐요!", "Hoy hace sol en Madrid."),
    (7, "Después, Lucía ve a su amigo Diego.", "그 후, Lucía는 친구 Diego를 만나요.", "Después, ve a Diego."),
    (8, "Hola, Diego. ¿Cómo estás?", "안녕, Diego. 어떻게 지내?", "Hola, ¿cómo estás hoy?"),
    (9, "Estoy muy bien. ¿Tomamos un café?", "아주 잘 지내. 커피 마실까?", "Estoy muy bien, gracias."),
    (10, "Sí. Un café, por favor.", "응. 커피 한 잔 주세요.", "Un café, por favor."),
    (11, "Al final, Lucía vuelve a casa.", "마지막에, Lucía는 집에 돌아가요.", "Al final, vuelve a casa."),
    (12, "¡Qué buen día!, dice Lucía.", "\"정말 좋은 하루야!\", Lucía가 말해요.", "¡Qué buen día!"),
]
BLOCKS = [
    {"block_id": 1, "title_es": "Por la mañana", "title_ko": "아침", "color_block": "coral", "start": 1},
    {"block_id": 2, "title_es": "En el metro", "title_ko": "지하철에서", "color_block": "amber", "start": 4},
    {"block_id": 3, "title_es": "En la calle", "title_ko": "거리에서", "color_block": "teal", "start": 6},
    {"block_id": 4, "title_es": "En la cafetería", "title_ko": "카페에서", "color_block": "blue", "start": 8},
    {"block_id": 5, "title_es": "Al final del día", "title_ko": "하루의 끝", "color_block": "green", "start": 11},
]
DIALOGUE = [
    ("Lucía", "Hola, Diego. ¿Cómo estás?", "안녕, Diego. 어떻게 지내?"),
    ("Diego", "Estoy muy bien. ¿Tomamos un café?", "아주 잘 지내. 커피 마실까?"),
    ("Lucía", "Sí. Un café, por favor.", "응. 커피 한 잔 주세요."),
]
MINI_QUIZ = [
    ("¿Cómo dices '먼저'?", "Primero"),
    ("¿Cómo dices '그다음'?", "Luego"),
    ("¿Cómo dices '마지막에'?", "Al final"),
    ("¿Cómo preguntas '어떻게 지내?'", "¿Cómo estás?"),
    ("¿Cómo dices '정말 좋은 하루야!'?", "¡Qué buen día!"),
]

# ---------------------------------------------------------------------------
# Visual design
# ---------------------------------------------------------------------------
DESIGN = {
    "output_size": (1920, 1080),
    "font_path": "assets/fonts/NotoSansKR-Bold.ttf",
    "font_index": 0,
    "font_path_ko": "assets/fonts/NotoSansKR-Regular.ttf",
    "font_index_ko": 0,
    "font_size_title": 82,
    "font_size_es": 84,
    "min_font_size_es": 52,
    "font_size_ko": 36,
    "font_size_example": 34,
    "background_color": (248, 247, 242),
    "text_color": (31, 35, 40),
    "muted_text_color": (96, 101, 109),
    "intro_title": "Un día de Lucía",
    "intro_subtitle": "Español A1 · Historia Ep.1",
    "intro_ko": "Lucía의 마드리드 하루",
    "thumbnail_title": "Un día de Lucía",
    "thumbnail_subtitle": "Español A1 · Historia",
    "thumbnail_ko": "Primero · Luego · Al final",
    "outro_ko": "다음 이야기에서 또 만나요",
    "color_blocks": {
        "coral": (224, 91, 76),
        "amber": (230, 158, 62),
        "teal": (44, 150, 142),
        "blue": (70, 120, 196),
        "green": (92, 148, 86),
        "neutral": (42, 48, 57),
    },
}

# ---------------------------------------------------------------------------
# v2 diary: STORY_SCENES
# ---------------------------------------------------------------------------
STORY_SCENES = [
    {
        "scene_id": 1,
        "title_es": "Por la mañana",
        "title_ko": "아침, 하루의 시작",
        "image_path": "assets/story/lucia_scene_01_morning.png",
        "ambient_sfx": "assets/audio/sfx/madrid_morning.wav",
        "ambient_sfx_license": "CC0",
        "pause_s": 2.0,
        "lines": [
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Es por la mañana en Madrid.",
                "text_ko": "마드리드의 아침이에요.",
            },
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Lucía se levanta temprano porque hoy tiene clase.",
                "text_ko": "Lucía는 오늘 수업이 있어서 일찍 일어나요.",
            },
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Abre la ventana y mira la calle.",
                "text_ko": "창문을 열고 거리를 바라봐요.",
            },
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Hay sol, y la ciudad empieza a moverse.",
                "text_ko": "해가 나고, 도시가 움직이기 시작해요.",
            },
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Toma café con leche y una tostada.",
                "text_ko": "카페라떼와 토스트를 먹어요.",
            },
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Escribe en su diario: Hoy quiero tener un día tranquilo.",
                "text_ko": "일기에 써요. 오늘은 조용한 하루를 보내고 싶다.",
            },
        ],
    },

    {
        "scene_id": 2,
        "title_es": "Un pequeño error",
        "title_ko": "작은 실수",
        "image_path": "assets/story/lucia_scene_02_bag.png",
        "ambient_sfx": "assets/audio/sfx/home_morning.wav",
        "ambient_sfx_license": "CC0",
        "ambient_sfx_volume_db": -9.0,
        "pause_s": 2.0,
        "lines": [
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Lucía prepara su bolso para ir a la universidad.",
                "text_ko": "Lucía는 대학교에 가려고 가방을 준비해요.",
            },
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Mete el móvil, las llaves y una botella de agua.",
                "text_ko": "휴대폰, 열쇠, 물병을 넣어요.",
            },
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Pero el cuaderno azul se queda en la mesa.",
                "text_ko": "하지만 파란 공책은 식탁 위에 남아 있어요.",
            },
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Lucía mira el reloj y dice: ¡Voy tarde!",
                "text_ko": "Lucía는 시계를 보고 말해요. 늦겠다!",
            },
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Sale de casa rápido y camina al metro.",
                "text_ko": "집에서 빨리 나와 지하철역으로 걸어가요.",
            },
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Nadie ve el cuaderno en la mesa.",
                "text_ko": "아무도 식탁 위의 공책을 보지 못해요.",
            },
        ],
    },

    {
        "scene_id": 3,
        "title_es": "En el metro",
        "title_ko": "지하철 안에서",
        "image_path": "assets/story/lucia_scene_03_metro.png",
        "ambient_sfx": "assets/audio/sfx/metro_inside.wav",
        "ambient_sfx_license": "CC0",
        "pause_s": 2.0,
        "lines": [
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Lucía llega a la estación de metro.",
                "text_ko": "Lucía는 지하철역에 도착해요.",
            },
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Hay muchas personas: estudiantes, trabajadores y turistas.",
                "text_ko": "학생, 직장인, 관광객 등 사람이 많아요.",
            },
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Lucía entra en el metro y se sienta.",
                "text_ko": "Lucía는 지하철에 타서 앉아요.",
            },
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Quiere repasar sus notas antes de la clase.",
                "text_ko": "수업 전에 필기를 복습하고 싶어요.",
            },
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Busca el cuaderno en el bolso, pero no está.",
                "text_ko": "가방에서 공책을 찾지만 없어요.",
            },
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "¿Dónde está mi cuaderno azul?, piensa Lucía.",
                "text_ko": "내 파란 공책이 어디 있지? Lucía는 생각해요.",
            },
        ],
    },

    {
        "scene_id": 4,
        "title_es": "Un mensaje a Diego",
        "title_ko": "Diego에게 보내는 메시지",
        "image_path": "assets/story/lucia_scene_04_message.png",
        "ambient_sfx": "assets/audio/sfx/soft_phone_typing.wav",
        "ambient_sfx_license": "CC0",
        "pause_s": 2.0,
        "lines": [
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Lucía escribe un mensaje a Diego, su compañero de piso.",
                "text_ko": "Lucía는 룸메이트 Diego에게 메시지를 써요.",
            },
            {
                "kind": "dialogue",
                "speaker": "Lucía",
                "text_es": "Hola, Diego. ¿Estás cerca de casa?",
                "text_ko": "안녕, Diego. 집 근처에 있어?",
            },
            {
                "kind": "dialogue",
                "speaker": "Diego",
                "text_es": "Sí, estoy en la cafetería de la esquina.",
                "text_ko": "응, 모퉁이 카페에 있어.",
            },
            {
                "kind": "dialogue",
                "speaker": "Lucía",
                "text_es": "Creo que mi cuaderno azul está en la mesa.",
                "text_ko": "내 파란 공책이 식탁 위에 있는 것 같아.",
            },
            {
                "kind": "dialogue",
                "speaker": "Diego",
                "text_es": "Voy a casa y lo miro. No te preocupes.",
                "text_ko": "집에 가서 확인해 볼게. 걱정하지 마.",
            },
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Lucía lee el mensaje y respira un poco mejor.",
                "text_ko": "Lucía는 메시지를 읽고 조금 안심해요.",
            },
        ],
    },

    {
        "scene_id": 5,
        "title_es": "En la universidad",
        "title_ko": "대학교에서",
        "image_path": "assets/story/lucia_scene_05_university.png",
        "ambient_sfx": "assets/audio/sfx/classroom_soft.wav",
        "ambient_sfx_license": "CC0",
        "ambient_sfx_volume_db": -8.0,
        "pause_s": 2.0,
        "lines": [
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Lucía llega a la universidad.",
                "text_ko": "Lucía는 대학교에 도착해요.",
            },
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "En la clase, todos sacan sus cuadernos.",
                "text_ko": "수업에서 모두 공책을 꺼내요.",
            },
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Lucía busca su cuaderno, pero no lo tiene.",
                "text_ko": "Lucía는 공책을 찾지만 가지고 있지 않아요.",
            },
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "No puede tomar notas como siempre.",
                "text_ko": "평소처럼 필기를 할 수 없어요.",
            },
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Entonces levanta la mano y habla con la profesora.",
                "text_ko": "그래서 손을 들고 교수님께 말해요.",
            },
            {
                "kind": "dialogue",
                "speaker": "Lucía",
                "text_es": "Perdón, ¿puedo grabar el audio de la clase en mi móvil?",
                "text_ko": "죄송하지만, 휴대폰으로 수업 음성을 녹음해도 될까요?",
            },
            {
                "kind": "dialogue",
                "speaker": "Profesora",
                "text_es": "Sí, claro. Pero solo para estudiar.",
                "text_ko": "네, 좋아요. 하지만 공부할 때만 사용하세요.",
            },
        ],
    },

    {
        "scene_id": 6,
        "title_es": "Por las calles de Madrid",
        "title_ko": "마드리드 거리에서",
        "image_path": "assets/story/lucia_scene_06_madrid_street.png",
        "ambient_sfx": "assets/audio/sfx/madrid_street.wav",
        "ambient_sfx_license": "CC0",
        "pause_s": 2.0,
        "lines": [
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Después de clase, Lucía camina por Madrid.",
                "text_ko": "수업이 끝난 후, Lucía는 마드리드를 걸어요.",
            },
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Pasa por una panadería, una librería y una plaza pequeña.",
                "text_ko": "빵집, 서점, 작은 광장을 지나가요.",
            },
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "En la calle, huele a pan y a café.",
                "text_ko": "거리에서는 빵과 커피 냄새가 나요.",
            },
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Lucía recibe un mensaje de Diego.",
                "text_ko": "Lucía는 Diego에게서 메시지를 받아요.",
            },
            {
                "kind": "dialogue",
                "speaker": "Diego",
                "text_es": "Tengo tu cuaderno. Estoy cerca de la Plaza Mayor.",
                "text_ko": "네 공책 있어. 나는 마요르 광장 근처에 있어.",
            },
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Lucía sonríe y camina hacia allí.",
                "text_ko": "Lucía는 미소 짓고 그쪽으로 걸어가요.",
            },
        ],
    },

    {
        "scene_id": 7,
        "title_es": "Lluvia y churros",
        "title_ko": "비와 추로스",
        "image_path": "assets/story/lucia_scene_07_churros.png",
        "ambient_sfx": "assets/audio/sfx/rain_cafe.wav",
        "ambient_sfx_license": "CC0",
        "pause_s": 2.0,
        "lines": [
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "De repente, el cielo cambia.",
                "text_ko": "갑자기 하늘이 변해요.",
            },
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Hace viento y empieza a llover.",
                "text_ko": "바람이 불고 비가 오기 시작해요.",
            },
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Lucía no tiene paraguas.",
                "text_ko": "Lucía는 우산이 없어요.",
            },
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Corre a una cafetería cercana.",
                "text_ko": "근처 카페로 뛰어가요.",
            },
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Dentro de la cafetería, ve a Diego con su cuaderno.",
                "text_ko": "카페 안에서, 공책을 들고 있는 Diego를 봐요.",
            },
            {
                "kind": "dialogue",
                "speaker": "Diego",
                "text_es": "Aquí está tu cuaderno azul.",
                "text_ko": "여기 네 파란 공책이 있어.",
            },
            {
                "kind": "dialogue",
                "speaker": "Lucía",
                "text_es": "¡Mi cuaderno! ¡Muchas gracias, Diego! Me has ayudado mucho.",
                "text_ko": "내 공책! 정말 고마워, Diego! 네가 정말 많이 도와줬어.",
            },
            {
                "kind": "dialogue",
                "speaker": "Diego",
                "text_es": "Entonces, ¿tomamos chocolate con churros?",
                "text_ko": "그럼 우리 초콜릿과 추로스를 먹을까?",
            },
        ],
    },

    {
        "scene_id": 8,
        "title_es": "El diario de la noche",
        "title_ko": "밤의 일기",
        "image_path": "assets/story/lucia_scene_08_diary.png",
        "ambient_sfx": "assets/audio/sfx/quiet_night_room.wav",
        "ambient_sfx_license": "CC0",
        "ambient_sfx_volume_db": -6.0,
        "pause_s": 2.0,
        "lines": [
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Por la noche, Lucía vuelve a casa.",
                "text_ko": "밤에 Lucía는 집으로 돌아와요.",
            },
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Se sienta en su escritorio y abre su diario.",
                "text_ko": "책상에 앉아 일기를 열어요.",
            },
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Hoy he salido de casa con prisa.",
                "text_ko": "오늘 나는 급하게 집을 나섰다.",
            },
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "He olvidado mi cuaderno azul en la mesa.",
                "text_ko": "파란 공책을 식탁 위에 두고 왔다.",
            },
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "En la clase, he grabado el audio con permiso de la profesora.",
                "text_ko": "수업에서는 교수님의 허락을 받고 음성을 녹음했다.",
            },
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Después, he caminado por Madrid y he visto calles bonitas.",
                "text_ko": "그 후 마드리드를 걸었고 예쁜 거리들을 보았다.",
            },
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Ha llovido, pero Diego me ha ayudado.",
                "text_ko": "비가 왔지만 Diego가 나를 도와줬다.",
            },
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "No ha sido un día tranquilo. Ha sido un día especial.",
                "text_ko": "조용한 하루는 아니었다. 특별한 하루였다.",
            },
        ],
    },
]

SFX_MANIFEST = [
    {
        "id": "door_close_footsteps",
        "kind": "spot",
        "scene_id": 2,
        "line_index": 6,
        "offset_s": 0.0,
        "path": "assets/audio/sfx/door_close_footsteps.wav",
        "volume_db": -10.6,
        "license": "CC0",
    },
    {
        "id": "metro_chime",
        "kind": "spot",
        "scene_id": 3,
        "line_index": 1,
        "offset_s": 0.0,
        "path": "assets/audio/sfx/metro_chime.wav",
        "volume_db": -10.6,
        "license": "CC0",
    },
    {
        "id": "phone_typing_send",
        "kind": "spot",
        "scene_id": 4,
        "line_index": 1,
        "offset_s": 0.5,
        "path": "assets/audio/sfx/phone_typing_send.wav",
        "volume_db": -10.6,
        "license": "CC0",
    },
    {
        "id": "chair_murmur",
        "kind": "spot",
        "scene_id": 5,
        "line_index": 6,
        "offset_s": 0.0,
        "path": "assets/audio/sfx/chair_murmur.wav",
        "volume_db": -10.6,
        "license": "CC0",
    },
    {
        "id": "thunder_rain",
        "kind": "spot",
        "scene_id": 7,
        "line_index": 1,
        "offset_s": 0.0,
        "path": "assets/audio/sfx/thunder_rain.wav",
        "volume_db": -10.6,
        "license": "CC0",
    },
    {
        "id": "doorbell_cups",
        "kind": "spot",
        "scene_id": 7,
        "line_index": 5,
        "offset_s": 0.0,
        "path": "assets/audio/sfx/doorbell_cups.wav",
        "volume_db": -10.6,
        "license": "CC0",
    },
    {
        "id": "night_tone_pen",
        "kind": "spot",
        "scene_id": 8,
        "line_index": 1,
        "offset_s": 0.0,
        "path": "assets/audio/sfx/night_tone_pen.wav",
        "volume_db": -10.6,
        "license": "CC0",
    },
]

# Out-of-scene segment SFX: the intro/montage/outro carry no scene_id and so are
# never reached by the ambient beds above. These fill that space -- a cheerful
# morning opener under the intro, a warm recap bed under the montage, and a calm
# evening bed under the outro. mode="bed" loops the clip across the segment span.
SEGMENT_SFX = [
    {
        "id": "intro_morning_madrid",
        "kind": "segment",
        "segment_type": "intro",
        "mode": "bed",
        "offset_s": 0.0,
        "path": "assets/audio/sfx/intro_morning_madrid.wav",
        "volume_db": -4.9,
        "license": "CC0",
    },
    {
        "id": "montage_warm_shimmer",
        "kind": "segment",
        "segment_type": "montage",
        "mode": "bed",
        "offset_s": 0.0,
        "path": "assets/audio/sfx/montage_warm_shimmer.wav",
        "volume_db": -3.9,
        "license": "CC0",
    },
    {
        "id": "outro_evening_calm",
        "kind": "segment",
        "segment_type": "outro",
        "mode": "bed",
        "offset_s": 0.0,
        "path": "assets/audio/sfx/outro_evening_calm.wav",
        "volume_db": -6.9,
        "license": "CC0",
    },
]

# ---------------------------------------------------------------------------
# Segment builder (v2 diary)
# ---------------------------------------------------------------------------

def _build_diary_segments() -> list[dict]:
    """Generate SEGMENTS from STORY_SCENES for the diary render pipeline."""
    segments: list[dict] = [
        {
            "type": "intro",
            "text_es": (
                "Hoy seguimos un día de Lucía en Madrid. Vas a escuchar frases que ya "
                "conoces: el café, el metro, el tiempo y un saludo. Fíjate en cuatro "
                "palabras de orden: primero, luego, después y al final."
            ),
            "duration_s": 16.0,
        }
    ]
    for scene in STORY_SCENES:
        # Scene header
        segments.append(
            {
                "type": "scene_header",
                "scene_id": scene["scene_id"],
                "title_es": scene["title_es"],
                "title_ko": scene["title_ko"],
                "duration_s": 3.0,
            }
        )
        # Lines
        for line in scene["lines"]:
            resolved_img = line.get("image_path") or scene.get("image_path", "")
            seg = {
                "type": "diary_line",
                "scene_id": scene["scene_id"],
                "kind": line["kind"],
                "speaker": line["speaker"],
                "text_es": line["text_es"],
                "text_ko": line["text_ko"],
                "image_path": resolved_img,
            }
            if "duration_s" in line:
                seg["duration_s"] = line["duration_s"]
            if "min_hold_s" in line:
                seg["min_hold_s"] = line["min_hold_s"]
            if "processing_pause_s" in line:
                seg["processing_pause_s"] = line["processing_pause_s"]
            segments.append(seg)
        # Pause after scene
        last_line_img = scene["lines"][-1].get("image_path") or scene.get("image_path", "") if scene["lines"] else scene.get("image_path", "")
        segments.append(
            {
                "type": "pause",
                "scene_id": scene["scene_id"],
                "duration_s": scene["pause_s"],
                "image_path": last_line_img,
            }
        )
    # Montage
    segments.append(
        {
            "type": "montage",
            "duration_s": 6.0,
        }
    )
    # Outro
    segments.append(
        {
            "type": "outro",
            "text_es": (
                "Muy bien. Ahora intenta contar el día de Lucía: primero, luego, "
                "después y al final. Practica otra vez y cuéntalo en voz alta."
            ),
            "duration_s": 15.0,
        }
    )
    return segments


SEGMENTS = _build_diary_segments()
CHAPTERS = [
    {"segment": 1, "title": "Introducción"},
    {"segment": 2, "title": "아침, 하루의 시작"},
    {"segment": 10, "title": "작은 실수"},
    {"segment": 18, "title": "지하철 안에서"},
    {"segment": 26, "title": "Diego에게 보내는 메시지"},
    {"segment": 34, "title": "대학교에서"},
    {"segment": 43, "title": "마드리드 거리에서"},
    {"segment": 51, "title": "비와 추로스"},
    {"segment": 61, "title": "밤의 일기"},
    {"segment": len(SEGMENTS), "title": "Repaso final"},
]
AUDIO = {
    "tts_engine": "edge",
    "edge_voice": "es-ES-ElviraNeural",
    "edge_rate": "+8%",
    "edge_pitch": "+0Hz",
    "edge_volume": "+0%",
    "voice": "es-ES-ElviraNeural",
    "rate_wpm": 160,
    "lead_padding_s": 0.25,
    "tail_padding_s": 0.4,
    "min_duration_s": 3.0,
    "readability_floor_ratio": 0.0,
        "processing_pause_s": 2.5,
    "min_hold_s": 2.5,
    "ambient_bed_db": -11.9,
    "bgm_path": "assets/audio/fur_elise_inspired_soft_piano.wav",
    # fur_elise source is very quiet (~-40 dB mean); a small positive gain keeps
    # the piano a faint wash that sits clearly UNDER the scene ambience, so the
    # narration-free gaps feel like the location, not a piano recital.
    "bgm_volume_db": 6.0,
    "narration_volume_db": 0.0,
    "ducking": True,
    "ducking_threshold": 0.05,
    "ducking_ratio": 4,
    "ducking_attack_ms": 80,
    "ducking_release_ms": 550,
    "fade_in_s": 4.0,
    "fade_out_s": 5.0,
    "audio_codec": "aac",
    "audio_bitrate_kbps": 192,
    "sample_rate_hz": 44100,
}
