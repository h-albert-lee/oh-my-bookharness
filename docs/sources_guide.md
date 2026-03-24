# Sources Guide — 참고문헌 제공 방법

이 문서는 멀티에이전트 파이프라인이 참고문헌을 어떻게 소비하는지, 사용자가 무엇을 준비해야 하는지를 설명한다.

## 문헌 투입 3단계

```
1. 원문 배치 (sources/raw/)
2. 레지스트리 등록 (sources/metadata/registry.yaml)
3. 파이프라인 실행 → 에이전트가 자동 가공
```

## 1단계: 원문 파일 배치

`init-project` 후 생성되는 디렉터리:

```
sources/
  raw/
    papers/       # 논문
    blogs/        # 블로그 글
    talks/        # 강연/발표 자료
    docs/         # 공식 문서
    interviews/   # 인터뷰
```

### 파일 형식

- Markdown(`.md`) 또는 텍스트(`.txt`)
- 파일명이 곧 `source_id`가 된다 (확장자 제외)

### 파일명 규칙

```
sources/raw/papers/anthropic_eval_2024.md   → source_id: anthropic_eval_2024
sources/raw/blogs/google_ai_testing.md      → source_id: google_ai_testing
sources/raw/docs/openai_evals_guide.txt     → source_id: openai_evals_guide
```

### 탐색 순서

`SourceAnalyst`는 다음 순서로 원문을 탐색한다:

1. `sources/raw/{papers,blogs,talks,docs,interviews}/{source_id}.md`
2. `sources/raw/{papers,blogs,talks,docs,interviews}/{source_id}.txt`
3. `sources/normalized/{source_id}.md` (이전 분석 결과가 있는 경우)

찾지 못하면 프롬프트에 "원문 미등록" 안내가 들어간다.

### 길이 제한

`SourceAnalyst`는 원문의 **앞 3000자**만 사용한다. 긴 논문의 경우, 핵심 내용을 앞부분에 배치하거나 별도로 요약한 md를 넣는 것이 효과적이다.

## 2단계: 레지스트리 등록

원문을 넣은 뒤 `sources/metadata/registry.yaml`에 메타데이터를 등록해야 한다. `ResearchLibrarian`이 이 파일을 읽고 장별 소스를 선별한다.

### 레지스트리 형식

```yaml
- id: anthropic_eval_2024
  title: "Anthropic의 AI 평가 프레임워크"
  type: paper
  author: "Anthropic Research"
  published_at: "2024-06"
  authority: high
  source_kind: primary
  topic_tags: [evaluation, llm, safety]
  relevance_tags: [ch01, ch03]
  status: active
  url: "https://arxiv.org/abs/..."
  local_path: "sources/raw/papers/anthropic_eval_2024.md"

- id: google_ai_testing
  title: "Google의 AI 시스템 테스트 전략"
  type: blog
  author: "Google AI Blog"
  published_at: "2024-03"
  authority: medium
  source_kind: secondary
  topic_tags: [testing, mlops]
  relevance_tags: []
  status: active
```

### 필드 설명

| 필드 | 필수 | 설명 |
|---|---|---|
| `id` | O | 원문 파일명과 일치해야 함 (확장자 제외) |
| `title` | O | 자료 제목 |
| `type` | O | `paper`, `blog`, `talk`, `doc`, `interview` 중 하나 |
| `author` | O | 저자 또는 기관 |
| `published_at` | O | 발행일 |
| `authority` | O | `high` / `medium` / `low` — Librarian의 선별 가중치 |
| `source_kind` | O | `primary` / `secondary` / `background` |
| `topic_tags` | O | 주제 분류 태그 리스트 |
| `relevance_tags` | O | 관련 장 ID 리스트. 빈 리스트 `[]`이면 **모든 장의 후보** |
| `status` | O | `active` / `deprecated` |
| `url` | - | 원본 URL |
| `local_path` | - | 원문 파일 경로 |
| `citation_priority` | - | 인용 우선순위 |
| `claims_supported` | - | 이 자료가 뒷받침하는 주장 목록 |
| `caution_notes` | - | 사용 시 주의사항 |

### `relevance_tags` 전략

