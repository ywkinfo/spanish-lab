"""A1+ story-card episode: Jin expresses small opinions with gustar."""

from __future__ import annotations

IMAGE_PATH = "images/ep18-me-gusta-pero-source.png"
DESCRIP_PATH = "a1-me-gusta-pero/descrip.md"
OUTPUT_NAME = "me-gusta-pero"
PUBLIC_SLUG = "a1-me-gusta-pero"
YOUTUBE_URL = ""
SERIES = "frases-a1"
SERIES_TITLE = "Español A1 -- Frases útiles"
EPISODE = 18
LEVEL = "A1+"
LANGUAGE = "es"
RENDER_VERSION = 1
RENDER_TYPE = "cards"
THUMBNAIL_PATH = "thumbs/a1-ep18-me-gusta-pero.jpg"
YOUTUBE_TITLE = "Me gusta, pero… 👍 좋아요, 그런데… | Español A1+ · Ep.18"
DESCRIPTION_INTRO = (
    "Jin sigue en Madrid con Lucía y Diego. Después de hablar de la ropa, aprende a dar "
    "una opinión un poco más completa: me gusta, pero... Practicamos me gusta la chaqueta, "
    "me gusta Madrid y me gusta, pero hace calor."
)
DESCRIPTION_OUTRO = (
    "Escucha primero, repite en voz alta y después di tu propia opinión: me gusta la chaqueta, "
    "me gusta Madrid, o me gusta, pero hace calor."
)
KOREAN_TEASER = (
    "한국어 티저: EP.18에서는 gustar를 조금 더 높은 난이도로 연습합니다. 핵심 표현은 하나, "
    "Me gusta + 명사, pero... 입니다. 좋아요에서 끝나지 않고 '좋아요, 그런데...'까지 말해 보세요."
)
BASE_TAGS = ["스페인어", "스페인어 입문", "스페인어 A1", "Spanish A1", "aprender español", "español para principiantes"]
EXTRA_TAGS = ["Me gusta", "gustar en español", "me gusta pero", "Spanish opinions", "스페인어 gustar", "스페인어 회화"]
BASE_HASHTAGS = ["#EspañolA1", "#aprenderespañol", "#스페인어"]
EXTRA_HASHTAGS = ["#SpanishA1", "#Madrid", "#Gustar"]

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
    {"block_id": 1, "title_es": "¿Te gusta?", "title_ko": "마음에 들어요?", "color_block": "coral", "start": 1},
    {"block_id": 2, "title_es": "Me gusta, pero...", "title_ko": "좋아요, 그런데...", "color_block": "teal", "start": 8},
    {"block_id": 3, "title_es": "Me gusta Madrid", "title_ko": "마드리드가 좋아요", "color_block": "amber", "start": 16},
    {"block_id": 4, "title_es": "Mini prueba", "title_ko": "미니 퀴즈", "color_block": "blue", "start": 24},
]

