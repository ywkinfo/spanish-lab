"""A1 Madrid directions story episode: Jin asks where the metro is."""

from __future__ import annotations

IMAGE_PATH = "assets/generated/madrid-street-directions-thumbnail-source.png"
DESCRIP_PATH = "a1-donde-esta-el-metro/descrip.md"
OUTPUT_NAME = "donde-esta-el-metro"
PUBLIC_SLUG = "a1-donde-esta-el-metro"
YOUTUBE_URL = ""
SERIES = "frases-a1"
SERIES_TITLE = "Español A1 -- Frases útiles"
EPISODE = 9
LEVEL = "A1"
LANGUAGE = "es"
RENDER_VERSION = 1
RENDER_TYPE = "cards"
THUMBNAIL_PATH = "thumbs/a1-donde-esta-el-metro.jpg"
YOUTUBE_TITLE = "¿Dónde está el metro? 🚇 길 묻기 | Español A1 · Ep.9"
DESCRIPTION_INTRO = (
    "Después de salir de la cafetería, Jin quiere ir al metro. "
    "Lucía y Diego practican con él una escena muy útil en Madrid: preguntar por un lugar, entender direcciones simples y pedir que repitan."
)
DESCRIPTION_OUTRO = (
    "Escucha primero, repite en voz alta y después haz toda la escena tú: "
    "¿Dónde está el metro? Sigue todo recto. Gira a la derecha. ¿Puedes repetir, por favor?"
)
KOREAN_TEASER = (
    "한국어 티저: EP.9은 마드리드 골목 거리에서 지하철역 가는 길을 묻는 A1 상황극입니다. "
    "Jin과 함께 ¿Dónde está el metro?, Sigue todo recto, Gira a la derecha를 연습합니다."
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
    "donde esta el metro",
    "direcciones en español",
    "preguntar direcciones español",
    "metro en español",
    "todo recto",
    "gira a la derecha",
    "conversacion español A1",
    "스페인어 길 묻기",
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
    {"block_id": 1, "title_es": "¿Dónde está el metro?", "title_ko": "장소 묻기", "color_block": "coral", "start": 1},
    {"block_id": 2, "title_es": "Sigue todo recto", "title_ko": "직진하기", "color_block": "amber", "start": 9},
    {"block_id": 3, "title_es": "A la derecha", "title_ko": "오른쪽으로", "color_block": "teal", "start": 15},
    {"block_id": 4, "title_es": "¿Puedes repetir?", "title_ko": "다시 말해 달라고 하기", "color_block": "blue", "start": 21},
]

