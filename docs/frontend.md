# Frontend Guide

## 개요

프론트엔드는 별도 번들러 없이 정적 HTML/CSS/JS로 제공된다.

파일:
- `src/bookharness_api/static/index.html`
- `src/bookharness_api/static/styles.css`
- `src/bookharness_api/static/app.js`

## UX 목표

1. **운영 집중형 정보구조**: 대시보드에서 chapter 상태, 승인 대기, 최근 agent 실행을 한눈에 파악
2. **관찰성 강화**: chapter 상세에서 run timeline + audit timeline + log 확인 가능
3. **반복 작업 최소화**: 검색/필터, 자동 새로고침, 글로벌 새로고침 지원
4. **의사결정 단축**: stage progress navigator와 approval 패널을 동일 화면에 배치

## 화면 구성

### Global Toolbar
표시/기능:
- 전체 운영 상태 요약
- 15초 자동 새로고침 토글
- 전체 뷰 새로고침

### Dashboard
표시/기능:
- 프로젝트 메트릭 카드
- chapter 테이블 (검색 + 상태 필터)
- stage progress 시각화
- 승인 대기 카드
- 최근 job 카드

### Approval Queue
표시/기능:
- pending approval 목록
- chapter detail 빠른 이동

### Create Chapter
기능:
- chapter id / title / dependencies / actor 입력
- `POST /api/chapters`

### Chapter Detail
표시/기능:
- sticky chapter 헤더
- stage progress navigator
- stage action 버튼
- artifact 검색/선택
- rendered/raw viewer
- diff viewer
- approval 제출 폼
- review report 카드
- agent run timeline (status/error/log)
- audit timeline (details fold)

## 렌더링 방식

- Markdown: backend가 제공하는 rendered_html 우선 사용
- Raw 보기: `<pre>` 기반
- Diff: changed/left_only/right_only 표시
- 오류 처리: toast 기반 피드백

## 운영 포인트

- 실시간 websocket 대신 polling + auto-refresh를 채택
- UI는 chapter 운영자와 승인 담당자의 단축 동선을 우선
- 상태 전환(run-stage, approve) 이후 즉시 재로딩으로 최신 상태 반영

## 향후 확장 후보

1. chapter dependency graph
2. global memory explorer
3. review must-fix 전용 정렬/필터
4. artifact full-text search index
5. 역할 기반 접근 제어
