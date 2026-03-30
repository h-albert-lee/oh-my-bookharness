# Search: LLM evaluation framework design "evaluation-driven" OR "eval-driven" graded scoring beyond pass fail benchmark

아래는 검색 결과를 바탕으로 정리한 자료입니다. 실제로 확인된 자료만 포함하였으며, 각 자료의 출처·저자·유형·URL·요약·핵심 주장을 JSON 형식으로 제공합니다.

---

다음은 검색을 통해 확인한 자료들의 개요입니다:



EDDOps 논문은 TDD/BDD가 LLM 에이전트 환경에서 갖는 한계를 명시적으로 분석합니다. 이 논문은 TDD/BDD가 안정적인 명세와 실행 가능한 오라클을 가정하는 반면, LLM 에이전트는 비결정론적이고 배포 후에도 계속 적응하기 때문에 이들 방법론만으로는 충분하지 않다고 주장합니다.





실무 가이드(Pragmatic Engineer)에서도 TDD의 근본적 한계를 지적합니다. TDD는 "주어진 입력에 대해 단일하고 결정론적으로 알 수 있는 정답이 있다"는 전제 위에서 작동하지만, LLM에서는 그것이 사실이 아닙니다. 정답이 수천 개일 수 있고, 입력의 무한한 표면적만이 문제가 아니라 유효하고 주관적이며 예측 불가한 출력의 광대한 공간이 도전입니다.





Anthropic 엔지니어링 블로그는 부분 점수(partial credit) 개념을 실질적으로 다룹니다. "여러 구성 요소를 가진 작업에서는 부분 점수를 반영하라. 문제를 올바르게 식별하고 고객을 확인했지만 환불 처리는 하지 못한 지원 에이전트는, 즉시 실패한 에이전트보다 의미 있게 낫다. 이 성공의 연속체를 결과에 표현하는 것이 중요하다."



이제 JSON 형식으로 최종 정리합니다:

```json
[
  {
    "title": "Evaluation-Driven Development and Operations of LLM Agents: A Process Model and Reference Architecture",
    "authors": ["저자 미상 (arXiv 2411.13768)"],
    "year": 2025,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2411.13768",
    "summary": "TDD/BDD가 LLM 에이전트 환경에서 왜 무력화되는지를 네 가지 구조적 한계(정적 요구사항 의존, 이진 pass/fail 단언, 배포 전 검증 집중, 창발적 행동 미지원)로 체계적으로 분석한다. 이를 대체하는 EDDOps(평가 주도 개발·운영) 프레임워크를 제안하며, TDD↔EDDOps 비교표도 제공한다. ch02에서 '왜 TDD가 무너지는가'를 논증하는 구조적 근거로 직접 인용 가능하다.",
    "key_claims": [
      "TDD/BDD는 (i) 정적 요구사항과 실행 가능한 오라클 의존, (ii) 맥락 의존적 결과를 포착하지 못하는 이진 pass/fail, (iii) 런타임 드리프트를 무시하는 배포 전 집중, (iv) 창발적 행동·안전·공정성 지원 부재 등 네 가지 한계로 LLM 에이전트를 제대로 지원하지 못한다.",
      "LLM 에이전트 출력은 '등급화(graded)'되거나 비교 평가될 수 있으며, 판정에는 플러그인 가능한 판사(judge) 또는 인간 감독이 필요하다.",
      "EDDOps는 평가를 일회성 게이트가 아니라 설계 시점부터 런타임까지 걸친 지속적 역량으로 취급한다."
    ]
  },
  {
    "title": "Demystifying Evals for AI Agents",
    "authors": ["Mikaela Grace", "Jeremy Hadfield", "Rodrigo Olivares", "Jiri De Jonghe"],
    "year": 2026,
    "type": "blog_post",
    "url": "https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents",
    "summary": "Anthropic 엔지니어링 블로그로, 실제 프로덕션 배포 경험에서 도출한 에이전트 평가 전략을 체계화한다. pass/fail을 넘어 부분 점수(partial credit), 다차원 성공 기준, LLM 루브릭 채점, 상태 검사 등을 조합하는 방법을 구체적 코드 예시와 함께 제시한다. ch02에서 'EDD가 어떻게 TDD의 빈자리를 채우는가'를 실용적으로 설명하는 산업 사례로 활용할 수 있다.",
    "key_claims": [
      "에이전트 평가에서 성공은 다차원적이다—티켓 해결 여부(상태 검사), 10턴 이내 완료(트랜스크립트 제약), 어조 적절성(LLM 루브릭) 등을 복합적으로 측정해야 한다.",
      "여러 구성 요소를 가진 작업에는 부분 점수를 반영해야 하며, 이는 성공의 연속체(continuum)를 결과에 표현한다는 원칙이다.",
      "결정론적(코드 기반) 채점기를 우선 쓰고, 불가피한 경우 LLM 기반 채점기를 보완하며, 인간 채점은 주로 캘리브레이션 용도로 사용하라는 실용적 원칙을 제시한다."
    ]
  },
  {
    "title": "A Pragmatic Guide to LLM Evals for Devs (with Hamel Husain)",
    "authors": ["Hamel Husain", "Gergely Orosz"],
    "year": 2025,
    "type": "blog_post",
    "url": "https://newsletter.pragmaticengineer.com/p/evals",
    "summary": "소프트웨어 엔지니어 관점에서 LLM 평가의 실전 워크플로를 다룬다. 'TDD가 LLM에서 왜 작동하지 않는가'를 명시적으로 논증하면서, 대안으로 오류 분석(error analysis) 중심 접근을 제안한다. ch02에서 TDD 붕괴 논리를 독자에게 친숙한 엔지니어링 언어로 설명하는 브리지 자료로 적합하다.",
    "key_claims": [
      "TDD는 '주어진 입력에 대해 단일하고 결정론적으로 알 수 있는 정답'이 있다는 전제에서 작동하지만, LLM에서는 그 전제가 성립하지 않는다.",
      "LLM 애플리케이션에서 평가의 어려움은 입력의 무한한 표면적뿐 아니라, 유효하고 주관적이며 예측 불가능한 출력의 광대한 공간에서 비롯된다.",
      "제네릭 off-the-shelf 지표(예: '환각 점수', '유용성')보다 실제 오류를 관찰한 뒤 그에 맞는 평가기를 작성하는 bottom-up 접근이 더 효과적이다."
    ]
  },
  {
    "title": "Your AI Product Needs Evals",
    "authors": ["Hamel Husain"],
    "year": 2023,
    "type": "blog_post",
    "url": "https://hamel.dev/blog/posts/evals/",
    "summary": "LLM 기반 제품에서 평가 시스템 구축이 왜 핵심인지를 실제 Rechat 사례를 통해 설명한다. Level 1(단언 기반)→Level 2(LLM-as-judge)→Level 3(인간 평가)의 3단계 평가 계층을 제시하며, 평가 시스템이 소프트웨어 테스트처럼 장기적으로 배당금을 지불한다고 주장한다. ch02에서 EDD의 실천적 구조를 계층별로 소개하는 참고 프레임으로 활용 가능하다.",
    "key_claims": [
      "성공하지 못한 AI 제품은 거의 항상 '견고한 평가 시스템 구축 실패'라는 공통 원인을 공유한다.",
      "LLM 단위 테스트는 pytest처럼 단언(assertion)을 쓰지만, 단위 테스트를 넘어 데이터 정제와 모델 추론 중 자동 재시도에도 이 단언을 재활용해야 한다.",
      "평가 수준(Level 1~3)에 따라 실행 비용과 빈도가 다르며, Level 1은 모든 코드 변경 시, Level 3는 중요한 제품 변경 이후에만 실행한다."
    ]
  },
  {
    "title": "LLM Evals: Everything You Need to Know (FAQ)",
    "authors": ["Hamel Husain", "Shreya Shankar"],
    "year": 2026,
    "type": "blog_post",
    "url": "https://hamel.dev/blog/posts/evals-faq/",
    "summary": "700명 이상의 엔지니어·PM을 대상으로 한 AI Evals 강의에서 수집된 질문들에 답하는 포괄적 FAQ다. 'eval-driven development(평가 주도 개발)를 실천해야 하는가?'라는 질문에 대해 '대체로 아니오'라고 답하며, LLM의 무한한 실패 표면적 때문에 구현 전에 평가기를 미리 작성하는 것은 문제를 더 만든다고 논증한다. ch02에서 EDD를 '단순 선언'이 아니라 '논리적 귀결'로 제시할 때, 기존의 순진한 eval-driven 접근의 한계를 솔직하게 인정하는 근거로 활용할 수 있다.",
    "key_claims": [
      "Eval-driven development(구현 전 평가기 작성)는 매력적으로 들리지만 실제로는 더 많은 문제를 일으킨다—LLM은 예측 가능한 실패 모드가 없는 무한한 실패 표면적을 가지기 때문이다.",
      "더 나은 접근은 '상상한 오류가 아니라 발견한 오류에 대해 평가기를 작성하는' error analysis 우선 방식이다.",
      "평가 기준(criteria)은 모델 출력을 검토한 후에야 명확해지는 경향이 있어('criteria drift'), 평가는 정적인 목표가 아니라 반복적이고 인간 주도적인 의미 파악 과정이다."
    ]
  },
  {
    "title": "Using LLM-as-a-Judge For Evaluation: A Complete Guide",
    "authors": ["Hamel Husain"],
    "year": 2024,
    "type": "blog_post",
    "url": "https://hamel.dev/blog/posts/llm-judge/",
    "summary": "LLM-as-a-judge 평가 시스템을 구축하는 실전 가이드로, 30개 이상의 기업에서 적용한 경험을 바탕으로 한다. 데이터를 먼저 보기 전에 judge 프롬프트를 작성할 수 없다는 원칙과, 1-5점 척도 같은 임의적 채점 시스템의 함정을 구체적으로 다룬다. ch02에서 EDD의 핵심 실천법(LLM 채점기 설계)을 설명하는 실용 자료로 적합하다.",
    "key_claims": [
      "데이터를 보기 전에는 좋은 judge 프롬프트를 작성할 수 없다—평가 기준은 출력물을 채점하는 과정에서 비로소 외재화되고 정의된다.",
      "팀이 반복하는 실수: 지표 과다 생성, 차이가 불명확한 1-5점 임의 채점, 도메인 전문가 배제.",
      "LLM 채점기는 인간 판단을 대체하는 것이 아니라 확장하는 것이며, 인간 레이블 없이는 신뢰할 수 없다."
    ]
  },
  {
    "title": "Judging the Judges: Evaluating Alignment and Vulnerabilities in LLMs-as-Judges",
    "authors": ["Aman
