# Architecture Overview

## 목표

이 시스템은 자유 대화형 에이전트 군집이 아니라, **상태 기반 편집 워크플로 엔진**을 중심으로 설계되어 있다.

핵심 원칙:
- 파일 기반 canonical 문서 유지
- deterministic stage 실행
- human approval gate 명시화
- 승인 전 문서를 canonical memory로 승격하지 않음
- UI와 API는 도메인 엔진 위의 얇은 서비스 계층

## 레이어 구성

### 1. Domain Engine: `src/bookharness/`
역할:
- chapter state 생성/저장
- workflow stage 실행
- manuscript/source/review/memory 산출물 작성
- approval 반영 후 final candidate와 memory 갱신

중심 파일:
- `src/bookharness/orchestrator/runner.py`
- `src/bookharness/orchestrator/state_manager.py`
- `src/bookharness/models/chapter_state.py`

### 2. Application/API Layer: `src/bookharness_api/`
역할:
- HTTP 요청 처리
- background job queue
- audit log 기록
- metadata DB 인덱싱
- artifact read/diff API
- dashboard UI 정적 파일 서빙

중심 파일:
- `src/bookharness_api/app.py`
- `src/bookharness_api/services/job_service.py`
- `src/bookharness_api/services/project_service.py`
- `src/bookharness_api/services/metadata_index.py`

### 3. Static UI: `src/bookharness_api/static/`
역할:
- dashboard 렌더링
- approval queue
- chapter detail
- artifact viewer / diff viewer

## 데이터 흐름

### CLI 경로
1. 사용자가 `bookharness` 명령 실행
2. `WorkflowRunner`가 stage 수행
3. 산출물이 파일 시스템에 기록됨
4. chapter state JSON 갱신
5. approval 시 final candidate / memory 갱신

### API/UI 경로
1. 브라우저가 API 호출
2. `ChapterService`/`ProjectService`가 요청 해석
3. `JobService`가 비동기 작업 파일 생성
4. worker thread가 `WorkflowRunner` 호출
5. 결과가 `workflow/runs/*.json`, `audit_log.jsonl`, `metadata.db`에 반영
6. UI가 polling으로 상태 갱신

## canonical source of truth

우선순위:
1. 파일 시스템 산출물 (`book/`, `sources/`, `manuscript/`, `memory/`, `workflow/`)
2. SQLite metadata index (`workflow/metadata.db`) — 조회 가속용 캐시

즉, DB는 canonical이 아니다.
