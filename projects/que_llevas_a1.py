"""A1 story-card episode: Jin talks about clothing in Madrid."""

from __future__ import annotations

IMAGE_PATH = "images/ep17-que-llevas-source.png"
DESCRIP_PATH = "a1-que-llevas/descrip.md"
OUTPUT_NAME = "que-llevas"
PUBLIC_SLUG = "a1-que-llevas"
YOUTUBE_URL = ""
SERIES = "frases-a1"
SERIES_TITLE = "Español A1 -- Frases útiles"
EPISODE = 17
LEVEL = "A1"
LANGUAGE = "es"
RENDER_VERSION = 1
RENDER_TYPE = "cards"
THUMBNAIL_PATH = "thumbs/a1-ep17-que-llevas.jpg"
YOUTUBE_TITLE = "¿Qué llevas? 🧥 오늘 뭐 입어요? | Español A1 · Ep.17"
DESCRIPTION_INTRO = (
    "Jin sigue practicando en Madrid con Lucía y Diego. Después de hablar del tiempo, "
    "aprende una frase A1 muy práctica para la ropa: ¿Qué llevas? Practicamos llevo una "
    "chaqueta, llevo un abrigo, llevo gafas de sol y llevo un paraguas."
)
DESCRIPTION_OUTRO = (
    "Escucha primero, repite en voz alta y después responde con tu ropa de hoy: "
    "¿Qué llevas? Llevo una chaqueta, llevo un abrigo o llevo gafas de sol."
)
KOREAN_TEASER = (
    "한국어 티저: EP.17에서는 날씨 다음 단계로 옷차림을 말합니다. 핵심 표현은 하나, "
    "Llevo + 옷 이름입니다. ¿Qué llevas? 라고 묻고 Llevo una chaqueta로 대답해 보세요."
)
BASE_TAGS = ["스페인어", "스페인어 입문", "스페인어 A1", "Spanish A1", "aprender español", "español para principiantes"]
EXTRA_TAGS = ["Qué llevas", "ropa en español", "llevo una chaqueta", "Spanish clothing vocabulary", "스페인어 옷", "스페인어 회화"]
BASE_HASHTAGS = ["#EspañolA1", "#aprenderespañol", "#스페인어"]
EXTRA_HASHTAGS = ["#SpanishA1", "#Madrid", "#옷표현"]

CHARACTERS = {
    "Jin": "assets/characters/peter-profile.png",
    "Lucía": "assets/characters/lucia-profile.png",
    "Diego": "assets/characters/diego-profile.png",
}
CHARACTER_VOICES = {
    "Lucía": "es-ES-ElviraNeural",
    "Jin": "es-ES-AlvaroNeural",
    "Diego": "es-MX-JorgeNeural",
}
CLOTHING_IMAGES = {
    "chaqueta": "assets/generated/clothing/chaqueta.png",
    "abrigo": "assets/generated/clothing/abrigo.png",
    "camiseta": "assets/generated/clothing/camiseta.png",
    "zapatos": "assets/generated/clothing/zapatos.png",
    "gafas": "assets/generated/clothing/gafas.png",
    "paraguas": "assets/generated/clothing/paraguas.png",
}

BLOCKS = [
    {"block_id": 1, "title_es": "¿Qué llevas?", "title_ko": "오늘 뭐 입어요?", "color_block": "coral", "start": 1, "clothing_items": ["chaqueta"]},
    {"block_id": 2, "title_es": "Hace frío", "title_ko": "추워요", "color_block": "teal", "start": 7, "clothing_items": ["abrigo", "chaqueta"]},
    {"block_id": 3, "title_es": "Hace sol", "title_ko": "해가 나요", "color_block": "amber", "start": 13, "clothing_items": ["gafas", "camiseta", "zapatos"]},
    {"block_id": 4, "title_es": "Mini prueba", "title_ko": "미니 퀴즈", "color_block": "blue", "start": 20, "clothing_items": ["paraguas", "chaqueta"]},
]

