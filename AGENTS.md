# AGENTS.md — AI 코드 어시스턴트를 위한 프로젝트 가이드

이 문서는 AI 코딩 에이전트(Cursor, Copilot 등)가 `oh-my-bookharness` 프로젝트를 처음부터 세팅하고, 운영하고, 수정할 수 있도록 만든 종합 가이드다.

## 이 프로젝트가 뭔가

책 집필 자동화 멀티에이전트 시스템이다. 9개의 전문 에이전트(편집장, 사서, 분석가, 설계자, 집필자, 리뷰어 3종, 수정 통합자)가 단계별로 LLM을 호출하여 brief → source → outline → draft → review → revision 파이프라인을 실행한다.

핵심 원칙:
- 파일이 canonical source of truth (DB는 캐시)
- 승인(approval) 없이는 final candidate/memory가 갱신되지 않음
- 모든 산출물은 Markdown/YAML/JSON

## 처음부터 세팅하기 (Step by Step)

### Step 0: 설치

```bash
# 기본 설치
pip install -e .

# 개발용 (테스트 포함)
pip install -e .[dev]

# LLM 백엔드 (택 1)
pip install -e '.[anthropic]'   # Anthropic Claude
pip install -e '.[openai]'      # OpenAI GPT
pip install -e '.[llm]'         # 둘 다
```

### Step 1: LLM 환경변수 설정

```bash
# Anthropic 사용 시
export ANTHROPIC_API_KEY="sk-ant-..."

# OpenAI 사용 시
export OPENAI_API_KEY="sk-..."

# 두 키가 모두 있으면 OpenAI 우선. 명시 지정:
export BOOKHARNESS_LLM_PROVIDER=anthropic  # 또는 openai

# 모델 변경 (선택)
export BOOKHARNESS_MODEL=gpt-4o-mini

# 테스트/개발 시 mock (실제 API 호출 없음)
export BOOKHARNESS_MOCK=1
```

### Step 2: 프로젝트 스캐폴드 생성

```bash
bookharness init-project --root ./book-project
```

이 명령이 생성하는 것:

```
book-project/
  book/                          ← canonical 문서 (사용자가 채워야 함)
    blueprint.md
    tone_guide.md
    argument_map.md
    decisions_log.md
    audience_profile.md
    writing_rules.md
    concept_dictionary.yaml
    chapter_dependencies.yaml
  sources/
    raw/{papers,blogs,talks,docs,interviews}/  ← 원문 배치
    normalized/                                ← 자동 생성됨
    metadata/registry.yaml                     ← 소스 메타데이터 (사용자가 채워야 함)
    chapter_packs/                             ← 자동 생성됨
  manuscript/shared/
  memory/
    global_summary.md
    chapter_summaries/
    unresolved_questions.md
    recurring_examples.md
  eval/rubrics/                  ← 품질 평가 기준
  workflow/
    runs/
    chapter_states/
    approvals/approvals.yaml
```

### Step 3: canonical 문서 작성 (필수)

`book/` 아래 6개 Markdown + 2개 YAML을 **실제 책 내용으로 채워야** 한다. 스캐폴드는 플레이스홀더만 넣는다.

| 파일 | 역할 | 에이전트 사용처 |
|---|---|---|
| `blueprint.md` | 책 전체 기획 (제목, 독자, 장 구성) | 모든 에이전트 |
| `tone_guide.md` | 문체 규칙 | DraftWriter, StyleReviewer |
| `argument_map.md` | 책의 핵심 주장 구조 | ChiefEditor, ChapterArchitect |
| `decisions_log.md` | 편집 결정 기록 | 모든 에이전트 |
| `audience_profile.md` | 대상 독자 정의 | ChiefEditor, DraftWriter |
| `writing_rules.md` | 집필 규칙 | DraftWriter, StyleReviewer |
| `concept_dictionary.yaml` | 용어집 (한국어 선호 표기 포함) | DraftWriter, TechnicalReviewer |
| `chapter_dependencies.yaml` | 장 간 의존성, 도입 개념 | ChiefEditor, ContinuityReviewer |

#### `concept_dictionary.yaml` 형식

```yaml
harness:
  preferred_korean: "평가 하네스"
  definition: "반복 가능하게 실행과 평가를 수행하는 외부 구조"
  notes: ["첫 등장 시 쉬운 설명을 덧붙인다"]

edd:
  preferred_korean: "평가 주도 개발"
  definition: "평가자(Evaluator)와 하네스를 먼저 설계하는 개발 방법론"
  notes: []
```

#### `chapter_dependencies.yaml` 형식

```yaml
ch01:
  introduces: [harness, poc_vs_production]
  depends_on: []
  required_by: [ch02, ch03]
  expected_pages: 20
  note: "1장은 하네스 개념의 첫 등장"

ch02:
  introduces: [edd, software_2_0]
  depends_on: [harness]
  required_by: [ch10, ch11]
  expected_pages: 20
  note: ""
```