# line_num, speaker, Spanish, Korean, focus, block_id, color, duration_s
DIALOGUE = [
    (1, "Diego", "Hoy hablamos de gustos y opiniones pequeñas.", "오늘은 좋아하는 것과 작은 의견을 말해요.", "gustos", 1, "coral", 9.0),
    (2, "Lucía", "Jin lleva una chaqueta nueva.", "Jin은 새 재킷을 입고 있어요.", "contexto", 1, "coral", 8.0),
    (3, "Lucía", "Jin, ¿te gusta la chaqueta?", "Jin, 그 재킷 마음에 들어요?", "¿te gusta?", 1, "coral", 8.5),
    (4, "Jin", "Sí, me gusta.", "네, 마음에 들어요.", "me gusta", 1, "coral", 7.0),
    (5, "Diego", "Repite: me gusta.", "따라 해요: 마음에 들어요.", "shadowing", 1, "coral", 7.5),
    (6, "Jin", "Me gusta.", "마음에 들어요.", "repite", 1, "coral", 6.5),
    (7, "Diego", "Muy bien. Me gusta es una opinión simple.", "좋아요. Me gusta는 간단한 의견이에요.", "opinión", 1, "coral", 9.5),
    (8, "Lucía", "Pero hoy hace calor.", "그런데 오늘은 더워요.", "pero", 2, "teal", 7.5),
    (9, "Jin", "Sí, me gusta, pero hace calor.", "네, 마음에 들어요. 그런데 더워요.", "me gusta, pero", 2, "teal", 9.0),
    (10, "Diego", "Perfecto: me gusta, pero...", "완벽해요: 좋아요, 그런데...", "patrón", 2, "teal", 8.0),
    (11, "Jin", "Me gusta la chaqueta, pero hace calor.", "재킷은 마음에 들어요. 그런데 더워요.", "chaqueta", 2, "teal", 9.5),
    (12, "Lucía", "La chaqueta es bonita.", "재킷은 예뻐요.", "bonita", 2, "teal", 7.5),
    (13, "Jin", "Sí. Me gusta, pero no hoy.", "네. 마음에 들어요. 그런데 오늘은 아니에요.", "no hoy", 2, "teal", 8.5),
    (14, "Diego", "Repite despacio: me gusta, pero hace calor.", "천천히 따라 해요: 좋아요, 그런데 더워요.", "shadowing", 2, "teal", 10.0),
    (15, "Jin", "Me gusta, pero hace calor.", "마음에 들어요. 그런데 더워요.", "repite", 2, "teal", 8.0),
    (16, "Diego", "Ahora mira Madrid.", "이제 마드리드를 봐요.", "Madrid", 3, "amber", 7.0),
    (17, "Jin", "Me gusta Madrid.", "저는 마드리드가 좋아요.", "Madrid", 3, "amber", 7.0),
    (18, "Lucía", "A mí también. Me gusta Madrid.", "저도요. 저는 마드리드가 좋아요.", "a mí también", 3, "amber", 8.5),
    (19, "Diego", "Pero hay mucha gente.", "그런데 사람이 많아요.", "mucha gente", 3, "amber", 7.5),
    (20, "Jin", "Me gusta Madrid, pero hay mucha gente.", "저는 마드리드가 좋아요. 그런데 사람이 많아요.", "frase completa", 3, "amber", 9.5),
    (21, "Diego", "Es una frase más completa.", "조금 더 완성된 문장이에요.", "completa", 3, "amber", 8.0),
    (22, "Lucía", "Me gusta este parque.", "저는 이 공원이 좋아요.", "parque", 3, "amber", 7.0),
    (23, "Jin", "Me gusta este parque, pero hace calor.", "저는 이 공원이 좋아요. 그런데 더워요.", "parque + pero", 3, "amber", 9.5),
    (24, "Diego", "Mini prueba: ¿qué significa me gusta?", "미니 퀴즈: me gusta는 무슨 뜻일까요?", "quiz", 4, "blue", 9.0),
    (25, "Lucía", "Significa: me gusta, me agrada.", "뜻은 좋아요, 마음에 들어요예요.", "significado", 4, "blue", 8.5),
    (26, "Diego", "Pregunta: ¿te gusta la chaqueta?", "질문: 그 재킷 마음에 들어요?", "pregunta", 4, "blue", 8.5),
    (27, "Jin", "Respuesta: sí, me gusta, pero hace calor.", "대답: 네, 마음에 들어요. 그런데 더워요.", "respuesta", 4, "blue", 9.5),
    (28, "Diego", "Otra frase: me gusta Madrid, pero hay mucha gente.", "다른 문장: 마드리드가 좋아요. 그런데 사람이 많아요.", "otra frase", 4, "blue", 10.0),
    (29, "Jin", "Me gusta Madrid, pero hay mucha gente.", "저는 마드리드가 좋아요. 그런데 사람이 많아요.", "repite", 4, "blue", 9.0),
    (30, "Diego", "Excelente. Ya puedes decir una opinión pequeña.", "훌륭해요. 이제 작은 의견을 말할 수 있어요.", "cierre", 4, "blue", 9.5),
]

DESIGN = {
    "output_size": (1280, 720),
    "font_path": "assets/fonts/NotoSansKR-Bold.ttf",
    "font_index": 0,
    "font_path_ko": "assets/fonts/NotoSansKR-Regular.ttf",
    "font_index_ko": 0,
    "font_size_title": 66,
    "font_size_es": 62,
    "min_font_size_es": 34,
    "font_size_ko": 32,
    "font_size_example": 30,
    "background_color": (248, 247, 242),
    "text_color": (31, 35, 40),
    "muted_text_color": (96, 101, 109),
    "intro_title": "Me gusta, pero...",
    "intro_subtitle": "Español A1+ · Ep.18",
    "intro_ko": "좋아요, 그런데...",
    "intro_scene_image_path": "images/ep18-me-gusta-pero-source.png",
    "intro_scene_fit": "contain",
    "thumbnail_title": "Me gusta, pero...",
    "thumbnail_subtitle": "Español A1+ · Ep.18",
    "thumbnail_ko": "좋아요, 그런데...",
    "outro_ko": "이제 스페인어로 작은 의견을 말할 수 있어요",
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
            "text_es": "Hoy Jin aprende a decir una opinión pequeña: me gusta, pero...",
            "duration_s": 14.0,
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
                "Muy bien. Ahora puedes decir: me gusta la chaqueta, "
                "me gusta Madrid, o me gusta, pero hace calor."
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
    {"segment": 2, "title": "¿Te gusta?"},
    {"segment": 10, "title": "Me gusta, pero..."},
    {"segment": 19, "title": "Me gusta Madrid"},
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
