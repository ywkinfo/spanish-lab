"""DRAFT v2 (diary format) -- historia-a1 Ep.2: "Las llaves en el café".

Comprehensible-input mini-historia (SERIES "historia-a1"). v2 diary format
adds STORY_SCENES with per-scene lines, ambient SFX slots, and pause timings.

STATUS: approved
"""

from __future__ import annotations

IMAGE_PATH = ""
DESCRIP_PATH = "historia-a1-ep02-llaves-cafe/descrip.md"
OUTPUT_NAME = "historia-a1-ep02-llaves-cafe"
PUBLIC_SLUG = "historia-a1-ep02-llaves-cafe"
YOUTUBE_URL = ""
SERIES = "historia-a1"
SERIES_TITLE = "Español A1 -- Mini-historias"
EPISODE = 2
LEVEL = "A1"
LANGUAGE = "es"
RENDER_VERSION = 1
RENDER_TYPE = "diary"
THUMBNAIL_PATH = None
YOUTUBE_TITLE = "Las llaves en el café 🔑 카페에 두고 온 열쇠 | Español A1 · Historia Ep.2"
DESCRIPTION_INTRO = (
    "Sigue otro día de Lucía en Madrid en español A1. Después de la clase de español, "
    "Lucía va a un café, pero pierde sus llaves. Una historia sencilla con verbos clave "
    "como tener y perder."
)
DESCRIPTION_OUTRO = (
    "Intenta contar la historia de Lucía usando primero, luego, después y al final. "
    "¿Dónde perdió las llaves? Practica en voz alta."
)
KOREAN_TEASER = (
    "루시아가 수업 후 카페에서 열쇠를 잃어버리고 다시 찾는 이야기입니다. "
    "Tener(가지다), Perder(잃어버리다), Buscar(찾다) 등의 중요한 동사 표현을 익혀봅니다."
)

BASE_TAGS = [
    "스페인어",
    "스페인어 입문",
    "스페인어 A1",
]
EXTRA_TAGS = [
    "스페인어 이야기",
    "스페인어 듣기 연습",
    "루시아의 일기",
]
BASE_HASHTAGS = ["#EspañolA1", "#스페인어"]
EXTRA_HASHTAGS = ["#스페인어이야기", "#루시아의일기"]

MINI_QUIZ = [
    ("¿Cómo dices '열쇠'?", "Las llaves"),
    ("¿Cómo dices '카페'?", "El café"),
    ("¿Cómo dices '잃어버리다'?", "Perder"),
    ("¿Cómo dices '찾다'?", "Buscar"),
    ("¿Cómo dices '안심하다/차분하다'?", "Tranquila"),
]

DESIGN = {
    "output_size": (1920, 1080),
    "font_path": "assets/fonts/NotoSansKR-Bold.ttf",
    "font_index": 0,
    "font_path_ko": "assets/fonts/NotoSansKR-Regular.ttf",
    "font_index_ko": 0,
    "font_size_title": 82,
    "font_size_es": 84,
    "min_font_size_es": 52,
    "font_size_ko": 36,
    "font_size_example": 34,
    "background_color": (248, 247, 242),
    "text_color": (31, 35, 40),
    "muted_text_color": (96, 101, 109),
    "intro_title": "Las llaves en el café",
    "intro_subtitle": "Español A1 · Historia Ep.2",
    "intro_ko": "루시아가 카페에 열쇠를 두고 온 날",
    "thumbnail_title": "Las llaves en el café",
    "thumbnail_subtitle": "Español A1 · Historia",
    "thumbnail_ko": "Tener · Perder · Buscar",
    "outro_ko": "다음 이야기에서 또 만나요",
    "color_blocks": {
        "coral": (224, 91, 76),
        "amber": (230, 158, 62),
        "teal": (44, 150, 142),
        "blue": (70, 120, 196),
        "green": (92, 148, 86),
        "neutral": (42, 48, 57),
    },
}

