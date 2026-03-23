# Backend Guide

## FastAPI 앱 구조

엔트리포인트:
- `src/bookharness_api/app.py`
- `src/bookharness_api/main.py`

라우터:
- `routers/project.py`
- `routers/chapters.py`
- `routers/approvals.py`
- `routers/artifacts.py`
- `routers/runs.py`

## 서비스 레이어

### `ChapterService`
책임:
- 장 초기화
- stage 실행 job 큐잉
- MVP job 큐잉
- approval job 큐잉

### `JobService`
책임:
- `workflow/runs/*.json` 생성
- worker thread에서 `WorkflowRunner` 호출
- 상태 변경 기록
- approval 대기 / 실패 / 성공 상태 기록
- audit 기록과 metadata index 동기화 트리거

상태값:
- `queued`
- `running`
- `succeeded`
- `failed`
- `waiting_for_approval`

### `ProjectService`
책임:
- dashboard 요약 데이터 제공
- chapter detail payload 구성
- pending approval 계산

### `ArtifactService`
책임:
- markdown/json/yaml/text 산출물 읽기
- markdown HTML 변환
- draft diff 생성

### `MetadataIndex`
책임:
- `workflow/metadata.db` 초기화
- chapter state / approvals / runs / review scores / audit log 색인
- UI 조회 속도 향상

## 감사 로그

파일:
- `workflow/audit_log.jsonl`

현재 기록 이벤트 예시:
- `chapter_initialized`
- `stage_requested`
- `mvp_requested`
- `approval_requested`
- `job_queued`
- `job_completed`
- `job_waiting_for_approval`
- `job_failed`
- `final_candidate_generated`

## 주의사항

1. 파일이 canonical source of truth다.
2. metadata DB는 재생성 가능해야 한다.
3. API는 가능하면 도메인 엔진 규칙을 우회하지 않는다.
4. approval은 반드시 `WorkflowRunner.approve(...)`를 통해 처리한다.
