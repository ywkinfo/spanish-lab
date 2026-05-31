
"""A1+ story-card episode: Jin says where he is using estar en + place."""

from __future__ import annotations

IMAGE_PATH = "images/ep26-estoy-en-la-estacion-source.png"
DESCRIP_PATH = "a1-estoy-en-la-estacion/descrip.md"
OUTPUT_NAME = "estoy-en-la-estacion"
PUBLIC_SLUG = "a1-estoy-en-la-estacion"
YOUTUBE_URL = ""
SERIES = "frases-a1"
SERIES_TITLE = "Español A1 -- Frases útiles"
EPISODE = 26
LEVEL = "A1+"
LANGUAGE = "es"
RENDER_VERSION = 2
RENDER_TYPE = "cards"
THUMBNAIL_PATH = "thumbs/a1-ep26-estoy-en-la-estacion.jpg"
YOUTUBE_TITLE = "Estoy en la estación 🚉 나 역에 있어요 | Español A1+ · Ep.26"
DESCRIPTION_INTRO = (
    "Jin practica una frase muy útil para viajar: estoy en la estación. "
    "En este episodio aprendemos a usar estar en + lugar para decir dónde estamos."
)
DESCRIPTION_OUTRO = (
    "Escucha, repite en voz alta y cambia solo el lugar: estoy en la estación, "
    "estoy en el hotel, estoy en el café."
)
KOREAN_TEASER = (
    "한국어 티저: EP.26은 A1+ 위치 표현입니다. "
    "핵심은 하나, estar en + 장소입니다. "
    "Estoy en la estación처럼 여행 중 내 위치를 짧고 자연스럽게 말해 보세요."
)
BASE_TAGS = ["스페인어", "스페인어 입문", "스페인어 A1", "Spanish A1", "aprender español", "español para coreanos"]
EXTRA_TAGS = ["estoy en", "estar en", "la estación", "Spanish travel", "스페인어 회화", "스페인어 위치 표현", "여행 스페인어"]
BASE_HASHTAGS = ["#EspañolA1", "#aprenderespañol", "#스페인어"]
EXTRA_HASHTAGS = ["#SpanishA1", "#EstoyEnLaEstacion", "#SpanishLab"]

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
    {"block_id": 1, "title_es": "¿Dónde estás?", "title_ko": "너 어디야?", "color_block": "coral", "start": 1},
    {"block_id": 2, "title_es": "Estoy en la estación", "title_ko": "나는 역에 있어요", "color_block": "teal", "start": 8},
    {"block_id": 3, "title_es": "Cambia el lugar", "title_ko": "장소만 바꾸기", "color_block": "amber", "start": 17},
    {"block_id": 4, "title_es": "Mini prueba", "title_ko": "미니 퀴즈", "color_block": "blue", "start": 25},
]

