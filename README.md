# oh-my-bookharness

**책 집필 자동화를 위한 멀티에이전트 워크플로 엔진**

oh-my-bookharness는 LLM 기반 9개 전문 에이전트가 단계별로 협업하여 기술서를 집필하는 시스템입니다. "그럴듯한 텍스트 생성"이 아니라, **재현 가능한 단계 실행**과 **인간 승인 기반 품질 관리**에 초점을 맞추었습니다.

## 왜 이 프로젝트인가

LLM으로 긴 글을 쓰면 흔히 겪는 문제들이 있습니다:

- 출처 없는 주장이 섞여 들어옴
- 앞뒤 장 연결이 끊김
- 한번 생성하면 수정이 어려움
- 문체가 일관되지 않음

oh-my-bookharness는 이 문제를 **편집장 → 사서 → 분석가 → 설계자 → 집필자 → 리뷰어 → 수정자**의 역할 분리와, 각 단계마다 파일로 남는 산출물 + 인간 승인 게이트로 해결합니다.

## 동작 방식

```
                          book/* (기획서, 톤가이드, 용어집)
                          sources/raw/* (참고문헌 원문)
                                    │
                                    ▼
  ┌─────────────────────────────────────────────────────────────┐
  │                      파이프라인                               │
  │                                                             │
  │  brief ─→ source ─→ analysis ─→ outline ─→ [승인A]          │
  │                                                │            │
  │  draft ─→ review(×3) ─→ revision plan ─→ revision ─→ [승인B]│
  │                                                │            │
  │                                      final candidate        │
  │                                      + memory 갱신          │
  └─────────────────────────────────────────────────────────────┘
```

### 9개 전문 에이전트

| 에이전트 | 역할 | 산출물 |
|---|---|---|
| **ChiefEditor** | 장 목표 설정, brief 작성 | `brief.md` |
| **ResearchLibrarian** | 참고문헌 선별 및 번들 구성 | `bundle.yaml`, `notes.md` |
| **SourceAnalyst** | 원문 분석, 인용 가능한 노트 정리 | `normalized/*.md`, `must_cite.md` |
| **ChapterArchitect** | 장 구조 설계 | `outline.md` |
| **DraftWriter** | 초안 및 수정안 작성 | `draft_v1.md`, `draft_v2.md` |
| **TechnicalReviewer** | 사실성, 개념 정의, source 정합 검토 | `review_technical_v1.md` |
| **StyleReviewer** | 문체 일관성, 톤 적합성 검토 | `review_style_v1.md` |
| **ContinuityReviewer** | 앞뒤 장 연결, 용어 일관성 검토 | `review_continuity_v1.md` |
| **RevisionSynthesizer** | 3개 리뷰 통합, 수정 계획 작성 | `revision_plan_v1.md` |

## 핵심 특징

- **Markdown-first**: 모든 산출물이 Markdown/YAML/JSON — Git으로 버전 관리 가능
- **인간 승인 게이트**: 승인 없이는 최종 원고와 글로벌 메모리가 갱신되지 않음
- **단계별 재실행**: 각 단계를 독립적으로 재실행할 수 있음 (전체를 다시 돌릴 필요 없음)
- **파일이 source of truth**: SQLite DB는 조회 가속용 캐시, 언제든 재생성 가능
- **LLM 교체 가능**: Anthropic Claude / OpenAI GPT를 환경변수 하나로 전환
- **Dashboard UI**: FastAPI 기반 웹 UI로 상태 확인, 단계 실행, 승인 처리

## 빠른 시작

### 1. 설치

```bash
git clone https://github.com/your-org/oh-my-bookharness.git
cd oh-my-bookharness
pip install -e '.[dev]'
```

### 2. LLM 백엔드 설정

```bash
# Anthropic Claude (기본)
pip install -e '.[anthropic]'
export ANTHROPIC_API_KEY="sk-ant-..."

# 또는 OpenAI GPT
pip install -e '.[openai]'
export OPENAI_API_KEY="sk-..."
```

### 3. 프로젝트 초기화

```bash
bookharness init-project --root ./my-book
```

이 명령이 `book/`, `sources/`, `manuscript/`, `memory/`, `eval/`, `workflow/` 디렉터리와 기본 설정 파일들을 생성합니다.

### 4. 기획서와 참고문헌 준비

```bash
# book/ 아래 기획서, 톤가이드, 용어집 등을 실제 내용으로 채우기
vim my-book/book/blueprint.md
vim my-book/book/tone_guide.md
vim my-book/book/concept_dictionary.yaml

# 참고문헌 원문을 sources/raw/에 배치
cp my-paper.md my-book/sources/raw/papers/eval_framework_2024.md

# 메타데이터 등록
vim my-book/sources/metadata/registry.yaml
```

> 참고문헌 등록 방법의 상세 가이드는 [docs/sources_guide.md](docs/sources_guide.md)를 참고하세요.

### 5. 한 장 집필 실행

```bash
# MVP: brief부터 revision까지 한 번에 실행
bookharness run-mvp ch01 "AI는 왜 항상 데모까지만 잘 되는가" --root ./my-book
```

또는 단계별로:

```bash
bookharness init-chapter ch01 "AI는 왜 항상 데모까지만 잘 되는가" --root ./my-book
bookharness run-stage ch01 brief_generation --root ./my-book
bookharness run-stage ch01 source_collection --root ./my-book
bookharness run-stage ch01 source_analysis --root ./my-book
bookharness run-stage ch01 outline_design --root ./my-book
bookharness run-stage ch01 draft_writing --root ./my-book
bookharness run-stage ch01 automated_review --root ./my-book
bookharness run-stage ch01 revision_plan_synthesis --root ./my-book
bookharness run-stage ch01 draft_revision --root ./my-book
```