STORY_SCENES = [
    {
        "scene_id": 1,
        "title_es": "Después de la clase",
        "title_ko": "수업이 끝난 후",
        "image_path": "assets/images/historia_a1_ep02_llaves_cafe/scene_01_cafe_exterior.png",
        "ambient_sfx": "assets/audio/sfx/madrid_street_soft.wav",
        "ambient_sfx_license": "CC0",
        "ambient_sfx_volume_db": -13.1,
        "pause_s": 3.0,
        "lines": [
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Es martes por la tarde en Madrid.",
                "text_ko": "마드리드의 화요일 오후입니다.",
                "duration_s": 7.0,
            },
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Lucía sale de su clase de español.",
                "text_ko": "루시아는 스페인어 수업을 마치고 나옵니다.",
                "duration_s": 7.5,
            },
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Tiene una mochila azul y un cuaderno pequeño.",
                "text_ko": "그녀는 파란 배낭과 작은 공책을 가지고 있습니다.",
                "duration_s": 8.5,
            },
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "También tiene sus llaves en el bolsillo.",
                "text_ko": "또한 주머니에 열쇠도 가지고 있습니다.",
                "duration_s": 8.0,
            },
            {
                "kind": "dialogue",
                "speaker": "Lucía",
                "text_es": "Tengo un poco de hambre.",
                "text_ko": "나는 조금 배가 고파.",
                "duration_s": 7.0,
            },
            {
                "kind": "dialogue",
                "speaker": "Lucía",
                "text_es": "Voy a tomar un café y un bocadillo.",
                "text_ko": "커피와 작은 샌드위치를 먹으러 갈 거야.",
                "duration_s": 8.5,
            },
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Entra en un café pequeño cerca de la escuela.",
                "text_ko": "그녀는 학교 근처의 작은 카페에 들어갑니다.",
                "duration_s": 8.5,
            },
        ],
    },
    {
        "scene_id": 2,
        "title_es": "Una mesa junto a la ventana",
        "title_ko": "창가 자리",
        "image_path": "assets/images/historia_a1_ep02_llaves_cafe/scene_02_window_table.png",
        "ambient_sfx": "assets/audio/sfx/cafe_ambience_soft_2.wav",
        "ambient_sfx_license": "CC0",
        "ambient_sfx_volume_db": -12.0,
        "pause_s": 3.0,
        "lines": [
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "El café es tranquilo and bonito.",
                "text_es": "El café es tranquilo y bonito.",
                "text_ko": "카페는 조용하고 예쁩니다.",
                "duration_s": 7.0,
            },
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Hay tres mesas y muchas plantas.",
                "text_ko": "테이블이 세 개 있고 식물이 많습니다.",
                "duration_s": 7.5,
            },
            {
                "kind": "dialogue",
                "speaker": "Camarero",
                "text_es": "Hola, buenas tardes. ¿Qué quieres tomar?",
                "text_ko": "안녕하세요, 좋은 오후예요. 무엇을 드시겠어요?",
                "duration_s": 9.0,
            },
            {
                "kind": "dialogue",
                "speaker": "Lucía",
                "text_es": "Quiero un café con leche y un bocadillo, por favor.",
                "text_ko": "카페 콘 레체 하나와 작은 샌드위치 하나 주세요.",
                "duration_s": 10.0,
            },
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Lucía se sienta junto a la ventana.",
                "text_ko": "루시아는 창가에 앉습니다.",
                "duration_s": 7.5,
            },
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Pone el cuaderno sobre la mesa.",
                "text_ko": "그녀는 공책을 테이블 위에 놓습니다.",
                "duration_s": 7.0,
            },
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "También pone sus llaves al lado del vaso.",
                "text_ko": "그녀는 열쇠도 컵 옆에 놓습니다.",
                "duration_s": 8.5,
            },
        ],
    },
    {
        "scene_id": 3,
        "title_es": "Un mensaje de Diego",
        "title_ko": "디에고의 메시지",
        "image_path": "assets/images/historia_a1_ep02_llaves_cafe/scene_03_phone_message.png",
        "ambient_sfx": "assets/audio/sfx/cafe_ambience_soft_3.wav",
        "ambient_sfx_license": "CC0",
        "ambient_sfx_volume_db": -12.4,
        "pause_s": 3.5,
        "lines": [
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Lucía toma su café lentamente.",
                "text_ko": "루시아는 천천히 커피를 마십니다.",
                "duration_s": 7.5,
            },
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Mira por la ventana y escribe dos frases.",
                "text_ko": "그녀는 창밖을 보고 두 문장을 씁니다.",
                "duration_s": 8.5,
            },
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "De repente, su teléfono hace un sonido.",
                "text_ko": "갑자기 그녀의 휴대폰에서 소리가 납니다.",
                "duration_s": 8.0,
            },
            {
                "kind": "dialogue",
                "speaker": "Diego",
                "text_es": "Lucía, ¿tienes tiempo ahora?",
                "text_ko": "루시아, 지금 시간 있어?",
                "duration_s": 7.5,
            },
            {
                "kind": "dialogue",
                "speaker": "Lucía",
                "text_es": "Sí, tengo diez minutos.",
                "text_ko": "응, 나 10분 있어.",
                "duration_s": 7.0,
            },
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Lucía guarda el teléfono en la mochila.",
                "text_ko": "루시아는 휴대폰을 배낭에 넣습니다.",
                "duration_s": 8.0,
            },
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Pero las llaves todavía están en la mesa.",
                "text_ko": "하지만 열쇠는 아직 테이블 위에 있습니다.",
                "duration_s": 8.5,
            },
        ],
    },
    {
        "scene_id": 4,
        "title_es": "La puerta de casa",
        "title_ko": "집 문 앞",
        "image_path": "assets/images/historia_a1_ep02_llaves_cafe/scene_04_apartment_door.png",
        "ambient_sfx": "assets/audio/sfx/apartment_hall_soft_4.wav",
        "ambient_sfx_license": "CC0",
        "ambient_sfx_volume_db": -14.0,
        "pause_s": 4.0,
        "lines": [
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Después del café, Lucía vuelve a casa.",
                "text_ko": "카페 후에 루시아는 집으로 돌아갑니다.",
                "duration_s": 8.0,
            },
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Sube las escaleras despacio.",
                "text_ko": "그녀는 천천히 계단을 올라갑니다.",
                "duration_s": 7.0,
            },
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Está delante de la puerta.",
                "text_ko": "그녀는 문 앞에 있습니다.",
                "duration_s": 6.5,
            },
            {
                "kind": "dialogue",
                "speaker": "Lucía",
                "text_es": "Bien, ahora necesito mis llaves.",
                "text_ko": "좋아, 이제 내 열쇠가 필요해.",
                "duration_s": 8.0,
            },
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Busca en el bolsillo derecho.",
                "text_ko": "그녀는 오른쪽 주머니를 찾습니다.",
                "duration_s": 7.0,
            },
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Busca en el bolsillo izquierdo.",
                "text_ko": "그녀는 왼쪽 주머니를 찾습니다.",
                "duration_s": 7.0,
            },
            {
                "kind": "dialogue",
                "speaker": "Lucía",
                "text_es": "No tengo mis llaves.",
                "text_ko": "내 열쇠가 없어.",
                "duration_s": 7.0,
            },
            {
                "kind": "dialogue",
                "speaker": "Lucía",
                "text_es": "¿Dónde están?",
                "text_ko": "어디에 있지?",
                "duration_s": 6.0,
            },
        ],
    },
    {
        "scene_id": 5,
        "title_es": "Buscar con calma",
        "title_ko": "차분히 찾기",
        "image_path": "assets/images/historia_a1_ep02_llaves_cafe/scene_05_search_bag.png",
        "ambient_sfx": "assets/audio/sfx/apartment_hall_soft_5.wav",
        "ambient_sfx_license": "CC0",
        "ambient_sfx_volume_db": -14.9,
        "pause_s": 4.0,
        "lines": [
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Lucía respira y se sienta un momento.",
                "text_ko": "루시아는 숨을 쉬고 잠시 앉습니다.",
                "duration_s": 8.5,
            },
            {
                "kind": "dialogue",
                "speaker": "Lucía",
                "text_es": "Tranquila, Lucía. Busca con calma.",
                "text_ko": "차분히 하자, 루시아. 천천히 찾아.",
                "duration_s": 8.5,
            },
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Abre la mochila azul.",
                "text_ko": "그녀는 파란 배낭을 엽니다.",
                "duration_s": 6.5,
            },
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Hay un cuaderno, un lápiz y un teléfono.",
                "text_ko": "공책, 연필, 휴대폰이 있습니다.",
                "duration_s": 8.5,
            },
            {
                "kind": "dialogue",
                "speaker": "Lucía",
                "text_es": "Tengo mi cuaderno.",
                "text_ko": "내 공책은 있어.",
                "duration_s": 6.5,
            },
            {
                "kind": "dialogue",
                "speaker": "Lucía",
                "text_es": "Tengo mi teléfono.",
                "text_ko": "내 휴대폰도 있어.",
                "duration_s": 6.5,
            },
            {
                "kind": "dialogue",
                "speaker": "Lucía",
                "text_es": "Pero no tengo las llaves.",
                "text_ko": "하지만 열쇠가 없어.",
                "duration_s": 7.0,
            },
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Entonces recuerda el café.",
                "text_ko": "그때 그녀는 카페를 떠올립니다.",
                "duration_s": 7.0,
            },
        ],
    },
    {
        "scene_id": 6,
        "title_es": "Volver al café",
        "title_ko": "카페로 돌아가기",
        "image_path": "assets/images/historia_a1_ep02_llaves_cafe/scene_06_return_to_cafe.png",
        "ambient_sfx": "assets/audio/sfx/madrid_street_evening_soft.wav",
        "ambient_sfx_license": "CC0",
        "ambient_sfx_volume_db": -12.8,
        "pause_s": 3.0,
        "lines": [
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Lucía baja las escaleras rápidamente.",
                "text_ko": "루시아는 빠르게 계단을 내려갑니다.",
                "duration_s": 7.5,
            },
            {
                "kind": "dialogue",
                "speaker": "Lucía",
                "text_es": "Creo que pierdo las llaves en el café.",
                "text_ko": "나는 카페에서 열쇠를 잃어버린 것 같아.",
                "duration_s": 9.0,
            },
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Camina por la calle pequeña.",
                "text_ko": "그녀는 작은 거리를 걸어갑니다.",
                "duration_s": 7.0,
            },
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Mira el suelo, las mesas y las puertas.",
                "text_ko": "그녀는 바닥, 테이블들, 문들을 봅니다.",
                "duration_s": 8.5,
            },
            {
                "kind": "dialogue",
                "speaker": "Lucía",
                "text_es": "Las llaves son pequeñas.",
                "text_ko": "열쇠는 작아.",
                "duration_s": 6.5,
            },
            {
                "kind": "dialogue",
                "speaker": "Lucía",
                "text_es": "Pero tienen una cinta roja.",
                "text_ko": "하지만 빨간 끈이 있어.",
                "duration_s": 7.0,
            },
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Por fin, llega otra vez al café.",
                "text_ko": "마침내 그녀는 다시 카페에 도착합니다.",
                "duration_s": 7.5,
            },
        ],
    },
    {
        "scene_id": 7,
        "title_es": "Las llaves están aquí",
        "title_ko": "열쇠는 여기 있어요",
        "image_path": "assets/images/historia_a1_ep02_llaves_cafe/scene_07_keys_found.png",
        "ambient_sfx": "assets/audio/sfx/cafe_ambience_soft_7.wav",
        "ambient_sfx_license": "CC0",
        "ambient_sfx_volume_db": -12.4,
        "pause_s": 3.5,
        "lines": [
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Lucía entra en el café.",
                "text_ko": "루시아는 카페에 들어갑니다.",
                "duration_s": 6.5,
            },
            {
                "kind": "dialogue",
                "speaker": "Camarero",
                "text_es": "Hola otra vez. ¿Todo bien?",
                "text_ko": "다시 안녕하세요. 괜찮으세요?",
                "duration_s": 7.5,
            },
            {
                "kind": "dialogue",
                "speaker": "Lucía",
                "text_es": "Perdón. Busco mis llaves.",
                "text_ko": "죄송해요. 제 열쇠를 찾고 있어요.",
                "duration_s": 7.5,
            },
            {
                "kind": "dialogue",
                "speaker": "Lucía",
                "text_es": "Son pequeñas y tienen una cinta roja.",
                "text_ko": "작고 빨간 끈이 있어요.",
                "duration_s": 8.5,
            },
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "El camarero sonríe y mira detrás del mostrador.",
                "text_ko": "직원은 웃고 카운터 뒤를 봅니다.",
                "duration_s": 9.0,
            },
            {
                "kind": "dialogue",
                "speaker": "Camarero",
                "text_es": "Sí, aquí están tus llaves.",
                "text_ko": "네, 여기 당신의 열쇠가 있어요.",
                "duration_s": 7.5,
            },
            {
                "kind": "dialogue",
                "speaker": "Lucía",
                "text_es": "¡Muchas gracias! Ahora estoy tranquila.",
                "text_ko": "정말 감사합니다! 이제 안심돼요.",
                "duration_s": 8.5,
            },
        ],
    },
    {
        "scene_id": 8,
        "title_es": "Diario de Lucía",
        "title_ko": "루시아의 일기",
        "image_path": "assets/images/historia_a1_ep02_llaves_cafe/scene_08_diary_night.png",
        "ambient_sfx": "assets/audio/sfx/quiet_room_night.wav",
        "ambient_sfx_license": "CC0",
        "ambient_sfx_volume_db": -14.9,
        "pause_s": 5.0,
        "lines": [
            {
                "kind": "narration",
                "speaker": "",
                "text_es": "Por la noche, Lucía escribe en su diario.",
                "text_ko": "밤에 루시아는 일기에 씁니다.",
                "duration_s": 8.0,
            },
            {
                "kind": "dialogue",
                "speaker": "Lucía",
                "text_es": "Hoy he tenido una tarde pequeña, pero importante.",
                "text_ko": "오늘 나는 작지만 중요한 오후를 보냈다.",
                "duration_s": 9.5,
            },
            {
                "kind": "dialogue",
                "speaker": "Lucía",
                "text_es": "Primero, he ido a un café después de clase.",
                "text_ko": "먼저, 나는 수업 후에 카페에 갔다.",
                "duration_s": 9.0,
            },
            {
                "kind": "dialogue",
                "speaker": "Lucía",
                "text_es": "Después, he perdido mis llaves.",
                "text_ko": "그 후, 나는 내 열쇠를 잃어버렸다.",
                "duration_s": 7.5,
            },
            {
                "kind": "dialogue",
                "speaker": "Lucía",
                "text_es": "Luego, he vuelto al café.",
                "text_ko": "그다음, 나는 카페로 돌아갔다.",
                "duration_s": 7.0,
            },
            {
                "kind": "dialogue",
                "speaker": "Lucía",
                "text_es": "Al final, el camarero me ha ayudado.",
                "text_ko": "마지막에, 카페 직원이 나를 도와주었다.",
                "duration_s": 8.0,
            },
            {
                "kind": "dialogue",
                "speaker": "Lucía",
                "text_es": "Ahora tengo mis llaves and estoy en casa.",
                "text_es": "Ahora tengo mis llaves y estoy en casa.",
                "text_ko": "이제 나는 내 열쇠를 가지고 있고 집에 있다.",
                "duration_s": 8.5,
            },
            {
                "kind": "dialogue",
                "speaker": "Lucía",
                "text_es": "Mañana voy a mirar la mesa antes de salir.",
                "text_ko": "내일은 나가기 전에 테이블을 볼 것이다.",
                "duration_s": 9.0,
            },
        ],
    },
]

