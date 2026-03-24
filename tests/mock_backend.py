"""Mock LLM backend for testing.

Returns realistic, pre-crafted responses for each agent role.
Matches on system prompt substrings to determine which agent is calling.
"""

from __future__ import annotations


BRIEF_RESPONSE = """# Chapter Brief: {chapter_id}

## 제목

{title}

## 이 장의 목표

- 책 전체 논지 안에서 이 장의 역할을 분명히 정의한다.
- 독자가 이 장을 통해 핵심 개념을 실무에 적용할 수 있도록 안내한다.

## 독자가 얻을 것

- 운영 가능한 AI 시스템 관점에서의 핵심 이해
- 실무 적용 가능한 구체적 지식

## 장의 핵심 질문

- 이 주제가 실무에서 왜 중요한가?
- 기존 접근 방식의 한계는 무엇인가?
- 어떤 대안이 있는가?

## 반드시 들어갈 개념

- system_vs_model
- workflow state
- human approval gate

## 피해야 할 오해

- LLM이 알아서 문맥을 기억할 것이라는 가정
- 출처 없는 단정적 표현

## 앞 장과의 연결

- 이전 장에서 다룬 기초 개념을 기반으로 한다.

## 뒤 장으로의 연결

- 이후 장에서 더 깊은 구현 세부사항을 다룬다.

## 원하는 톤 메모

- 독자 안내형 설명체를 사용한다.
- 선언문처럼 시작하지 않는다.

## 참고할 이전 장 요약

- 아직 승인된 이전 장 요약이 없다.
"""

SOURCE_BUNDLE_RESPONSE = """## Bundle

```yaml
chapter_id: {chapter_id}
core_sources:
  - source_id: core_source_1
    title: "핵심 자료 1"
    authority: high
    why_it_matters: "이 장의 핵심 논지를 직접 지지한다."
    expected_usage: "정의와 사례 제공"
    quality_score: 5
supporting_sources:
  - source_id: supporting_source_1
    title: "보조 자료 1"
    authority: medium
    why_it_matters: "핵심 설명을 보완한다."
    expected_usage: "보조 사례 제공"
    quality_score: 3
```

## Notes

# {chapter_id} Source Pack Notes

## Core Sources

### core_source_1
- authority: high
- 활용 방향: 핵심 논지를 직접 지지하는 자료
- 예상 사용처: 정의와 사례 제공

## Supporting Sources

### supporting_source_1
- authority: medium
- 활용 방향: 핵심 설명 보완
"""

SOURCE_NOTE_RESPONSE = """# Source Note: {source_id}

## 핵심 주장

- 이 자료는 AI 시스템의 운영 과제를 체계적으로 분석한다.
- 데모와 운영 환경의 차이를 구체적 사례로 설명한다.

## 책에 활용 가능한 포인트

- 운영 환경에서의 실패 패턴 분류
- 평가 체계의 필요성 논증

## 이 장과의 관련성

- 이 장의 핵심 논지를 직접 지지하는 근거를 제공한다.

## 주의할 점 / 한계

- 특정 도메인에 한정된 사례일 수 있다.
- 일반화 시 조건을 명시해야 한다.

## 인용 시 주의 표현

- "~에 따르면" 형식으로 출처를 명시한다.
- 단정 표현을 피한다.
"""

OUTLINE_RESPONSE = """# Outline: {chapter_id}

## 장 제목

{title}

## Argument Flow

이 장은 독자에게 핵심 문제를 소개하고, 개념을 정의한 뒤, 실무 사례와 함께 분석하며, 마지막으로 정리와 다음 장 예고로 마무리한다.

## Section 1. 도입: 이 장에서 다루는 것

- **목적**: 독자에게 이 장의 범위와 중요성을 설명한다.
- **사용 source**: core_source_1
- **포함할 예시**: 실무에서 마주치는 구체적 상황
- **핵심 요점**: 왜 이 주제가 중요한가
- **연결 아이디어**: 문제 제시 후 개념 분석으로 전환

## Section 2. 핵심 개념과 배경

- **목적**: 핵심 용어와 개념을 정의한다.
- **사용 source**: core_source_1, supporting_source_1
- **포함할 예시**: concept_dictionary 용어 설명
- **핵심 요점**: 핵심 개념의 정의와 관계
- **연결 아이디어**: 개념에서 실무 적용으로 전환

## Section 3. 심화 분석과 사례

- **목적**: 핵심 개념을 깊이 분석하고 사례를 제시한다.
- **사용 source**: core_source_1
- **포함할 예시**: 구체적 구현 사례
- **핵심 요점**: 이론과 실무의 연결
- **연결 아이디어**: 사례에서 정리로 전환

## Section 4. 정리와 다음 장 예고

- **목적**: 핵심 내용을 정리하고 다음 장을 예고한다.
- **사용 source**: 없음
- **포함할 예시**: 없음
- **핵심 요점**: 이 장의 핵심 메시지 3개
- **연결 아이디어**: 다음 장 주제 예고
"""

