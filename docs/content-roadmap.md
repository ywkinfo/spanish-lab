# Spanish Lab 콘텐츠 로드맵 (단일 출처 · SoT)

> 이 파일 **하나만** 보면 (1) 무엇을 이미 만들었고, (2) 어떤 상황/분야가 커버됐고,
> (3) 다음에 무엇을 만들지 알 수 있게 하는 것이 목적입니다. 매번 `projects/*.py`,
> `positioning.md`, `content-backlog.md`를 다시 대조하지 마세요(토큰 낭비 + 중복 위험).
>
> - **A 인벤토리**는 `scripts/build_episode_index.py`가 `projects/*.py`의 권위 필드에서
>   자동 생성합니다. 권위 = 각 모듈의 `EPISODE`/`SERIES` 필드(문서·positioning이 아님).
> - **B 커버리지 맵 / C 후보 큐**는 사람이 관리합니다.
> - `docs/benchmark/positioning.md`는 실제 생산과 어긋나 **역사적 벤치마크로 강등**됨.
>   다음 소재의 권위는 아래 **C 큐**입니다.
> - 참고: 컨트롤플레인(`hermes` repo)의 `docs/content-backlog.md`는 **별개 시스템**(Studio A
>   e2e-package)으로, 이 파일과 무관합니다.

## 다음 소재 고르는 법 (저비용 절차)

1. 이 파일만 연다.
2. **C 큐**의 최상단(권장) 후보를 고른다.
3. **A 인벤토리**(아래 자동 표)와 `a1-*/descrip.md`에 핵심 표현을 `grep`해 **중복이 아님**을 재확인한다.
4. 제작한다 (`projects/<module>.py` + `a2-<slug>/` 폴더, Moex 파이프라인, 사람 프리뷰 후 publish).
5. 완료 후 `python3 scripts/build_episode_index.py --write`를 다시 실행하고, C 큐에서 그 행을 지운다.

---

## A. 제작 완료 인벤토리 (자동 생성 — 손으로 고치지 말 것)

아래 `BEGIN:generated`~`END:generated` 구역은 `scripts/build_episode_index.py --write`가 덮어씁니다.
직접 편집하면 다음 실행 때 사라집니다.

<!-- BEGIN:generated -->

### [TODO: SERIES]

| Ep | module | slug | 레벨 | 학습 포인트 (YOUTUBE_TITLE) | URL 상태 |
|---:|---|---|---|---|---|
| 1 | `_template_historia_diary` | `[TODO: PUBLIC_SLUG]` | [TODO: LEVEL] | [TODO: YOUTUBE_TITLE] | URL 미기록 |

### descripcion

| Ep | module | slug | 레벨 | 학습 포인트 (YOUTUBE_TITLE) | URL 상태 |
|---:|---|---|---|---|---|
| 1 | `reunion_madrid` | `` | B2 | Reunión en Madrid \| Descripción de imagen B2 · Ep.1 | URL 미기록 |
| 2 | `mercado` | `` | B2 | En el mercado \| Descripción de imagen B2 · Ep.2 | URL 미기록 |
| 3 | `ave_andalucia` | `` | B2 | En el AVE por Andalucía \| Descripción de imagen B2 · Ep.3 | URL 미기록 |
| 4 | `cocina_mediterranea` | `` | B2 | En la cocina mediterránea \| Descripción de imagen B2 · Ep.4 | URL 미기록 |
| 5 | `panaderia_pueblo` | `` | B2 | Charla en la panadería \| Descripción de imagen B2 · Ep.5 | URL 미기록 |
| 6 | `madrid_callejera` | `` | B2 | Por una calle de Madrid \| Descripción de imagen B2 · Ep.6 | URL 미기록 |

### frases-a1

