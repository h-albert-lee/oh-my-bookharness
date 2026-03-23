# API Contract

## Base
- UI root: `/`
- Static assets: `/static/*`
- JSON API: `/api/*`

## Project

### `GET /api/project`
반환:
- title
- blueprint_preview
- chapters[]
- pending_approvals[]
- recent_runs[]
- metrics{}

### `GET /api/project/chapters`
반환:
- chapter summary list

## Chapters

### `POST /api/chapters`
입력:
```json
{
  "chapter_id": "ch01",
  "title": "데모는 되는데 왜 운영은 어려울까",
  "dependencies": ["ch00_blueprint"],
  "actor": "editor"
}
```

### `GET /api/chapters/{chapter_id}`
반환:
- state
- artifacts
- approvals
- review_reports
- runs
- audit

### `GET /api/chapters/{chapter_id}/artifacts`
반환:
- chapter 관련 artifact 목록

### `POST /api/chapters/{chapter_id}/run-stage`
입력:
```json
{
  "stage": "brief_generation",
  "actor": "ui-editor"
}
```
반환:
- queued job payload

### `POST /api/chapters/{chapter_id}/run-mvp`
입력:
```json
{
  "title": "데모는 되는데 왜 운영은 어려울까",
  "dependencies": [],
  "actor": "ui-editor"
}
```

### `POST /api/chapters/{chapter_id}/approve`
입력:
```json
{
  "approval_key": "approval_b",
  "result": "approved",
  "notes": ["looks good"],
  "actor": "editor_in_chief"
}
```

## Approvals

### `GET /api/approvals/pending`
반환:
- approval 대기 chapter 목록

### `GET /api/approvals/{chapter_id}`
반환:
- chapter approval payload

## Artifacts

### `GET /api/artifacts?path=...`
반환:
- path
- kind
- content
- rendered_html
- modified_at

### `GET /api/artifacts/diff?left=...&right=...`
반환:
- left_path
- right_path
- left_only[]
- right_only[]
- changed[]

## Runs

### `GET /api/runs`
반환:
- recent jobs

### `GET /api/runs/{job_id}`
반환:
- single job payload
