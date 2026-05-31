"""Segment data for the mercado Spanish-learning video."""

from __future__ import annotations

IMAGE_PATH = "images/mercado.png"
DESCRIP_PATH = "projects/mercado_descrip.md"
OUTPUT_NAME = "mercado"
SERIES = "descripcion"
SERIES_TITLE = "Descripción de imagen B2"
EPISODE = 2
LEVEL = "B2"
LANGUAGE = "es"
RENDER_VERSION = 1
YOUTUBE_TITLE = "En el mercado | Descripción de imagen B2 · Ep.2"
DESCRIPTION_INTRO = (
    "Práctica de descripción de imagen para estudiantes de español B2. "
    "Escucha la escena, repite las frases clave y observa cómo se describen personas, objetos y ambiente."
)
DESCRIPTION_OUTRO = (
    "Vuelve a ver el video e intenta describir el mercado con tus propias palabras. "
    "Después usa el guion como modelo para mejorar tu respuesta."
)
CHAPTERS = [
    {"segment": 1, "title": "Vocabulario clave"},
    {"segment": 5, "title": "El frutero"},
    {"segment": 9, "title": "La clienta"},
    {"segment": 14, "title": "La fruta tropical"},
    {"segment": 18, "title": "El ambiente del mercado"},
    {"segment": 21, "title": "Cierre y repaso"},
]

DESIGN = {
    "output_size": (1280, 720),
    "font_path": "/System/Library/Fonts/Optima.ttc",
    "font_index": 0,
    "font_path_emph": "/System/Library/Fonts/Optima.ttc",
    "font_index_emph": 3,
    "font_size": 36,
    "min_font_size": 26,
    "letter_spacing": 0.5,
    "bar_style": "gradient",
    "bar_top_color": (24, 18, 12, 200),
    "bar_bottom_color": (8, 6, 4, 220),
    "bar_corner_radius": 0,
    "bar_accent_color": (244, 162, 97, 255),
    "bar_accent_height": 2,
    "bar_padding_x": 36,
    "bar_padding_y": 22,
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
        "text": "Antes de empezar, observa el mercado: fruta tropical, mucho sol y dos protagonistas conversando en un puesto.",
        "frame": {"x": 0, "y": 0, "w": 1280, "h": 720},
        "zoom": {"start": 1.00, "end": 1.00},
    },
    {
        "text": "La escena tiene lugar en un mercado al aire libre, posiblemente en un pueblo costero de España o de Latinoamérica.",
        "frame": {"x": 0, "y": 0, "w": 1280, "h": 720},
        "zoom": {"start": 1.00, "end": 1.03},
    },
    {
        "text": "Es un día soleado y luminoso,",
        "frame": {"x": 120, "y": 0, "w": 540, "h": 304},
        "zoom": {"start": 1.00, "end": 1.04},
    },
    {
        "text": "y el ambiente está muy animado: se nota que el mercado es popular entre los vecinos.",
        "frame": {"x": 0, "y": 0, "w": 1024, "h": 576},
        "zoom": {"start": 1.00, "end": 1.03},
    },
    {
        "text": "En el centro de la imagen, un frutero está atendiendo a una clienta. Es un señor mayor, de unos sesenta años, con barba canosa y bigote.",
        "frame": {"x": 380, "y": 30, "w": 480, "h": 270},
        "zoom": {"start": 1.00, "end": 1.05},
    },
    {
        "text": "Lleva un sombrero panamá de color claro y un delantal verde oscuro sobre una camisa blanca.",
        "frame": {"x": 420, "y": 30, "w": 520, "h": 293},
        "zoom": {"start": 1.00, "end": 1.05},
    },
    {
        "text": "En las manos sostiene un mango maduro que parece estar mostrándole con orgullo a la mujer,",
        "frame": {"x": 520, "y": 240, "w": 450, "h": 253},
        "zoom": {"start": 1.00, "end": 1.06},
    },
    {
        "text": "como si le estuviera explicando por qué esta fruta es la mejor del puesto.",
        "frame": {"x": 520, "y": 240, "w": 450, "h": 253},
        "zoom": {"start": 1.06, "end": 1.02},
    },
    {
        "text": "Frente a él está una mujer joven, de pelo largo y oscuro.",
        "frame": {"x": 120, "y": 60, "w": 480, "h": 270},
        "zoom": {"start": 1.00, "end": 1.04},
    },
    {
        "text": "Lleva un vestido blanco sin mangas y un bolso de mimbre colgado del hombro,",
        "frame": {"x": 120, "y": 60, "w": 480, "h": 270},
        "zoom": {"start": 1.00, "end": 1.04},
    },
    {
        "text": "dentro del cual asoman algunas verduras.",
        "frame": {"x": 120, "y": 360, "w": 450, "h": 253},
        "zoom": {"start": 1.00, "end": 1.05},
    },
    {
        "text": "Está escuchando atentamente al vendedor con una expresión interesada —",
        "frame": {"x": 200, "y": 80, "w": 450, "h": 253},
        "zoom": {"start": 1.00, "end": 1.04},
    },
    {
        "text": "quizás esté pensando si comprar el mango o no.",
        "frame": {"x": 200, "y": 80, "w": 450, "h": 253},
        "zoom": {"start": 1.04, "end": 1.00},
    },
    {
        "text": "El puesto está repleto de fruta tropical: hay mangos verdes y rojizos,",
        "frame": {"x": 640, "y": 360, "w": 640, "h": 360},
        "zoom": {"start": 1.00, "end": 1.04},
    },
    {
        "text": "naranjas brillantes, piñas con sus hojas puntiagudas,",
        "frame": {"x": 520, "y": 450, "w": 480, "h": 270},
        "zoom": {"start": 1.00, "end": 1.05},
    },
    {
        "text": "y al fondo se ven plátanos, limones y otras frutas exóticas.",
        "frame": {"x": 830, "y": 300, "w": 450, "h": 253},
        "zoom": {"start": 1.00, "end": 1.05},
    },
    {
        "text": "Todo está colocado en cajas de madera y plástico, formando una explosión de colores.",
        "frame": {"x": 640, "y": 360, "w": 640, "h": 360},
        "zoom": {"start": 1.04, "end": 1.00},
    },
    {
        "text": "Detrás de los protagonistas, otros clientes pasean por el mercado.",
        "frame": {"x": 0, "y": 100, "w": 480, "h": 270},
        "zoom": {"start": 1.00, "end": 1.05},
    },
    {
        "text": "Una mujer con una camiseta a rayas observa los puestos,",
        "frame": {"x": 0, "y": 100, "w": 480, "h": 270},
        "zoom": {"start": 1.00, "end": 1.05},
    },
    {
        "text": "y más al fondo se distinguen sombrillas rojas y edificios blancos típicos de la arquitectura mediterránea.",
        "frame": {"x": 120, "y": 0, "w": 540, "h": 304},
        "zoom": {"start": 1.00, "end": 1.04},
    },
    {
        "text": "Hace mucho sol, así que el sombrero del frutero no es solo un accesorio — es una protección necesaria.",
        "frame": {"x": 460, "y": 30, "w": 450, "h": 253},
        "zoom": {"start": 1.00, "end": 1.05},
    },
    {
        "text": "Para cerrar, recuerda cómo la descripción usa estar para estados y ser para identidad o función.",
        "frame": {"x": 0, "y": 0, "w": 1280, "h": 720},
        "zoom": {"start": 1.02, "end": 1.00},
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
