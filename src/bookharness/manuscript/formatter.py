from __future__ import annotations

from bookharness.utils.markdown import bullet_list, section


class MarkdownFormatter:
    def chapter_brief(
        self,
        chapter_id: str,
        title: str,
        dependencies: list[str],
        prior_summaries: list[str],
    ) -> str:
        return "\n".join(
            [
                f"# Chapter Brief: {chapter_id}",
                "",
                f"## 제목\n\n{title}",
                "",
                section("이 장의 목표", "- 책 전체 논지 안에서 장의 역할을 분명히 정의한다."),
                section("독자가 얻을 것", "- 데모 수준의 설명이 아닌 운영 가능한 AI 시스템 관점을 이해한다."),
                section("장의 핵심 질문", "- 이 장이 해결해야 할 질문을 문서화한다."),
                section("반드시 들어갈 개념", bullet_list(["system vs. model", "workflow state", "human approval gate"])),
                section("피해야 할 오해", bullet_list(["LLM이 알아서 문맥을 기억할 것이라는 가정", "출처 없는 단정"])),
                section("앞 장과의 연결", bullet_list(dependencies or ["선행 장 의존성이 아직 없다."])),
                section("뒤 장으로의 연결", "- 이후 장에서 source pack, review loop, global memory로 연결한다."),
                section(
                    "원하는 톤 메모",
                    bullet_list(
                        [
                            "독자 안내형 설명체를 사용한다.",
                            "선언문처럼 시작하지 않는다.",
                            "과장된 수사와 자기 고양적 표현을 피한다.",
                        ]
                    ),
                ),
                section("참고할 이전 장 요약", bullet_list(prior_summaries or ["아직 승인된 이전 장 요약이 없다."])),
            ]
        )

    def outline(self, chapter_id: str, title: str) -> str:
        ch_num = int("".join(c for c in chapter_id if c.isdigit()) or "0")
        return f"""# Outline: {chapter_id}

## 장 제목

**{ch_num}장. {title}**

## 장 전체 Argument Flow

(이 장의 전체 논증 흐름을 한 문단으로 서술)

### Section {ch_num}.1 문제 설정
- 목적: 독자에게 이 장이 다룰 운영 문제를 소개한다.
- 사용 source: core source 1, supporting source 1
- 포함할 예시: 데모는 성공했지만 운영에서 실패한 QA 시스템 사례
- 핵심 요점: 모델 품질과 시스템 품질은 다르다.
- 연결 아이디어: 문제를 정의한 뒤 왜 상태 기반 워크플로가 필요한지로 전환한다.
- 구조물 배치: <!-- note: 핵심 용어 정의 -->, <!-- table: 표 {ch_num}-1. 비교표 -->

#### {ch_num}.1.1 (중제목 예시)
#### {ch_num}.1.2 (중제목 예시)

### Section {ch_num}.2 상태 기반 워크플로의 필요성
- 목적: 자유 대화형 멀티에이전트보다 deterministic workflow가 적합한 이유를 설명한다.
- 사용 source: core source 2
- 포함할 예시: brief → outline → draft → review → approval 파이프라인
- 핵심 요점: 재실행과 승인 게이트가 있어야 긴 집필 작업을 통제할 수 있다.
- 연결 아이디어: 워크플로에서 문서 중심 메모리로 자연스럽게 넘어간다.
- 구조물 배치: <!-- box: 참고사항 제목 -->, <!-- figure: 그림 {ch_num}-1. 다이어그램 -->

#### {ch_num}.2.1 (중제목 예시)
#### {ch_num}.2.2 (중제목 예시)

### Section {ch_num}.3 문서 중심 메모리와 리뷰 루프
- 목적: canonical docs, chapter summaries, review loop가 품질을 유지하는 이유를 설명한다.
- 사용 source: core source 3, supporting source 2
- 포함할 예시: concept dictionary와 must-cite list
- 핵심 요점: 생성보다 리뷰와 수정 구조가 중요하다.
- 연결 아이디어: 다음 장에서 세부 구현 모듈로 이어지도록 정리한다.
- 구조물 배치: <!-- tip: 실무 권장사항 -->

#### {ch_num}.3.1 (중제목 예시)
#### {ch_num}.3.2 (중제목 예시)
"""
