# Frontend Guide

## 개요

프론트엔드는 별도 번들러 없이 정적 HTML/CSS/JS로 제공된다.

파일:
- `src/bookharness_api/static/index.html`
- `src/bookharness_api/static/styles.css`
- `src/bookharness_api/static/app.js`

## 화면 구성

### Dashboard
표시:
- 프로젝트 메트릭
- chapter 테이블
- approval queue 요약
- recent jobs

### Approval Queue
표시:
- Approval A/B 대기 항목
- chapter detail 이동 버튼

### Create Chapter
기능:
- chapter id / title / dependencies / actor 입력
- `POST /api/chapters`

### Chapter Detail
표시/기능:
- chapter 상태 헤더
- stage action 버튼
- artifact 목록
- rendered/raw viewer
- diff viewer
- approval 제출 폼
- review report 카드
- chapter jobs / audit timeline

## 렌더링 방식

- Markdown: backend가 간단한 HTML로 변환 가능
- Raw 보기: `<pre>` 기반
- Diff: line-level added/removed 리스트

## 한계

현재 UI는 다음을 의도적으로 단순화했다.
- rich markdown editor 없음
- 실시간 websocket 없음
- polling 기반 갱신
- 디자인 시스템 없음
- 인증/권한 모델 없음

## 다음 확장 후보

1. chapter dependency graph
2. global memory explorer
3. must-fix 전용 review 패널
4. artifact search/filter
5. 역할 기반 접근 제어
