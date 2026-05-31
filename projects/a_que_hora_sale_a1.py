"""A1 station-time story episode: Jin asks train departure time."""

from __future__ import annotations

IMAGE_PATH = "assets/generated/station-time-thumbnail-source.png"
DESCRIP_PATH = "a1-a-que-hora-sale/descrip.md"
OUTPUT_NAME = "a-que-hora-sale"
PUBLIC_SLUG = "a1-a-que-hora-sale"
YOUTUBE_URL = ""
SERIES = "frases-a1"
SERIES_TITLE = "Español A1 -- Frases útiles"
EPISODE = 11
LEVEL = "A1"
LANGUAGE = "es"
RENDER_VERSION = 2
RENDER_TYPE = "cards"
THUMBNAIL_PATH = "thumbs/a1-a-que-hora-sale.jpg"
YOUTUBE_TITLE = "¿A qué hora sale? 🚆 출발 시간 묻기 | Español A1 · Ep.11"
DESCRIPTION_INTRO = (
    "Después de comprar el billete, Jin necesita mirar la hora, la salida del tren y el andén. "
    "Lucía y Diego practican con él frases muy útiles en la estación: ¿Qué hora es?, ¿A qué hora sale?, "
    "¿Cuánto tarda? y ¿En qué andén?"
)
DESCRIPTION_OUTRO = (
    "Escucha primero, repite en voz alta y después haz toda la escena tú: "
    "¿Qué hora es? ¿A qué hora sale? Sale a las tres. ¿Cuánto tarda? ¿En qué andén?"
)
KOREAN_TEASER = (
    "한국어 티저: EP.11은 역에서 출발 시간, 소요 시간, 승강장을 묻는 A1 상황극입니다. "
    "Jin과 함께 ¿A qué hora sale?, Sale a las tres, ¿Cuánto tarda?, ¿En qué andén?을 연습합니다."
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
    "a que hora sale",
    "hora en español",
    "tren en español",
    "anden en español",
    "metro en español",
    "conversacion español A1",
    "스페인어 시간",
    "스페인어 기차",
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
    {"block_id": 1, "title_es": "¿Qué hora es?", "title_ko": "몇 시예요?", "color_block": "coral", "start": 1},
    {"block_id": 2, "title_es": "¿A qué hora sale?", "title_ko": "몇 시에 출발해요?", "color_block": "amber", "start": 9},
    {"block_id": 3, "title_es": "¿Cuánto tarda?", "title_ko": "얼마나 걸려요?", "color_block": "teal", "start": 15},
    {"block_id": 4, "title_es": "¿En qué andén?", "title_ko": "어느 승강장이에요?", "color_block": "blue", "start": 23},
]