### Step 4: 참고문헌 등록 (필수)

**두 가지를 세트로** 준비해야 한다:

#### 4-1. 원문 파일 배치

`sources/raw/` 아래 적절한 카테고리 폴더에 `.md` 또는 `.txt` 파일을 넣는다. **파일명 = source_id**.

```
sources/raw/papers/swe_bench_2024.md
sources/raw/blogs/karpathy_software_2_0.md
sources/raw/docs/anthropic_eval_guide.md
```

SourceAnalyst는 원문의 **앞 3000자**만 사용한다. 핵심 내용을 앞부분에 배치하라.

#### 4-2. 레지스트리 등록

`sources/metadata/registry.yaml`에 메타데이터를 추가한다. 초기값은 빈 리스트 `[]`.

```yaml
- id: swe_bench_2024                # 파일명과 일치 (확장자 제외)
  title: "SWE-bench: Evaluating LLMs on Real-World Software Engineering"
  type: paper
  author: "Carlos E. Jimenez et al."
  published_at: "2024-01"
  authority: high                   # high / medium / low
  source_kind: primary              # primary / secondary / background
  topic_tags: [evaluation, coding_agent, benchmark]
  relevance_tags: [ch01, ch10]      # 빈 리스트면 전체 장 후보
  status: active

- id: karpathy_software_2_0
  title: "Software 2.0"
  type: blog
  author: "Andrej Karpathy"
  published_at: "2017-11"
  authority: high
  source_kind: primary
  topic_tags: [paradigm, neural_network]
  relevance_tags: [ch02]
  status: active
```

### Step 5: 장 생성 및 파이프라인 실행

```bash
# 장 초기화
bookharness init-chapter ch01 "AI는 왜 항상 데모까지만 잘 되는가" --root ./book-project

# 단계별 실행
bookharness run-stage ch01 brief_generation --root ./book-project
bookharness run-stage ch01 source_collection --root ./book-project
bookharness run-stage ch01 source_analysis --root ./book-project
bookharness run-stage ch01 outline_design --root ./book-project
bookharness run-stage ch01 draft_writing --root ./book-project
bookharness run-stage ch01 automated_review --root ./book-project
bookharness run-stage ch01 revision_plan_synthesis --root ./book-project
bookharness run-stage ch01 draft_revision --root ./book-project

# 또는 한 번에 (approval gate 건너뜀)
bookharness run-mvp ch01 "AI는 왜 항상 데모까지만 잘 되는가" --root ./book-project

# 승인
bookharness approve ch01 approval_b approved --root ./book-project
```

### Step 6: UI 서버 (선택)

```bash
bookharness serve --root ./book-project --host 127.0.0.1 --port 8000
```

`http://127.0.0.1:8000/` 에서 dashboard, approval queue, chapter detail, diff viewer 사용 가능.

## 파이프라인 단계 요약

```
brief_generation      → ChiefEditor       → manuscript/chXX/brief.md
source_collection     → ResearchLibrarian  → chapter_packs/chXX/bundle.yaml, notes.md
source_analysis       → SourceAnalyst      → normalized/*.md, must_cite.md, counterpoints.md
outline_design        → ChapterArchitect   → manuscript/chXX/outline.md
[human_approval_a]    → 인간 승인 게이트
draft_writing         → DraftWriter        → manuscript/chXX/draft_v1.md
automated_review      → 3 Reviewers        → review_*.md, eval/reports/*.json
revision_plan_synthesis → RevisionSynth    → manuscript/chXX/revision_plan_v1.md
draft_revision        → DraftWriter        → manuscript/chXX/draft_v2.md
[human_approval_b]    → 인간 승인 게이트
→ final_candidate.md + memory/chapter_summaries/chXX.md + global_summary.md
```

## 코드 수정 시 규칙

### 절대 하지 말 것

1. `book/*` canonical 문서를 자동으로 덮어쓰기
2. `workflow/metadata.db`를 source of truth로 취급
3. approval 없이 `final_candidate.md`를 생성
4. state/status를 바꾸고 artifact는 안 만들기
5. artifact 파일명 규칙을 무심코 변경

### 변경 영향 범위

- **stage 이름 변경** → API router, UI, tests, docs, state machine spec 전부 같이 변경
- **approval 의미 변경** → `specs/state_machine.md` 갱신 필수
- **artifact 파일명 변경** → diff viewer, chapter detail UI가 깨질 수 있음
- **API 응답 형태 변경** → UI polling 코드 + `tests/test_api.py` 영향

### 변경 전에 읽을 파일 (최소)