SFX_MANIFEST = [
    {
        "id": "cafe_door_bell_01",
        "kind": "spot",
        "scene_id": 1,
        "line_index": 7,
        "offset_s": 0.2,
        "path": "assets/audio/sfx/door_bell_soft_1.wav",
        "volume_db": -9.1,
        "license": "CC0",
    },
    {
        "id": "cup_on_table_01",
        "kind": "spot",
        "scene_id": 2,
        "line_index": 5,
        "offset_s": 1.2,
        "path": "assets/audio/sfx/cup_place_soft.wav",
        "volume_db": -11.0,
        "license": "CC0",
    },
    {
        "id": "key_jingle_01",
        "kind": "spot",
        "scene_id": 2,
        "line_index": 7,
        "offset_s": 0.4,
        "path": "assets/audio/sfx/key_jingle_soft_1.wav",
        "volume_db": -9.4,
        "license": "CC0",
    },
    {
        "id": "phone_message_01",
        "kind": "spot",
        "scene_id": 3,
        "line_index": 3,
        "offset_s": 0.8,
        "path": "assets/audio/sfx/phone_notification_soft.wav",
        "volume_db": -10.5,
        "license": "CC0",
    },
    {
        "id": "bag_zip_01",
        "kind": "spot",
        "scene_id": 3,
        "line_index": 6,
        "offset_s": 0.6,
        "path": "assets/audio/sfx/bag_zip_soft.wav",
        "volume_db": -11.7,
        "license": "CC0",
    },
    {
        "id": "door_handle_01",
        "kind": "spot",
        "scene_id": 4,
        "line_index": 4,
        "offset_s": 1.0,
        "path": "assets/audio/sfx/door_handle_soft.wav",
        "volume_db": -10.5,
        "license": "CC0",
    },
    {
        "id": "pocket_search_01",
        "kind": "spot",
        "scene_id": 4,
        "line_index": 5,
        "offset_s": 0.4,
        "path": "assets/audio/sfx/clothes_rustle_soft_1.wav",
        "volume_db": -12.4,
        "license": "CC0",
    },
    {
        "id": "pocket_search_02",
        "kind": "spot",
        "scene_id": 4,
        "line_index": 6,
        "offset_s": 0.4,
        "path": "assets/audio/sfx/clothes_rustle_soft_2.wav",
        "volume_db": -12.4,
        "license": "CC0",
    },
    {
        "id": "bag_open_01",
        "kind": "spot",
        "scene_id": 5,
        "line_index": 3,
        "offset_s": 0.5,
        "path": "assets/audio/sfx/bag_open_soft.wav",
        "volume_db": -11.0,
        "license": "CC0",
    },
    {
        "id": "fast_steps_01",
        "kind": "spot",
        "scene_id": 6,
        "line_index": 1,
        "offset_s": 0.3,
        "path": "assets/audio/sfx/footsteps_fast_soft.wav",
        "volume_db": -11.4,
        "license": "CC0",
    },
    {
        "id": "cafe_door_bell_02",
        "kind": "spot",
        "scene_id": 7,
        "line_index": 1,
        "offset_s": 0.4,
        "path": "assets/audio/sfx/door_bell_soft_2.wav",
        "volume_db": -9.4,
        "license": "CC0",
    },
    {
        "id": "key_jingle_02",
        "kind": "spot",
        "scene_id": 7,
        "line_index": 6,
        "offset_s": 0.6,
        "path": "assets/audio/sfx/key_jingle_soft_2.wav",
        "volume_db": -8.9,
        "license": "CC0",
    },
    {
        "id": "pen_write_01",
        "kind": "spot",
        "scene_id": 8,
        "line_index": 1,
        "offset_s": 0.8,
        "path": "assets/audio/sfx/pen_writing_soft.wav",
        "volume_db": -13.1,
        "license": "CC0",
    },
]

