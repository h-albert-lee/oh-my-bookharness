# Agent Pipeline — 에이전트 파이프라인 구조

이 문서는 멀티에이전트 시스템의 전체 파이프라인, 각 에이전트의 역할, 입출력, 그리고 컨텍스트 흐름을 설명한다.

## 파이프라인 개요

```
init-chapter
  │
  ▼
brief_generation          ← ChiefEditor
  │
  ▼
source_collection         ← ResearchLibrarian
  │
  ▼
source_analysis           ← SourceAnalyst
  │
  ▼
outline_design            ← ChapterArchitect
  │
  ▼
[human_approval_a]        ← 인간 승인 게이트 (brief + outline + source bundle)
  │
  ▼
draft_writing             ← DraftWriter
  │
  ▼
automated_review          ← TechnicalReviewer + StyleReviewer + ContinuityReviewer
  │
  ▼
revision_plan_synthesis   ← RevisionSynthesizer
  │
  ▼
draft_revision            ← DraftWriter (revision mode)
  │
  ▼
[human_approval_b]        ← 인간 승인 게이트 (revised draft + review summary)
  │
  ▼
final_candidate + memory 갱신
```

## 공통 구조

### LLM 호출

모든 에이전트는 `BaseAgent._call_llm(system, user)`를 통해 LLM을 호출한다.

- `system`: `prompts.py`에 정의된 역할별 시스템 프롬프트
- `user`: 각 에이전트가 조립하는 작업 지시문 (한국어)

### 프로젝트 컨텍스트

대부분의 에이전트가 `load_project_context()` → `_build_context_block()`으로 다음 canonical 문서를 프롬프트에 주입한다:

- `book/blueprint.md`
- `book/tone_guide.md`
- `book/argument_map.md`
- `book/decisions_log.md`
- `book/writing_rules.md`
- `book/audience_profile.md`
- `book/concept_dictionary.yaml`
- `book/chapter_dependencies.yaml`

### 프롬프트 4계층

```
1. System Layer      → 역할, 제약, 출력 형식 (prompts.py)
2. Project Context   → book/* canonical 문서 (런타임 주입)
3. Task Layer        → 단계별 작업 지시 (에이전트별)
4. Local Context     → 장별 입력: brief, outline, notes 등
```

## 에이전트별 상세

### 1. ChiefEditor — 편집장

역할: 장별 목표를 설정하고 chapter brief를 작성한다.

| 항목 | 내용 |
|---|---|
| 단계 | `brief_generation` |
| 입력 | `book/*` canonical 문서, `chapter_dependencies.yaml`에서 해당 장의 introduces/depends_on, 인자로 받은 이전 장 요약 |
| 프롬프트 핵심 | 장 메타 정보, 의존 개념, 프로젝트 맥락, 출력 섹션 9개 지시 |
| 산출물 | `manuscript/{chapter_id}/brief.md` |
| 소스 사용 | 없음 — `book/*` 맥락만 사용 |

brief.md에 포함되는 섹션:
- 이 장의 목표
- 독자가 얻을 것
- 장의 핵심 질문
- 반드시 들어갈 개념
- 피해야 할 오해
- 앞/뒤 장과의 연결
- 톤 메모
- 참고할 이전 장 요약

### 2. ResearchLibrarian — 연구 사서

역할: 장에 필요한 source를 레지스트리에서 선별하고 번들로 구성한다.

| 항목 | 내용 |
|---|---|
| 단계 | `source_collection` |
| 입력 | `sources/metadata/registry.yaml`, `manuscript/{chapter_id}/brief.md`, `book/*` canonical 문서 |
| 필터 규칙 | `relevance_tags`에 `chapter_id`가 포함되거나, `relevance_tags`가 빈 리스트인 항목 |
| 산출물 | `sources/chapter_packs/{chapter_id}/bundle.yaml`, `sources/chapter_packs/{chapter_id}/notes.md` |

bundle.yaml 구조:
```yaml
chapter_id: ch01
core_sources:
  - source_id: eval_framework_2024
    title: "..."
    authority: high
    why_it_matters: "..."
    expected_usage: "..."
    quality_score: 5
supporting_sources:
  - source_id: mlops_best_practices
    ...
```

### 3. SourceAnalyst — 자료 분석가

역할: 원문을 읽고 장 집필에 사용할 수 있는 분석 노트로 정리한다.

