# Operations Guide

## 프로젝트 루트 운영 규칙

### 절대 원칙
- `book/*` canonical 문서는 자동으로 덮어쓰지 않는다.
- 승인되지 않은 draft는 canonical memory로 취급하지 않는다.
- review 결과는 원문을 직접 덮어쓰지 않는다.
- 모든 핵심 산출물은 버전명을 가진다.

## 중요한 파일

### state / runs / approvals
- `workflow/chapter_states/*.json`
- `workflow/runs/*.json`
- `workflow/approvals/approvals.yaml`
- `workflow/audit_log.jsonl`

### memory
- `memory/global_summary.md`
- `memory/chapter_summaries/*.md`
- `memory/unresolved_questions.md`
- `memory/recurring_examples.md`

## 장애 대응

### job stuck
확인 순서:
1. `workflow/runs/*.json`
2. `workflow/audit_log.jsonl`
3. `workflow/chapter_states/*.json`
4. `eval/reports/*`

### metadata index mismatch
대응:
- `workflow/metadata.db`는 캐시로 간주
- 삭제 후 앱 재기동 또는 `MetadataIndex.sync_all()` 호출로 재구성 가능

### approval 반영 이상
확인:
- `workflow/approvals/approvals.yaml`
- `manuscript/chXX/final_candidate.md`
- `memory/chapter_summaries/chXX.md`

## 안전한 수동 수정

가능:
- Markdown 산출물 내용 수동 편집
- approvals note 보강
- source registry 정리

주의:
- stage/status와 실제 artifact가 불일치하지 않도록 해야 한다.
- 수동 수정 뒤에는 UI나 API 조회 전에 관련 state를 재검토한다.
