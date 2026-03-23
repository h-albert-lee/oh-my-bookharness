# Getting Started

## 1. 설치

```bash
python -m pip install -e .[dev]
```

## 2. 프로젝트 초기화

```bash
bookharness init-project --root ./book-project
```

생성되는 핵심 디렉터리:
- `book/`
- `sources/`
- `manuscript/`
- `memory/`
- `eval/`
- `workflow/`

## 3. CLI로 장 생성 및 실행

```bash
bookharness init-chapter ch01 "데모는 되는데 왜 운영은 어려울까" --root ./book-project
bookharness run-stage ch01 brief_generation --root ./book-project
bookharness run-stage ch01 source_collection --root ./book-project
bookharness run-stage ch01 source_analysis --root ./book-project
bookharness run-stage ch01 outline_design --root ./book-project
bookharness run-stage ch01 draft_writing --root ./book-project
bookharness run-stage ch01 automated_review --root ./book-project
bookharness run-stage ch01 revision_plan_synthesis --root ./book-project
bookharness run-stage ch01 draft_revision --root ./book-project
bookharness approve ch01 approval_b approved --root ./book-project
```

## 4. API/UI 실행

```bash
bookharness serve --root ./book-project --host 127.0.0.1 --port 8000
```

또는:

```bash
bookharness-api --root ./book-project --host 127.0.0.1 --port 8000
```

열기:
- UI: `http://127.0.0.1:8000/`
- API docs는 현재 별도 문서 기반으로 운영하며, 엔드포인트 목록은 `specs/api_contract.md` 참고

## 5. 가장 짧은 UI 워크플로

1. Dashboard에서 chapter 생성
2. Chapter Detail에서 stage 버튼 클릭
3. Draft/Review 산출물 확인
4. Approval Queue 또는 Chapter Detail에서 승인 제출
5. 승인 후 `final_candidate.md`와 `memory/chapter_summaries/*.md` 확인

## 6. 테스트

```bash
python -m pytest
```