DRAFT_RESPONSE = """# {title}

이 장에서는 {title}을 다룬다. 먼저 이 주제가 왜 중요한지 살펴보고, 핵심 개념을 정의한 뒤, 실무에서 어떻게 적용되는지 사례와 함께 설명한다.

## 도입: 이 장에서 다루는 것

AI 시스템을 설계하고 운영하는 과정에서 가장 흔하게 마주치는 문제 중 하나는 데모 환경과 운영 환경의 격차다. 데모에서 잘 작동하던 시스템이 운영 환경에서 예상치 못한 방식으로 실패하는 경우가 빈번하다.[^core_source_1]

이 격차가 발생하는 근본적인 이유는 AI 시스템이 단순한 모델이 아니라 복잡한 소프트웨어 시스템이기 때문이다. 모델의 성능만으로는 시스템의 운영 품질을 보장할 수 없다.

이 장에서는 이 문제를 체계적으로 분석하고, 운영 가능한 AI 시스템을 위한 핵심 원칙을 정리한다.

## 핵심 개념과 배경

**시스템 대 모델**(system vs. model) 관점에서 보면, AI 애플리케이션은 모델 하나가 아니라 데이터 파이프라인, 전처리, 후처리, 모니터링, 평가 체계를 포함하는 전체 시스템이다.[^core_source_1]

**평가 하네스**(evaluation harness)는 이러한 시스템의 품질을 반복 가능하게 검증하기 위한 외부 구조다. 단순한 단위 테스트와는 달리, 평가 하네스는 시스템의 출력 품질을 다양한 관점에서 측정한다.

**워크플로 상태**(workflow state) 관리는 장기적인 시스템 운영에서 필수적이다. 각 단계의 입력과 출력이 명확해야 하며, 실패 시 해당 단계만 재실행할 수 있어야 한다.

## 심화 분석과 사례

앞서 정의한 개념을 실제 사례에 적용해 보자. 문서 QA 시스템을 예로 들면, 데모 환경에서는 미리 준비된 문서와 질문으로 높은 정확도를 보여줄 수 있다. 그러나 운영 환경에서는 예상치 못한 문서 형식, 모호한 질문, 컨텍스트 창 초과 등의 문제가 발생한다.[^supporting_source_1]

이러한 격차를 줄이기 위해서는 평가 하네스를 통한 체계적인 품질 측정이 필요하다. 평가 하네스는 다음과 같은 요소를 포함한다:

- 대표적인 테스트 케이스 세트
- 자동화된 품질 측정 메트릭
- 운영 환경을 모사하는 시나리오
- 회귀 테스트 파이프라인

## 정리와 다음 장 예고

이 장에서는 다음 핵심 메시지를 다루었다.

1. AI 시스템은 모델이 아니라 시스템으로 봐야 한다.
2. 데모 성공과 운영 성공은 근본적으로 다르다.
3. 체계적인 평가 구조가 운영 품질의 핵심이다.

다음 장에서는 이 평가 체계를 더 깊이 살펴보고, 평가 주도 개발(EDD) 접근 방식을 소개한다.

---

## 참고 문헌

[^core_source_1]: core_source_1 참조
[^supporting_source_1]: supporting_source_1 참조
"""

TECHNICAL_REVIEW_RESPONSE = """```json
{
  "must_fix": [],
  "should_fix": [
    "핵심 개념 정의가 concept dictionary와 정확히 일치하는지 재확인한다."
  ],
  "nice_to_have": [
    "deterministic component와 conventional tests의 관계를 한 문장 추가할 수 있다."
  ],
  "score": {
    "technical_accuracy": 4,
    "source_grounding": 4,
    "clarity": 4
  }
}
```"""

STYLE_REVIEW_RESPONSE = """```json
{
  "must_fix": [],
  "should_fix": [
    "장 도입부가 독자 안내형 설명체를 유지하는지 확인한다."
  ],
  "nice_to_have": [
    "예시 문장을 조금 더 실무적인 장면으로 조정할 수 있다."
  ],
  "score": {
    "tone_fit": 4,
    "reader_friendliness": 4,
    "redundancy": 5
  }
}
```"""