# line_num, speaker, Spanish, Korean, focus, block_id, color, duration_s
DIALOGUE = [
    (1, 'Diego', 'Hoy volvemos a una situación de viaje.', '오늘은 여행 상황으로 돌아가요.', 'viaje', 1, 'coral', 8.0),
    (2, 'Lucía', 'Jin llega a la estación y manda un mensaje.', 'Jin은 역에 도착해서 메시지를 보내요.', 'contexto', 1, 'coral', 8.5),
    (3, 'Diego', 'La pregunta es muy simple: ¿dónde estás?', '질문은 아주 간단해요: 너 어디에 있어?', 'pregunta', 1, 'coral', 8.5),
    (4, 'Lucía', 'Escucha: ¿dónde estás?', '들어 보세요: ¿dónde estás?', 'modelo', 1, 'coral', 7.0),
    (5, 'Jin', '¿Dónde estás?', '너 어디에 있어?', 'repetición', 1, 'coral', 6.5),
    (6, 'Diego', 'Ahora necesitamos responder con estar.', '이제 estar로 대답해야 해요.', 'estar', 1, 'coral', 8.0),
    (7, 'Lucía', 'La frase clave es: estoy en la estación.', '핵심 표현은 estoy en la estación이에요.', 'clave', 1, 'coral', 9.0),
    (8, 'Diego', 'Primero: estoy.', '먼저 estoy예요.', 'estoy', 2, 'teal', 6.5),
    (9, 'Jin', 'Estoy.', '저는 있어요.', 'repetición', 2, 'teal', 6.0),
    (10, 'Lucía', 'Estoy viene de estar, para decir ubicación.', 'estoy는 위치를 말할 때 쓰는 estar에서 와요.', 'ubicación', 2, 'teal', 8.5),
    (11, 'Diego', 'Después añadimos en, como “at” o “in”.', '그다음 en을 붙여요. “~에”라는 느낌이에요.', 'en', 2, 'teal', 8.0),
    (12, 'Jin', 'Estoy en.', '저는 ~에 있어요.', 'modelo', 2, 'teal', 6.5),
    (13, 'Lucía', 'Ahora el lugar: la estación.', '이제 장소예요: la estación, 역.', 'lugar', 2, 'teal', 7.5),
    (14, 'Jin', 'Estoy en la estación.', '저는 역에 있어요.', 'frase completa', 2, 'teal', 8.0),
    (15, 'Diego', 'Literalmente: estoy en la estación.', '직역하면: 나는 역에 있다.', 'literal', 2, 'teal', 8.0),
    (16, 'Lucía', 'Naturalmente, suena como una ubicación simple.', '자연스럽게는 “나 역에 있어요”예요.', 'natural', 2, 'teal', 8.0),
    (17, 'Diego', 'Cambiamos solo el lugar.', '장소만 바꿔 볼게요.', 'cambiar', 3, 'amber', 7.0),
    (18, 'Lucía', 'Estoy en el hotel.', '저는 호텔에 있어요.', 'hotel', 3, 'amber', 7.0),
    (19, 'Jin', 'Estoy en el hotel.', '저는 호텔에 있어요.', 'repetición', 3, 'amber', 7.0),
    (20, 'Diego', 'Otra opción: estoy en el café.', '다른 표현: 저는 카페에 있어요.', 'café', 3, 'amber', 7.5),
    (21, 'Jin', 'Estoy en el café.', '저는 카페에 있어요.', 'repetición', 3, 'amber', 7.0),
    (22, 'Lucía', 'Si estás aquí, dices: estoy aquí.', '여기에 있으면 estoy aquí라고 말해요.', 'aquí', 3, 'amber', 8.0),
    (23, 'Jin', 'Estoy aquí.', '저 여기 있어요.', 'aquí', 3, 'amber', 6.5),
    (24, 'Diego', 'Muy bien. Usamos estar para ubicación.', '좋아요. 위치에는 estar를 써요.', 'resumen', 3, 'amber', 8.0),
    (25, 'Diego', 'Mini prueba: ¿cómo dices “너 어디야?”', '미니 퀴즈: “너 어디야?”를 어떻게 말할까요?', 'quiz', 4, 'blue', 8.5),
    (26, 'Jin', '¿Dónde estás?', '너 어디에 있어?', 'respuesta', 4, 'blue', 7.0),
    (27, 'Lucía', 'Ahora responde en español.', '이제 대답해 보세요: “나는 역에 있어요.”', 'quiz', 4, 'blue', 7.5),
    (28, 'Jin', 'Estoy en la estación.', '저는 역에 있어요.', 'respuesta', 4, 'blue', 8.0),
    (29, 'Diego', 'Recuerda: no decimos soy en la estación.', '기억하세요: soy en la estación이라고 하지 않아요.', 'error común', 4, 'blue', 8.5),
    (30, 'Lucía', 'Decimos: estoy en la estación.', '이렇게 말해요: estoy en la estación.', 'cierre', 4, 'blue', 8.0),

]

DESIGN = {
    "output_size": (1280, 720),
    "font_path": "assets/fonts/NotoSansKR-Bold.ttf",
    "font_index": 0,
    "font_path_ko": "assets/fonts/NotoSansKR-Regular.ttf",
    "font_index_ko": 0,
    "font_size_title": 58,
    "font_size_es": 60,
    "min_font_size_es": 30,
    "font_size_ko": 32,
    "font_size_example": 30,
    "background_color": (248, 247, 242),
    "text_color": (31, 35, 40),
    "muted_text_color": (96, 101, 109),
    "intro_title": "Estoy en la estación",
    "intro_subtitle": "Español A1+ · Ep.26",
    "intro_ko": "나 역에 있어요",
    "intro_scene_image_path": "images/ep26-estoy-en-la-estacion-source.png",
    "intro_scene_fit": "cover",
    "thumbnail_title": "Estoy en la estación",
    "thumbnail_subtitle": "Español A1+ · Ep.26",
    "thumbnail_ko": "나 역에 있어요",
    "outro_ko": "이제 스페인어로 내 위치를 짧게 말할 수 있어요",
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
            "text_es": "Hoy Jin aprende a decir dónde está: estoy en la estación.",
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
                "Muy bien. Ahora puedes decir dónde estás: estoy en la estación, "
                "estoy en el hotel, estoy en el café."
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
    {"segment": 2, "title": "¿Dónde estás?"},
    {"segment": 10, "title": "Estoy en la estación"},
    {"segment": 20, "title": "Cambia el lugar"},
    {"segment": 29, "title": "Mini prueba"},
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
