# Assistant Guide

이 문서는 코드 어시스턴트가 이 저장소를 수정할 때 먼저 읽어야 하는 실무 가이드다.

## 1. 먼저 이해해야 할 것

### 핵심 철학
이 저장소의 중심은:
- 상태 기반 workflow
- 파일 기반 canonical memory
- human approval gate
- review-first 편집 구조

즉, "그럴듯한 텍스트 생성"보다 "재현 가능한 단계 운영"이 더 중요하다.

## 2. 변경 전에 읽을 파일

최소 권장 순서:
1. `README.md`
2. `specs/system_spec.md`
3. `specs/state_machine.md`
4. 작업 대상에 따라 아래 중 선택
   - 워크플로 변경: `src/bookharness/orchestrator/runner.py`
   - 상태 변경: `src/bookharness/models/chapter_state.py`
   - API 변경: `src/bookharness_api/routers/*`, `services/*`
   - UI 변경: `src/bookharness_api/static/*`

## 3. 안전한 변경 패턴

### 워크플로 변경 시
- stage 이름을 바꾸면 API/UI/tests/docs를 같이 바꿔야 한다.
- approval 단계 의미를 바꾸면 `specs/state_machine.md`도 갱신해야 한다.
- artifact 파일명이 바뀌면 diff viewer와 chapter detail UI가 깨질 수 있다.

### API 변경 시
- router만 수정하지 말고 service와 docs/specs/tests를 같이 갱신한다.
- background job 응답 형태를 바꾸면 UI polling 코드와 `tests/test_api.py`가 영향을 받는다.

### UI 변경 시
- 가능한 한 API contract를 깨지 않는다.
- chapter detail 화면은 항상 approval 흐름이 보이게 유지한다.

## 4. 자주 하는 실수

1. canonical 파일을 앱 시작 시 덮어쓰기
2. metadata DB를 source of truth처럼 다루기
3. approval 없이 final candidate를 생성하기
4. state/status는 바뀌었는데 artifact는 안 만드는 경우
5. artifact 파일명 규칙을 무심코 바꾸는 경우

## 5. 변경 후 최소 확인

```bash
python -m pytest
```

추가로 가능하면:
- chapter API smoke run
- approval flow smoke run
- UI root page 응답 확인
