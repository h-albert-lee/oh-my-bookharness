# Search: nondeterminism software testing challenges ML models classification recommendation systems

이제 충분한 자료를 수집했습니다. JSON 형식으로 정리하겠습니다.

---

아래는 조사 결과를 장 집필에 활용 가능한 자료로 정리한 JSON입니다.

```json
[
  {
    "title": "Challenges in Testing Large Language Model Based Software: A Faceted Taxonomy",
    "authors": ["Felix Dobslaw", "Robert Feldt", "Juyeon Yoon", "Shin Yoo"],
    "year": 2025,
    "type": "academic_paper",
    "url": "https://arxiv.org/html/2503.00481v1",
    "summary": "LLM 기반 소프트웨어의 비결정론적 특성이 기존 테스트 패러다임(결정론적 오라클)을 어떻게 무력화하는지를 분류 체계로 정리한 논문. ch02의 핵심 주장인 '전통 TDD가 확률론적 시스템에서 작동하지 않는다'를 뒷받침하는 학술적 근거로 활용 가능. 특히 prompt-driven variability, 반복 쿼리에서의 출력 불일치 사례가 결정론 붕괴 지점 설명에 직접 인용 가능.",
    "key_claims": [
      "전통 소프트웨어 테스팅은 결정론적 오라클에 의존하지만, LLM의 확률론적 특성은 이 전제를 깨뜨린다.",
      "temperature=0으로 설정해도 반복 쿼리는 비일관적인 출력을 낼 수 있다(Atil et al., 2024).",
      "ML 테스팅은 패러다임의 전환을 요구하며(Braiek and Khomh, 2020), 변동성(variation)을 1등급 관심사로 다루는 접근이 없다.",
      "LLM의 정확성 정의는 기존 결정론적·확률론적·ML 특화 패러다임 어느 것으로도 포괄하기 어렵다."
    ]
  },
  {
    "title": "Non-Determinism and the Lawlessness of Machine Learning Code",
    "authors": ["A. Feder Cooper", "Jonathan Frankle", "Christopher De Sa"],
    "year": 2022,
    "type": "academic_paper",
    "url": "https://arxiv.org/pdf/2206.11834",
    "summary": "ML 코드의 비결정론을 정의하고, 동일한 학습 절차에서도 공정성 지표가 크게 달라질 수 있음을 논증하는 논문. ch02에서 '결정론적 세계관의 붕괴 지점'을 설명할 때, 같은 입력도 다른 출력을 낳는 비결정론의 정의 및 실제 폐해를 인용하기에 적합. 결정론 vs 확률론 대비 구조를 개념적으로 지지.",
    "key_claims": [
      "비결정론이란 동일한 입력이 다른 출력을 낳을 수 있는 프로세스의 속성이며, 이는 결정론적 if/then 로직과 근본적으로 다르다.",
      "ML의 비결정론은 공정성(fairness) 지표의 광범위한 변동을 야기하고, 어떤 모델이 '최선'인지 판단하기 어렵게 만든다.",
      "실제로 비결정론은 특정 입력에 대해 모델이 극단적으로 상이한 결과를 내는 원인이 된다."
    ]
  },
  {
    "title": "On Testing Machine Learning Programs",
    "authors": ["Houssem Ben Braiek", "Foutse Khomh"],
    "year": 2020,
    "type": "academic_paper",
    "url": "https://www.sciencedirect.com/science/article/abs/pii/S0164121220300248",
    "summary": "ML 프로그램 테스팅의 난점을 체계적으로 정리한 선구적 논문으로, ML에서 개발 패러다임 자체가 '연역적(rule 명시)→귀납적(데이터에서 규칙 추출)'으로 전환된다는 핵심 명제를 제시. ch02에서 TDD가 전제하는 '규칙의 명시적 기술' 패러다임이 ML에서 무너지는 이유를 설명할 때 직접 인용할 수 있는 가장 영향력 있는 학술 자료. 후속 연구들이 광범위하게 인용.",
    "key_claims": [
      "ML 프로그램을 테스트하기 어려운 근본 이유는 ML·AI가 유발하는 개발 패러다임의 전환에 있다.",
      "전통 소프트웨어는 연역적으로 시스템 동작 규칙을 코드로 명시하지만, ML은 학습 데이터에서 귀납적으로 규칙을 도출한다.",
      "ML 테스팅은 패러다임의 전환(paradigm shift)을 필요로 한다."
    ]
  },
  {
    "title": "Testing Machine Learning Based Systems: A Systematic Mapping",
    "authors": ["Vincenzo Riccio", "Gunel Jahangirova", "Andrea Stocco", "Nargiz Humbatova", "Michael Weiss", "Paolo Tonella"],
    "year": 2020,
    "type": "academic_paper",
    "url": "https://link.springer.com/article/10.1007/s10664-020-09881-0",
    "summary": "ML 기반 시스템 테스팅 기법을 70개 주요 연구에서 체계적으로 매핑한 논문. ch02에서 '기존 테스트 방법으로는 왜 ML 시스템을 검증할 수 없는가'를 구조적으로 논증할 때, 현존하는 연구 지형과 미해결 과제(신뢰성 있는 평가 메트릭 정의 등)를 개관하는 용도로 활용 가능.",
    "key_claims": [
      "MLS(Machine Learning-based System) 테스팅에서 가장 활발한 연구 분야는 자동 시나리오/입력 생성과 테스트 오라클 생성이다.",
      "MLS 테스팅은 빠르게 성장하는 분야이지만, 현실적 입력 생성과 신뢰성 있는 평가 메트릭·벤치마크 정의 등 미해결 과제가 많다."
    ]
  },
  {
    "title": "An Empirical Study of Testing Machine Learning in the Wild",
    "authors": ["Moses Openja", "Foutse Khomh", "Armstrong Foundjem", "Zhen Ming (Jack) Jiang", "Mouna Abidi", "Ahmed E. Hassan"],
    "year": 2024,
    "type": "academic_paper",
    "url": "https://dl.acm.org/doi/10.1145/3680463",
    "summary": "실제 ML 소프트웨어 프로젝트에서 테스팅이 어떻게 수행되는지를 실증적으로 분석한 논문. ch02에서 '이론적 테스트 방법이 실무에서 채택되지 않는다'는 논거를 뒷받침하는 데 유용. ML 시스템이 데이터→규칙의 귀납적 패러다임을 따르기 때문에 전통 소프트웨어 검증 방식 적용이 어렵다는 주장을 실증으로 보완.",
    "key_claims": [
      "전통 소프트웨어와 달리, ML에서는 알고리즘이 데이터로부터 자동으로 규칙을 형성한다.",
      "ML 시스템의 품질을 보장하는 것은 여전히 연구 커뮤니티의 열린 과제다.",
      "ML 시스템의 주요 테스트 대상은 데이터, 모델, ML 코드의 세 가지 고수준 컴포넌트다."
    ]
  },
  {
    "title": "Non-Determinism of 'Deterministic' LLM Settings",
    "authors": ["Bolaji Akinwande", "Ana Marasović", "others"],
    "year": 2024,
    "type": "academic_paper",
    "url": "https://arxiv.org/html/2408.04667v5",
    "summary": "temperature=0 등 '결정론적' 하이퍼파라미터 설정하에서도 LLM이 비일관적 출력을 낸다는 것을 실험적으로 입증한 논문. ch02에서 '표면적 결정론화 시도도 실패한다'는 논거로 직접 사용 가능. 특히 단위 테스트(unit test)의 한계를 명시적으로 언급해 TDD 무력화 메커니즘 설명에 핵심 자료.",
    "key_claims": [
      "비결정론적 AI는 특히 상업적 응용에서 개발자에게 새로운 도전을 제기한다.",
      "AI 함수에 대한 단위 테스트 사용은 비결정론 때문에 제한적이며, 가변성을 허용하는 회귀 테스트가 대안이 될 수 있다.",
      "동일 입력·동일 설정에서 LLM의 불안정성을 체계적으로 조사한 연구가 지금까지 없었다."
    ]
  },
  {
    "title": "Defeating Nondeterminism in LLM Inference",
    "authors": ["Horace He", "Thinking Machines Lab"],
    "year": 2025,
    "type": "blog_post",
    "url": "https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/",
    "summary": "LLM 추론의 비결정론 근본 원인(부동소수점 비결합성, 병렬 실행, 배치 크기 의존성 등)을 기술적으로 분석한 엔지니어링 블로그. ch02에서 '왜 AI 시스템은 구조적으로 결정론적이기 어려운가'를 하드웨어·소프트웨어 수준에서 설명하는 기술적 근거로 활용 가능. 독자가 납득하도록 구체적 예시 제공.",
    "key_claims": [
      "temperature=0으로 이론적으로 결정론적 설정을 해도 LLM API는 실제로 비결정론적이다.",
      "개별 사용자 관점에서 동시 사용자는 시스템의 '입력'이 아닌 비결정론적 속성이므로, LLM 추론은 사용자 입장에서 본질적으로 비결정론적이다.",
      "ML에서 비결정론에 부딪힐 때 '어차피 확률론적 시스템이니까'라고 덮어두는 패배주의를 거부해야 한다."
    ]
  },
  {
    "title": "Beyond Traditional Testing: Addressing the Challenges of Non-Deterministic Software",
    "authors": ["AWS Developer Relations"],
    "year": 2024,
    "type": "blog_post",
    "url": "https://dev.to/aws/beyond-traditional-testing-addressing-the-challenges-of-non-deterministic-software-583a",
    "summary": "AI 기반 추천 시스템을 예시로 비결정론적 소프트웨어 테스팅 전략을 실용적으로 설명하는 글. ch02에서 '추천 시스템 같은 ML 모델이 왜 기존 테스트로 검증 불가한가'를 독자 친화적인 예시로 설명할 때 활용 가능. 비결정론의 여러 원천(LLM, 실시간 데이터, 모델 추론)을 구체적으로 열거.",
    "key_claims": [
      "비결정론적 소프트웨어는 동일한 입력에 대해 동일한 조건에서도 다른 출력을 낼 수 있으며, 이는 테스팅에 중대한 도전을 제기한다.",
      "LLM 등 AI 기술의 통합은 실행할 때마다 달라질 수 있는 데이터를 도입한다.",
      "비결정론적 소프트웨어 개발은 분산 시스템부터 AI 솔루션까지 점점 보편화되고 있다."
    ]
  },
  {
    "title": "Seven Recommendations for Testing in a Non-Deterministic World",
    "authors": ["Software Engineering Institute (SEI), Carnegie Mellon University"],
    "year": 2020,
    "type": "blog_post",
    "url": "https://www.sei.cmu.edu/blog/seven-recommendations-for-testing-in-a-non-deterministic-world/",
    "summary": "비결정론적 세계에서 테스팅의 한계와 보완 전략 7가지를 CMU SEI 관점에서 정리한 글. ch02에서 '단일 테스트 기법으로는 비결정론적 결함을 잡을 수 없다'는 논거를 권위 있는 기관의 목소리로 보완할 때 유용. 기존 방법론의 한계를 인정하면서 새 접근의 필요성을 제기하는 흐름 구
