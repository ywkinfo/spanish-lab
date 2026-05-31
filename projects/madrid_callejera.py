"""Segment data for the Madrid street Spanish-learning video."""

from __future__ import annotations

IMAGE_PATH = "images/madrid-callejera.png"
DESCRIP_PATH = "6thsc/descrip.md"
OUTPUT_NAME = "madrid-callejera"
SERIES = "descripcion"
SERIES_TITLE = "Descripción de imagen B2"
EPISODE = 6
LEVEL = "B2"
LANGUAGE = "es"
RENDER_VERSION = 1
YOUTUBE_TITLE = "Por una calle de Madrid | Descripción de imagen B2 · Ep.6"
DESCRIPTION_INTRO = (
    "Práctica de descripción de imagen para estudiantes de español B2. "
    "Observa una calle de Madrid por la mañana y aprende a ordenar la escena "
    "con marcadores espaciales y a formular hipótesis prudentes con el condicional."
)
DESCRIPTION_OUTRO = (
    "Vuelve a ver el video y describe la imagen con tus propias palabras. "
    "Después, organiza tres detalles con en primer plano, a su derecha y de fondo, "
    "y formula una hipótesis con podría tratarse de."
)
KOREAN_TEASER = (
    "한국어 티저: 마드리드 아침 거리 장면을 보며 위치 표현과 "
    "podría tratarse de 같은 조심스러운 가설 표현을 B2 말하기 흐름으로 연습합니다."
)
EXTRA_TAGS = [
    "Madrid",
    "escena callejera",
    "metro Madrid",
    "café terraza",
    "marcadores de orden",
    "condicional hipótesis",
    "B2 vocabulario urbano",
]
EXTRA_HASHTAGS = ["#Madrid", "#españolurbano"]
CHAPTERS = [
    {"segment": 1, "title": "Vocabulario urbano"},
    {"segment": 3, "title": "El centro de Madrid"},
    {"segment": 6, "title": "La mujer en primer plano"},
    {"segment": 10, "title": "Ropa y detalles"},
    {"segment": 12, "title": "A su derecha: el metro"},
    {"segment": 14, "title": "La terraza y el ciclista"},
    {"segment": 16, "title": "Los edificios al fondo"},
    {"segment": 20, "title": "Cierre y repaso (orden e hipótesis)"},
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
        "text": "Antes de empezar, observa la escena: una calle madrileña, una entrada de metro, una terraza y gente que empieza el día.",
        "frame": {"x": 0, "y": 0, "w": 1280, "h": 720},
        "zoom": {"start": 1.00, "end": 1.00},
    },
    {
        "text": "Fíjate en cómo ordenamos la imagen: en primer plano, a su derecha, más allá y de fondo.",
        "frame": {"x": 0, "y": 0, "w": 1280, "h": 720},
        "zoom": {"start": 1.00, "end": 1.03},
    },
    {
        "text": "La escena se desarrolla en una mañana luminosa de primavera, en pleno centro de Madrid —",
        "frame": {"x": 0, "y": 0, "w": 1280, "h": 720},
        "zoom": {"start": 1.00, "end": 1.03},
    },
    {
        "text": "quizás en una de las grandes avenidas como la Gran Vía o el Paseo del Prado.",
        "frame": {"x": 360, "y": 0, "w": 920, "h": 518},
        "zoom": {"start": 1.00, "end": 1.04},
    },
    {
        "text": "La luz dorada que se filtra entre los árboles sugiere que es temprano, alrededor de las nueve,",
        "frame": {"x": 0, "y": 0, "w": 900, "h": 506},
        "zoom": {"start": 1.00, "end": 1.04},
    },
    {
        "text": "cuando la ciudad ya está despierta pero todavía conserva una calma agradable.",
        "frame": {"x": 380, "y": 0, "w": 900, "h": 506},
        "zoom": {"start": 1.04, "end": 1.00},
    },
    {
        "text": "En primer plano, una mujer joven camina con paso decidido por la acera.",
        "frame": {"x": 205, "y": 45, "w": 620, "h": 349},
        "zoom": {"start": 1.00, "end": 1.05},
    },
    {
        "text": "Tiene el pelo largo y castaño, lleva pendientes dorados pequeños y una sonrisa sutil.",
        "frame": {"x": 230, "y": 20, "w": 540, "h": 304},
        "zoom": {"start": 1.00, "end": 1.05},
    },
    {
        "text": "Su mirada está dirigida hacia un lado, como si estuviera observando algo que le ha llamado la atención —",
        "frame": {"x": 200, "y": 20, "w": 620, "h": 349},
        "zoom": {"start": 1.05, "end": 1.00},
    },
    {
        "text": "tal vez un escaparate, tal vez a alguien conocido.",
        "frame": {"x": 630, "y": 105, "w": 650, "h": 366},
        "zoom": {"start": 1.00, "end": 1.04},
    },
    {
        "text": "Lleva una gabardina beige sobre una blusa blanca y pantalones negros, un look que combina elegancia urbana y comodidad.",
        "frame": {"x": 230, "y": 185, "w": 620, "h": 349},
        "zoom": {"start": 1.00, "end": 1.05},
    },
    {
        "text": "En el hombro lleva un bolso de tipo tote negro,",
        "frame": {"x": 165, "y": 190, "w": 540, "h": 304},
        "zoom": {"start": 1.00, "end": 1.05},
    },
    {
        "text": "y en la mano sostiene una botella de acero inoxidable, probablemente para mantenerse hidratada durante el día.",
        "frame": {"x": 250, "y": 280, "w": 600, "h": 338},
        "zoom": {"start": 1.00, "end": 1.05},
    },
    {
        "text": "A su derecha se ve la entrada al metro, con sus típicas escaleras descendentes y barandillas de cristal.",
        "frame": {"x": 565, "y": 215, "w": 600, "h": 338},
        "zoom": {"start": 1.00, "end": 1.05},
    },
    {
        "text": "Más allá, una terraza llena de gente desayunando bajo sombrillas blancas,",
        "frame": {"x": 790, "y": 125, "w": 490, "h": 276},
        "zoom": {"start": 1.00, "end": 1.05},
    },
    {
        "text": "tomando un cafecito antes de empezar la jornada.",
        "frame": {"x": 775, "y": 170, "w": 505, "h": 284},
        "zoom": {"start": 1.05, "end": 1.00},
    },
    {
        "text": "Por la calle pasa un ciclista con una camiseta verde y una mochila, moviéndose por el carril bici recién pintado.",
        "frame": {"x": 800, "y": 165, "w": 480, "h": 270},
        "zoom": {"start": 1.00, "end": 1.05},
    },
    {
        "text": "De fondo se alzan los edificios señoriales típicos del centro madrileño —",
        "frame": {"x": 360, "y": 0, "w": 920, "h": 518},
        "zoom": {"start": 1.00, "end": 1.04},
    },
    {
        "text": "fachadas color crema con balcones de hierro forjado y ventanales altos.",
        "frame": {"x": 475, "y": 0, "w": 805, "h": 453},
        "zoom": {"start": 1.04, "end": 1.00},
    },
    {
        "text": "Estos edificios fueron construidos hace más de un siglo, pero siguen siendo el corazón vibrante de la ciudad.",
        "frame": {"x": 430, "y": 0, "w": 850, "h": 478},
        "zoom": {"start": 1.00, "end": 1.04},
    },
    {
        "text": "Es una imagen que captura perfectamente el ritmo de Madrid:",
        "frame": {"x": 0, "y": 0, "w": 1280, "h": 720},
        "zoom": {"start": 1.00, "end": 1.03},
    },
    {
        "text": "una ciudad que se mueve, pero sin prisa;",
        "frame": {"x": 520, "y": 145, "w": 760, "h": 428},
        "zoom": {"start": 1.00, "end": 1.04},
    },
    {
        "text": "donde la gente camina por la calle no solo para llegar a algún sitio, sino para disfrutar del trayecto.",
        "frame": {"x": 0, "y": 120, "w": 780, "h": 439},
        "zoom": {"start": 1.04, "end": 1.00},
    },
    {
        "text": "Recuerda: los marcadores espaciales ayudan a guiar la mirada: en primer plano, a su derecha, más allá y de fondo.",
        "frame": {"x": 0, "y": 0, "w": 1280, "h": 720},
        "zoom": {"start": 1.00, "end": 1.02},
    },
    {
        "text": "Y el condicional sirve para una hipótesis prudente: podría tratarse de una mañana laboral en el centro de Madrid.",
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
