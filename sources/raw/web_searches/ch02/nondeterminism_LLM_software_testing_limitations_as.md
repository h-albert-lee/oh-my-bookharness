# Search: "nondeterminism" "LLM" "software testing" limitations assertEqual unit test failure machine learning systems

조사가 충분히 완료되었습니다. 이제 결과를 JSON 형식으로 정리하겠습니다.

아래는 검색을 통해 실제로 확인된 자료들을 ch02 집필에 활용 가능한 형태로 정리한 결과입니다.

---

```json
[
  {
    "title": "Eradicating Non-Determinism in Tests",
    "authors": ["Martin Fowler"],
    "year": 2011,
    "type": "blog_post",
    "url": "https://martinfowler.com/articles/nonDeterminism.html",
    "summary": "TDD·자동화 회귀 테스트의 전제가 '결정론적 동작'임을 명확히 선언하며, 비결정론적 테스트가 테스트 스위트 전체를 감염시키는 방식을 설명한다. ch02에서 기존 소프트웨어가 가진 결정론적 설계 가정의 출발점으로 인용하기에 적합하다. '비결정론 = 제거해야 할 버그'라는 전통적 관점을 명시적으로 보여 줌으로써 AI 시스템과의 대비를 극명하게 구성할 수 있다.",
    "key_claims": [
      "비결정론적 테스트는 쓸모없을 뿐 아니라 전체 테스트 스위트를 오염시키는 바이러스와 같으므로 즉시 제거해야 한다.",
      "자동화 회귀 테스트의 핵심 가치는 코드 변경 없이도 테스트가 반드시 같은 결과를 내야 한다는 결정론적 신뢰에 있다.",
      "비결정론의 주요 원인은 격리 부재, 비동기 동작, 원격 서비스, 시간 의존성, 리소스 누수이며—이것들은 모두 '고쳐야 할 대상'으로 분류된다."
    ]
  },
  {
    "title": "Challenges in Testing Large Language Model Based Software: A Faceted Taxonomy",
    "authors": ["Felix Dobslaw", "Robert Feldt", "Juyeon Yoon", "Shin Yoo"],
    "year": 2025,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2503.00481",
    "summary": "LLM 기반 소프트웨어의 비결정론이 전통 소프트웨어·기존 ML 소프트웨어와도 구조적으로 다른 성격임을 분류 체계(taxonomy)로 제시한다. assertEqual 류의 단일 출력 비교가 왜 LLM에 적용 불가능한지를 '원자적 오라클'과 '집합적 오라클'의 구분으로 설명한다. ch02에서 '단순 출력 비교를 넘어서는 정확성 검증'이 왜 필요한지를 학술적으로 뒷받침하는 핵심 참고 문헌이다.",
    "key_claims": [
      "LLM과 멀티에이전트 LLM은 전통 소프트웨어나 기존 ML 소프트웨어와 달리 구조적 비결정론을 가지며, 단순 출력 비교나 테스트 데이터셋 정확도만으로는 정확성을 검증할 수 없다.",
      "현행 LLM 테스트 도구들은 개별 테스트 실행을 고립된 사건으로 취급하고, 모델 버전·설정·반복 실행에 걸친 변동성을 충분히 포착하지 못한다.",
      "정확성은 이진 속성이 아니라 결과의 분포로 바라봐야 하며, 이를 위해 변동성 인식(variability-aware) 테스트 방법론이 필요하다."
    ]
  },
  {
    "title": "You Can't Assert Your Way Out of Non-Determinism: A Practical QA Strategy for LLM Applications",
    "authors": ["Advisor360 Engineering"],
    "year": 2026,
    "type": "blog_post",
    "url": "https://medium.com/advisor360-com/you-cant-assert-your-way-out-of-non-determinism-a-practical-qa-strategy-for-llm-applications-fd32e617cdec",
    "summary": "실무 현장에서 엔지니어가 LLM 출력에 assertEqual을 작성하는 순간 맞닥뜨리는 모순을 매우 구체적인 코드 예시와 함께 묘사한다. '결정론적 레이어'와 '비결정론적 레이어'의 분리라는 프레임은 ch02에서 TDD가 무력화되는 지점을 독자에게 직관적으로 전달하는 데 활용할 수 있다. LLM 출력을 분포의 표본으로 재해석해야 한다는 주장은 EDD 도입의 논리적 준비 단계로 이어진다.",
    "key_claims": [
      "assert output == '...' 형태의 단언문은 LLM 환경에서 작성 당일 한 번만 통과하며, 의미적으로 동일한 다른 출력은 모두 실패로 처리하는 구조적 결함을 가진다.",
      "LLM 애플리케이션에는 결정론적 레이어(프롬프트 조립, 데이터 처리)와 비결정론적 레이어(모델 출력)가 공존하며, 이를 혼동하는 것이 대부분의 QA 전략 실패 원인이다.",
      "LLM 출력을 분포의 표본으로 받아들이면, 테스트의 질문은 '출력이 X인가?'가 아니라 '이 분포는 수용 가능한가?'로 바뀐다."
    ]
  },
  {
    "title": "Beyond Traditional Testing: Addressing the Challenges of Non-Deterministic Software",
    "authors": ["AWS / DEV Community"],
    "year": 2024,
    "type": "blog_post",
    "url": "https://dev.to/aws/beyond-traditional-testing-addressing-the-challenges-of-non-deterministic-software-583a",
    "summary": "LLM을 포함한 AI 시스템이 왜 '동일 입력→동일 출력' 가정을 붕괴시키는지 다층적 원인과 대안 전략(속성 기반 테스트, 의미적 유사도 검사, 반복 실행 환경 구성)을 실용적으로 설명한다. ch02에서 기존 소프트웨어의 결정론적 가정이 무너지는 지점을 설명한 후, 대안적 접근의 필요성을 제시하는 전환점으로 사용하기 좋다.",
    "key_claims": [
      "비결정론적 소프트웨어는 동일 입력·동일 조건에서도 매번 다른 출력을 생성하며, LLM 통합은 이 문제를 구조적으로 심화시킨다.",
      "LLM이 포함된 테스트에서 속성 기반 테스트는 강력하지만 LLM 호출이 반복될수록 비용과 시간이 급증하는 한계가 있다.",
      "AI 시스템에서는 정확한 출력 일치 대신 의미적 유사도(semantic similarity) 측정으로 출력을 평가해야 한다."
    ]
  },
  {
    "title": "Testing AI Agents: Validating Non-Deterministic Behavior",
    "authors": ["SitePoint Editorial"],
    "year": 2026,
    "type": "blog_post",
    "url": "https://www.sitepoint.com/testing-ai-agents-deterministic-evaluation-in-a-non-deterministic-world/",
    "summary": "동일한 질문에 대해 '프랑스의 수도는?'→'Paris', 'The capital of France is Paris', 'Paris is the capital of France' 세 가지 올바른 답변이 모두 존재할 수 있음을 보여 주며, 문자열 동등성 단언이 왜 구조적으로 실패하는지를 설명한다. ch02에서 assertEqual 실패가 '버그'가 아니라 '패러다임 불일치'임을 독자에게 납득시키는 구체적 사례로 직접 인용할 수 있다. 평가 프레임워크(DeepEval 등)를 통한 임계값 기반 품질 게이트 전략은 EDD 도입 논거의 실증적 토대가 된다.",
    "key_claims": [
      "Temperature·top-p 샘플링은 동일 프롬프트에서도 매번 다른 어구·구조·내용을 생성하며, temperature=0에서도 배치 연산의 부동소수점 비결정론으로 인해 비트 단위 동일성을 보장받지 못한다.",
      "문자열 동등성 단언은 의미적으로 동일한 여러 정답 중 하나만 수용하고 나머지를 실패로 처리하는 구조적 결함을 가진다.",
      "LLM 평가는 exact-match 단언을 점수 기반 품질 차원(충실도·관련성·환각)으로 대체하며, 통과 조건은 특정 값이 아닌 품질 임계값이 된다."
    ]
  },
  {
    "title": "Defeating Nondeterminism in LLM Inference",
    "authors": ["Horace He", "Thinking Machines Lab"],
    "year": 2025,
    "type": "blog_post",
    "url": "https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/",
    "summary": "temperature=0으로 설정해도 LLM API가 동일 입력에 대해 서로 다른 출력을 반환하는 구조적 원인을 배치 불변성(batch invariance) 실패로 규명한다. ch02에서 '비결정론을 없애면 되지 않나?'는 독자의 반론을 선제적으로 차단하는 근거로 활용할 수 있다—결정론은 이론적으로 달성 가능하지만 현재 프로덕션 인프라 수준에서는 기본값이 아님을 보인다. 동시에 '유닛 테스트의 atol/rtol을 완화하는 것'을 결함 묵인으로 비판하는 논조는 ch02의 핵심 메시지와 정렬된다.",
    "key_claims": [
      "temperature=0을 설정해도 LLM API는 실제로 결정론적이지 않으며, 근본 원인은 GPU 병렬성이 아니라 배치 크기에 따라 결과가 달라지는 배치 불변성 실패다.",
      "실패한 유닛 테스트의 허용 오차(atol/rtol)를 올려 통과시키는 관행은 결함을 덮는 패배주의이며, 비결정론의 근본 원인을 이해하고 해결해야 한다.",
      "현재 거의 모든 LLM 추론 엔드포인트가 비결정론적인 주된 이유는 서버 부하에 따라 배치 크기가 비결정론적으로 변하기 때문이다."
    ]
  },
  {
    "title": "Non-determinism and Failure Modes in Machine Learning",
    "authors": ["José Miguel Faria"],
    "year": 2017,
    "type": "academic_paper",
    "url": "https://ieeexplore.ieee.org/document/8109300/",
    "summary": "안전 필수 소프트웨어 인증에서 결정론이 핵심 요건임을 확인하고, ML 알고리즘이 그 요건을 어떻게 위반하는지를 체계적으로 분석한 초기 학술 문헌이다. ch02에서 결정론적 설계 가정이 전통 소프트웨어 공학의 공식 인증 기준에까지 내재되어 있음을 보여 주는 권위 있는 출처로 인용할 수 있다. ML 시스템의 변동성 요인을 실패 모드로 분류하는 프레임워크는 AI 시스템과 기존 소프트웨어의 구조적 차이를 설명하는 토대가 된다.",
    "key_claims": [
      "결정론은 안전 필수 소프트웨어 인증의 핵심 조건이며, ML 알고리즘은 그 결정론 요건을 근본적으로 충족시키기 어렵다.",
      "ML 시스템의 동작 변동에 기여하는 요인들은 기존 소프트웨어의 실패 모드와 유사한 방식으로 체계적으로 관리되어야 한다.",
      "ML 알고리즘에 결정론 관련 요건과 개념을 적용하려면 기존 소프트웨어 공학의 방법론을 근본적으로 재해석해야 한다."
    ]
  },
  {
    "title": "The Challenges of Testing in a Non-Deterministic World",
    "authors": ["Donald Firesmith"],
    "year": 2017