SEGMENT_SFX = [
    {
        "id": "intro_sfx",
        "kind": "segment",
        "segment_type": "intro",
        "mode": "bed",
        "offset_s": 0.0,
        "path": "assets/audio/sfx/soft_page_open.wav",
        "volume_db": -11.0,
        "license": "CC0",
    },
    {
        "id": "montage_sfx",
        "kind": "segment",
        "segment_type": "montage",
        "mode": "bed",
        "offset_s": 0.0,
        "path": "assets/audio/sfx/light_city_montage.wav",
        "volume_db": -14.9,
        "license": "CC0",
    },
    {
        "id": "outro_sfx",
        "kind": "segment",
        "segment_type": "outro",
        "mode": "bed",
        "offset_s": 0.0,
        "path": "assets/audio/sfx/soft_notebook_close.wav",
        "volume_db": -11.0,
        "license": "CC0",
    },
]

def _build_diary_segments() -> list[dict]:
    """Generate SEGMENTS from STORY_SCENES for the diary render pipeline."""
    segments: list[dict] = [
        {
            "type": "intro",
            "text_es": (
                "Hoy seguimos otro día de Lucía en Madrid. Lucía toma un café y pierde sus llaves. "
                "Vas a escuchar palabras que ya conoces: las llaves, el camarero, el vaso y la mochila. "
                "Fíjate en los verbos tener y perder."
            ),
            "duration_s": 16.0,
        }
    ]
    for scene in STORY_SCENES:
        # Scene header
        segments.append(
            {
                "type": "scene_header",
                "scene_id": scene["scene_id"],
                "title_es": scene["title_es"],
                "title_ko": scene["title_ko"],
                "duration_s": 3.0,
            }
        )
        # Lines
        for line in scene["lines"]:
            resolved_img = line.get("image_path") or scene.get("image_path", "")
            seg = {
                "type": "diary_line",
                "scene_id": scene["scene_id"],
                "kind": line["kind"],
                "speaker": line["speaker"],
                "text_es": line["text_es"],
                "text_ko": line["text_ko"],
                "image_path": resolved_img,
            }
            if "duration_s" in line:
                seg["duration_s"] = line["duration_s"]
            if "min_hold_s" in line:
                seg["min_hold_s"] = line["min_hold_s"]
            if "processing_pause_s" in line:
                seg["processing_pause_s"] = line["processing_pause_s"]
            segments.append(seg)
        # Pause after scene
        last_line_img = scene["lines"][-1].get("image_path") or scene.get("image_path", "") if scene["lines"] else scene.get("image_path", "")
        segments.append(
            {
                "type": "pause",
                "scene_id": scene["scene_id"],
                "duration_s": scene["pause_s"],
                "image_path": last_line_img,
            }
        )
    # Montage
    segments.append(
        {
            "type": "montage",
            "duration_s": 6.0,
        }
    )
    # Outro
    segments.append(
        {
            "type": "outro",
            "text_es": (
                "Muy bien. Ahora intenta contar la historia de Lucía usando primero, luego, "
                "después y al final. ¿Dónde perdió las llaves? Practica en voz alta."
            ),
            "duration_s": 15.0,
        }
    )
    return segments