- `[ch01, ch03]`: 해당 장에서만 후보로 노출
- `[]` (빈 리스트): 모든 장에서 후보로 노출
- Librarian이 최종 선별하므로, 넓게 태깅해도 무방

## 3단계: 파이프라인이 자동 생성하는 것

### `source_collection` 단계 (ResearchLibrarian)

입력:
- `sources/metadata/registry.yaml` 전체 목록
- `manuscript/{chapter_id}/brief.md`
- `book/*` canonical 문서

출력:
- `sources/chapter_packs/{chapter_id}/bundle.yaml` — core/supporting 분류
- `sources/chapter_packs/{chapter_id}/notes.md` — 소스 요약 노트

### `source_analysis` 단계 (SourceAnalyst)

입력:
- `bundle.yaml`의 각 소스 항목
- `sources/raw/.../{source_id}.md` 원문 (앞 3000자)
- `book/*` canonical 문서

출력 (소스별):
- `sources/normalized/{source_id}.md` — 정규화된 분석 노트

출력 (장별):
- `sources/chapter_packs/{chapter_id}/must_cite.md` — 필수 인용 목록
- `sources/chapter_packs/{chapter_id}/counterpoints.md` — 반론과 한계점

## 이후 단계에서의 소스 사용

| 단계 | 사용하는 소스 산출물 | 길이 제한 |
|---|---|---|
| `outline_design` | `bundle.yaml` 목록 + `notes.md` | notes 2000자 |
| `draft_writing` | `notes.md` | 3000자 |
| `draft_revision` | `notes.md` + revision plan | 3000자 |
| `automated_review` (technical) | `notes.md` | 2000자 |

`must_cite.md`와 `counterpoints.md`는 현재 이후 단계 프롬프트에 자동 주입되지 않는다. 필요 시 수동으로 참고하거나, 에이전트 코드를 확장할 수 있다.

## 디렉터리 전체 구조

```
sources/
  raw/
    papers/
      anthropic_eval_2024.md        ← 사용자가 배치
      openai_simple_evals.md
    blogs/
      google_ai_testing.md
    talks/
    docs/
    interviews/
  normalized/
    anthropic_eval_2024.md          ← SourceAnalyst가 생성
    google_ai_testing.md
  metadata/
    registry.yaml                   ← 사용자가 작성
  chapter_packs/
    ch01/
      bundle.yaml                   ← ResearchLibrarian이 생성
      notes.md
      must_cite.md                  ← SourceAnalyst가 생성
      counterpoints.md
    ch02/
      ...
```

## 핵심 규칙

1. **원문 + 레지스트리는 세트**다. 레지스트리만 있으면 Librarian이 목록은 보지만 Analyst가 원문을 분석하지 못한다. 원문만 있으면 Librarian이 해당 소스의 존재를 모른다.
2. **파일명 = source_id**다. 레지스트리의 `id`와 원문 파일명(확장자 제외)이 일치해야 한다.
3. **원문은 앞부분이 중요**하다. 분석 시 3000자만 사용되므로, 핵심 내용을 앞에 배치한다.
4. **`relevance_tags`가 장 필터링**이다. 비어있으면 전체 후보, 특정 장만 넣으면 해당 장에서만 선별 대상이 된다.
5. **registry는 수동 관리**다. `SourceRegistry` 클래스가 존재하지만 현재 워크플로에서 자동 호출되지 않는다.

## 실전 예시: 3개 소스로 ch01 실행

```bash
# 1. 프로젝트 초기화
bookharness init-project --root ./book-project

# 2. 원문 배치
cp paper_a.md ./book-project/sources/raw/papers/eval_framework_2024.md
cp blog_b.md  ./book-project/sources/raw/blogs/mlops_best_practices.md
cp doc_c.md   ./book-project/sources/raw/docs/python_testing_guide.md

# 3. registry.yaml 작성 (위 형식 참고)

# 4. book/ canonical 문서 편집 (blueprint, tone_guide 등)

# 5. 파이프라인 실행
bookharness init-chapter ch01 "데모는 되는데 왜 운영은 어려울까" --root ./book-project
bookharness run-stage ch01 brief_generation --root ./book-project
bookharness run-stage ch01 source_collection --root ./book-project
bookharness run-stage ch01 source_analysis --root ./book-project
# ... 이후 단계 계속
```
