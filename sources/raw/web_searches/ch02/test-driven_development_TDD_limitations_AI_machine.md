# Search: test-driven development TDD limitations AI machine learning systems nondeterministic behavior

조사를 마쳤습니다. 이제 수집된 자료를 품질과 적합성 기준으로 엄선하여 JSON 형식으로 정리하겠습니다.

---

아래는 조사를 통해 확인된 **실제 존재하는 자료**만을 엄선하여 ch02 집필에 활용 가능한 형태로 정리한 결과입니다.



기존 TDD는 명확한 pass/fail 결과를 가진 결정론적 테스트를 사용하는데, AI 시스템의 확률론적 특성 때문에 이 접근법이 한계에 부딪힌다는 점

, 

LLM은 전통적 소프트웨어나 일반 머신러닝 소프트웨어와는 다른 방식의 비결정론성을 도입하기 때문에 단순한 출력 비교나 통계적 정확도를 넘어선 새로운 정확성 검증 접근법이 필요하다는 점

, 

TDD는 주어진 입력에 대해 결정론적이고 알 수 있는 단일의 정답이 존재할 때 작동하지만, LLM에서는 그것이 사실이 아니며 수천 가지의 유효한 출력이 가능하다는 점

을 뒷받침하는 자료들이 확인됩니다.

