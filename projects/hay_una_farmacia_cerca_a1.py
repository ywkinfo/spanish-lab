
"""A1+ story-card episode: Jin says what exists nearby using hay + noun."""

from __future__ import annotations

IMAGE_PATH = "images/ep27-hay-una-farmacia-cerca-source.png"
DESCRIP_PATH = "a1-hay-una-farmacia-cerca/descrip.md"
OUTPUT_NAME = "hay-una-farmacia-cerca"
PUBLIC_SLUG = "a1-hay-una-farmacia-cerca"
YOUTUBE_URL = ""
SERIES = "frases-a1"
SERIES_TITLE = "Español A1 -- Frases útiles"
EPISODE = 27
LEVEL = "A1+"
LANGUAGE = "es"
RENDER_VERSION = 1
RENDER_TYPE = "cards"
THUMBNAIL_PATH = "thumbs/a1-ep27-hay-una-farmacia-cerca.jpg"
YOUTUBE_TITLE = "Hay una farmacia cerca 💊 근처에 약국이 있어요 | Español A1+ · Ep.27"
DESCRIPTION_INTRO = (
    "Jin aprende a usar hay + sustantivo para decir que algo existe cerca. "
    "En este episodio practicamos frases de viaje como hay una farmacia cerca."
)
DESCRIPTION_OUTRO = (
    "Escucha, repite en voz alta y cambia solo el lugar: hay una farmacia cerca, "
    "hay un café aquí, hay un baño en la estación."
)
KOREAN_TEASER = (
    "한국어 티저: EP.27은 A1+ 존재 표현입니다. "
    "핵심은 하나, hay + 명사입니다. "
    "Hay una farmacia cerca처럼 여행 중 주변에 무엇이 있는지 짧게 말해 보세요."
)
BASE_TAGS = ["스페인어", "스페인어 입문", "스페인어 A1", "Spanish A1", "aprender español", "español para coreanos"]
EXTRA_TAGS = ["hay", "hay una farmacia", "Spanish travel", "스페인어 회화", "스페인어 여행", "스페인어 존재 표현", "약국 스페인어"]
BASE_HASHTAGS = ["#EspañolA1", "#aprenderespañol", "#스페인어"]
EXTRA_HASHTAGS = ["#SpanishA1", "#HayUnaFarmacia", "#SpanishLab"]

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
    {"block_id": 1, "title_es": "¿Hay una farmacia?", "title_ko": "약국이 있나요?", "color_block": "coral", "start": 1},
    {"block_id": 2, "title_es": "Hay una farmacia cerca", "title_ko": "근처에 약국이 있어요", "color_block": "teal", "start": 8},
    {"block_id": 3, "title_es": "Cambia el lugar", "title_ko": "장소만 바꾸기", "color_block": "amber", "start": 16},
    {"block_id": 4, "title_es": "Mini prueba", "title_ko": "미니 퀴즈", "color_block": "blue", "start": 25},
]