| Ep | module | slug | 레벨 | 학습 포인트 (YOUTUBE_TITLE) | URL 상태 |
|---:|---|---|---|---|---|
| 0 | `greetings_50_phrases_a1` | `a1-greetings-50-phrases` | A1 | 스페인어 인사 50문장 \| 처음 만남부터 헤어질 때까지 A1 반복 듣기 | URL 미기록 |
| 0 | `presentarse_50_phrases_a1` | `a1-presentarse-50-phrases` | A1 | 스페인어 자기소개 50문장 \| A1 레벨 인사와 소개 연습 | URL 미기록 |
| 1 | `frases_a1_50_utiles` | `a1-50-frases-utiles` | A1 | 50 frases útiles para hablar español desde hoy \| Español A1 · Ep.1 | 발행(2WrERE9LOyE) |
| 2 | `primer_encuentro_a1` | `a1-primer-encuentro` | A1 | Frases útiles para un primer encuentro en español \| Español A1 · Ep.2 | 발행(tkNs4tJunaU) |
| 2 | `primer_encuentro_remake_a1` | `a1-primer-encuentro-remake` | A1 | ¿Cómo te llamas? 이름 묻고 답하기 \| Español A1 · Ep.2 remake | URL 미기록 |
| 3 | `como_estas_a1` | `a1-como-estas` | A1 | ¿Cómo estás? 피곤해요, 괜찮아요 말하기 \| Español A1 · Ep.3 | URL 미기록 |
| 4 | `tengo_hambre_a1` | `a1-tengo-hambre` | A1 | Tengo hambre 배고파요, 물 주세요 말하기 \| Español A1 · Ep.4 | URL 미기록 |
| 5 | `cafeteria_a1` | `a1-cafeteria` | A1 | Un café, por favor ☕ 주문하고 계산하기 \| Español A1 · Ep.5 | URL 미기록 |
| 6 | `cuanto_cuesta_a1` | `a1-cuanto-cuesta` | A1 | ¿Cuánto cuesta? 얼마예요? 가격 묻고 계산하기 \| Español A1 · Ep.6 | URL 미기록 |
| 7 | `lucia_cafe_a1` | `a1-lucia-cafe` | A1 | Lucía está tomando café ☕ 그림 묘사하기 \| Español A1 · Ep.7 | URL 미기록 |
| 8 | `la_cuenta_a1` | `a1-la-cuenta` | A1 | La cuenta, por favor 💶 카페에서 계산하기 \| Español A1 · Ep.8 | URL 미기록 |
| 9 | `donde_esta_el_metro_a1` | `a1-donde-esta-el-metro` | A1 | ¿Dónde está el metro? 🚇 길 묻기 \| Español A1 · Ep.9 | URL 미기록 |
| 10 | `un_billete_por_favor_a1` | `a1-un-billete-por-favor` | A1 | Un billete, por favor 🎫 지하철표 사기 \| Español A1 · Ep.10 | URL 미기록 |
| 11 | `a_que_hora_sale_a1` | `a1-a-que-hora-sale` | A1 | ¿A qué hora sale? 🚆 출발 시간 묻기 \| Español A1 · Ep.11 | URL 미기록 |
| 12 | `que_tal_el_viaje_a1` | `a1-que-tal-el-viaje` | A1 | ¿Qué tal el viaje? 🚆 여행 어땠어? \| Español A1 · Ep.12 | URL 미기록 |
| 13 | `quiero_volver_a1` | `a1-quiero-volver` | A1 | Quiero volver 😊 다시 가고 싶어 \| Español A1 · Ep.13 | URL 미기록 |
| 14 | `voy_a_practicar_a1` | `a1-voy-a-practicar` | A1 | Voy a practicar mañana 📚 내일 연습할 거야 \| Español A1 · Ep.14 | URL 미기록 |
| 15 | `primavera_madrid_a1` | `a1-primavera-madrid` | A1 | ¿Cómo es la primavera en Madrid? 🌸 마드리드의 봄은 어때? \| Español A1 · Ep.15 | URL 미기록 |
| 16 | `que_tiempo_hace_a1` | `a1-que-tiempo-hace` | A1 | ¿Qué tiempo hace? ☀️ 날씨가 어때? \| Español A1 · Ep.16 | URL 미기록 |
| 17 | `que_llevas_a1` | `a1-que-llevas` | A1 | ¿Qué llevas? 🧥 오늘 뭐 입어요? \| Español A1 · Ep.17 | URL 미기록 |
| 18 | `me_gusta_pero_a1` | `a1-me-gusta-pero` | A1+ | Me gusta, pero… 👍 좋아요, 그런데… \| Español A1+ · Ep.18 | URL 미기록 |
| 19 | `prefiero_cafe_a1` | `a1-prefiero-cafe` | A1+ | Prefiero café ☕ 저는 커피가 더 좋아요 \| Español A1+ · Ep.19 | URL 미기록 |
| 20 | `porque_tengo_sueno_a1` | `a1-porque-tengo-sueno` | A1+ | Porque tengo sueño 😴 졸려서요 \| Español A1+ · Ep.20 | URL 미기록 |
| 21 | `a_veces_me_levanto_temprano_a1` | `a1-a-veces-me-levanto-temprano` | A1+ | A veces me levanto temprano 🌅 가끔 일찍 일어나요 \| Español A1+ · Ep.21 | URL 미기록 |
| 22 | `siempre_tomo_cafe_a1` | `a1-siempre-tomo-cafe` | A1+ | Siempre tomo café por la mañana ☕ 항상 커피 마셔요 \| Español A1+ · Ep.22 | URL 미기록 |
| 23 | `nunca_tomo_cafe_a1` | `a1-nunca-tomo-cafe` | A1+ | Nunca tomo café por la noche ☕ 밤에는 커피 안 마셔요 \| Español A1+ · Ep.23 | URL 미기록 |
| 26 | `estoy_en_la_estacion_a1` | `a1-estoy-en-la-estacion` | A1+ | Estoy en la estación 🚉 나 역에 있어요 \| Español A1+ · Ep.26 | URL 미기록 |
| 27 | `hay_una_farmacia_cerca_a1` | `a1-hay-una-farmacia-cerca` | A1+ | Hay una farmacia cerca 💊 근처에 약국이 있어요 \| Español A1+ · Ep.27 | URL 미기록 |
| 28 | `quiero_cafe_para_llevar_a1` | `a1-quiero-cafe-para-llevar` | A1+ | Quiero un café para llevar ☕ 포장해 주세요 \| Español A1+ · Ep.28 | URL 미기록 |
| 29 | `me_lo_llevo_a1` | `a1-me-lo-llevo` | A1+ | Me lo llevo 🛍️ 이걸로 할게요 \| Español A1+ · Ep.29 | URL 미기록 |
| 30 | `tiene_otro_color_a1` | `a1-tiene-otro-color` | A1+ | ¿Tiene otro color? 🛍️ 다른 색 있어요? \| Español A1+ · Ep.30 | URL 미기록 |
| 31 | `mas_despacio_por_favor_a1` | `a1-mas-despacio-por-favor` | A1+ | Más despacio, por favor 🗣️ 천천히 말해주세요 \| Español A1+ · Ep.31 | URL 미기록 |

