# Repository Layout Specification

## 목적

이 문서는 프로젝트 루트 아래 어떤 디렉터리와 파일이 어떤 의미를 가지는지 명확히 정의한다.

## 상위 디렉터리

### `book/`
책 전체 canonical 문서
- blueprint
- tone guide
- argument map
- concept dictionary
- chapter dependencies
- decisions log

### `sources/`
참고문헌과 chapter pack
- raw
- normalized
- metadata
- chapter_packs

### `manuscript/`
장별 원고와 리뷰 산출물
- `chXX/brief.md`
- `chXX/outline.md`
- `chXX/draft_v*.md`
- `chXX/review_*.md`
- `chXX/revision_plan_v*.md`
- `chXX/final_candidate.md`

### `memory/`
전역 맥락 문서
- global summary
- chapter summaries
- unresolved questions
- recurring examples

### `eval/`
리뷰 rubric과 structured report
- rubrics
- reports

### `workflow/`
실행 상태와 운영 메타데이터
- `chapter_states/*.json`
- `runs/*.json`
- `approvals/approvals.yaml`
- `audit_log.jsonl`
- `metadata.db`

### `prompts/`
향후 프롬프트 템플릿 확장용 디렉터리

### `scripts/`
자동화 스크립트용 디렉터리

## 파일명 규칙

### drafts
- `draft_v1.md`
- `draft_v2.md`
- ...

### reviews
- `review_technical_v1.md`
- `review_style_v1.md`
- `review_continuity_v1.md`

### plans
- `revision_plan_v1.md`

### state
- `{chapter_id}_state.json`

## 보존 규칙

- artifact 이름은 UI와 테스트가 기대하므로 함부로 바꾸지 않는다.
- 기존 파일을 덮어쓰는 대신 새 버전을 추가하는 방향을 우선한다.
