"""A1 Madrid metro-ticket story episode: Jin buys a ticket."""

from __future__ import annotations

IMAGE_PATH = "assets/generated/metro-ticket-thumbnail-source.png"
DESCRIP_PATH = "a1-un-billete-por-favor/descrip.md"
OUTPUT_NAME = "un-billete-por-favor"
PUBLIC_SLUG = "a1-un-billete-por-favor"
YOUTUBE_URL = ""
SERIES = "frases-a1"
SERIES_TITLE = "Español A1 -- Frases útiles"
EPISODE = 10
LEVEL = "A1"
LANGUAGE = "es"
RENDER_VERSION = 1
RENDER_TYPE = "cards"
THUMBNAIL_PATH = "thumbs/a1-un-billete-por-favor.jpg"
YOUTUBE_TITLE = "Un billete, por favor 🎫 지하철표 사기 | Español A1 · Ep.10"
DESCRIPTION_INTRO = (
    "Después de encontrar la estación de metro, Jin necesita comprar un billete. "
    "Lucía y Diego practican con él una escena muy útil en Madrid: pedir un billete, decir el destino, preguntar el precio y elegir solo ida."
)
DESCRIPTION_OUTRO = (
    "Escucha primero, repite en voz alta y después haz toda la escena tú: "
    "Un billete, por favor. Voy al centro. ¿Cuánto cuesta? Solo ida, por favor."
)
KOREAN_TEASER = (
    "한국어 티저: EP.10은 마드리드 지하철역에서 표를 사는 A1 상황극입니다. "
    "Jin과 함께 Un billete, por favor, Voy al centro, ¿Cuánto cuesta?, Solo ida를 연습합니다."
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
    "un billete por favor",
    "comprar billete en español",
    "metro en español",
    "billete de metro",
    "cuanto cuesta",
    "solo ida",
    "ida y vuelta",
    "conversacion español A1",
    "스페인어 지하철",
    "스페인어 여행 회화",
]
BASE_HASHTAGS = ["#EspañolA1", "#aprenderespañol", "#스페인어"]
EXTRA_HASHTAGS = ["#SpanishA1", "#frasesenespañol", "#Madrid"]

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
    {"block_id": 1, "title_es": "Un billete, por favor", "title_ko": "표 한 장 주세요", "color_block": "coral", "start": 1},
    {"block_id": 2, "title_es": "Voy al centro", "title_ko": "시내로 가요", "color_block": "amber", "start": 9},
    {"block_id": 3, "title_es": "¿Cuánto cuesta?", "title_ko": "얼마예요?", "color_block": "teal", "start": 15},
    {"block_id": 4, "title_es": "Solo ida", "title_ko": "편도요", "color_block": "blue", "start": 21},
]