| 항목 | 내용 |
|---|---|
| 단계 | `source_analysis` |
| 입력 | `bundle.yaml` 항목, `sources/raw/.../{source_id}.md` 원문 (앞 3000자), `book/*` canonical 문서, brief |
| LLM 호출 | core + supporting 소스 **각각**에 대해 개별 호출 |
| 산출물 | `sources/normalized/{source_id}.md` (소스별), `sources/chapter_packs/{chapter_id}/must_cite.md`, `sources/chapter_packs/{chapter_id}/counterpoints.md` |

normalized note 섹션:
1. 핵심 주장
2. 책에 활용 가능한 포인트
3. 이 장과의 관련성
4. 주의할 점 / 한계
5. 인용 시 주의 표현

### 4. ChapterArchitect — 장 설계자

역할: brief와 source pack을 바탕으로 장 구조를 설계한다.

| 항목 | 내용 |
|---|---|
| 단계 | `outline_design` |
| 입력 | brief, `bundle.yaml` (source_id, why_it_matters 목록), `notes.md` (앞 2000자), 이전 장 요약 (각 300자), `book/*` canonical 문서 |
| 산출물 | `manuscript/{chapter_id}/outline.md` |

outline.md 구조:
- 장 제목
- Argument Flow (한 문단)
- Section별: 제목, 목적, 사용 source, 포함 예시, 핵심 요점, 연결 아이디어

### 5. DraftWriter — 집필자

역할: outline과 source pack을 기반으로 Markdown 초안을 작성한다.

| 항목 | 내용 |
|---|---|
| 단계 | `draft_writing` (초안), `draft_revision` (수정) |
| 입력 | brief, outline, `notes.md` (앞 3000자), 이전 장 요약 (각 300자), `book/*` canonical 문서 |
| 수정 모드 추가 입력 | revision plan, 이전 초안 (앞 4000자) |
| max_tokens | 16384 |
| 산출물 | `manuscript/{chapter_id}/draft_vN.md` |
| 수정 모드 추가 산출물 | `manuscript/{chapter_id}/change_log_vN.md` |

출처 참조는 각주 형태(`[^source_id]`)로 표기된다.

### 6. TechnicalReviewer — 기술 리뷰어

역할: 사실성, 개념 정의, source 정합성을 검토한다.

| 항목 | 내용 |
|---|---|
| 단계 | `automated_review` (병렬 실행) |
| 입력 | 최신 초안 (앞 8000자), brief (앞 2000자), `notes.md` (앞 2000자), `book/*` context (앞 2000자) |
| 평가 점수 | `technical_accuracy`, `source_grounding`, `clarity` (각 1-5) |
| Binary checks | `has_unsupported_claims`, `has_source_references`, `meets_minimum_length` |
| 산출물 | `ReviewReport` → `manuscript/{chapter_id}/review_technical_v1.md`, `eval/reports/{chapter_id}_technical_v1.json` |

### 7. StyleReviewer — 문체 리뷰어

역할: 문체 일관성, 용어 통일, 톤 적합성을 검토한다.

| 항목 | 내용 |
|---|---|
| 단계 | `automated_review` (병렬 실행) |
| 입력 | 최신 초안 (앞 8000자), `book/*` context (앞 2000자) |
| 평가 점수 | `tone_fit`, `reader_friendliness`, `redundancy` (각 1-5) |
| Binary checks | 선언적/과장 표현, 블로그체 패턴 |
| 산출물 | `ReviewReport` → `review_style_v1.md`, `eval/reports/..._style_v1.json` |

### 8. ContinuityReviewer — 연속성 리뷰어

역할: 앞 장과의 연결, 중복, 누락 개념을 검토한다.

| 항목 | 내용 |
|---|---|
| 단계 | `automated_review` (병렬 실행) |
| 입력 | 최신 초안 (앞 8000자), 이전 장 요약 (각 500자), `book/*` context (앞 2000자) |
| 평가 점수 | `continuity`, `dependency_coverage` (각 1-5) |
| Binary checks | depends_on 개념 포함 여부, 전방/후방 참조 키워드 |
| 산출물 | `ReviewReport` → `review_continuity_v1.md`, `eval/reports/..._continuity_v1.json` |

### 9. RevisionSynthesizer — 수정 통합자

