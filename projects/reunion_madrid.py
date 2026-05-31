"""Segment data for the Madrid meeting Spanish-learning video."""

from __future__ import annotations

IMAGE_PATH = "images/reunion-madrid.png"
DESCRIP_PATH = "descrip.md"
OUTPUT_NAME = "reunion-madrid"
SERIES = "descripcion"
SERIES_TITLE = "Descripción de imagen B2"
EPISODE = 1
LEVEL = "B2"
LANGUAGE = "es"
RENDER_VERSION = 1
YOUTUBE_TITLE = "Reunión en Madrid | Descripción de imagen B2 · Ep.1"
DESCRIPTION_INTRO = (
    "Práctica de descripción de imagen para estudiantes de español B2. "
    "Escucha la escena, repite las frases clave y observa cómo se organizan los detalles."
)
DESCRIPTION_OUTRO = (
    "Vuelve a ver el video e intenta describir la imagen sin mirar el texto. "
    "Después compara tu descripción con las frases del guion."
)
CHAPTERS = [
    {"segment": 1, "title": "Vocabulario clave"},
    {"segment": 5, "title": "La sala de reuniones"},
    {"segment": 7, "title": "La presentadora"},
    {"segment": 11, "title": "El equipo"},
    {"segment": 16, "title": "La mesa y el ambiente"},
    {"segment": 19, "title": "Estructuras B2"},
]

DESIGN = {
    "output_size": (1024, 576),
    "font_path": "/System/Library/Fonts/Optima.ttc",
    "font_index": 0,
    "font_path_emph": "/System/Library/Fonts/Optima.ttc",
    "font_index_emph": 3,
    "font_size": 28,
    "min_font_size": 22,
    "letter_spacing": 0.5,
    "bar_style": "gradient",
    "bar_top_color": (24, 18, 12, 200),
    "bar_bottom_color": (8, 6, 4, 220),
    "bar_corner_radius": 0,
    "bar_accent_color": (244, 162, 97, 255),
    "bar_accent_height": 2,
    "bar_padding_x": 29,
    "bar_padding_y": 18,
    "bar_bottom_margin_ratio": 0.07,
    "text_color": (255, 252, 246, 255),
    "text_shadow_color": (0, 0, 0, 200),
    "text_shadow_offset": (0, 2),
    "text_shadow_blur": 3,
    "easing": "ease_in_out_cubic",
    "transition_s": 0.8,
    "fade_s": 0.4,
    "idle_zoom_drift": 0.012,
    "grade": {
        "saturation": 1.10,
        "contrast": 1.05,
        "warmth": 6,
    },
}

