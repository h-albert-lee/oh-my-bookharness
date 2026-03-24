# Documentation Index

이 디렉토리는 **인간 기여자**와 **코드 어시스턴트**가 `oh-my-bookharness`를 빠르게 이해하고 변경할 수 있도록 만든 운영 문서 모음이다.

## 문서 맵

### 빠른 시작
- `docs/getting_started.md`
  - 로컬 설치
  - CLI/API/UI 실행 방법
  - 가장 짧은 end-to-end 시나리오

### 아키텍처
- `docs/architecture.md`
  - 도메인 엔진과 API/UI 레이어의 관계
  - 주요 디렉토리 설명
  - 데이터 흐름

### 에이전트 파이프라인
- `docs/agent_pipeline.md`
  - 전체 파이프라인 흐름도
  - 에이전트별 역할, 입력, 산출물
  - 프롬프트 4계층 구조
  - 컨텍스트 흐름 다이어그램
  - 비-LLM 구성요소 (AcceptanceGate, BinaryGateChecker, SummaryBuilder)

### 참고문헌 제공
- `docs/sources_guide.md`
  - 원문 파일 배치 규칙
  - 레지스트리(registry.yaml) 작성법
  - 파이프라인 자동 산출물
  - 이후 단계에서의 소스 사용 범위
  - 실전 예시

### 백엔드
- `docs/backend.md`
  - FastAPI 앱 구조
  - 서비스 레이어 역할
  - job/audit/metadata index 설계

### 프론트엔드
- `docs/frontend.md`
  - 정적 dashboard UI 구조
  - 화면별 책임
  - API 연동 방식

### 운영/유지보수
- `docs/operations.md`
  - 스캐폴딩 규칙
  - canonical 문서 보호 규칙
  - job/approval/audit 운영 팁

### 코드 어시스턴트용 가이드
- `docs/assistant_guide.md`
  - 변경 전에 읽을 파일
  - 안전한 변경 순서
  - 자주 하는 실수와 회피법

## specs/와의 관계

`docs/`가 설명 중심 문서라면, `specs/`는 더 엄격한 계약 문서다.

- `specs/system_spec.md`: 시스템 전체 계약
- `specs/state_machine.md`: 장 상태와 stage 전이 규칙
- `specs/api_contract.md`: REST API 요청/응답 계약
- `specs/repository_layout.md`: 산출물 디렉터리와 파일 규칙

## 권장 읽기 순서

### 사람(개발자/편집자)
1. `README.md`
2. `docs/getting_started.md`
3. `docs/architecture.md`
4. `docs/agent_pipeline.md`
5. `docs/sources_guide.md`
6. `docs/backend.md` 또는 `docs/frontend.md`
7. 필요 시 `specs/*`

### 코드 어시스턴트
1. `docs/assistant_guide.md`
2. `specs/system_spec.md`
3. `specs/state_machine.md`
4. 작업 대상 모듈의 구현 파일
