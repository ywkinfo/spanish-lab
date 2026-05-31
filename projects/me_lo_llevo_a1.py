
"""A1+ story-card episode: Jin chooses a souvenir using Me lo llevo."""

from __future__ import annotations

IMAGE_PATH = "images/ep29-me-lo-llevo-source.png"
DESCRIP_PATH = "a1-me-lo-llevo/descrip.md"
OUTPUT_NAME = "me-lo-llevo"
PUBLIC_SLUG = "a1-me-lo-llevo"
YOUTUBE_URL = ""
SERIES = "frases-a1"
SERIES_TITLE = "Español A1 -- Frases útiles"
EPISODE = 29
LEVEL = "A1+"
LANGUAGE = "es"
RENDER_VERSION = 1
RENDER_TYPE = "cards"
THUMBNAIL_PATH = "thumbs/a1-ep29-me-lo-llevo.jpg"
YOUTUBE_TITLE = "Me lo llevo 🛍️ 이걸로 할게요 | Español A1+ · Ep.29"
DESCRIPTION_INTRO = (
    "Jin está en una tienda de recuerdos y aprende una frase muy útil para decidir: "
    "me lo llevo."
)
DESCRIPTION_OUTRO = (
    "Escucha, repite en voz alta y usa la frase como una unidad: "
    "me lo llevo, sí, me lo llevo, me lo llevo, por favor."
)
KOREAN_TEASER = (
    "한국어 티저: EP.29는 여행 쇼핑에서 바로 쓰는 A1+ 표현입니다. "
    "핵심은 하나, Me lo llevo입니다. "
    "기념품 가게에서 '이걸로 할게요 / 이거 살게요'를 자연스럽게 말해 보세요."
)
BASE_TAGS = ["스페인어", "스페인어 입문", "스페인어 A1", "Spanish A1", "aprender español", "español para coreanos"]
EXTRA_TAGS = ["Me lo llevo", "스페인어 쇼핑", "스페인어 여행", "Spanish shopping", "souvenir Spanish", "스페인어 회화"]
BASE_HASHTAGS = ["#EspañolA1", "#aprenderespañol", "#스페인어"]
EXTRA_HASHTAGS = ["#SpanishA1", "#MeLoLlevo", "#SpanishLab"]

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

BLOCKS = [
    {"block_id": 1, "title_es": "Me lo llevo", "title_ko": "이걸로 할게요", "color_block": "coral", "start": 1},
    {"block_id": 2, "title_es": "Una frase completa", "title_ko": "덩어리로 기억하기", "color_block": "teal", "start": 8},
    {"block_id": 3, "title_es": "En la tienda", "title_ko": "가게에서 말하기", "color_block": "amber", "start": 16},
    {"block_id": 4, "title_es": "Mini prueba", "title_ko": "미니 퀴즈", "color_block": "blue", "start": 24},
]