역할: 3개 리뷰 결과를 통합하고 Writer가 반영할 revision plan을 만든다.

| 항목 | 내용 |
|---|---|
| 단계 | `revision_plan_synthesis` |
| 입력 | 3개 `ReviewReport`에서 통합한 must_fix/should_fix/nice_to_have + 점수 요약, brief (앞 1500자), 최신 초안 (앞 3000자) |
| 산출물 | `manuscript/{chapter_id}/revision_plan_vN.md` |

revision plan 구조:
1. Score Summary
2. Must Fix (반드시 수정)
3. Should Fix (권장 수정)
4. Optional Improvements
5. Contradictory Comments (상충 의견)
6. Rewrite Instructions for Writer

## 비-LLM 구성요소

### AcceptanceGate

- 3개 리뷰의 점수를 `eval/rubrics/*.yaml` 임계값과 비교
- LLM 호출 없음
- 결과: `gate_passed` boolean + 상세 dict

### BinaryGateChecker

- 초안 텍스트를 정규식/패턴으로 검사
- 각주 유무, 최소 길이, 선언체 패턴, 의존 개념 포함 등
- LLM 호출 없음
- 결과: `dict[str, bool]` — 각 리뷰어가 `ReviewReport.binary_checks`에 첨부

### SummaryBuilder

- `approval_b` 승인 후 final candidate에서 요약 추출
- 정규식/휴리스틱 기반 (LLM 호출 없음)
- 산출물: `memory/chapter_summaries/{chapter_id}.md`, `memory/global_summary.md`, `memory/recurring_examples.md`

## 컨텍스트 흐름 다이어그램

```
book/* canonical docs ─────────────────┬──────────────────────────────────┐
                                       │                                  │
                                       ▼                                  ▼
                              ChiefEditor                    모든 에이전트
                                  │                         (project context)
                                  ▼
                           brief.md ──────────┬──────────────────────┐
                                              │                      │
                                              ▼                      ▼
registry.yaml ──────────► ResearchLibrarian            SourceAnalyst
                                  │                         │
                                  ▼                         ▼
                         bundle.yaml + notes.md     normalized/*.md
                                  │                  must_cite.md
                                  │                  counterpoints.md
                                  │
                    ┌─────────────┼──────────────┐
                    ▼             ▼               ▼
          ChapterArchitect   DraftWriter   TechnicalReviewer
                    │             │               │
                    ▼             ▼               ▼
              outline.md    draft_vN.md    ReviewReport ×3
                                               │
                                               ▼
                                     RevisionSynthesizer
                                               │
                                               ▼
                                     revision_plan_vN.md
                                               │
                                               ▼
                                   DraftWriter (revision mode)
                                               │
                                               ▼
                                     draft_vN+1.md
                                               │
                                       [approval_b]
                                               │
                                               ▼
                                 final_candidate.md + memory/*
```

## 실행 모드

### `run-stage` — 단일 단계 실행

```bash
bookharness run-stage ch01 brief_generation --root ./book-project
```

각 단계를 독립적으로 실행하고 재실행할 수 있다.

### `run-mvp` — approval gate 없이 전체 실행

```bash
bookharness run-mvp ch01 "제목" --root ./book-project
```

`brief_generation` → `source_collection` → `source_analysis` → `outline_design` → `draft_writing` → `automated_review` → `revision_plan_synthesis` → `draft_revision`을 순서대로 실행한다. approval gate는 건너뛴다.

### `run-full` — approval gate 포함 실행

`brief_generation` ~ `human_approval_a`까지 실행 후 멈춘다. 승인 후 `resume_after_approval()`로 `draft_writing` ~ `human_approval_b`까지 이어간다.

## LLM 백엔드

에이전트들은 `LLMBackend` Protocol을 통해 LLM을 호출한다. Anthropic과 OpenAI를 지원한다.

```bash
# Anthropic (기본)
export ANTHROPIC_API_KEY="sk-ant-..."

# OpenAI
export OPENAI_API_KEY="sk-..."

# 명시적 지정
export BOOKHARNESS_LLM_PROVIDER=openai
export BOOKHARNESS_MODEL=gpt-4o

# 테스트용 mock
export BOOKHARNESS_MOCK=1
```

상세 설정은 `docs/getting_started.md`의 "LLM 백엔드 설정" 섹션을 참고한다.
