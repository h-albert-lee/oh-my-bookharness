# Search: why test-driven development fails LLM nondeterministic AI systems software engineering

모든 검색이 완료되었습니다. 이제 찾은 자료를 정리하겠습니다.

---

아래는 검색을 통해 확인한 **실제 존재하는 자료**만을 엄선하여 ch02 집필에 활용 가능한 형태로 정리한 결과입니다.

---



LLM의 확률론적 특성이 결정론적 소프트웨어 개발 방법론과 근본적으로 충돌한다는 것은

 이제 학계와 실무 모두에서 광범위하게 논의되고 있습니다. 

TDD·BDD가 LLM 시스템에서 작동하지 않는 이유는 정적 요구사항과 실행 가능한 오라클에 의존하고, 이진 pass/fail 판정으로 맥락 의존적 결과를 포착하지 못하며, 사전 배포 검증에만 집중하여 런타임 드리프트를 간과하기 때문입니다.



아래는 최종 정리된 JSON 참고자료 목록입니다.

```json
[
  {
    "title": "Non-Determinism of 'Deterministic' LLM Settings",
    "authors": [
      "Berk Atil", "Sarp Aykent", "Alexa Chittams", "Lisheng Fu",
      "Rebecca J. Passonneau", "Evan Radcliffe", "Guru Rajan Rajagopal",
      "Adam Sloan", "Tomasz Tudrej", "Ferhan Ture", "Zhe Wu",
      "Lixinyu Xu", "Breck Baldwin"
    ],
    "year": 2024,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2408.04667",
    "summary": "temperature=0 등 결정론적 설정으로 구성한 LLM 5종을 8개 태스크·10회 반복 실험한 결과, 정확도 편차가 최대 15%, 최악·최선 성능 격차가 최대 70%에 달함을 실증한다. '결정론적으로 설정된 LLM도 사실상 비결정론적'이라는 명제를 수치로 증명하므로, ch02의 '왜 기존 TDD가 무력화되는가' 논증의 핵심 증거 자료로 활용할 수 있다. 특히 비결정성이 컴퓨팅 효율화(입력 버퍼 혼합)와 구조적으로 연결되어 있어 쉽게 해결되지 않는다는 점도 강조할 수 있다.",
    "key_claims": [
      "temperature=0으로 설정해도 LLM은 동일 입력에 대해 서로 다른 출력을 생성하며, 어떤 모델도 모든 태스크에서 일관된 정확도를 유지하지 못했다.",
      "비결정성은 GPU 병렬 처리와 입력 버퍼 혼합 등 인프라 최적화에 기인하므로 구조적으로 제거하기 어렵다.",
      "단일 실험 결과로 LLM 성능을 보고하는 관행은 신뢰도를 심각하게 저하시키며, 최대-최솟값 범위 보고가 필요하다."
    ]
  },
  {
    "title": "Challenges in Testing Large Language Model Based Software: A Faceted Taxonomy",
    "authors": [
      "Felix Dobslaw", "Robert Feldt", "Juyeon Yoon", "Shin Yoo"
    ],
    "year": 2025,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2503.00481",
    "summary": "LLM 기반 소프트웨어 테스트의 도전 과제를 4개 패싯(테스트 대상, 목표, 오라클, 입력)으로 분류한 체계적 분류법을 제시한다. 결정론적 오라클이라는 전통 소프트웨어 테스트의 전제가 LLM 앞에서 붕괴함을 이론적으로 정리하며, '정확성을 단일 이진 속성이 아닌 결과의 분포'로 재정의해야 한다는 핵심 주장은 ch02의 TDD 무력화 논증과 EDD 대안 제시를 뒷받침하는 학술적 근거로 활용 가능하다.",
    "key_claims": [
      "LLM은 전통 ML 소프트웨어와도 다른 비결정성을 도입하며, 단순 출력 비교나 통계적 정확도만으로는 정확성 검증이 불가능하다.",
      "기존 패러다임(결정론적·확률론적·ML 특화)은 모두 LLM 기반 시스템의 다층적 복잡성을 처리하지 못한다.",
      "현행 테스트 도구들은 테스트 실행을 독립 이벤트로 취급하고 명시적 집계 메커니즘이 없어, 모델 버전과 반복 실행 간 변동성을 제대로 포착하지 못한다."
    ]
  },
  {
    "title": "Evaluation-Driven Development and Operations of LLM Agents: A Process Model and Reference Architecture",
    "authors": [
      "Boming Xia", "Qinghua Lu", "Liming Zhu", "Zhenchang Xing",
      "Dehai Zhao", "Hao Zhang"
    ],
    "year": 2024,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2411.13768",
    "summary": "TDD·BDD가 LLM 에이전트에 작동하지 않는 4가지 구조적 한계를 분석하고, 평가를 개발 라이프사이클 전반의 '지속적 거버넌스 함수'로 내재화한 EDDOps 프로세스 모델과 참조 아키텍처를 제안한다. TDD→EDD 전환을 선언하는 ch02의 논리적 뼈대로 활용할 수 있는 가장 직접적인 학술 자료이며, 특히 TDD 한계를 4가지로 명료하게 구분한 분석 틀은 인용 가치가 높다.",
    "key_claims": [
      "TDD·BDD는 ① 정적 요구사항 의존, ② 이진 pass/fail 판정, ③ 사전 배포 검증에 집중한 런타임 드리프트 간과, ④ 창발적 행동·공정성 등 질적 요소 지원 부재라는 4가지 한계로 LLM 에이전트에 적합하지 않다.",
      "평가를 최종 체크포인트가 아닌 지속적 거버넌스 함수로 내재화해야 하며, 오프라인(개발 시점)과 온라인(런타임) 평가를 통합한 폐루프가 필요하다.",
      "LLM 에이전트는 배포 후에도 명시적 코드·모델 변경 없이 행동이 달라지므로, 정적 테스트 스위트 중심의 접근법은 구조적으로 한계가 있다."
    ]
  },
  {
    "title": "LLMs Are Facing a QA Crisis: Here's How We Could Solve It",
    "authors": ["LogRocket Editorial"],
    "year": 2025,
    "type": "blog_post",
    "url": "https://blog.logrocket.com/llms-are-facing-a-qa-crisis/",
    "summary": "결정론적 코드에서 확률론적 AI로의 전환이 QA에 근본적 위기를 초래했음을 설명하며, 기존 단위 테스트가 LLM 시스템에서 작동하지 않는 이유를 실무 관점에서 정리한다. TDD 등장 배경('2+2=4는 항상 성립한다'는 소프트웨어 결정론)을 소개한 뒤 LLM이 왜 이 전제를 깨트리는지 서술하므로, ch02 도입부에서 결정론적 소프트웨어와의 대비를 독자에게 직관적으로 설명하는 데 유용하다.",
    "key_claims": [
      "전통 QA는 입력이 특정 출력에 매핑되는 안정적·통제 가능한 환경을 전제하지만, LLM은 동일 프롬프트에서 50개의 서로 다른 유효한 응답을 생성할 수 있어 이 전제가 붕괴한다.",
      "'요약하라'는 프롬프트에 LLM은 기술적으로 모두 정확하지만 예측 불가능한 다양한 응답을 돌려주므로 고정 테스트 케이스 작성이 불가능하다.",
      "AI 시스템의 버그는 단순 크래시가 아니라 사용자를 오도하고 편향을 증폭시키며 신뢰를 무너뜨리는 방식으로 작동해 전통적 버그보다 훨씬 심각하다."
    ]
  },
  {
    "title": "The Complete Guide for TDD with LLMs",
    "authors": ["Rogério Chaves"],
    "year": 2024,
    "type": "blog_post",
    "url": "https://rchavesferna.medium.com/the-complete-guide-for-tdd-with-llms-1dfea9041998",
    "summary": "TDD가 LLM 애플리케이션 개발에 '철학적으로는 잘 맞지만, 실행 방식은 맞지 않는다'는 역설을 실무자 관점에서 해부한다. 단위 테스트가 LLM에 맞지 않는 이유, 그리고 그 대안으로 확률적 테스트가 필요한 이유를 구체적 코드 예시와 함께 설명한다. ch02에서 TDD의 '정신(spec first)'은 유효하지만 '방법론(단위 테스트)'은 무력화된다는 논증을 구체화할 때 유용한 참고 자료다.",
    "key_claims": [
      "LLM은 확률적으로 실패할 수 있어 단위 테스트에 적합하지 않으며, 대부분 통과를 보장하려면 많은 예시가 필요하다.",
      "TDD 철학(구현 전 기대값 정의)은 LLM 개발에도 유효하지만, 단위 테스트라는 실행 메커니즘은 LLM의 비결정성과 충돌한다.",
      "작동하는 프롬프트도 변경 시 쉽게 깨질 수 있고, 언어의 개방성 때문에 모든 기대 동작을 사전에 정의하기 어렵다."
    ]
  },
  {
    "title": "Beyond Traditional Testing: Addressing the Challenges of Non-Deterministic Software",
    "authors": ["AWS / DEV Community"],
    "year": 2024,
    "type": "blog_post",
    "url": "https://dev.to/aws/beyond-traditional-testing-addressing-the-challenges-of-non-deterministic-software-583a",
    "summary": "분산 시스템부터 LLM까지 비결정론적 소프트웨어가 점차 보편화되고 있음을 실무 관점에서 설명하며, 카오스 엔지니어링·적대적 테스트 등 대안적 접근법을 소개한다. ch02에서 LLM만의 문제가 아니라 소프트웨어 공학 전반의 패러다임 전환임을 보여주는 맥락 자료로 활용 가능하며, AWS라는 출처의 신뢰도도 인용에 유리하다.",
    "key_claims": [
      "비결정론적 소프트웨어는 동일한 조건에서도 다른 출력을 생성하며, 이는 LLM 통합으로 더욱 심화되고 있다.",
      "전통적 테스트 전략은 완전히 예측 가능하지 않은 환경에서 신뢰성과 일관성을 보장하는 데 근본적 한계를 갖는다.",
      "LLM 기반 시스템 테스트에서는 입력 프롬프트로 에지 케이스를 의도적으로 생성하는 적대적 테스트 접근법이 유효하다."
    ]
  },
  {
    "title": "A Pragmatic Guide to LLM Evals for Devs",
    "authors": ["The Pragmatic Engineer (Gergely Orosz)", "Hamel Husain (인터뷰 대상)"],
    "year": 2025,
    "type": "blog_post",
    "url": "https://newsletter.pragmaticengineer.com/p/evals",
    "summary": "LLM은 비결정론적이므로 전통적 자동화 테스트 대신 'evals(평가)'가 AI 엔지니어링의 핵심 도구로 부상하고 있음을 3,000명 이