# line_num, speaker, Spanish, Korean, focus, block_id, color, duration_s
DIALOGUE = [
    (1, "Diego", "Mira la calle, Jin.", "Jin, 거리를 봐.", "Mira la calle", 1, "coral", 8.0),
    (2, "Jin", "Veo una calle de Madrid.", "마드리드 거리가 보여.", "Veo una calle", 1, "coral", 8.5),
    (3, "Lucía", "Muy bien. Salimos de la cafetería.", "좋아. 우리는 카페에서 나왔어.", "salimos", 1, "coral", 8.5),
    (4, "Jin", "Quiero ir al metro.", "나는 지하철역에 가고 싶어.", "quiero ir", 1, "coral", 8.5),
    (5, "Diego", "Perfecto. Pregunta con esta frase.", "좋아. 이 문장으로 물어봐.", "pregunta", 1, "coral", 8.5),
    (6, "Jin", "¿Dónde está el metro?", "지하철역은 어디에 있어요?", "¿Dónde está?", 1, "coral", 8.5),
    (7, "Lucía", "Muy bien. El metro está cerca.", "아주 좋아. 지하철역은 가까워.", "está cerca", 1, "coral", 8.5),
    (8, "Jin", "Está cerca.", "가까워요.", "Está cerca", 1, "coral", 8.0),
    (9, "Diego", "Ahora escucha la dirección.", "이제 길 안내를 들어 봐.", "dirección", 2, "amber", 8.5),
    (10, "Lucía", "Sigue todo recto.", "쭉 직진해.", "todo recto", 2, "amber", 8.5),
    (11, "Jin", "Todo recto.", "쭉 직진.", "Todo recto", 2, "amber", 8.0),
    (12, "Diego", "Sí. Sigue todo recto.", "맞아. 쭉 직진해.", "repetición", 2, "amber", 8.5),
    (13, "Lucía", "Sí, todo recto por esta calle.", "응, 이 길로 쭉 직진해.", "por esta calle", 2, "amber", 8.5),
    (14, "Jin", "Vale. Sigo todo recto.", "좋아요. 쭉 직진할게요.", "sigo", 2, "amber", 8.5),
    (15, "Diego", "Después, gira a la derecha.", "그다음 오른쪽으로 돌아.", "después", 3, "teal", 8.5),
    (16, "Jin", "¿A la derecha?", "오른쪽으로요?", "a la derecha", 3, "teal", 8.0),
    (17, "Lucía", "Sí, a la derecha.", "응, 오른쪽으로.", "derecha", 3, "teal", 8.0),
    (18, "Jin", "Gira a la derecha.", "오른쪽으로 도세요.", "gira", 3, "teal", 8.5),
    (19, "Lucía", "Hoy usamos a la derecha.", "오늘은 오른쪽을 써.", "usamos", 3, "teal", 8.5),
    (20, "Jin", "Todo recto y a la derecha.", "쭉 직진하고 오른쪽으로.", "frase completa", 3, "teal", 8.5),
    (21, "Lucía", "El metro está en la esquina.", "지하철역은 모퉁이에 있어.", "en la esquina", 4, "blue", 8.5),
    (22, "Jin", "¿En la esquina?", "모퉁이에요?", "la esquina", 4, "blue", 8.0),
    (23, "Diego", "Sí. En la esquina.", "맞아. 모퉁이에.", "repetición", 4, "blue", 8.0),
    (24, "Jin", "No entiendo.", "이해하지 못했어요.", "No entiendo", 4, "blue", 8.0),
    (25, "Jin", "¿Puedes repetir, por favor?", "다시 말해 줄 수 있나요?", "repetir", 4, "blue", 9.0),
    (26, "Lucía", "Claro. Sigue todo recto y gira a la derecha.", "물론이지. 쭉 직진하고 오른쪽으로 돌아.", "claro", 4, "blue", 9.5),
    (27, "Jin", "Todo recto y a la derecha. El metro está en la esquina.", "쭉 직진하고 오른쪽으로. 지하철역은 모퉁이에 있어요.", "resumen", 4, "blue", 10.0),
    (28, "Diego", "Perfecto, Jin.", "완벽해, Jin.", "Perfecto", 4, "blue", 8.0),
    (29, "Jin", "Muchas gracias.", "정말 감사합니다.", "Gracias", 4, "blue", 8.0),
    (30, "Lucía", "De nada. ¡Vamos!", "천만에. 가자!", "Vamos", 4, "blue", 8.0),
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
    "intro_title": "¿Dónde está el metro?",
    "intro_subtitle": "Español A1 · Ep.9",
    "intro_ko": "마드리드에서 길 묻기",
    "intro_scene_image_path": "assets/generated/madrid-street-directions-thumbnail-source.png",
    "intro_scene_fit": "contain",
    "thumbnail_title": "¿Dónde está el metro?",
    "thumbnail_subtitle": "Español A1 · Ep.9",
    "thumbnail_ko": "길 묻기",
    "outro_ko": "이제 스페인어로 길을 물어보세요",
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
                "Hoy salimos de la cafetería. Jin quiere ir al metro. Lucía y Diego ayudan a Jin con frases muy útiles: "
                "¿Dónde está el metro? Sigue todo recto. Gira a la derecha."
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
                "Muy bien. Ahora puedes preguntar por un lugar en español: ¿Dónde está el metro? Sigue todo recto. "
                "Gira a la derecha. ¿Puedes repetir, por favor? En el próximo episodio seguimos caminando por Madrid."
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
    {"segment": 2, "title": "¿Dónde está el metro?"},
    {"segment": 11, "title": "Sigue todo recto"},
    {"segment": 19, "title": "A la derecha"},
    {"segment": 25, "title": "¿Puedes repetir?"},
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