SEGMENTS = [
    {
        "text": "Antes de empezar, vamos a repasar el vocabulario clave que vas a escuchar en esta descripción.",
        "frame": {"x": 0, "y": 0, "w": 1024, "h": 576},
        "zoom": {"start": 1.00, "end": 1.03},
    },
    {
        "text": "Fíjate en el lugar: una sala de reuniones con grandes ventanales, los tejados y las cúpulas al fondo, y una pizarra blanca.",
        "frame": {"x": 380, "y": 0, "w": 640, "h": 360},
        "zoom": {"start": 1.00, "end": 1.05},
    },
    {
        "text": "Observa también la ropa: un blazer, una blusa verde oliva, un top a lunares y un jersey color crema.",
        "frame": {"x": 180, "y": 60, "w": 440, "h": 248},
        "zoom": {"start": 1.00, "end": 1.04},
    },
    {
        "text": "Y presta atención a las acciones: gesticular, tomar notas y escuchar con atención.",
        "frame": {"x": 140, "y": 20, "w": 500, "h": 281},
        "zoom": {"start": 1.00, "end": 1.04},
    },
    {
        "text": "En la imagen vemos una sala de reuniones moderna, probablemente en una oficina del centro de Madrid.",
        "frame": {"x": 0, "y": 0, "w": 1024, "h": 576},
        "zoom": {"start": 1.00, "end": 1.04},
    },
    {
        "text": "A través de los grandes ventanales se ven los tejados y las cúpulas de los edificios clásicos de la ciudad — el paisaje es realmente impresionante.",
        "frame": {"x": 380, "y": 0, "w": 640, "h": 360},
        "zoom": {"start": 1.00, "end": 1.05},
    },
    {
        "text": "Una mujer joven, de pelo oscuro, está de pie junto a una pizarra blanca.",
        "frame": {"x": 110, "y": 30, "w": 600, "h": 338},
        "zoom": {"start": 1.00, "end": 1.05},
    },
    {
        "text": "Lleva una blusa verde oliva y pantalones beige.",
        "frame": {"x": 180, "y": 60, "w": 440, "h": 248},
        "zoom": {"start": 1.00, "end": 1.04},
    },
    {
        "text": "Tiene un rotulador en la mano y parece estar explicando algo importante a su equipo.",
        "frame": {"x": 200, "y": 80, "w": 440, "h": 248},
        "zoom": {"start": 1.00, "end": 1.05},
    },
    {
        "text": "Está gesticulando con la mano izquierda, lo que sugiere que es una presentadora dinámica y segura de sí misma.",
        "frame": {"x": 140, "y": 20, "w": 500, "h": 281},
        "zoom": {"start": 1.00, "end": 1.04},
    },
    {
        "text": "Alrededor de la mesa de madera están sentados cuatro compañeros que la escuchan con atención.",
        "frame": {"x": 0, "y": 0, "w": 1024, "h": 576},
        "zoom": {"start": 1.00, "end": 1.03},
    },
    {
        "text": "A la izquierda, un hombre de pelo rizado lleva un blazer azul oscuro y toma notas en un cuaderno.",
        "frame": {"x": 0, "y": 150, "w": 400, "h": 225},
        "zoom": {"start": 1.00, "end": 1.05},
    },
    {
        "text": "Frente a él, otro hombre con camisa azul claro tiene un portátil abierto.",
        "frame": {"x": 224, "y": 50, "w": 800, "h": 450},
        "zoom": {"start": 1.00, "end": 1.05},
    },
    {
        "text": "A su lado, una mujer con un top a lunares sostiene un bolígrafo,",
        "frame": {"x": 580, "y": 120, "w": 400, "h": 225},
        "zoom": {"start": 1.00, "end": 1.05},
    },
    {
        "text": "y al final de la mesa, otra mujer con un jersey color crema escucha atentamente.",
        "frame": {"x": 624, "y": 80, "w": 400, "h": 225},
        "zoom": {"start": 1.00, "end": 1.05},
    },
    {
        "text": "Sobre la mesa hay varias tazas de café, vasos de agua y algunos móviles.",
        "frame": {"x": 175, "y": 180, "w": 704, "h": 396},
        "zoom": {"start": 1.00, "end": 1.04},
    },
    {
        "text": "El ambiente es profesional pero relajado.",
        "frame": {"x": 0, "y": 0, "w": 1024, "h": 576},
        "zoom": {"start": 1.05, "end": 1.00},
    },
    {
        "text": "Aunque la reunión parece ser seria, no hay tensión: todos están concentrados y muestran interés en lo que dice la presentadora.",
        "frame": {"x": 0, "y": 0, "w": 1024, "h": 576},
        "zoom": {"start": 1.00, "end": 1.02},
    },
    {
        "text": "Para terminar, repasemos tres estructuras B2 que aparecieron en la descripción.",
        "frame": {"x": 0, "y": 0, "w": 1024, "h": 576},
        "zoom": {"start": 1.03, "end": 1.00},
    },
    {
        "text": "Recuerda «parecer + infinitivo» para impresiones: parece estar explicando algo importante.",
        "frame": {"x": 200, "y": 80, "w": 440, "h": 248},
        "zoom": {"start": 1.00, "end": 1.04},
    },
    {
        "text": "Usa «aunque + indicativo» para contraste real: aunque la reunión parece ser seria, no hay tensión.",
        "frame": {"x": 0, "y": 0, "w": 1024, "h": 576},
        "zoom": {"start": 1.00, "end": 1.02},
    },
    {
        "text": "Y «lo que sugiere que…» añade una conclusión: la presentadora está segura de sí misma.",
        "frame": {"x": 140, "y": 20, "w": 500, "h": 281},
        "zoom": {"start": 1.00, "end": 1.04},
    },
]

AUDIO = {
    "voice": "Mónica",
    "rate_wpm": 175,
    "lead_padding_s": 0.35,
    "tail_padding_s": 0.55,
    "min_duration_s": 4.0,
    "readability_floor_ratio": 0.9,
    "bgm_path": "assets/audio/bgm.mp3",
    "bgm_volume_db": -16.0,
    "narration_volume_db": 0.0,
    "ducking": True,
    "ducking_threshold": 0.05,
    "ducking_ratio": 8,
    "ducking_attack_ms": 120,
    "ducking_release_ms": 600,
    "fade_in_s": 1.5,
    "fade_out_s": 2.0,
    "audio_codec": "aac",
    "audio_bitrate_kbps": 192,
    "sample_rate_hz": 44100,
}
