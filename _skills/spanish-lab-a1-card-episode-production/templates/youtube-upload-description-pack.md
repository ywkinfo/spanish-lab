# <Episode title> YouTube upload pack

Use this template when the user asks for YouTube 게재 설명자료 / upload description material for a finished Spanish Lab A1 card episode.

## 1. 업로드 제목

**<YOUTUBE_TITLE from project/meta JSON>**

대체안, 조금 더 짧게 가고 싶을 때:

**<shorter title option>**

## 2. 설명란 본문

```text
<chapter timestamps first, exactly as in output/meta/*.md>

<Spanish description intro>

한국어 티저:
<Korean teaser, cleaned for readability>

오늘의 핵심 표현:
- <Spanish phrase> — <Korean meaning>
- <Spanish phrase> — <Korean meaning>

Guion del video:

<script/body from output/meta/*.md, if useful for this upload>

<description outro / repetition CTA>

Serie: <series title>
Nivel: <level>

<hashtags>
```

## 3. 태그

```text
<tag1>, <tag2>, <tag3>, ...
```

## 4. 카테고리 / 설정

- **카테고리:** Education
- **기본 오디오 언어:** Spanish / Español
- **시청자층:** 아동용 아님
- **재생목록:** <playlist / series title>
- **영상 길이:** 약 <duration>
- **해상도:** <width>×<height>
- **버전:** v<version>

## 5. 업로드 파일 경로

- 영상:  
`output/publish/<asset>.mp4`

- 썸네일:  
`output/thumbs/<asset>.jpg`

- 설명 메타 파일:  
`output/meta/<asset>.md`

- JSON 메타 파일:  
`output/meta/<asset>.json`