# line_num, speaker, Spanish, Korean, focus, block_id, color, duration_s, clothing_items
DIALOGUE = [
    (1, "Diego", "Hoy hablamos de la ropa en Madrid.", "오늘은 마드리드에서 옷에 대해 이야기해요.", "ropa", 1, "coral", 8.5, ["chaqueta", "gafas"]),
    (2, "Jin", "Lucía, ¿qué llevas hoy?", "Lucía, 오늘 뭐 입었어요?", "¿qué llevas?", 1, "coral", 9.0, ["chaqueta"]),
    (3, "Lucía", "Llevo una chaqueta.", "저는 재킷을 입고 있어요.", "llevo + ropa", 1, "coral", 8.5, ["chaqueta"]),
    (4, "Diego", "Muy bien. Para la ropa usamos llevo.", "아주 좋아요. 옷에는 llevo를 써요.", "llevo", 1, "coral", 9.5, ["chaqueta"]),
    (5, "Jin", "¿Qué llevas?", "뭐 입었어요?", "pregunta", 1, "coral", 7.5, ["chaqueta"]),
    (6, "Lucía", "Llevo una chaqueta.", "저는 재킷을 입고 있어요.", "respuesta", 1, "coral", 8.0, ["chaqueta"]),
    (7, "Jin", "Hace frío. Llevo un abrigo.", "추워서 코트를 입었어요.", "un abrigo", 2, "teal", 9.5, ["abrigo"]),
    (8, "Diego", "Un abrigo es para el frío.", "abrigo는 추울 때 입는 코트예요.", "abrigo", 2, "teal", 8.5, ["abrigo"]),
    (9, "Lucía", "Hace frío. Llevo una chaqueta.", "추워서 재킷을 입었어요.", "una chaqueta", 2, "teal", 9.5, ["chaqueta"]),
    (10, "Diego", "Un abrigo. Una chaqueta.", "코트 하나. 재킷 하나.", "abrigo / chaqueta", 2, "teal", 9.0, ["abrigo", "chaqueta"]),
    (11, "Diego", "Repite: llevo un abrigo.", "따라 해요: 저는 코트를 입고 있어요.", "shadowing", 2, "teal", 8.5, ["abrigo"]),
    (12, "Jin", "Llevo un abrigo.", "저는 코트를 입고 있어요.", "repite", 2, "teal", 7.5, ["abrigo"]),
    (13, "Lucía", "Hace sol en Madrid.", "마드리드는 해가 나요.", "hace sol", 3, "amber", 8.0, ["gafas"]),
    (14, "Lucía", "Hace sol. Llevo gafas de sol.", "햇빛이 있어서 선글라스를 써요.", "gafas de sol", 3, "amber", 9.5, ["gafas"]),
    (15, "Jin", "Llevo una camiseta.", "저는 티셔츠를 입고 있어요.", "una camiseta", 3, "amber", 8.0, ["camiseta"]),
    (16, "Diego", "Yo llevo unos zapatos cómodos.", "저는 편한 신발을 신고 있어요.", "unos zapatos", 3, "amber", 9.0, ["zapatos"]),
    (17, "Diego", "Gafas de sol, camiseta y zapatos.", "선글라스, 티셔츠, 그리고 신발이에요.", "vocabulario", 3, "amber", 9.5, ["gafas", "camiseta", "zapatos"]),
    (18, "Jin", "Llevo gafas de sol.", "저는 선글라스를 써요.", "repite", 3, "amber", 8.0, ["gafas"]),
    (19, "Lucía", "Llevo una camiseta.", "저는 티셔츠를 입고 있어요.", "repite", 3, "amber", 8.0, ["camiseta"]),
    (20, "Jin", "¿Y si llueve?", "비가 오면요?", "si llueve", 4, "blue", 8.0, ["paraguas"]),
    (21, "Diego", "Llevo un paraguas pequeño.", "저는 작은 우산을 가지고 있어요.", "un paraguas", 4, "blue", 9.0, ["paraguas"]),
    (22, "Diego", "Llevo puede ser ropa o un paraguas.", "llevo는 옷이나 우산에 쓸 수 있어요.", "llevar", 4, "blue", 10.0, ["chaqueta", "paraguas"]),
    (23, "Lucía", "Jin, ¿qué llevas hoy?", "Jin, 오늘 뭐 입었어요?", "pregunta", 4, "blue", 8.5, ["chaqueta", "zapatos"]),
    (24, "Jin", "Llevo una chaqueta y zapatos cómodos.", "저는 재킷을 입고 편한 신발을 신었어요.", "respuesta", 4, "blue", 10.0, ["chaqueta", "zapatos"]),
    (25, "Lucía", "Yo llevo gafas de sol.", "저는 선글라스를 써요.", "yo llevo", 4, "blue", 8.0, ["gafas"]),
    (26, "Diego", "Yo llevo un paraguas.", "저는 우산을 가지고 있어요.", "yo llevo", 4, "blue", 8.0, ["paraguas"]),
    (27, "Diego", "Mini prueba: llevo una chaqueta.", "미니 퀴즈: 저는 재킷을 입고 있어요.", "quiz", 4, "blue", 9.0, ["chaqueta"]),
    (28, "Diego", "Pregunta: ¿qué llevas?", "질문: 뭐 입었어요?", "quiz", 4, "blue", 8.5, ["chaqueta"]),
    (29, "Jin", "Respuesta: llevo una chaqueta.", "대답: 저는 재킷을 입고 있어요.", "respuesta", 4, "blue", 8.5, ["chaqueta"]),
    (30, "Diego", "Excelente. Ya puedes hablar de tu ropa.", "훌륭해요. 이제 옷차림을 말할 수 있어요.", "cierre", 4, "blue", 9.5, ["chaqueta", "gafas"]),
]