CONTINUITY_REVIEW_RESPONSE = """```json
{
  "must_fix": [],
  "should_fix": [
    "이전 장 요약과 연결되는 전이 문장을 보강한다."
  ],
  "nice_to_have": [
    "다음 장 예고를 한 문단 더 명확히 쓸 수 있다."
  ],
  "score": {
    "continuity": 4,
    "dependency_coverage": 5
  }
}
```"""

REVISION_PLAN_RESPONSE = """# Revision Plan: {chapter_id}

## Score Summary

### technical
- technical_accuracy: 4/5 ✓
- source_grounding: 4/5 ✓
- clarity: 4/5 ✓
- must_fix: 0건
- should_fix: 1건

## Must Fix

- 없음

## Should Fix

- 핵심 개념 정의가 concept dictionary와 정확히 일치하는지 재확인한다.
- 장 도입부가 독자 안내형 설명체를 유지하는지 확인한다.
- 이전 장 요약과 연결되는 전이 문장을 보강한다.

## Optional Improvements

- deterministic component와 conventional tests의 관계를 한 문장 추가할 수 있다.
- 예시 문장을 조금 더 실무적인 장면으로 조정할 수 있다.

## Contradictory Comments

- 상충하는 리뷰 의견이 감지되지 않았다.

## Rewrite Instructions for Writer

1. concept_dictionary의 선호 한국어 표현을 확인하고 일관되게 사용한다.
2. 장 도입부를 독자 안내형 설명체로 유지한다.
3. 이전 장과의 연결 문장을 보강한다.
"""


# Agent role keywords for matching
_ROLE_RESPONSES = {
    "편집장": BRIEF_RESPONSE,
    "Chief Editor": BRIEF_RESPONSE,
    "연구 사서": SOURCE_BUNDLE_RESPONSE,
    "Research Librarian": SOURCE_BUNDLE_RESPONSE,
    "자료 분석가": SOURCE_NOTE_RESPONSE,
    "Source Analyst": SOURCE_NOTE_RESPONSE,
    "장 설계자": OUTLINE_RESPONSE,
    "Chapter Architect": OUTLINE_RESPONSE,
    "집필자": DRAFT_RESPONSE,
    "Draft Writer": DRAFT_RESPONSE,
    "기술 리뷰어": TECHNICAL_REVIEW_RESPONSE,
    "Technical Reviewer": TECHNICAL_REVIEW_RESPONSE,
    "문체 리뷰어": STYLE_REVIEW_RESPONSE,
    "Style Reviewer": STYLE_REVIEW_RESPONSE,
    "연속성 리뷰어": CONTINUITY_REVIEW_RESPONSE,
    "Continuity Reviewer": CONTINUITY_REVIEW_RESPONSE,
    "수정 통합자": REVISION_PLAN_RESPONSE,
    "Revision Synthesizer": REVISION_PLAN_RESPONSE,
}


class MockLLMBackend:
    """Test-only LLM backend that returns pre-crafted responses."""

    def __init__(self, overrides: dict[str, str] | None = None) -> None:
        self.overrides = overrides or {}
        self.calls: list[tuple[str, str]] = []

    def generate(self, system: str, user: str, *, max_tokens: int | None = None) -> str:
        self.calls.append((system, user))

        # Check overrides first
        for key, response in self.overrides.items():
            if key in system or key in user:
                return self._fill_template(response, user)

        # Match by agent role keyword
        for keyword, response in _ROLE_RESPONSES.items():
            if keyword in system:
                return self._fill_template(response, user)

        return "# Generated Content\n\nMock response for unmatched agent."

    def _fill_template(self, template: str, user: str) -> str:
        """Fill {chapter_id} and {title} placeholders from user prompt."""
        chapter_id = self._extract(user, "chapter_id:")
        title = self._extract(user, "제목:")
        source_id = self._extract(user, "source_id:")
        return (
            template
            .replace("{chapter_id}", chapter_id or "chXX")
            .replace("{title}", title or "제목 미정")
            .replace("{source_id}", source_id or "unknown_source")
        )

    @staticmethod
    def _extract(text: str, prefix: str) -> str | None:
        for line in text.splitlines():
            stripped = line.strip().lstrip("- ")
            if stripped.startswith(prefix):
                return stripped[len(prefix):].strip()
        return None