1. `specs/system_spec.md` — 시스템 계약
2. `specs/state_machine.md` — 상태 전이 규칙
3. 작업 대상 모듈의 구현 파일

### 변경 후 확인

```bash
python -m pytest
```

## 프로젝트 구조

```
src/bookharness/           # 도메인 엔진
  orchestrator/
    runner.py              # WorkflowRunner (핵심 오케스트레이터)
    state_manager.py       # 장 상태 JSON 관리
  agents/
    base.py                # BaseAgent (LLM 호출 + 컨텍스트 로드)
    prompts.py             # 에이전트별 시스템 프롬프트
    chief_editor.py        # brief 생성
    research_librarian.py  # 소스 선별/번들
    source_analyst.py      # 원문 분석
    chapter_architect.py   # outline 설계
    draft_writer.py        # 초안/수정안 작성
    technical_reviewer.py  # 기술 리뷰
    style_reviewer.py      # 문체 리뷰
    continuity_reviewer.py # 연속성 리뷰
    revision_synthesizer.py # 리뷰 통합
  models/
    chapter_state.py       # ChapterState dataclass
    source_metadata.py     # SourceMetadata dataclass
  llm.py                   # LLM 백엔드 추상화 (Anthropic/OpenAI)
  memory/
    loader.py              # book/* + memory/* 로드
    summarizer.py          # 승인 후 요약 생성
  sources/
    registry.py            # SourceRegistry (YAML 읽기/쓰기)
  reviews/
    evaluator.py           # ReviewIO + BinaryGateChecker
    gates.py               # AcceptanceGate (루브릭 기반 통과 판정)

src/bookharness_api/       # API/UI 레이어
  app.py                   # FastAPI 앱 팩토리
  routers/                 # REST API 엔드포인트
  services/                # 서비스 레이어 (Job, Project, Chapter, Artifact)
  static/                  # Dashboard UI (정적 HTML/JS/CSS)
```

## 환경변수 요약

| 변수 | 역할 | 기본값 |
|---|---|---|
| `ANTHROPIC_API_KEY` | Anthropic API 키 | - |
| `OPENAI_API_KEY` | OpenAI API 키 | - |
| `BOOKHARNESS_LLM_PROVIDER` | `anthropic` 또는 `openai` 명시 지정 | 자동 감지 |
| `BOOKHARNESS_MODEL` | 모델 ID | Anthropic: `claude-sonnet-4-6`, OpenAI: `gpt-4o` |
| `BOOKHARNESS_MAX_TOKENS` | 최대 출력 토큰 | `8192` |
| `BOOKHARNESS_TIMEOUT` | API 호출 타임아웃(초) | `300` |
| `BOOKHARNESS_MOCK` | `1`이면 mock 백엔드 사용 | - |

## 자주 하는 작업 레시피

### 새 장 추가

```bash
bookharness init-chapter ch03 "문제는 모델이 아니라 시스템이다" \
  --depends-on ch01 ch02 \
  --root ./book-project
```

`chapter_dependencies.yaml`에도 해당 장 정보를 추가해야 ContinuityReviewer가 의존성을 제대로 검사한다.

### 특정 단계만 재실행

```bash
bookharness run-stage ch01 draft_writing --root ./book-project
```

각 단계는 독립적으로 재실행 가능하다. 이전 단계의 산출물이 있어야 한다.

### 승인 처리

```bash
# 승인
bookharness approve ch01 approval_b approved --root ./book-project

# 노트 포함 승인
bookharness approve ch01 approval_b approved_with_notes \
  --note "도입부 톤 조정 필요" --note "3절 사례 보강" \
  --root ./book-project

# 수정 요청
bookharness approve ch01 approval_b revision_requested --root ./book-project

# 거절
bookharness approve ch01 approval_b rejected --root ./book-project
```

### 소스 추가 후 재분석

```bash
# 1. sources/raw/에 파일 추가
# 2. sources/metadata/registry.yaml에 항목 추가
# 3. 해당 장 소스 단계 재실행
bookharness run-stage ch01 source_collection --root ./book-project
bookharness run-stage ch01 source_analysis --root ./book-project
```

## 상세 문서 참조

- `docs/getting_started.md` — 빠른 시작
- `docs/agent_pipeline.md` — 에이전트 파이프라인 전체 구조
- `docs/sources_guide.md` — 참고문헌 제공 방법 상세
- `docs/architecture.md` — 아키텍처 개요
- `docs/backend.md` — FastAPI 서비스 구조
- `docs/frontend.md` — Dashboard UI 구조
- `docs/operations.md` — 운영 가이드
- `specs/system_spec.md` — 시스템 계약
- `specs/state_machine.md` — 상태 전이 규칙
- `specs/api_contract.md` — REST API 계약
- `specs/repository_layout.md` — 파일/디렉터리 명세
