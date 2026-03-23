# System Specification

## 목적

`bookharness`는 장기 책 집필을 위한 **deterministic, markdown-first workflow system**이다.

## 핵심 요구사항

1. 장 단위 state를 영속 저장해야 한다.
2. 장 산출물은 파일로 남아야 한다.
3. workflow는 stage별로 재실행 가능해야 한다.
4. approval은 명시적 gate여야 한다.
5. 승인 전 draft는 canonical memory가 아니다.
6. API/UI는 도메인 엔진의 규칙을 우회하면 안 된다.

## 시스템 경계

### 포함
- chapter initialization
- brief/source/outline/draft/review/revision/approval workflow
- artifact persistence
- approval recording
- dashboard/API 조회
- job audit and metadata indexing

### 비포함
- 고급 문서 협업 편집기
- 출판용 조판 파이프라인
- citation formatter 통합
- 복수 사용자 인증/권한 완성형 구현

## canonical vs derived

### canonical
- `book/*`
- `sources/*`
- `manuscript/*`
- `memory/*`
- `workflow/chapter_states/*`
- `workflow/approvals/approvals.yaml`
- `workflow/runs/*.json`
- `workflow/audit_log.jsonl`

### derived/cache
- `workflow/metadata.db`
- UI rendered HTML
- diff 계산 결과

## 변경 불변조건

1. approval_b 승인 없이는 `final_candidate.md`를 만들지 않는다.
2. summary/global summary는 승인된 chapter만 반영한다.
3. chapter state의 `latest_draft`는 실제 존재 파일과 일치해야 한다.
4. review report와 revision plan은 별도 파일이어야 한다.
