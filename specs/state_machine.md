# Chapter State Machine Specification

## 상태 필드

핵심 필드:
- `chapter_id`
- `title`
- `status`
- `current_stage`
- `approved`
- `source_pack_ready`
- `outline_ready`
- `draft_versions`
- `latest_draft`
- `review_reports`
- `revision_plan`
- `artifacts`

## 대표 status

- `not_started`
- `brief_generated`
- `source_collection_done`
- `source_analysis_done`
- `outline_ready`
- `awaiting_human_outline_approval`
- `draft_generated`
- `auto_review_done`
- `revision_ready`
- `awaiting_human_draft_approval`
- `chapter_approved`
- `locked`

## stage와 기대 결과

### `brief_generation`
- `brief.md` 생성
- status → `brief_generated`

### `source_collection`
- chapter pack bundle/notes 생성
- status → `source_collection_done`
- `source_pack_ready = true`

### `source_analysis`
- normalized source notes, must_cite, counterpoints 생성
- status → `source_analysis_done`

### `outline_design`
- `outline.md` 생성
- status → `outline_ready`
- `outline_ready = true`

### `human_approval_a`
- 자동 생성 산출물을 사람이 검토하는 대기 상태
- status → `awaiting_human_outline_approval`

### `draft_writing`
- `draft_v1.md` 생성
- status → `draft_generated`

### `automated_review`
- technical/style/continuity review 생성
- status → `auto_review_done`

### `revision_plan_synthesis`
- `revision_plan_v1.md` 생성
- status → `revision_ready`

### `draft_revision`
- `draft_v2.md` 생성
- status → `awaiting_human_draft_approval`

### `human_approval_b`
- 승인 대기 gate
- 실제 승인은 `approve(...)`에서 처리

## 승인 처리 규칙

### Approval A
허용 결과:
- `approved`
- `approved_with_notes`
- `revision_requested`
- `rejected`

### Approval B
허용 결과:
- `approved`
- `approved_with_notes`
- `revision_requested`
- `rejected`

Approval B가 `approved` 또는 `approved_with_notes`이면:
- `final_candidate.md` 생성
- chapter summary 생성
- global summary 갱신
- `approved = true`
- status → `chapter_approved`