# line_num, speaker, Spanish, Korean, focus, block_id, color, duration_s
DIALOGUE = [
    (1, "Diego", "Mira, Jin. Estamos en la estación.", "봐, Jin. 우리는 역에 있어.", "estación", 1, "coral", 8.5),
    (2, "Jin", "Estamos en la estación de metro.", "우리는 지하철역에 있어요.", "estación de metro", 1, "coral", 8.5),
    (3, "Lucía", "Muy bien. Ahora vamos a comprar un billete.", "좋아. 이제 표를 살 거야.", "comprar", 1, "coral", 9.0),
    (4, "Jin", "Quiero comprar un billete.", "표를 사고 싶어요.", "quiero comprar", 1, "coral", 8.5),
    (5, "Diego", "Perfecto. Usa esta frase.", "좋아. 이 문장을 써 봐.", "usa", 1, "coral", 8.0),
    (6, "Jin", "Un billete, por favor.", "표 한 장 주세요.", "Un billete", 1, "coral", 8.5),
    (7, "Lucía", "Muy bien. Un billete, por favor.", "아주 좋아. 표 한 장 주세요.", "repetición", 1, "coral", 8.5),
    (8, "Jin", "Un billete.", "표 한 장.", "Un billete", 1, "coral", 8.0),
    (9, "Diego", "Ahora di tu destino.", "이제 목적지를 말해 봐.", "destino", 2, "amber", 8.0),
    (10, "Lucía", "¿A dónde vas?", "어디로 가?", "¿A dónde?", 2, "amber", 8.0),
    (11, "Jin", "Voy al centro.", "시내로 가요.", "voy al centro", 2, "amber", 8.0),
    (12, "Diego", "Muy bien. Voy al centro.", "좋아. 시내로 가요.", "repetición", 2, "amber", 8.5),
    (13, "Jin", "Un billete al centro, por favor.", "시내까지 표 한 장 주세요.", "al centro", 2, "amber", 9.0),
    (14, "Lucía", "Perfecto, Jin.", "완벽해, Jin.", "Perfecto", 2, "amber", 8.0),
    (15, "Diego", "Ahora pregunta el precio.", "이제 가격을 물어봐.", "precio", 3, "teal", 8.0),
    (16, "Jin", "¿Cuánto cuesta?", "얼마예요?", "¿Cuánto cuesta?", 3, "teal", 8.0),
    (17, "Lucía", "Cuesta dos euros.", "2유로예요.", "cuesta", 3, "teal", 8.0),
    (18, "Jin", "Dos euros.", "2유로.", "dos euros", 3, "teal", 7.5),
    (19, "Diego", "Aquí tienes.", "여기 있어요.", "Aquí tienes", 3, "teal", 8.0),
    (20, "Jin", "Gracias. Aquí tienes.", "감사합니다. 여기 있어요.", "gracias", 3, "teal", 8.5),
    (21, "Lucía", "Hay dos opciones.", "두 가지 선택지가 있어.", "opciones", 4, "blue", 8.0),
    (22, "Diego", "Solo ida.", "편도.", "solo ida", 4, "blue", 7.5),
    (23, "Lucía", "Ida y vuelta.", "왕복.", "ida y vuelta", 4, "blue", 8.0),
    (24, "Diego", "¿Solo ida o ida y vuelta?", "편도예요, 왕복이에요?", "opciones", 4, "blue", 9.0),
    (25, "Jin", "Solo ida, por favor.", "편도 주세요.", "solo ida", 4, "blue", 8.5),
    (26, "Lucía", "Muy bien. Solo ida.", "좋아. 편도.", "repetición", 4, "blue", 8.0),
    (27, "Diego", "Ya tienes el billete.", "이제 표가 있어.", "tienes", 4, "blue", 8.0),
    (28, "Jin", "Tengo el billete.", "표가 있어요.", "tengo", 4, "blue", 8.0),
    (29, "Lucía", "Buen viaje, Jin.", "좋은 여행 되세요, Jin.", "Buen viaje", 4, "blue", 8.0),
    (30, "Jin", "Gracias. ¡Vamos al metro!", "감사합니다. 지하철 타러 가요!", "Vamos", 4, "blue", 8.5),
]

DESIGN = {
    "output_size": (1280, 720),
    "font_path": "assets/fonts/NotoSansKR-Bold.ttf",
    "font_index": 0,
    "font_path_ko": "assets/fonts/NotoSansKR-Regular.ttf",
    "font_index_ko": 0,
    "font_size_title": 70,
    "font_size_es": 68,
    "min_font_size_es": 38,
    "font_size_ko": 32,
    "font_size_example": 30,
    "background_color": (248, 247, 242),
    "text_color": (31, 35, 40),
    "muted_text_color": (96, 101, 109),
    "intro_title": "Un billete, por favor",
    "intro_subtitle": "Español A1 · Ep.10",
    "intro_ko": "지하철표 사기",
    "intro_scene_image_path": "assets/generated/metro-ticket-thumbnail-source.png",
    "intro_scene_fit": "contain",
    "thumbnail_title": "Un billete, por favor",
    "thumbnail_subtitle": "Español A1 · Ep.10",
    "thumbnail_ko": "지하철표 사기",
    "outro_ko": "이제 스페인어로 지하철표를 살 수 있어요",
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
            "text_es": (
                "Hoy estamos en la estación de metro. Jin quiere comprar un billete. Lucía y Diego ayudan a Jin con frases muy útiles: "
                "Un billete, por favor. Voy al centro. ¿Cuánto cuesta? Solo ida."
            ),
            "duration_s": 12.0,
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
                    "character": speaker,
                }
            )
    segments.append(
        {
            "type": "outro",
            "text_es": (
                "Muy bien. Ahora puedes comprar un billete en español: Un billete, por favor. Voy al centro. "
                "¿Cuánto cuesta? Solo ida, por favor. En el próximo episodio seguimos en el metro de Madrid."
            ),
            "duration_s": 23.0,
            "color_block": "neutral",
            "characters": ["Jin", "Lucía", "Diego"],
        }
    )
    return segments


SEGMENTS = _build_segments()
CHAPTERS = [
    {"segment": 1, "title": "Introducción"},
    {"segment": 2, "title": "Un billete, por favor"},
    {"segment": 11, "title": "Voy al centro"},
    {"segment": 19, "title": "¿Cuánto cuesta?"},
    {"segment": 25, "title": "Solo ida"},
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