# line_num, speaker, Spanish, Korean, focus, block_id, color, duration_s
DIALOGUE = [(1, 'Diego', 'Hoy seguimos en la ciudad, cerca de la estación.', '오늘은 역 근처 도시에서 이어가요.', 'contexto', 1, 'coral', 8.0), (2, 'Lucía', 'Jin necesita una farmacia, pero no sabe dónde hay una.', 'Jin은 약국이 필요한데 어디에 있는지 몰라요.', 'situación', 1, 'coral', 9.0), (3, 'Diego', 'La frase clave de hoy es muy útil: hay.', '오늘의 핵심 표현은 아주 유용한 hay예요.', 'clave', 1, 'coral', 8.0), (4, 'Lucía', 'Hay significa: existe, o está disponible.', 'hay는 존재한다, 이용할 수 있다는 뜻이에요.', 'hay', 1, 'coral', 8.0), (5, 'Jin', '¿Hay una farmacia cerca?', '근처에 약국이 있나요?', 'pregunta', 1, 'coral', 8.0), (6, 'Lucía', 'Sí, hay una farmacia cerca.', '네, 근처에 약국이 있어요.', 'respuesta', 1, 'coral', 8.0), (7, 'Diego', 'Muy bien. Hoy practicamos hay con nombres útiles.', '좋아요. 오늘은 hay와 유용한 명사만 연습해요.', 'objetivo', 1, 'coral', 8.5), (8, 'Diego', 'Primero, escucha: hay una farmacia.', '먼저 들어 보세요: 약국이 있어요.', 'modelo', 2, 'teal', 8.0), (9, 'Jin', 'Hay una farmacia.', '약국이 있어요.', 'repetición', 2, 'teal', 7.0), (10, 'Lucía', 'Ahora añadimos cerca: hay una farmacia cerca.', '이제 cerca를 붙여요: 근처에 약국이 있어요.', 'cerca', 2, 'teal', 9.0), (11, 'Jin', 'Hay una farmacia cerca.', '근처에 약국이 있어요.', 'frase completa', 2, 'teal', 8.0), (12, 'Diego', 'Literalmente: hay una farmacia cerca.', '직역하면: 근처에 약국 하나가 있다.', 'literal', 2, 'teal', 8.0), (13, 'Lucía', 'Naturalmente, es una frase sencilla para viajar.', '자연스럽게는 “근처에 약국이 있어요”예요.', 'natural', 2, 'teal', 9.0), (14, 'Jin', '¿Hay una farmacia cerca?', '근처에 약국이 있나요?', 'pregunta', 2, 'teal', 8.0), (15, 'Diego', 'Para preguntar, usamos la misma palabra: hay.', '질문할 때도 같은 단어 hay를 써요.', 'pregunta', 2, 'teal', 8.0), (16, 'Lucía', 'Cambiamos solo el lugar.', '장소만 바꿔 볼게요.', 'cambiar', 3, 'amber', 7.0), (17, 'Lucía', 'Hay un café aquí.', '여기에 카페가 있어요.', 'café', 3, 'amber', 7.0), (18, 'Jin', 'Hay un café aquí.', '여기에 카페가 있어요.', 'repetición', 3, 'amber', 7.0), (19, 'Diego', 'También puedes decir: hay un baño en la estación.', '이렇게도 말할 수 있어요: 역에 화장실이 있어요.', 'baño', 3, 'amber', 9.0), (20, 'Jin', 'Hay un baño en la estación.', '역에 화장실이 있어요.', 'repetición', 3, 'amber', 8.0), (21, 'Lucía', 'Otra pregunta útil: ¿hay un supermercado cerca?', '또 다른 유용한 질문: 근처에 슈퍼마켓이 있나요?', 'supermercado', 3, 'amber', 9.0), (22, 'Jin', '¿Hay un supermercado cerca?', '근처에 슈퍼마켓이 있나요?', 'pregunta', 3, 'amber', 8.0), (23, 'Diego', 'Si no quieres repetir, dices: sí, hay uno cerca.', '반복하고 싶지 않으면 이렇게 말해요: 네, 근처에 하나 있어요.', 'uno', 3, 'amber', 9.0), (24, 'Lucía', 'Sí, hay uno cerca.', '네, 근처에 하나 있어요.', 'respuesta corta', 3, 'amber', 7.5), (25, 'Diego', 'Mini prueba: traduce esta frase al español.', '미니 퀴즈: “근처에 약국이 있어요”를 스페인어로 말해 보세요.', 'quiz', 4, 'blue', 8.5), (26, 'Jin', 'Hay una farmacia cerca.', '근처에 약국이 있어요.', 'respuesta', 4, 'blue', 8.0), (27, 'Lucía', 'Ahora conviértela en una pregunta.', '이제 질문으로 바꿔 보세요: “근처에 약국이 있나요?”', 'quiz', 4, 'blue', 8.0), (28, 'Jin', '¿Hay una farmacia cerca?', '근처에 약국이 있나요?', 'respuesta', 4, 'blue', 8.0), (29, 'Diego', 'Recuerda: hay habla de existencia, no de ubicación exacta.', '기억하세요: hay는 정확한 위치보다 “있다”를 말해요.', 'contraste', 4, 'blue', 9.0), (30, 'Lucía', 'Después puedes preguntar: ¿dónde está la farmacia?', '그다음에는 이렇게 물을 수 있어요: 약국은 어디에 있나요?', 'puente', 4, 'blue', 8.5)]

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
    "intro_title": "Hay una farmacia cerca",
    "intro_subtitle": "Español A1+ · Ep.27",
    "intro_ko": "근처에 약국이 있어요",
    "intro_scene_image_path": "images/ep27-hay-una-farmacia-cerca-source.png",
    "intro_scene_fit": "cover",
    "thumbnail_title": "Hay una farmacia cerca",
    "thumbnail_subtitle": "Español A1+ · Ep.27",
    "thumbnail_ko": "근처에 약국이 있어요",
    "outro_ko": "이제 스페인어로 주변에 무엇이 있는지 말할 수 있어요",
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
            "text_es": "Hoy Jin aprende a decir qué hay cerca: hay una farmacia cerca.",
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
                "Muy bien. Ahora puedes preguntar y responder: hay una farmacia cerca, "
                "hay un café aquí, hay un baño en la estación."
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
    {"segment": 2, "title": "¿Hay una farmacia?"},
    {"segment": 10, "title": "Hay una farmacia cerca"},
    {"segment": 19, "title": "Cambia el lugar"},
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