SEGMENTS = _build_diary_segments()

def _find_chapter_segment(scene_id: int) -> int:
    for idx, seg in enumerate(SEGMENTS):
        if seg.get("type") == "scene_header" and seg.get("scene_id") == scene_id:
            return idx + 1
    raise ValueError(f"missing scene_header for scene_id={scene_id}")

CHAPTERS = [
    {"segment": 1, "title": "Introducción"},
    {"segment": _find_chapter_segment(1), "title": "Después de la clase"},
    {"segment": _find_chapter_segment(2), "title": "Una mesa junto a la ventana"},
    {"segment": _find_chapter_segment(3), "title": "Un mensaje de Diego"},
    {"segment": _find_chapter_segment(4), "title": "La puerta de casa"},
    {"segment": _find_chapter_segment(5), "title": "Buscar con calma"},
    {"segment": _find_chapter_segment(6), "title": "Volver al café"},
    {"segment": _find_chapter_segment(7), "title": "Las llaves están aquí"},
    {"segment": _find_chapter_segment(8), "title": "Diario de Lucía"},
    {"segment": len(SEGMENTS), "title": "Repaso final"},
]

AUDIO = {
    "tts_engine": "edge",
    "edge_voice": "es-ES-ElviraNeural",
    "edge_rate": "+8%",
    "edge_pitch": "+0Hz",
    "edge_volume": "+0%",
    "voice": "es-ES-ElviraNeural",
    "rate_wpm": 160,
    "lead_padding_s": 0.25,
    "tail_padding_s": 0.4,
    "min_duration_s": 3.0,
    "readability_floor_ratio": 0.0,
    "processing_pause_s": 2.5,
    "min_hold_s": 2.5,
    "ambient_bed_db": -11.9,
    "bgm_path": "assets/audio/fur_elise_inspired_soft_piano.wav",
    "bgm_volume_db": 6.0,
    "narration_volume_db": 0.0,
    "ducking": True,
    "ducking_threshold": 0.05,
    "ducking_ratio": 4,
    "ducking_attack_ms": 80,
    "ducking_release_ms": 550,
    "fade_in_s": 4.0,
    "fade_out_s": 5.0,
    "audio_codec": "aac",
    "audio_bitrate_kbps": 192,
    "sample_rate_hz": 44100,
}