### frases-a2

| Ep | module | slug | 레벨 | 학습 포인트 (YOUTUBE_TITLE) | URL 상태 |
|---:|---|---|---|---|---|
| 24 | `no_puedo_ir_a2` | `a2-no-puedo-ir` | A2 입문 | No puedo ir porque tengo que trabajar 💻 일해야 해서 못 가요 \| Español A2 · Ep.24 | URL 미기록 |
| 25 | `podemos_quedar_manana_a2` | `a2-podemos-quedar-manana` | A2 입문 | ¿Podemos quedar mañana? ☕ 내일 만날 수 있을까요? \| Español A2 · Ep.25 | URL 미기록 |
| 32 | `restaurante_reserva_a2` | `a2-restaurante-reserva` | A2 입문 | Quiero reservar una mesa 🍽️ 테이블을 예약하고 싶어요 \| Español A2 · Ep.32 | URL 미기록 |
| 33 | `confirmar_reserva_a2` | `a2-confirmar-reserva` | A2 입문 | He reservado la mesa 💬 예약 완료했어 \| Español A2 · Ep.33 | URL 미기록 |
| 34 | `en_el_restaurante_pedir_a2` | `a2-en-el-restaurante-pedir` | A2 입문 | ¿Qué nos recomienda? 🍽️ 어떤 걸 추천해요? \| Español A2 · Ep.34 | URL 미기록 |
| 35 | `en_el_restaurante_pagar_a2` | `a2-en-el-restaurante-pagar` | A2 입문 | Invito yo 💳 내가 낼게 \| Español A2 · Ep.35 | URL 미기록 |
| 36 | `en_el_medico_sintomas_a2` | `a2-en-el-medico-sintomas` | A2 입문 | Me duele la cabeza 🤕 머리가 아파요 \| Español A2 · Ep.36 | URL 미기록 |
| 37 | `llamada_gripe_rechazo_a2` | `a2-llamada-gripe-rechazo` | A2 입문 | No puedo ir porque estoy enfermo 📞 전화로 약속 거절하기 \| Español A2 · Ep.37 | URL 미기록 |

### historia-a1

| Ep | module | slug | 레벨 | 학습 포인트 (YOUTUBE_TITLE) | URL 상태 |
|---:|---|---|---|---|---|
| 1 | `historia_a1_un_dia_de_lucia` | `historia-a1-un-dia-de-lucia` | A1 | Un día de Lucía en Madrid 🌞 하루 일과 따라가기 \| Español A1 · Historia Ep.1 | URL 미기록 |
| 2 | `historia_a1_ep02_llaves_cafe` | `historia-a1-ep02-llaves-cafe` | A1 | Las llaves en el café 🔑 카페에 두고 온 열쇠 \| Español A1 · Historia Ep.2 | URL 미기록 |

> 요약: [TODO: SERIES]: 1모듈(최대 Ep.1) · descripcion: 6모듈(최대 Ep.6) · frases-a1: 32모듈(최대 Ep.31) · frases-a2: 8모듈(최대 Ep.37) · historia-a1: 2모듈(최대 Ep.2) — 학습 채널 타임라인(frases-*) 최대 Ep.37 → **다음 = Ep.38**. 주의: frases-a1 모듈 수 ≠ 도달 Ep번호 (Ep.0×2 · Ep.2 remake 포함, Ep.24/25는 frases-a2, descripcion은 독립 번호 Ep.1–6).

