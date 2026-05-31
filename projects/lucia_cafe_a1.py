"""A1 image-description story episode: Lucía is drinking coffee in a café."""

from __future__ import annotations

IMAGE_PATH = "assets/generated/lucia-cafe-table.png"
DESCRIP_PATH = "a1-lucia-cafe/descrip.md"
OUTPUT_NAME = "lucia-cafe"
PUBLIC_SLUG = "a1-lucia-cafe"
YOUTUBE_URL = ""
SERIES = "frases-a1"
SERIES_TITLE = "Español A1 -- Frases útiles"
EPISODE = 7
LEVEL = "A1"
LANGUAGE = "es"
RENDER_VERSION = 1
RENDER_TYPE = "cards"
THUMBNAIL_PATH = "thumbs/a1-lucia-cafe.jpg"
YOUTUBE_TITLE = "Lucía está tomando café ☕ 그림 묘사하기 | Español A1 · Ep.7"
DESCRIPTION_INTRO = (
    "Mira una imagen de Lucía en una cafetería y practica cómo describirla en español A1. "
    "Peter, Lucía y Diego convierten una escena simple en una conversación guiada con veo, hay, está y quiero."
)
DESCRIPTION_OUTRO = (
    "Escucha primero, repite en voz alta y al final describe la imagen tú. "
    "Este episodio conecta Ep.6 ¿Cuánto cuesta? con Ep.8 La cuenta, por favor."
)
KOREAN_TEASER = (
    "한국어 티저: EP.7은 루시아가 카페에서 커피를 마시는 이미지를 보고 스페인어로 장면을 묘사하는 연습입니다. "
    "Peter, Lucía, Diego의 3인 상황극으로 veo, hay, está tomando café, quiero una tapa를 반복합니다."
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
    "describir imagen español",
    "estar gerundio español",
    "cafeteria español",
    "tomar cafe español",
    "hay una tapa",
    "conversacion español A1",
    "스페인어 그림 묘사",
    "스페인어 카페 표현",
]
BASE_HASHTAGS = ["#EspañolA1", "#aprenderespañol", "#스페인어"]
EXTRA_HASHTAGS = ["#SpanishA1", "#frasesenespañol", "#Cafetería"]

CHARACTERS = {
    "Peter": "assets/characters/peter-profile.png",
    "Lucía": "assets/generated/lucia-cafe-table.png",
    "Diego": "assets/characters/diego-profile.png",
}
CHARACTER_VOICES = {
    "Lucía": "es-ES-ElviraNeural",
    "Peter": "es-ES-AlvaroNeural",
    "Diego": "es-MX-JorgeNeural",
}

BLOCKS = [
    {"block_id": 1, "title_es": "Mira la imagen", "title_ko": "그림을 천천히 보기", "color_block": "coral", "start": 1},
    {"block_id": 2, "title_es": "¿Qué hay en la mesa?", "title_ko": "테이블 위 묘사하기", "color_block": "amber", "start": 8},
    {"block_id": 3, "title_es": "Lucía está tomando café", "title_ko": "지금 하는 일 말하기", "color_block": "teal", "start": 16},
    {"block_id": 4, "title_es": "Ahora habla tú", "title_ko": "직접 따라 말하기", "color_block": "blue", "start": 23},
]

