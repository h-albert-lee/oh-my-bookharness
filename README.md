# oh-my-bookharness

`oh-my-bookharness`는 책 집필 자동화 멀티에이전트 시스템을 위한 **Markdown-first, 상태 기반 워크플로 엔진 + API/UI 레이어**입니다. 이 저장소는 자유 대화형 에이전트 시뮬레이션보다, 재현 가능한 단계 실행과 명시적 문서 메모리를 우선하는 구현을 제공합니다.

## 구현 범위

현재 구현은 다음을 포함합니다.

- 프로젝트 스캐폴딩: `book/`, `sources/`, `manuscript/`, `memory/`, `eval/`, `workflow/`, `prompts/` 디렉터리와 기본 canonical 문서 생성
- 장 상태 관리: JSON 기반 `workflow/chapter_states/chXX_state.json`
- deterministic 단계 실행: brief → source collection → source analysis → outline → draft → review → revision
- human approval gate 기록: `workflow/approvals/approvals.yaml`
- source 계층 구조: registry / normalized notes / chapter pack
- 자동 리뷰 산출물: technical / style / continuity markdown 및 JSON report
- revised draft 승인 후 summary / global summary 갱신
- FastAPI 기반 backend: project / chapters / approvals / artifacts / runs API 제공
- background job execution: `workflow/runs/*.json` 기반 큐 및 상태 추적
- SQLite metadata index: UI 조회 가속용 `workflow/metadata.db`
- audit log: `workflow/audit_log.jsonl`
- 정적 dashboard UI: 프로젝트 홈, approval queue, chapter detail, artifact viewer, diff viewer

## 추가 문서

- `docs/README.md`: 문서 인덱스
- `docs/getting_started.md`: 빠른 시작
- `docs/architecture.md`: 아키텍처 개요
- `docs/backend.md`: backend 서비스 구조
- `docs/frontend.md`: dashboard UI 구조
- `docs/operations.md`: 운영 가이드
- `docs/assistant_guide.md`: 코드 어시스턴트용 변경 가이드
- `specs/system_spec.md`: 시스템 전체 계약
- `specs/state_machine.md`: 장 상태 전이 명세
- `specs/api_contract.md`: API 계약
- `specs/repository_layout.md`: 파일/디렉터리 명세

## 설치

```bash
pip install -e .
```

개발용 테스트 의존성까지 설치하려면 다음을 사용합니다.

```bash
pip install -e .[dev]
```

## CLI 사용 예시

### 1) 프로젝트 초기화

```bash
bookharness init-project --root ./book-project
```

### 2) 한 장 초기화

```bash
bookharness init-chapter ch01 "데모는 되는데 왜 운영은 어려울까" --root ./book-project
```

### 3) 특정 단계 실행

```bash
bookharness run-stage ch01 brief_generation --root ./book-project
bookharness run-stage ch01 source_collection --root ./book-project
bookharness run-stage ch01 source_analysis --root ./book-project
bookharness run-stage ch01 outline_design --root ./book-project
bookharness run-stage ch01 draft_writing --root ./book-project
bookharness run-stage ch01 automated_review --root ./book-project
bookharness run-stage ch01 revision_plan_synthesis --root ./book-project
bookharness run-stage ch01 draft_revision --root ./book-project
```

### 4) MVP 한 번에 실행

```bash
bookharness run-mvp ch01 "데모는 되는데 왜 운영은 어려울까" --root ./book-project
```

### 5) 인간 승인 기록

```bash
bookharness approve ch01 approval_b approved --root ./book-project
```

### 6) API/UI 서버 실행

```bash
bookharness serve --root ./book-project --host 127.0.0.1 --port 8000
# 또는
bookharness-api --root ./book-project --host 127.0.0.1 --port 8000
```

브라우저에서 `http://127.0.0.1:8000/`로 접속하면 dashboard UI를 사용할 수 있습니다.

## 주요 API

- `GET /api/project`
- `GET /api/project/chapters`
- `POST /api/chapters`
- `GET /api/chapters/{chapter_id}`
- `POST /api/chapters/{chapter_id}/run-stage`
- `POST /api/chapters/{chapter_id}/run-mvp`
- `POST /api/chapters/{chapter_id}/approve`
- `GET /api/approvals/pending`
- `GET /api/artifacts?path=...`
- `GET /api/artifacts/diff?left=...&right=...`
- `GET /api/runs`
- `GET /api/runs/{job_id}`

## UI 구성

### Dashboard
- 프로젝트 메트릭
- 장 목록
- approval queue 요약
- 최근 job 목록

### Approval Queue
- Approval A / B 대기 항목 조회
- 장 상세로 이동

### Chapter Detail
- 상태 헤더
- 단계 실행 버튼
- artifact 목록
- draft / review / revision viewer
- diff viewer
- approval 제출 폼
- chapter job / audit timeline

## 설계 원칙 반영 방식

- **상태 우선**: 각 장은 독립 JSON 상태 파일로 관리됩니다.
- **문서 중심 메모리**: `book/*`, `memory/*`, `sources/*` 문서를 읽고 산출물을 만듭니다.
- **리뷰 우선**: 초안 생성 뒤에 technical/style/continuity 리뷰와 revision plan이 생성됩니다.
- **인간 승인 게이트**: approval 기록 없이는 final candidate와 global memory가 갱신되지 않습니다.
- **Git 친화성**: 모든 산출물은 Markdown, YAML, JSON으로 저장됩니다.
- **파일 canonical / DB index**: 문서는 파일이 source of truth이고, SQLite는 조회 가속용 인덱스입니다.

## 주요 모듈

```text
src/bookharness/
  orchestrator/
  agents/
  models/
  memory/
  sources/
  manuscript/
  reviews/
  utils/

src/bookharness_api/
  app.py
  routers/
  services/
  static/
```

## 테스트

```bash
pytest
```