<!-- END:generated -->

---

## B. 상황·분야 커버리지 맵 (수기)

> 우리는 **상황극으로 주제를 매번 바꿔가는** 학습법을 씁니다. 그래서 커버리지는 문법이 아니라
> **"상황/장면"** 기준으로 관리합니다. 새 소재는 *아직 안 다룬 상황*을 고르는 것이 원칙입니다.

| 상황·분야 | 커버한 에피소드 | 비고 |
|---|---|---|
| 인사 · 자기소개 | Ep.0(50문장×2), Ep.1, Ep.2(+remake) | 입문 |
| 안부 · 감정/상태 | Ep.3, Ep.4 | ¿Cómo estás? / Tengo hambre |
| 카페 주문 | Ep.5, Ep.7, Ep.28 | 주문·포장 (※ 레스토랑 예약/주문과는 구분) |
| **가격 · 계산/결제** | Ep.6, Ep.8 | **중복 주의** — ¿Cuánto cuesta? / ¿Cuánto es? / 카드결제 이미 커버 |
| 교통 · 표 · 시각 | Ep.9, Ep.10, Ep.11 | 지하철·표·출발시각 |
| 여행 감상 · 날씨 · 옷차림 | Ep.12, Ep.13, Ep.15, Ep.16, Ep.17 | |
| **호불호 · 선호 · 이유** | Ep.18(pero=대조), Ep.19(prefiero=선호), **Ep.20(porque=이유)** | `Me gusta porque…` 단독 신규 금지(Ep.20과 부분중복) |
| 빈도 · 일과 | Ep.21, Ep.22, Ep.23 | a veces / siempre / nunca |
| 약속 · 거절 (A2) | Ep.24, Ep.25 | No puedo ir / ¿Podemos quedar? |
| 위치 · 존재 | Ep.9, Ep.26, Ep.27 | dónde está / estar location / hay |
| 구매 결정 · 색상 | Ep.29, Ep.30 | Me lo llevo / ¿Tiene otro color? |
| 듣기 생존 | Ep.31 | Más despacio, por favor |
| 레스토랑 예약 (A2) | Ep.32 | Quiero reservar una mesa |
| 식당 예약 확인 (A2) | Ep.33 | He reservado la mesa |
| 레스토랑 주문 (A2) | Ep.34 | ¿Qué nos recomienda? |
| 식당 계산 · 더치페이 (A2) | Ep.35 | Invito yo / ¿Pagamos a medias? |
| 병원 · 진료/증상 (A2) | Ep.36 | Me duele la cabeza / Tengo fiebre / Tengo tos |
| 전화 약속 거절 (A2) | Ep.37 | No puedo ir / Tengo gripe / Que te mejores pronto |

**아직 안 다룬 상황(분야) 예:** 호텔 체크인, 옷 사이즈/피팅, 길 안내(받기/주기), 전화 응대 등 → **C 큐**로.

---

## C. 미커버 후보 큐 (수기 · 다음 소재의 권위)

> 방향: **문법 드릴은 피하고, A2 레벨의 전문 분야별 상황극**으로 간다(상황 1개 = 기능 목표 1개).
> 각 후보는 Diego/Jin/Lucía 장면 + mini-prueba 구조로 제작.

| 우선 | slug | 시리즈/레벨 | 상황(장면) · 단일 기능 목표 | 중복 아님 근거 |
|---|---|---|---|---|
| **권장 (Ep.38)** | `a2-en-el-hotel-checkin` | frases-a2 / A2 | 호텔 **체크인 · 예약 확인** | 미커버 |
| 대안 | `a2-comprar-ropa-talla` | frases-a2 / A2 | 옷 가게 **사이즈 · 입어보기**(`¿Tiene una talla…?`) | Ep.29(me-lo-llevo)는 구매결정만 → 사이즈/피팅 미커버 |

**제외(이미 제작/중복):** `cuanto-cuesta-question`(=Ep.6·8), `quiero-para-llevar`(=Ep.28),
`me-lo-llevo`(=Ep.29), `estar-location`(≈Ep.26), `hay`(≈Ep.27).

**문법 드릴 파킹(단독 에피소드로 만들지 않음):** `numbers-0-10`, `definite-articles-el-la`,
`me-gusta-porque`(Ep.20 porque와 부분중복). 필요하면 상황극 장면 안에 녹인다
(예: 숫자 → 예약 인원·시각, 과거형 → 여행 후기 장면).
