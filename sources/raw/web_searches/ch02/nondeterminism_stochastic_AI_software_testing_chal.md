# Search: nondeterminism stochastic AI software testing challenges evaluation methodology research

검색 결과를 충분히 수집했습니다. 이제 ch02 집필에 실제로 활용 가능한 자료들을 엄선하여 JSON 형식으로 정리하겠습니다.

---

아래는 검색 결과를 바탕으로 실제 존재가 확인된 자료들만 선별하여 JSON 형식으로 정리한 목록입니다.

```json
[
  {
    "title": "Software Engineering for Machine Learning: A Case Study",
    "authors": ["Saleema Amershi", "Andrew Begel", "Christian Bird", "Robert DeLine", "Harald Gall", "Ece Kamar", "Nachiappan Nagappan", "Besmira Nushi", "Thomas Zimmermann"],
    "year": 2019,
    "type": "academic_paper",
    "url": "https://doi.org/10.1109/ICSE-SEIP.2019.00042",
    "summary": "Microsoft 내부 500명 이상을 대상으로 한 실증 연구로, AI 컴포넌트가 기존 소프트웨어 모듈과 근본적으로 다른 세 가지 이유를 제시한다. TDD와 같은 전통 방법론이 왜 ML 시스템에서 작동하지 않는지를 설명하는 '결정론 vs 확률론' 논증의 산업 현장 근거로 활용하기에 매우 적합하다. 특히 모델의 비결정적 오류 거동(non-monotonic error behavior)과 컴포넌트 얽힘 문제는 기존 테스트 패러다임의 붕괴를 실증적으로 뒷받침한다.",
    "key_claims": [
      "AI 컴포넌트는 기존 소프트웨어 모듈과 달리 '비단조적 오류 거동(non-monotonic error behavior)'을 보이며 복잡하게 얽혀 있어 별도 모듈로 다루기 어렵다",
      "데이터 관리·버전 관리는 기존 소프트웨어 엔지니어링보다 훨씬 복잡하며, ML 시스템 개발은 Agile 같은 기존 프로세스와 통합할 때 본질적인 마찰이 발생한다",
      "ML 개발의 실험적·반복적 특성은 기존 명세 → 구현 → 테스트 순서를 근본적으로 뒤흔든다"
    ]
  },
  {
    "title": "Non-Determinism and the Lawlessness of Machine Learning Code",
    "authors": ["A. Feder Cooper", "Jonathan Frankle", "Christopher De Sa"],
    "year": 2022,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2206.11834",
    "summary": "ML 코드의 확률성(stochasticity)과 비결정론(non-determinism)을 개념적으로 정확히 구분하고, 두 개념이 왜 기존 소프트웨어 공학 및 법적 프레임워크와 충돌하는지를 논증한다. ch02의 '결정론 vs 확률론' 핵심 개념 정의 절에서 두 용어를 엄밀하게 구분하는 이론적 토대로 직접 인용 가능하다. 특히 ML 출력이 단일 결과가 아닌 '가능한 결과들의 분포'라는 관점은 EDD 도입의 당위성을 뒷받침하는 강력한 논거다.",
    "key_claims": [
      "ML 코드는 '코드 = 법칙(code as law)' 프레임 밖에 있다. 이 프레임은 코드가 결정론적이라고 가정하기 때문이다",
      "확률성(stochasticity)은 비결정론의 특수한 경우로, 결과를 확률로 추론할 수 있는 비결정적 과정이다. 두 개념은 명확히 구분되어야 한다",
      "ML 출력은 단일 결과가 아닌 가능한 결과들의 분포로 이해해야 하며, 동일한 학습 절차로도 공정성 지표가 최대 12.6%까지 차이날 수 있다"
    ]
  },
  {
    "title": "Evaluation-Driven Development and Operations of LLM Agents: A Process Model and Reference Architecture",
    "authors": ["Boming Xia", "Qinghua Lu", "Liming Zhu", "Zhenchang Xing", "Dehai Zhao", "Hao Zhang"],
    "year": 2024,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2411.13768",
    "summary": "TDD/BDD와 EDD(평가 주도 개발)를 체계적으로 비교하는 최초의 학술 논문 수준의 자료로, ch02가 선언하는 'TDD→EDD 전환' 논증의 학문적 기반이 된다. 다중 문헌 리뷰(MLR)를 통해 LLM 에이전트 평가의 핵심 도전 과제를 정리하고, 개발-운영 전체 주기에 걸쳐 평가를 중심 축으로 삼는 EDDOps 방법론을 제안한다. TDD가 '안정적 명세와 결정론적 테스트 결과'를 전제하는 반면 LLM 에이전트는 비결정적이고 명세가 유동적이라는 대비가 ch02의 핵심 논증과 정확히 일치한다.",
    "key_claims": [
      "TDD와 BDD는 안정적 명세와 결정론적 테스트 결과를 전제로 설계되었으나, LLM 에이전트는 비결정적 출력과 배포 후 지속 진화라는 특성을 가지므로 기존 방법론이 적용되지 않는다",
      "LLM 에이전트는 고정된 벤치마크와 정적 테스트 스위트로는 포착할 수 없는 창발적 행동을 보이므로 평가를 '일회성 체크포인트'가 아닌 '지속적 거버넌스 기능'으로 재정의해야 한다",
      "EDDOps는 개발 시점(오프라인)과 런타임(온라인) 평가를 하나의 폐쇄 피드백 루프로 통합함으로써 더 안전하고 추적 가능한 LLM 에이전트 진화를 지원한다"
    ]
  },
  {
    "title": "A Survey on Evaluation of Large Language Models",
    "authors": ["Yupeng Chang", "Xu Wang", "Jindong Wang", "Yuan Wu", "Linyi Yang", "Kaijie Zhu", "Hao Chen", "Xiaoyuan Yi", "Cunxiang Wang", "Yidong Wang", "Wei Ye", "Yue Zhang", "Yi Chang", "Philip S. Yu", "Qiang Yang", "Xing Xie"],
    "year": 2024,
    "type": "academic_paper",
    "url": "https://dl.acm.org/doi/10.1145/3641289",
    "summary": "ACM TIST에 게재된 LLM 평가 방법론의 포괄적 서베이로, '무엇을, 어디서, 어떻게 평가할 것인가'라는 세 차원으로 평가 방법론을 체계화한다. ch02에서 '평가가 개발의 핵심 규율이어야 한다'는 EDD 선언을 뒷받침하는 학술적 근거로 활용 가능하다. 특히 LLM 평가가 태스크 수준을 넘어 사회적 위험 수준까지 포함해야 한다는 주장은 기존 소프트웨어 테스팅과의 질적 차이를 설명하는 데 유용하다.",
    "key_claims": [
      "LLM 평가는 더 이상 태스크 수행 능력만이 아니라 사회적 수준의 잠재적 위험을 이해하기 위해서도 점점 더 중요해지고 있다",
      "평가는 LLM 개발을 더 효과적으로 지원하기 위한 필수 규율(essential discipline)로 다루어져야 한다",
      "기존 NLP 정확도 메트릭(BLEU 등)은 LLM의 실제 능력과 위험을 포착하기에 불충분하며, 추론·윤리·교육 등 다차원 평가 방법론이 필요하다"
    ]
  },
  {
    "title": "The Challenges of Testing in a Non-Deterministic World",
    "authors": ["Donald Firesmith"],
    "year": 2017,
    "type": "blog_post",
    "url": "https://www.sei.cmu.edu/blog/the-challenges-of-testing-in-a-non-deterministic-world/",
    "summary": "카네기멜론대 소프트웨어공학연구소(CMU SEI)의 공식 블로그로, 비결정론적 시스템이 기존 테스트 방법론에 제기하는 구조적 도전 과제를 정리한다. 동일 입력에 대해 다른 결과가 나올 때 '버그인지 이상인지 우연인지' 판별할 수 없다는 문제를 명확히 규정하며, TDD의 '빨강-녹색-리팩토링' 순환이 왜 AI 시스템에서 작동하지 않는지를 설명하는 직관적 예시로 활용 가능하다. CMU SEI라는 권위 있는 출처로 독자 신뢰도를 높이는 데 기여한다.",
    "key_claims": [
      "개발자와 테스터 대부분은 시스템이 결정론적으로 작동한다고 암묵적으로 가정하지만, 비결정론적 시스템에서는 동일한 테스트가 반복 시 다른 결과를 낼 수 있다",
      "비결정론적 시스템에서는 합격/불합격이 아닌 '부분 합격'과 '불확정(indeterminate)' 결과가 발생하며, 확률적 합격 기준(stochastic pass/fail criteria)이 필요하다",
      "검증 오라클(adequate oracle)의 부재, 창발 행동(emergent behavior), 블랙스완 이벤트는 비결정론적 세계에서의 테스팅을 근본적으로 어렵게 만든다"
    ]
  },
  {
    "title": "Seven Recommendations for Testing in a Non-Deterministic World",
    "authors": ["Donald Firesmith"],
    "year": 2017,
    "type": "blog_post",
    "url": "https://www.sei.cmu.edu/blog/seven-recommendations-for-testing-in-a-non-deterministic-world/",
    "summary": "위 SEI 블로그의 후속 편으로, 비결정론적 시스템 테스팅의 실천적 대안을 제시한다. '테스팅만으로는 충분하지 않으며 정적·동적 분석, 통계적 모델 체킹 등을 병행해야 한다'는 주장은 EDD로의 전환이 단순한 방법론 교체가 아니라 패러다임 전환임을 강조하는 데 활용할 수 있다. ch02에서 '왜 기존 방법으로는 부족한가'를 설명하는 절에서 구체적 근거로 인용 가능하다.",
    "key_claims": [
      "비결정론적 결함을 발견하려면 테스팅이 거의 항상 필요하지만, 테스팅만으로는 충분하지 않다. 정적·동적 분석과 모델링·시뮬레이션으로 보완해야 한다",
      "통계적 모델 체킹(statistical model checking)은 전통적 테스팅이 처리할 수 없는 비결정론을 다루는 유효한 대안 접근법이다"
    ]
  },
  {
    "title": "Testing Non-Deterministic Behaviors in AI Systems: Challenges and Innovations",
    "authors": ["Şermin Eldek"],
    "year": 2024,
    "type": "blog_post",
    "url": "https://medium.com/@sermineldek/testing-non-deterministic-behaviors-in-ai-systems-challenges-and-innovations-6e1996025504",
    "summary": "AI 시스템의 비결정론이 어디서 기인하는지(확률적 알고리즘, 적응형 학습, 모델 초기화 등)를 분류하고 기존 테스팅 방법론의 한계를 설명한다. ch02의 도입부에서 '왜 AI는 기존 소프트웨어와 다른가'를 직관적으로 설명하는 구체적 예시(입력 동일 → 출력 상이)를 제공한다. 독자 접근성이 높은 Medium 글이므로 이론 설명 전 워밍업 사례로 활용하기 좋다.",
    "key_claims": [
      "AI의 비결정론은 동일한 입력이 반복 평가 시 다른 출력을 낳을 때 발생하며, 이는 확