### 6. 승인 및 최종 원고 생성

```bash
bookharness approve ch01 approval_b approved --root ./my-book
# → manuscript/ch01/final_candidate.md 생성
# → memory/chapter_summaries/ch01.md 갱신
```

### 7. Dashboard UI

```bash
bookharness serve --root ./my-book --port 8000
# → http://127.0.0.1:8000/
```

## 사용자가 준비해야 하는 것

| 파일 | 내용 | 역할 |
|---|---|---|
| `book/blueprint.md` | 책 전체 기획 (제목, 독자, 장 구성) | 모든 에이전트의 방향성 |
| `book/tone_guide.md` | 문체 규칙 | 초안 작성 및 문체 리뷰 기준 |
| `book/argument_map.md` | 핵심 주장 구조 | 편집장과 설계자의 판단 근거 |
| `book/concept_dictionary.yaml` | 용어집 (한국어 표기 포함) | 용어 일관성 검증 |
| `book/chapter_dependencies.yaml` | 장 간 의존성 | 연속성 리뷰 기준 |
| `sources/raw/**/*.md` | 참고문헌 원문 | 자료 분석 및 인용 근거 |
| `sources/metadata/registry.yaml` | 참고문헌 메타데이터 | 사서 에이전트의 선별 기준 |

> 상세 형식과 예시는 [AGENTS.md](AGENTS.md)의 "Step 3~4" 섹션을 참고하세요.

## 프로젝트 구조

```
src/
  bookharness/                 # 도메인 엔진
    orchestrator/runner.py     #   WorkflowRunner (핵심 오케스트레이터)
    agents/                    #   9개 전문 에이전트
    llm.py                     #   LLM 백엔드 추상화 (Anthropic/OpenAI)
    models/                    #   ChapterState, SourceMetadata
    memory/                    #   프로젝트 컨텍스트 로더, 요약 빌더
    sources/                   #   소스 레지스트리
    reviews/                   #   리뷰 I/O, 품질 게이트
  bookharness_api/             # API/UI 레이어
    app.py                     #   FastAPI 앱
    routers/                   #   REST API 엔드포인트
    services/                  #   Job, Project, Chapter, Artifact 서비스
    static/                    #   Dashboard UI

docs/                          # 운영 문서
specs/                         # 계약 문서 (상태 머신, API, 레이아웃)
tests/                         # 테스트 (mock LLM 백엔드 사용)
```

## API

Dashboard UI 외에도 REST API로 직접 제어할 수 있습니다.

| 엔드포인트 | 설명 |
|---|---|
| `GET /api/project` | 프로젝트 대시보드 데이터 |
| `POST /api/chapters` | 새 장 생성 |
| `GET /api/chapters/{id}` | 장 상세 정보 |
| `POST /api/chapters/{id}/run-stage` | 단계 실행 |
| `POST /api/chapters/{id}/run-mvp` | MVP 전체 실행 |
| `POST /api/chapters/{id}/approve` | 승인 처리 |
| `GET /api/approvals/pending` | 승인 대기 목록 |
| `GET /api/artifacts?path=...` | 산출물 조회 |
| `GET /api/artifacts/diff?left=...&right=...` | 산출물 diff |
| `GET /api/runs` | 실행 이력 |

## 설계 원칙

| 원칙 | 설명 |
|---|---|
| **상태 기반 워크플로** | 각 장은 독립 JSON 상태 파일로 관리. 실패 시 해당 단계만 재실행 |
| **문서 중심 메모리** | 에이전트는 `book/*`, `memory/*`, `sources/*` 파일을 읽고 산출물을 만듬 |
| **리뷰 우선** | 초안 뒤에 technical/style/continuity 3종 자동 리뷰 → revision plan 생성 |
| **인간 승인 게이트** | 2단계 승인(outline + revised draft) 없이는 최종 원고 생성 불가 |
| **파일 canonical** | 파일 시스템이 source of truth. SQLite는 조회 가속 캐시 |
| **Git 친화** | 모든 산출물이 텍스트 (Markdown, YAML, JSON) — diff, blame, PR 리뷰 가능 |

## 테스트

```bash
python -m pytest
```

모든 테스트는 mock LLM 백엔드를 사용하므로 API 키 없이 실행됩니다.

## 요구사항

- Python >= 3.11
- LLM 백엔드: Anthropic Claude 또는 OpenAI GPT (환경변수로 설정)

## 문서

| 문서 | 설명 |
|---|---|
| [AGENTS.md](AGENTS.md) | AI 코드 어시스턴트를 위한 종합 가이드 |
| [docs/getting_started.md](docs/getting_started.md) | 빠른 시작 가이드 |
| [docs/agent_pipeline.md](docs/agent_pipeline.md) | 에이전트 파이프라인 구조 |
| [docs/sources_guide.md](docs/sources_guide.md) | 참고문헌 제공 방법 |
| [docs/architecture.md](docs/architecture.md) | 아키텍처 개요 |
| [docs/backend.md](docs/backend.md) | FastAPI 백엔드 구조 |
| [docs/frontend.md](docs/frontend.md) | Dashboard UI 구조 |
| [docs/operations.md](docs/operations.md) | 운영 가이드 |
| [specs/system_spec.md](specs/system_spec.md) | 시스템 계약 |
| [specs/state_machine.md](specs/state_machine.md) | 상태 전이 명세 |
| [specs/api_contract.md](specs/api_contract.md) | REST API 계약 |

## 라이선스

MIT