```json
[
  {
    "title": "The Challenges of Testing in a Non-Deterministic World",
    "authors": ["Donald Firesmith"],
    "year": 2017,
    "type": "blog_post",
    "url": "https://www.sei.cmu.edu/blog/the-challenges-of-testing-in-a-non-deterministic-world/",
    "summary": "CMU SEI(소프트웨어 공학 연구소)의 권위 있는 출처에서 비결정론적 시스템이 기존 테스트 가정을 어떻게 무너뜨리는지를 체계적으로 설명한다. '동일한 입력 → 동일한 출력'이라는 결정론 전제가 ML 기반 시스템에서 성립하지 않음을 논증하며, 이는 ch02에서 TDD의 구조적 한계를 입증하는 핵심 논거로 활용할 수 있다. 특히 기존 테스터와 개발자들이 암묵적으로 공유하는 결정론적 가정이 왜 위험한지를 설명하는 데 최적이다.",
    "key_claims": [
      "많은 개발자와 테스터는 동일한 입력과 조건에서 시스템이 항상 동일하게 동작한다고 가정하지만, 이 가정은 ML이 포함된 현대 시스템에서 틀렸다",
      "비결정론적 시스템에서는 동일한 테스트 케이스를 여러 번 실행해도 서로 다른 결과가 나올 수 있으며, 이는 테스트를 근본적으로 어렵게 만든다",
      "비결정론적 결함(non-deterministic defects)에 대한 훈련과 인식의 부재로 인해 테스트가 이러한 결함을 발견하지 못하고 위양성·위음성이 증가한다"
    ]
  },
  {
    "title": "Adapting TDD for Reliable AI Systems",
    "authors": ["Galileo AI Team"],
    "year": 2024,
    "type": "blog_post",
    "url": "https://galileo.ai/blog/test-driven-development-ai-systems",
    "summary": "TDD를 AI 시스템에 적용하려면 근본적인 수정이 필요하다는 것을 실무적 관점에서 논증한다. 블랙박스 특성, 확률론적 출력, 데이터 의존성 등 AI 시스템의 고유한 특성이 기존 TDD를 무력화하는 메커니즘을 구체적으로 설명하므로, ch02에서 TDD 무력화 선언의 근거로 직접 인용할 수 있다. 기존 TDD의 3단계(Red-Green-Refactor)에 Monitor 단계가 추가되어야 한다는 주장은 EDD 필요성 논거로 활용 가능하다.",
    "key_claims": [
      "전통적 TDD는 명확한 pass/fail 결과를 가진 결정론적 테스트에 의존하는데, 이 접근법은 AI 시스템의 확률론적 특성 때문에 한계에 부딪힌다",
      "AI 시스템은 코드 동작뿐 아니라 훈련 데이터에도 동등하게 의존하기 때문에, 데이터 중심 설계가 TDD 프로세스의 핵심 부분이 되어야 한다",
      "AI 테스트에서 전통적 TDD와 달리 테스트가 완전히 실패하지 않고 통계적 임계값 미달 상태로 부분 성공할 수 있으며, 이를 위해 Red-Green-Refactor-Monitor 4단계 사이클이 필요하다",
      "많은 AI 모델은 '블랙박스'로 동작하여 특정 출력이 왜 생성됐는지 이해하기 어렵고, 기존 소프트웨어처럼 실행 경로를 추적하는 것이 불가능하다"
    ]
  },
  {
    "title": "On Testing Machine Learning Programs",
    "authors": ["Houssem Ben Braiek", "Foutse Khomh"],
    "year": 2020,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/1812.02257",
    "summary": "ML 프로그램 테스팅의 고유한 도전과제를 체계적으로 정리한 동료심사 학술논문(Journal of Systems and Software, 2020)으로, 학문적 권위를 갖춘 핵심 참고문헌이다. ML 시스템은 연역적으로 규칙이 작성되는 것이 아니라 훈련 데이터로부터 귀납적으로 규칙을 추론한다는 근본적 차이를 논증하며, ch02의 '결정론 vs. 확률론' 구조적 차이 설명에 학술적 근거를 제공한다. 이 논문은 이후 LLM 테스팅 관련 다수의 연구에서 기초 문헌으로 광범위하게 인용된다.",
    "key_claims": [
      "ML/DL 시스템은 전통적 소프트웨어처럼 연역적으로(명시적 규칙 코드로) 구성되지 않고, 훈련 데이터로부터 귀납적으로 규칙을 추론하므로 품질 보증이 근본적으로 다른 패러다임을 요구한다",
      "소프트웨어 테스팅 영역의 개념(코드 커버리지, 뮤테이션 테스팅, 속성 기반 테스팅)을 ML에 적용하려는 시도가 있으나, ML 특유의 복잡성 때문에 패러다임 전환이 필요하다",
      "안전 임계 시스템에서 ML 모델의 광범위한 채택으로 신뢰성 보장의 중요성이 극도로 커졌다"
    ]
  },
  {
    "title": "Challenges in Testing Large Language Model Based Software: A Faceted Taxonomy",
    "authors": ["Felix Dobslaw", "Robert Feldt", "Juyeon Yoon", "Shin Yoo"],
    "year": 2025,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2503.00481",
    "summary": "2025년 3월 발표된 최신 학술 논문으로, LLM 기반 소프트웨어 테스팅의 도전과제를 4가지 패싯(SUT, Goal, Oracles, Inputs)으로 분류한 분류 체계를 제시한다. '정확성을 이진 속성이 아닌 결과의 분포로 봐야 한다'는 핵심 주장은 ch02에서 TDD의 assert 기반 검증이 왜 작동하지 않는지를 논증하는 데 결정적 근거가 된다. temperature=0 설정에서도 LLM이 비결정론적임을 실험으로 입증한 선행 연구를 인용해 비결정론의 심층성을 보여준다.",
    "key_claims": [
      "LLM과 다중 에이전트 LLM은 전통적 소프트웨어나 일반 ML 소프트웨어와는 다른 방식의 비결정론성을 도입하며, 단순한 출력 비교나 통계적 정확도를 넘어선 정확성 검증이 필요하다",
      "미묘한 프롬프트 변형이 모델 응답을 뒤집을 수 있고, 결정론적 설정(temperature=0)에서도 반복 질의 시 비일관적 출력이 나올 수 있어 재현 가능성에 심각한 문제가 생긴다",
      "정확성은 이진 속성이 아닌 결과의 분포로 봐야 하며, 기존 도구들은 테스트 실행을 고립된 이벤트로 취급하고 모델 버전·설정·반복 실행 간 변동성을 충분히 포착하지 못한다"
    ]
  },
  {
    "title": "Eradicating Non-Determinism in Tests",
    "authors": ["Martin Fowler"],
    "year": 2011,
    "type": "blog_post",
    "url": "https://martinfowler.com/articles/nonDeterminism.html",
    "summary": "TDD의 창시자 계보에 있는 Martin Fowler가 비결정론적 테스트가 자동화 회귀 테스트 스위트 전체를 어떻게 파괴하는지를 직접 논한 고전적 참고문헌이다. Fowler가 전통적 TDD의 가장 큰 가치를 회귀 테스트 스위트로 보면서도, 비결정론적 테스트가 이 가치를 완전히 소멸시킨다고 경고한다는 점에서, ch02에서 '기존 TDD의 전제'와 'AI 시스템에서의 무력화'를 대비하는 데 TDD 진영 내부의 목소리로 인용할 수 있다.",
    "key_claims": [
      "비결정론적 테스트(때로 통과하고 때로 실패하는 테스트)는 통제되지 않을 경우 자동화 회귀 테스트 스위트의 가치를 완전히 파괴할 수 있다",
      "비결정론성의 원인으로 격리 부재, 비동기 동작, 원격 서비스, 시간, 리소스 누수 등을 들며, AI 시스템은 이 모든 요소를 구조적으로 내포한다",
      "테스트의 핵심 가치는 버그 탐지 메커니즘으로서의 회귀 테스트 스위트이며, 비결정론이 이를 무력화하면 전체 배포 파이프라인이 위협받는다"
    ]
  },
  {
    "title": "Probabilistic and Deterministic Systems (Substack: Decision Matrix)",
    "authors": ["Daniel Vaughan"],
    "year": 2025,
    "type": "blog_post",
    "url": "https://decisionmatrix.substack.com/p/probabilistic-and-deterministic-systems",
    "summary": "결정론적 시스템과 확률론적 시스템의 구조적 차이를 실용적으로 설명하며, 전통적 단위 테스트가 AI 애플리케이션에서 작동하지 않는 이유를 동전 던지기 비유로 명쾌하게 논증한다. 이 비유는 ch02에서 독자에게 '왜 assert 하나로는 충분하지 않은가'를 직관적으로 납득시키는 데 탁월한 교육적 도구가 된다. 또한 일반 소프트웨어 개발자가 확률론적 시스템 구축에 필요한 비평가(evals) 방법론 역량을 갖추지 못했다는 실무적 관찰을 제시한다.",
    "key_claims": [
      "GenAI 시스템은 결정론적이지 않다. 전통적 소프트웨어가 예측 가능한 출력을 내놓는 것과 달리, AI 시스템은 불확실성을 내포하며 근본적으로 다른 구축·테스트 접근법을 필요로 한다",
      "확률론적 시스템에는 전통적 단위 테스트가 작동하지 않으며, 데이터셋·지표·반복 측정을 통한 평가(