# line_num, speaker, Spanish, Korean, focus, block_id, color, duration_s
DIALOGUE = [
    (1, "Lucía", "Mira, Jin. Ya tienes el billete.", "봐, Jin. 이제 표가 있어.", "billete", 1, "coral", 8.5),
    (2, "Jin", "Sí. Tengo el billete.", "네. 표가 있어요.", "tengo", 1, "coral", 8.0),
    (3, "Diego", "Ahora necesitamos la hora.", "이제 시간이 필요해.", "la hora", 1, "coral", 8.0),
    (4, "Jin", "¿Qué hora es?", "몇 시예요?", "¿Qué hora es?", 1, "coral", 8.0),
    (5, "Lucía", "Son las dos.", "2시예요.", "son las dos", 1, "coral", 8.0),
    (6, "Jin", "¿Son las dos?", "2시예요?", "son las dos", 1, "coral", 7.5),
    (7, "Lucía", "Sí, son las dos. Muy bien.", "응, 2시야. 아주 좋아.", "muy bien", 1, "coral", 8.5),
    (8, "Diego", "Perfecto. La hora es importante.", "좋아. 시간은 중요해.", "la hora", 1, "coral", 8.5),
    (9, "Diego", "Mira la pantalla.", "전광판을 봐.", "pantalla", 2, "amber", 7.5),
    (10, "Jin", "¿A qué hora sale el tren?", "기차는 몇 시에 출발해요?", "¿A qué hora sale?", 2, "amber", 8.5),
    (11, "Lucía", "Sale a las tres.", "3시에 출발해요.", "sale", 2, "amber", 8.0),
    (12, "Jin", "¿A las tres?", "3시에요?", "a las tres", 2, "amber", 7.5),
    (13, "Lucía", "Sí, a las tres.", "응, 3시에.", "a las tres", 2, "amber", 7.5),
    (14, "Diego", "El tren sale a las tres.", "기차는 3시에 출발해.", "sale a las tres", 2, "amber", 8.5),
    (15, "Jin", "¿A qué hora llega?", "몇 시에 도착해요?", "llega", 3, "teal", 8.0),
    (16, "Diego", "Llega a las tres y veinte.", "3시 20분에 도착해요.", "tres y veinte", 3, "teal", 8.5),
    (17, "Jin", "Tres y veinte.", "3시 20분.", "tres y veinte", 3, "teal", 7.5),
    (18, "Lucía", "Muy bien, Jin.", "아주 좋아, Jin.", "muy bien", 3, "teal", 7.5),
    (19, "Jin", "¿Cuánto tarda?", "얼마나 걸려요?", "¿Cuánto tarda?", 3, "teal", 8.0),
    (20, "Lucía", "Tarda veinte minutos.", "20분 걸려요.", "veinte minutos", 3, "teal", 8.0),
    (21, "Jin", "Veinte minutos. Es rápido.", "20분. 빠르네요.", "es rápido", 3, "teal", 8.5),
    (22, "Diego", "Sí, es rápido.", "응, 빨라.", "rápido", 3, "teal", 7.5),
    (23, "Diego", "Ahora necesitamos el andén.", "이제 승강장이 필요해.", "andén", 4, "blue", 8.0),
    (24, "Jin", "¿En qué andén?", "어느 승강장이에요?", "¿En qué andén?", 4, "blue", 8.0),
    (25, "Lucía", "En el andén dos.", "2번 승강장이에요.", "andén dos", 4, "blue", 8.0),
    (26, "Jin", "¿Andén dos?", "2번 승강장이요?", "andén dos", 4, "blue", 7.5),
    (27, "Lucía", "Sí, andén dos.", "응, 2번 승강장.", "andén dos", 4, "blue", 7.5),
    (28, "Diego", "Estamos a tiempo.", "우리는 시간 맞춰 왔어.", "a tiempo", 4, "blue", 8.0),
    (29, "Jin", "Muy bien. Vamos al andén dos.", "좋아요. 2번 승강장으로 가요.", "vamos", 4, "blue", 8.5),
    (30, "Lucía", "Vamos. Buen viaje.", "가자. 좋은 여행 되세요.", "buen viaje", 4, "blue", 8.0),
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
    "intro_title": "¿A qué hora sale?",
    "intro_subtitle": "Español A1 · Ep.11",
    "intro_ko": "출발 시간 묻기",
    "intro_scene_image_path": "assets/generated/station-time-thumbnail-source.png",
    "intro_scene_fit": "contain",
    "thumbnail_title": "¿A qué hora sale?",
    "thumbnail_subtitle": "Español A1 · Ep.11",
    "thumbnail_ko": "몇 시에 출발해요?",
    "outro_ko": "이제 스페인어로 출발 시간과 승강장을 물어볼 수 있어요",
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
                "Hoy estamos en la estación. Jin ya tiene el billete. "
                "Ahora pregunta la hora, la salida del tren y el andén."
            ),
            "duration_s": 12.0,
            "color_block": "neutral",
            "characters": ["Jin", "Lucía", "Diego"],
        }
    ]
    for block in BLOCKS:
        # The first block header is intentionally a clear 3-second breathing space
        # between the intro slide and the first body dialogue slide.
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
                "Muy bien. Ahora puedes preguntar la hora en la estación: ¿Qué hora es? ¿A qué hora sale? "
                "Sale a las tres. ¿Cuánto tarda? ¿En qué andén? En el próximo episodio seguimos practicando español útil para viajar."
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
    {"segment": 2, "title": "¿Qué hora es?"},
    {"segment": 11, "title": "¿A qué hora sale?"},
    {"segment": 18, "title": "¿Cuánto tarda?"},
    {"segment": 27, "title": "¿En qué andén?"},
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
