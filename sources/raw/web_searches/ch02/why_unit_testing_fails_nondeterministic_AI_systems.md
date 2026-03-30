# Search: why unit testing fails nondeterministic AI systems LLM probabilistic outputs software engineering

수집된 자료가 충분합니다. 이제 ch02 집필에 활용할 수 있는 자료를 JSON 형식으로 정리하겠습니다.

---

```json
[
  {
    "title": "Evaluation-Driven Development and Operations of LLM Agents: A Process Model and Reference Architecture",
    "authors": ["Boming Xia", "et al."],
    "year": 2025,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2411.13768",
    "summary": "TDD/BDD가 사전 정의된 테스트와 결정론적 결과를 전제하는 반면, LLM 에이전트는 비결정론적 출력·사후 적응·개방형 목표를 갖기 때문에 기존 방법론이 무력화된다는 것을 구조적으로 논증한다. 이 논문은 그 대안으로 EDDOps(평가 주도 개발·운영)를 제안하며, 평가를 개발 전 주기를 관통하는 '지배 함수'로 위치시킨다. ch02의 'TDD 무력화 메커니즘 → EDD 선언' 흐름의 학술적 근거로 직접 활용 가능하다.",
    "key_claims": [
      "TDD와 BDD는 안정적이고 명확히 정의된 명세와 결정론적 테스트 결과를 전제하지만, LLM 에이전트는 미명세 목표를 추구하고 비결정론적 출력을 생성하며 배포 후에도 계속 적응한다.",
      "고정 벤치마크와 정적 테스트 스위트에 기반한 전통적 평가 방법은 창발적 행동을 포착하거나 생애주기 전반에 걸친 지속적 적응을 지원하는 데 실패한다.",
      "EDDOps는 오프라인(개발 시) 평가와 온라인(런타임) 평가를 닫힌 피드백 루프 안에 통합하여, 평가를 최종 검문소가 아닌 지속적·지배적 기능으로 임베드한다."
    ]
  },
  {
    "title": "Challenges in Testing Large Language Model Based Software: A Faceted Taxonomy",
    "authors": ["Felix Dobslaw", "Robert Feldt", "Juyeon Yoon", "Shin Yoo"],
    "year": 2025,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2503.00481",
    "summary": "LLM 기반 소프트웨어가 전통적 소프트웨어와 달리 도입하는 비결정론의 본질을 정밀하게 분류(faceted taxonomy)하고, 단순 출력 비교나 통계적 정확도로는 정확성을 검증할 수 없음을 체계적으로 논증한다. '정확성을 이진 속성이 아닌 결과의 분포'로 봐야 한다는 핵심 주장은 ch02의 결정론 vs. 확률론 대비 논증에 직접 사용할 수 있다. 6개 오픈소스 테스팅 프레임워크 실증 분석을 포함해 신뢰도가 높다.",
    "key_claims": [
      "LLM과 Multi-Agent LLM은 전통적 소프트웨어나 일반 ML 소프트웨어와 다른 방식의 비결정론을 도입하며, 단순 출력 비교나 테스트 데이터셋 통계적 정확도를 넘어선 새로운 정확성 검증 접근법이 필요하다.",
      "기존 도구들은 테스트 실행을 고립된 이벤트로 취급하고 명시적 집계 메커니즘이 없으며, 모델 버전·설정·반복 실행에 걸친 변동성을 불충분하게 포착한다.",
      "정확성을 이진 속성이 아닌 결과의 분포로 보는 관점의 전환이 필요하며, 이는 변동성 인식 테스팅 방법론의 성숙을 요구한다."
    ]
  },
  {
    "title": "Rethinking Testing for LLM Applications: Characteristics, Challenges, and a Lightweight Interaction Protocol",
    "authors": ["(arXiv 2508.20737 저자진)"],
    "year": 2025,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2508.20737",
    "summary": "LLM 애플리케이션이 기존 소프트웨어와 근본적으로 다른 이유를 '결정론적 계산→확률론적 생성', '논리적 실행→뇌 영감 모델링', '정적 규칙→동적 학습 행동'이라는 세 가지 패러다임 전환으로 명시화한다. 이는 ch02의 'AI 시스템이 결정론적 세계관을 무너뜨리는 지점'을 서술하는 데 이론적 뼈대로 사용할 수 있다. 전통적 테스팅의 적용 가능 영역과 불가 영역을 계층별로 분석한 점도 유용하다.",
    "key_claims": [
      "LLM 애플리케이션은 전통 소프트웨어와 달리 결정론적 계산에서 확률론적 생성으로, 논리적 실행에서 뇌 영감 패러다임으로, 정적 규칙 기반 시스템에서 동적 학습 행동으로 전환된 특성을 갖는다.",
      "전통적 소프트웨어는 동일 실행 환경과 입력에서 예측 가능하고 반복 가능한 출력을 생성하지만, LLM 애플리케이션의 추론 코어는 이 전제를 성립시키지 않는다.",
      "전통적 테스팅 방법은 크로스-레이어 오류 전파를 간과하는 경향이 있으며, AI 평가 방법은 시스템 전반의 상호작용 모델링이 제한적이다."
    ]
  },
  {
    "title": "Non-Determinism of 'Deterministic' LLM Settings",
    "authors": ["(arXiv 2408.04667 저자진)"],
    "year": 2024,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2408.04667",
    "summary": "temperature=0으로 설정해도 LLM API가 실제로는 비결정론적임을 실증적으로 보여주는 학술 논문이다. ChatGPT의 코드 생성 데이터셋(CodeContests, APPS, HumanEval)에서 동일 요청에 대해 출력이 일치하지 않는 비율이 각각 75.76%, 51%, 47.56%에 달한다는 수치는 ch02에서 '결정론의 환상'을 논증하는 강력한 실증 근거로 활용할 수 있다.",
    "key_claims": [
      "ChatGPT는 기본 설정(temperature=1)에서 높은 비결정론성을 보이며, 세 가지 코드 생성 데이터셋에서 동일 요청에 대해 출력이 전혀 일치하지 않는 비율이 75.76%, 51%, 47.56%에 달한다.",
      "temperature=0으로 설정해도 코드 생성의 결정론성이 보장되지 않으며, 다만 기본 설정보다는 비결정론성이 줄어든다.",
      "LLM 기반 연구를 보다 견고한 과학적 토대 위에 올려놓기 위해 연구자들은 결론 도출 시 비결정론성을 반드시 고려해야 한다."
    ]
  },
  {
    "title": "Defeating Nondeterminism in LLM Inference",
    "authors": ["Horace He", "Thinking Machines Lab"],
    "year": 2025,
    "type": "blog_post",
    "url": "https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/",
    "summary": "LLM 추론 엔진이 왜 결정론적이 될 수 없는지를 기술적으로 해부한 심층 포스트로, 부동소수점 비결합성과 배치 크기 의존적 커널이 실제 비결정론의 근본 원인임을 밝힌다. ch02에서 '비결정론은 버그가 아니라 구조적 속성'이라는 주장을 뒷받침하는 기술적 심층 근거로 사용할 수 있으며, temperature=0조차 해결책이 아님을 설명하는 데 유용하다.",
    "key_claims": [
      "LLM API는 temperature를 0으로 낮춰 이론상 결정론적 샘플링(그리디 샘플링)을 적용해도 실제로는 비결정론적이며, vLLM·SGLang 등 자체 하드웨어에서도 마찬가지다.",
      "비결정론의 진짜 원인은 GPU 병렬 부동소수점 연산 순서가 아니라, 동적 배칭에 따라 배치 크기가 달라지면서 배치-비불변 커널이 서로 다른 수치 경로를 통과하기 때문이다.",
      "동일한 사용자 요청이 서버 부하에 따라 서로 다른 배치에 편성되고, 배치 크기가 달라지면 greedy decoding에서도 출력 토큰이 달라질 수 있다."
    ]
  },
  {
    "title": "LLMs are facing a QA crisis: Here's how we could solve it",
    "authors": ["LogRocket Blog 편집팀"],
    "year": 2025,
    "type": "blog_post",
    "url": "https://blog.logrocket.com/llms-are-facing-a-qa-crisis/",
    "summary": "LLM QA가 단순한 도구 부재 문제가 아니라 소프트웨어 신뢰성에 대한 사고방식의 근본적 전환임을 주장하는 실무 관점의 글이다. 전통적 QA가 전제하는 '입력이 특정 출력에 매핑된다'는 안정·통제 가능한 환경 가정이 LLM에서 어떻게 붕괴하는지를 서술하며, ch02의 '결정론적 세계관의 명시화→AI의 전제 붕괴' 논증 구조와 정확히 맞닿아 있다.",
    "key_claims": [
      "단일 프롬프트가 실행마다 극적으로 다른 응답을 산출하여 기존 테스팅 프레임워크를 무용지물로 만든다.",
      "전통적 QA는 입력이 특정 출력에 매핑되는 안정적이고 통제 가능한 환경을 전제하지만, LLM은 이 전제를 산산이 부순다.",
      "LLM의 할루시네이션 같은 행동은 버그가 아니라 LLM이 작동하는 방식에 내재된 것이며, QA 프로세스는 이를 제거하는 것이 아니라 관리하고 측정해야 한다."
    ]
  },
  {
    "title": "Why Traditional Testing Fails for AI Agents (and What Actually Works)",
    "authors": ["Coralogix"],
    "year": 2025,
    "type": "blog_post",
    "url": "https://coralogix.com/ai-blog/why-traditional-testing-fails-for-ai-agents-and-what-actually-works/",
    "summary": "확률론적 시스템에 결정론적 도구(pass/fail assertions)를 적용할 때 어떤 참사가 발생하는지를 실제 사례($2.3M 계약 손실)와 함께 보여주는 실무 글이다. 테스트가 모두 통과해도 에이전트가 프로덕션에서 다르게 행동하는 '조용한 실패' 시나리오는 ch02에서 TDD 무력화 메커니즘을 설명하는 구체적 내러티브로 쓸 수 있다.",
    "key_claims": [
      "Pass/fail 단언은 확률론적 출력을 가진 시스템에서 무의미하며, 에이전트는 모든 테스트를 통과하고도 프로덕션에서 47가지 미묘한 방식으로 다르게 행동할 수 있다.",
      "전통적 QA는 API가 200을 반환하는지는 알 수 있지만, 에이전트가 50단계 추론 체인에서 할루시네이션을 하거나 컨텍스트를 잘못 해석하거나 조용히 실패하는지는 알 수 없다.",
      "이것은 패치 가능한 사소한 불편이 아니라 구조적 문제다."
    ]
  },
  {
    "title": "Production AI Systems: The Unit Testing Paradox",
    "authors":