# line_num, speaker, Spanish, Korean, focus, block_id, color, duration_s
DIALOGUE = [
    (1, "Diego", "Mira la imagen, Peter.", "Peter, 그림을 봐.", "Mira la imagen", 1, "coral", 8.0),
    (2, "Peter", "Veo a Lucía.", "루시아가 보여.", "Veo a Lucía", 1, "coral", 8.0),
    (3, "Diego", "Muy bien. ¿Dónde está Lucía?", "좋아. 루시아는 어디에 있어?", "¿Dónde está?", 1, "coral", 8.5),
    (4, "Peter", "Lucía está en una cafetería.", "루시아는 카페에 있어.", "está en...", 1, "coral", 9.0),
    (5, "Lucía", "Sí, estoy en una cafetería.", "맞아, 나는 카페에 있어.", "estoy en...", 1, "coral", 8.5),
    (6, "Diego", "La cafetería tiene luz de la mañana.", "카페에는 아침 햇살이 있어.", "luz de la mañana", 1, "coral", 9.0),
    (7, "Peter", "La imagen es tranquila y clara.", "그림은 차분하고 선명해.", "tranquila y clara", 1, "coral", 8.5),
    (8, "Diego", "Ahora mira la mesa.", "이제 테이블을 봐.", "mira la mesa", 2, "amber", 8.0),
    (9, "Peter", "Hay una taza de café.", "커피잔이 있어.", "Hay una taza", 2, "amber", 8.5),
    (10, "Lucía", "También hay una tapa pequeña.", "작은 타파스도 있어.", "También hay...", 2, "amber", 8.5),
    (11, "Peter", "Hay un plato en la mesa.", "테이블 위에 접시가 있어.", "un plato", 2, "amber", 8.5),
    (12, "Diego", "Exacto. Café, tapa y plato.", "맞아. 커피, 타파스, 접시.", "vocabulario", 2, "amber", 8.5),
    (13, "Peter", "La mesa es pequeña.", "테이블은 작아.", "La mesa es...", 2, "amber", 8.0),
    (14, "Lucía", "Pero la mesa es perfecta para mí.", "하지만 나에게 딱 좋은 테이블이야.", "perfecta para mí", 2, "amber", 9.0),
    (15, "Diego", "Muy bien. Ahora usamos: hay.", "좋아. 이제 hay를 써 보자.", "hay", 2, "amber", 8.5),
    (16, "Diego", "Lucía, ¿qué estás haciendo?", "Lucía, 뭐 하고 있어?", "¿Qué estás haciendo?", 3, "teal", 9.0),
    (17, "Lucía", "Estoy tomando café.", "나는 커피를 마시고 있어.", "estoy tomando", 3, "teal", 8.5),
    (18, "Peter", "Ella está tomando café.", "그녀는 커피를 마시고 있어.", "está tomando", 3, "teal", 8.5),
    (19, "Diego", "Muy bien. Repite despacio.", "좋아. 천천히 반복해.", "Repite despacio", 3, "teal", 8.0),
    (20, "Peter", "Lucía está tomando café.", "루시아는 커피를 마시고 있어.", "está tomando café", 3, "teal", 9.0),
    (21, "Lucía", "Y estoy comiendo una tapa.", "그리고 나는 타파스를 먹고 있어.", "estoy comiendo", 3, "teal", 8.5),
    (22, "Peter", "Lucía está comiendo una tapa.", "루시아는 타파스를 먹고 있어.", "está comiendo", 3, "teal", 9.0),
    (23, "Diego", "Perfecto. Ahora hacemos un mini diálogo.", "완벽해. 이제 짧은 대화를 해 보자.", "mini diálogo", 4, "blue", 9.0),
    (24, "Peter", "Lucía, ¿quieres más café?", "Lucía, 커피 더 원해?", "¿quieres más...?", 4, "blue", 8.5),
    (25, "Lucía", "Sí, quiero un poco más, por favor.", "응, 조금 더 원해, 부탁해.", "un poco más", 4, "blue", 9.0),
    (26, "Peter", "¿Y quieres otra tapa?", "그리고 타파스 하나 더 원해?", "otra tapa", 4, "blue", 8.5),
    (27, "Lucía", "No, gracias. Estoy bien.", "아니, 고마워. 괜찮아.", "No, gracias", 4, "blue", 8.5),
    (28, "Diego", "Peter, describe la imagen completa.", "Peter, 전체 그림을 묘사해 봐.", "imagen completa", 4, "blue", 9.0),
    (29, "Peter", "Lucía está en una cafetería.", "루시아는 카페에 있어.", "frase 1", 4, "blue", 8.5),
    (30, "Peter", "Está tomando café y hay una tapa en la mesa.", "커피를 마시고 있고 테이블 위에 타파스가 있어.", "frase completa", 4, "blue", 9.5),
]

DESIGN = {
    "output_size": (1280, 720),
    "font_path": "assets/fonts/NotoSansKR-Bold.ttf",
    "font_index": 0,
    "font_path_ko": "assets/fonts/NotoSansKR-Regular.ttf",
    "font_index_ko": 0,
    "font_size_title": 70,
    "font_size_es": 68,
    "min_font_size_es": 40,
    "font_size_ko": 32,
    "font_size_example": 30,
    "background_color": (248, 247, 242),
    "text_color": (31, 35, 40),
    "muted_text_color": (96, 101, 109),
    "intro_title": "Mira la imagen",
    "intro_subtitle": "Español A1 · Ep.7",
    "intro_ko": "그림을 보고 스페인어로 장면 묘사하기",
    "intro_scene_image_path": "assets/generated/lucia-cafe-table.png",
    "thumbnail_title": "Lucía está tomando café",
    "thumbnail_subtitle": "Español A1 · Ep.7",
    "thumbnail_ko": "그림 묘사하기: 카페 장면",
    "outro_ko": "이제 그림을 보고 직접 말해 보세요",
    "character_images": CHARACTERS,
    "show_character_portraits": True,
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
            "text_es": (
                "Hoy miramos una imagen de Lucía en una cafetería. "
                "Primero observamos, después describimos y al final hablamos como en una escena real."
            ),
            "duration_s": 12.0,
            "color_block": "neutral",
            "characters": ["Peter", "Lucía", "Diego"],
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
                "duration_s": 3.0,
            }
        )
        for line_num, speaker, text_es, text_ko, focus, block_id, color_block, duration_s in DIALOGUE:
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
                }
            )
    segments.append(
        {
            "type": "outro",
            "text_es": (
                "Muy bien. Ahora describe la imagen tú: Lucía está en una cafetería, "
                "está tomando café y hay una tapa en la mesa. En el próximo episodio pedimos la cuenta."
            ),
            "duration_s": 12.0,
            "color_block": "neutral",
            "characters": ["Peter", "Lucía", "Diego"],
        }
    )
    return segments


SEGMENTS = _build_segments()
CHAPTERS = [
    {"segment": 1, "title": "Introducción"},
    {"segment": 2, "title": "Mira la imagen"},
    {"segment": 10, "title": "¿Qué hay en la mesa?"},
    {"segment": 19, "title": "Está tomando café"},
    {"segment": 27, "title": "Ahora habla tú"},
    {"segment": len(SEGMENTS), "title": "Repaso final"},
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