# line_num, speaker, Spanish, Korean, focus, block_id, color, duration_s
DIALOGUE = [
    (1, "Diego", "Estamos en una tienda de recuerdos.", "우리는 기념품 가게에 있어요.", "contexto", 1, "coral", 7.5),
    (2, "Lucía", "Jin mira un imán pequeño.", "Jin은 작은 자석을 보고 있어요.", "situación", 1, "coral", 7.5),
    (3, "Jin", "Me gusta este imán.", "저는 이 자석이 마음에 들어요.", "objeto", 1, "coral", 7.0),
    (4, "Diego", "Muy bien. Hoy usamos una frase final.", "좋아요. 오늘은 마지막에 결정하는 표현을 써요.", "función", 1, "coral", 8.0),
    (5, "Diego", "La frase es: me lo llevo.", "표현은 me lo llevo예요.", "clave", 1, "coral", 7.5),
    (6, "Jin", "Me lo llevo.", "이걸로 할게요.", "modelo", 1, "coral", 6.5),
    (7, "Lucía", "Suena natural en una tienda.", "가게에서 자연스럽게 들려요.", "natural", 1, "coral", 7.5),
    (8, "Diego", "Primero, escucha la situación.", "먼저 상황을 들어 보세요.", "escucha", 2, "teal", 7.0),
    (9, "Diego", "El objeto es masculino: el imán.", "물건은 남성명사예요: el imán.", "objeto", 2, "teal", 8.0),
    (10, "Diego", "Por eso usamos lo.", "그래서 lo를 써요.", "lo", 2, "teal", 7.0),
    (11, "Lucía", "Pero hoy recuerda la frase completa.", "하지만 오늘은 전체 표현으로 기억하세요.", "frase", 2, "teal", 8.0),
    (12, "Jin", "Me lo llevo.", "이걸로 할게요.", "repetición", 2, "teal", 6.5),
    (13, "Diego", "Literalmente: lo llevo conmigo.", "직역하면 그것을 가지고 가요예요.", "literal", 2, "teal", 8.0),
    (14, "Lucía", "Naturalmente: lo compro.", "자연스럽게는 이거 살게요예요.", "natural", 2, "teal", 7.5),
    (15, "Jin", "Me lo llevo, por favor.", "이걸로 할게요, 부탁해요.", "cortés", 2, "teal", 7.0),
    (16, "Diego", "Ahora hacemos una mini conversación.", "이제 짧은 대화를 해 볼게요.", "diálogo", 3, "amber", 7.5),
    (17, "Lucía", "¿Te gusta este imán?", "이 자석 마음에 들어요?", "pregunta", 3, "amber", 7.0),
    (18, "Jin", "Sí, me gusta.", "네, 마음에 들어요.", "respuesta", 3, "amber", 6.5),
    (19, "Lucía", "¿Lo quieres?", "그거 원해요?", "pregunta", 3, "amber", 6.5),
    (20, "Jin", "Sí, me lo llevo.", "네, 이걸로 할게요.", "respuesta", 3, "amber", 6.8),
    (21, "Diego", "Perfecto. Es corto y muy útil.", "완벽해요. 짧고 아주 유용해요.", "feedback", 3, "amber", 7.5),
    (22, "Diego", "Otra vez, con ritmo.", "다시 한 번, 리듬으로요.", "ritmo", 3, "amber", 6.5),
    (23, "Jin", "Sí, me lo llevo.", "네, 이걸로 할게요.", "shadowing", 3, "amber", 6.8),
    (24, "Diego", "Mini prueba. ¿Cómo dices esta frase?", "미니 퀴즈. 이 표현을 어떻게 말할까요?", "quiz", 4, "blue", 8.0),
    (25, "Jin", "Me lo llevo.", "이걸로 할게요.", "respuesta", 4, "blue", 6.5),
    (26, "Lucía", "Muy bien. Ahora más natural.", "아주 좋아요. 이제 더 자연스럽게요.", "natural", 4, "blue", 7.0),
    (27, "Jin", "Sí, me lo llevo, por favor.", "네, 이걸로 할게요, 부탁해요.", "cortés", 4, "blue", 7.5),
    (28, "Diego", "¿Qué significa en coreano natural?", "자연스러운 한국어 뜻은 무엇일까요?", "quiz", 4, "blue", 8.0),
    (29, "Lucía", "Significa: lo compro.", "이걸로 할게요, 또는 이거 살게요라는 뜻이에요.", "respuesta", 4, "blue", 8.0),
]

DESIGN = {
    "output_size": (1280, 720),
    "font_path": "assets/fonts/NotoSansKR-Bold.ttf",
    "font_index": 0,
    "font_path_ko": "assets/fonts/NotoSansKR-Regular.ttf",
    "font_index_ko": 0,
    "font_size_title": 58,
    "font_size_es": 58,
    "min_font_size_es": 30,
    "font_size_ko": 32,
    "font_size_example": 30,
    "background_color": (248, 247, 242),
    "text_color": (31, 35, 40),
    "muted_text_color": (96, 101, 109),
    "intro_title": "Me lo llevo",
    "intro_subtitle": "Español A1+ · Ep.29",
    "intro_ko": "이걸로 할게요",
    "intro_scene_image_path": "images/ep29-me-lo-llevo-source.png",
    "intro_scene_fit": "contain",
    "thumbnail_title": "Me lo llevo",
    "thumbnail_subtitle": "Español A1+ · Ep.29",
    "thumbnail_ko": "이걸로 할게요",
    "outro_ko": "이제 스페인어로 쇼핑할 때 '이걸로 할게요'를 말할 수 있어요",
    "conversation_label": "Conversación A1+",
    "outro_font_size_es": 28,
    "outro_text_width_ratio": 0.76,
    "outro_max_lines": 5,
    "outro_text_y": 388,
    "outro_ko_y": 630,
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
            "text_es": "Hoy Jin aprende una frase para decidir en una tienda: me lo llevo.",
            "duration_s": 15.0,
            "color_block": "neutral",
            "characters": ["Jin", "Lucía", "Diego"],
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
                    "character": speaker,
                }
            )
    segments.append(
        {
            "type": "outro",
            "text_es": (
                "Muy bien. Ahora puedes decidir en una tienda con una frase corta: "
                "me lo llevo, sí, me lo llevo, me lo llevo, por favor."
            ),
            "duration_s": 24.0,
            "color_block": "neutral",
            "characters": ["Jin", "Lucía", "Diego"],
        }
    )
    return segments


SEGMENTS = _build_segments()
CHAPTERS = [
    {"segment": 1, "title": "Introducción"},
    {"segment": 2, "title": "Me lo llevo"},
    {"segment": 10, "title": "Una frase completa"},
    {"segment": 19, "title": "En la tienda"},
    {"segment": 28, "title": "Mini prueba"},
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