DESIGN = {
    "output_size": (1280, 720),
    "font_path": "assets/fonts/NotoSansKR-Bold.ttf",
    "font_index": 0,
    "font_path_ko": "assets/fonts/NotoSansKR-Regular.ttf",
    "font_index_ko": 0,
    "font_size_title": 66,
    "font_size_es": 62,
    "min_font_size_es": 36,
    "font_size_ko": 32,
    "font_size_example": 30,
    "background_color": (248, 247, 242),
    "text_color": (31, 35, 40),
    "muted_text_color": (96, 101, 109),
    "intro_title": "¿Qué llevas?",
    "intro_subtitle": "Español A1 · Ep.17",
    "intro_ko": "오늘 뭐 입어요?",
    "intro_scene_image_path": "images/ep17-que-llevas-source.png",
    "intro_scene_fit": "contain",
    "thumbnail_title": "¿Qué llevas?",
    "thumbnail_subtitle": "Español A1 · Ep.17",
    "thumbnail_ko": "오늘 뭐 입어요?",
    "outro_ko": "이제 스페인어로 옷차림을 말할 수 있어요",
    "outro_font_size_es": 28,
    "outro_text_width_ratio": 0.76,
    "outro_max_lines": 5,
    "outro_text_y": 388,
    "outro_ko_y": 630,
    "character_images": CHARACTERS,
    "show_character_portraits": True,
    "clothing_images": CLOTHING_IMAGES,
    "color_blocks": {
        "coral": (224, 91, 76),
        "amber": (230, 158, 62),
        "teal": (44, 150, 142),
        "blue": (70, 120, 196),
        "green": (92, 148, 86),
        "violet": (138, 104, 190),
        "neutral": (42, 48, 57),
    },
}


def _build_segments() -> list[dict]:
    segments: list[dict] = [
        {
            "type": "intro",
            "text_es": "Después del tiempo, Jin aprende a hablar de la ropa: ¿qué llevas?",
            "duration_s": 14.0,
            "color_block": "neutral",
            "characters": ["Jin", "Lucía", "Diego"],
            "clothing_items": ["chaqueta", "gafas", "paraguas"],
        }
    ]
    for block in BLOCKS:
        segments.append(
            {
                "type": "block_header",
                "block_id": block["block_id"],
                "title_es": block["title_es"],
                "title_ko": block["title_ko"],
                "color_block": block["color_block"],
                "duration_s": 3.5,
                "clothing_items": block.get("clothing_items", []),
            }
        )
        for line_num, speaker, text_es, text_ko, focus, block_id, color_block, duration_s, clothing_items in DIALOGUE:
            if block_id != block["block_id"]:
                continue
            segments.append(
                {
                    "type": "dialogue",
                    "line_num": line_num,
                    "speaker": speaker,
                    "text_es": text_es,
                    "text_ko": text_ko,
                    "focus": focus,
                    "block_id": block_id,
                    "color_block": color_block,
                    "duration_s": duration_s,
                    "character": speaker,
                    "clothing_items": clothing_items,
                }
            )
    segments.append(
        {
            "type": "outro",
            "text_es": (
                "Muy bien. Ahora puedes preguntar: ¿qué llevas? "
                "Y puedes responder: llevo una chaqueta, llevo un abrigo o llevo gafas de sol."
            ),
            "duration_s": 24.0,
            "color_block": "neutral",
            "characters": ["Jin", "Lucía", "Diego"],
            "clothing_items": ["chaqueta", "abrigo", "gafas"],
        }
    )
    return segments


SEGMENTS = _build_segments()
CHAPTERS = [
    {"segment": 1, "title": "Introducción"},
    {"segment": 2, "title": "¿Qué llevas?"},
    {"segment": 9, "title": "Hace frío"},
    {"segment": 16, "title": "Hace sol"},
    {"segment": 24, "title": "Mini prueba"},
]
AUDIO = {
    "tts_engine": "edge",
    "edge_voice": "es-ES-ElviraNeural",
    "edge_rate": "-8%",
    "edge_pitch": "+0Hz",
    "edge_volume": "+0%",
    "voice": "es-ES-ElviraNeural",
    "character_voices": CHARACTER_VOICES,
    "rate_wpm": 142,
    "lead_padding_s": 0.2,
    "tail_padding_s": 0.35,
    "min_duration_s": 3.0,
    "readability_floor_ratio": 0.0,
    "bgm_path": "assets/audio/spanish-lab-brand-bgm.mp3",
    "bgm_volume_db": -4.0,
    "narration_volume_db": 0.0,
    "ducking": True,
    "ducking_threshold": 0.04,
    "ducking_ratio": 6,
    "ducking_attack_ms": 80,
    "ducking_release_ms": 450,
    "fade_in_s": 0.0,
    "fade_out_s": 2.0,
    "audio_codec": "aac",
    "audio_bitrate_kbps": 192,
    "sample_rate_hz": 44100,
}
