# Search: testing vs evaluation machine learning systems determinism limitations assert equal

모든 자료를 충분히 수집했습니다. 이제 정리된 JSON 결과물을 출력합니다.

---

## 조사 결과

아래는 ch02 집필에 직접 활용 가능한 자료들을 실제 존재 여부를 확인하고 검증한 뒤 정리한 목록입니다.



TDD는 "무엇을 테스트할지 안다"는 전제 위에 성립하며, 결정론적 시스템에서는 자명하지만 ML 모델은 비결정론적이라는 점이 핵심 긴장 지점입니다.

 

ML 시스템은 모델의 실제 예측 행동을 사전에 명세하기 어렵기 때문에 구체적 테스트를 작성하는 것 자체가 어렵다는 문제가 구글 연구에서 정식 제기된 바 있습니다.

 

TDD·BDD 같은 고전적 소프트웨어 엔지니어링 방법론은 명확히 사전 정의된 명세를 가진 결정론적 시스템에는 효과적이나, 개방형·적응형 문맥에서 작동하는 LLM 에이전트에는 본질적으로 적합하지 않습니다.



```json
[
  {
    "title": "The ML Test Score: A Rubric for ML Production Readiness and Technical Debt Reduction",
    "authors": ["Eric Breck", "Shanqing Cai", "Eric Nielsen", "Michael Salib", "D. Sculley"],
    "year": 2017,
    "type": "academic_paper",
    "url": "https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/",
    "summary": "Google 연구진이 실제 프로덕션 ML 시스템 경험을 바탕으로 28개의 구체적 테스트·모니터링 항목을 제시한 논문. ML 시스템의 실제 예측 행동을 사전에 명세하기 어렵다는 근본적 한계를 공식화하여, TDD의 '사전 명세' 전제가 ML에서 무력화되는 메커니즘을 논증하는 데 핵심 근거로 활용할 수 있다. 또한 테스트(통과/실패)만으로는 프로덕션 준비도를 측정할 수 없고 평가 기반의 점수 체계가 필요하다는 EDD 전환 논거를 뒷받침한다.",
    "key_claims": [
      "ML 시스템 테스트는 전통 소프트웨어보다 복잡하며, 모델의 예측 행동을 사전에 정확히 명세하기 어렵다 (테스트 작성 자체가 난제).",
      "테스트와 모니터링을 함께 운용하는 평가 체계가 ML 시스템의 프로덕션 준비도를 결정한다.",
      "28개의 구체적 테스트 항목을 통해 ML 기술부채 감소를 위한 로드맵을 제시한다."
    ]
  },
  {
    "title": "Beyond Accuracy: Behavioral Testing of NLP Models with CheckList",
    "authors": ["Marco Tulio Ribeiro", "Tongshuang Wu", "Carlos Guestrin", "Sameer Singh"],
    "year": 2020,
    "type": "academic_paper",
    "url": "https://aclanthology.org/2020.acl-main.442/",
    "summary": "정확도(accuracy) 하나로 모델을 평가하는 방식이 성능을 과대 추정함을 실증하고, 소프트웨어 행동 테스팅 원칙에서 영감을 받은 체크리스트 방법론을 제안한 ACL 2020 Best Paper. 'assertEqual' 수준의 단일 값 비교로는 NLP 모델의 실제 품질을 검증할 수 없다는 사실을 구체적 사례로 보여주어, 기존 테스트 패러다임의 한계를 입증하는 핵심 사례로 활용 가능. 최소 기능 테스트(MFT), 불변성 테스트(INV), 방향성 기대 테스트(DIR)라는 새 평가 유형이 EDD의 구체적 도구로 소개될 수 있다.",
    "key_claims": [
      "held-out 정확도 측정은 NLP 모델의 일반화 성능을 과대 추정하는 주된 원인이다.",
      "행동 테스팅(Behavioral Testing) 프레임워크(CheckList)를 통해 상용 모델에서도 심각한 실패 패턴을 발견할 수 있다.",
      "CheckList를 사용한 실무자들은 그렇지 않은 그룹 대비 약 2배 많은 테스트를 만들고 약 3배 많은 버그를 발견했다."
    ]
  },
  {
    "title": "Evaluation-Driven Development of LLM Agents: A Process Model and Reference Architecture",
    "authors": ["Boming Xia", "Qinghua Lu", "Liming Zhu", "Zhenchang Xing", "Dehai Zhao", "Hao Zhang"],
    "year": 2024,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2411.13768",
    "summary": "TDD·BDD에서 영감을 받되 LLM 에이전트의 고유 특성에 맞게 재설계한 EDD(Evaluation-Driven Development) 프로세스 모델과 참조 아키텍처를 제안하는 학술 논문. TDD가 명확히 사전 정의된 결정론적 시스템에서만 효과적임을 명시하고, LLM 에이전트의 개방형·확률론적 행동이 기존 방법론을 무력화하는 메커니즘을 체계적으로 설명한다. ch02의 'TDD 무력화 → EDD 선언' 논증 구조와 가장 직접적으로 대응하는 학술 근거.",
    "key_claims": [
      "TDD·BDD는 사전 정의된 명세를 가진 결정론적 시스템에 효과적이지만, 개방형·적응형 LLM 에이전트에는 본질적으로 적합하지 않다.",
      "TDD와 달리 EDD는 실시간 피드백, 적응적 평가, 배포 후 모니터링을 통합하여 시스템이 진화하는 운영 요건에 대응하도록 한다.",
      "오프라인(개발 시점)과 온라인(런타임) 평가를 하나의 닫힌 피드백 루프로 통합한 EDDOps 접근법을 제시한다."
    ]
  },
  {
    "title": "Machine Learning Testing: Survey, Landscapes and Horizons",
    "authors": ["Jie M. Zhang", "Mark Harman", "Lei Ma", "Yang Liu"],
    "year": 2022,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/1906.10742",
    "summary": "IEEE Transactions on Software Engineering에 게재된 ML 테스팅 분야 최대 규모 서베이 논문(144편 분석). 정확성·강건성·공정성 등 테스팅 속성, 데이터·학습 프로그램·프레임워크 등 테스팅 대상, 자율주행·기계번역 등 응용 시나리오를 망라한다. ch02에서 '기존 소프트웨어 테스트 방법론이 ML에 적용될 때 무엇이 구조적으로 달라지는가'를 학문적으로 뒷받침하는 포괄적 레퍼런스로 활용 가능하다.",
    "key_claims": [
      "ML 테스팅은 전통 소프트웨어 테스팅과 구별되는 고유한 속성(정확성, 강건성, 공정성)과 구성요소(데이터, 학습 프로그램, 프레임워크)를 다룬다.",
      "테스트 오라클 문제(예상 출력을 정의하기 어려움)가 ML 테스팅의 근본적 난제다.",
      "메타모픽 테스팅 등 기존 소프트웨어 기법을 ML에 적용하려는 연구들이 존재하지만 한계가 있다."
    ]
  },
  {
    "title": "Beyond Traditional Testing: Addressing the Challenges of Non-Deterministic Software",
    "authors": ["AWS Developer Relations"],
    "year": 2024,
    "type": "blog_post",
    "url": "https://dev.to/aws/beyond-traditional-testing-addressing-the-challenges-of-non-deterministic-software-583a",
    "summary": "비결정론적 소프트웨어(특히 LLM 통합 시스템)를 테스트하는 새로운 전략들을 실용적 코드 예제와 함께 설명한 AWS 블로그. 정확한 출력 예측이 불가능할 때도 시스템 행동에 대한 의미 있는 단언(assertion)을 만들 수 있는 속성 기반 테스팅, 시맨틱 유사도 검사, LLM 보조 검증 전략을 소개한다. 기존 assertEqual 방식의 한계를 실제 코드로 대비시켜 독자에게 직관적으로 전달하는 데 유용하다.",
    "key_claims": [
      "LLM 등 생성형 AI 컴포넌트의 통합은 매 호출마다 동일 입력에 대해 크게 다른 출력을 만드는 새로운 비결정론의 원천이다.",
      "속성 기반 테스팅, 반복 가능한 환경, 시맨틱 유사도 검사, LLM 보조 테스트 생성·검증이 비결정론적 소프트웨어를 효과적으로 테스트하는 기반 전략이다.",
      "정확한 출력을 예측할 수 없는 상황에서도 시스템 행동에 대한 의미 있는 단언을 만들 수 있다."
    ]
  },
  {
    "title": "AI and Deterministic Testing",
    "authors": ["Dick Dowdell"],
    "year": 2025,
    "type": "blog_post",
    "url": "https://medium.com/nerd-for-tech/ai-and-deterministic-testing-1be8d1a0348a",
    "summary": "AI 시스템의 결정론적 검증 불가능성을 정면으로 다루는 글. '시스템 행동이 실행마다 달라지면 신뢰 가능성을 테스트로 확보할 수 없다'는 핵심 딜레마를 명료하게 서술한다. ch02의 '결정론 전제의 붕괴' 절에서 독자가 쉽게 납득할 수 있는 직관적 논거로 인용 가능하며, 전통적 단위 테스트(one input → one expected output)가 생성 AI에서 작동하지 않는 이유를 설명하는 데 활용할 수 있다.",
    "key_claims": [
      "생성 AI 시스템은 동일한 프롬프트, 동일한 모델 가중치, 동일한 온도·샘플링 파라미터에서도 다른 출력을 생성할 수 있다 — 이는 버그가 아니라 설계상의 특성이다.",
      "출력을 신뢰성 있게 재현할 수 없으면 수정 사항을 검증할 수 없고, 논리 경로를 검증할 수 없으면 안전성을 인증할 수 없다.",
      "전통적 단위 테스트(입력 하나 → 기대 출력 하나)는 생성 AI에서 완전히 작동하지 않는다."
    ]
  },
  {
    "title": "Effective testing for machine learning systems",
    "authors": ["Jeremy Jordan"],
    "year": 2020,
    "type": "blog_post",
    "url": "https://www.jeremyjordan.me/testing-ml/",
    "summary": "전통적 소프트웨어 테스트와 ML 시스템 테스트의 구조적 차이, 그리고 평가(evaluation)와 테스팅(testing)의 역할 구분을 실용적으로 다룬 블로그 포스트. '전통 소프트웨어에서는 인간이 로직을 작성하고 테스트가 그 로직을 검증하지만, ML에서는 학습 과정이 로직을 생성한다'는 핵심 역전(inversion)을 명료하게 설명한다. TDD의 전제가 ML에서 붕괴하는 지점을 독자에게 직관적으로 납득시키는 데 적합한 자료다.",
    "key_claims": [
      "전통 소프트웨어에서는 인간이 로직을 작성하고 테스
