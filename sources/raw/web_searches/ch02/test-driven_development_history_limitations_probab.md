# Search: test-driven development history limitations probabilistic systems paradigm shift software quality

검색 결과를 종합하여 ch02 집필에 직접 활용 가능한 자료들을 아래와 같이 정리합니다.

---

```json
[
  {
    "title": "Evaluation-Driven Development and Operations of LLM Agents: A Process Model and Reference Architecture",
    "authors": ["Boming Xia", "et al."],
    "year": 2024,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2411.13768",
    "summary": "TDD/BDD가 LLM 에이전트에 왜 불충분한지를 4가지 구조적 한계로 명시하고, 그 대안으로 EDDOps(평가 주도 개발·운영)를 제안한다. TDD→EDD 전환의 논증 구조와 용어 체계를 직접 참조할 수 있으며, 'EDD는 사전 배포 단계에 국한된 TDD와 달리 런타임 이후까지 평가를 확장한다'는 핵심 주장이 ch02의 패러다임 선언에 직접 인용 가능하다. EDD와 TDD의 비교표(Table 1)는 두 패러다임의 차이를 시각화하는 데 유용하다.",
    "key_claims": [
      "TDD/BDD는 정적 요구사항과 결정론적 테스트 결과를 전제하지만, LLM 에이전트는 비결정론적이고 사후 배포 이후에도 계속 진화한다.",
      "TDD의 4가지 구조적 한계: (i) 정적 요구사항 의존, (ii) 이진 pass/fail 단언, (iii) 배포 전 검증에 집중, (iv) 창발 행동·공정성 등 정성적 요소 미지원",
      "EDD는 평가를 개발 생애주기 전체에 걸친 연속적·지배적 기능으로 내재화한다."
    ]
  },
  {
    "title": "From Test- and Behavior-Driven to Evaluation-Driven Development",
    "authors": ["Vivek Suresh"],
    "year": 2025,
    "type": "blog_post",
    "url": "https://medium.com/ylogx/from-test-and-behavior-driven-to-evaluation-driven-development-68865002aea2",
    "summary": "TDD(Kent Beck, 1990s) → BDD(Dan North, 2006) → EDD로의 방법론 계보를 명확히 정리한다. AI 시스템이 TDD/BDD를 무력화하는 3가지 이유(확률적 출력, 정적 테스트 대 동적 행동, 다차원 품질)를 독자 친화적으로 설명하며, ch02의 '기존 방법론의 한계' 절 서술에 참조 가능하다. TDD의 역사적 맥락과 EDD의 필요성을 하나의 흐름으로 연결하는 구조가 ch02의 논증 전개와 일치한다.",
    "key_claims": [
      "TDD는 Kent Beck이 1990년대 말 XP의 핵심 관행으로 정립했으며, 코드를 먼저 테스트하는 방식으로 소프트웨어 엔지니어링을 재편했다.",
      "TDD와 BDD는 고정된 pass/fail 경계를 가진 결정론적 시스템을 전제하지만, Agentic AI는 이 전제를 위반한다.",
      "EDD는 배포 전후를 막론하고 연속적·적응적·다차원적 평가를 개발 생애주기의 1등 시민으로 만든다."
    ]
  },
  {
    "title": "Hidden Technical Debt in Machine Learning Systems",
    "authors": ["D. Sculley", "Gary Holt", "Daniel Golovin", "Eugene Davydov", "Todd Phillips", "Dietmar Ebner", "Vinay Chaudhary", "Michael Young", "Jean-François Crespo", "Dan Dennison"],
    "year": 2015,
    "type": "academic_paper",
    "url": "https://proceedings.neurips.cc/paper_files/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf",
    "summary": "Google의 ML 시스템 운영 경험을 바탕으로, ML 시스템이 전통적 코드의 유지보수 문제에 더해 ML 고유의 기술 부채를 추가로 안고 있음을 논증한 기념비적 논문이다. 데이터 의존성, 경계 침식, 숨겨진 피드백 루프 등 ML 고유 위험 요소는 TDD가 전제하는 '코드 중심 결정론적 시스템' 모델이 AI 시스템에 적용될 때 무력화되는 메커니즘을 구조적으로 뒷받침한다. 'ML 시스템에서 데이터가 코드를 대체한다면, 코드가 아닌 데이터도 테스트되어야 한다'는 명제는 EDD로의 전환 필요성을 정당화하는 근거로 활용 가능하다.",
    "key_claims": [
      "ML 시스템은 전통적 코드의 유지보수 문제를 모두 가지면서 ML 고유의 추가 기술 부채(데이터 의존성, 경계 침식, 피드백 루프 등)를 누적한다.",
      "전통적 코드 수준의 기술 부채 해소 방법(단위 테스트, 리팩터링 등)은 시스템 수준의 ML 기술 부채를 처리하기에 충분하지 않다.",
      "재현성 부채(Reproducibility Debt): 무작위화 알고리즘, 분산 학습의 비결정론, 초기 조건 의존 등이 ML 시스템의 엄밀한 재현을 어렵게 만든다."
    ]
  },
  {
    "title": "Testing AI-Based Software Systems: From Theory to Practice",
    "authors": ["Shay Ginsbourg"],
    "year": 2025,
    "type": "academic_paper",
    "url": "https://www.researchgate.net/publication/399054078_Testing_AI-Based_Software_Systems_From_Theory_to_Practice",
    "summary": "결정론적 시스템을 위해 설계된 전통적 소프트웨어 테스트 패러다임이 확률적 행동, 지속적 학습, 적응적 속성을 가진 AI 시스템에 적용될 때 구식이 되고 부적합해진다는 점을 체계적으로 논증한다. 결정론에서 확률론으로의 패러다임 전환을 명시적으로 선언하며, ch02의 핵심 주제인 '왜 기존 방법으로는 AI를 테스트할 수 없는가'를 학술적으로 뒷받침한다.",
    "key_claims": [
      "결정론적 시스템과 정적 입력·예측 가능한 출력을 위해 설계된 전통적 소프트웨어 테스트 패러다임은 확률적 행동, 지속적 학습, 적응적 속성을 지닌 AI 시스템에는 구식이고 부적합하다.",
      "AI 테스팅은 결정론적 출력 검증에서 학습된 행동, 확률적 성능, 공정성·견고성 등 윤리적 고려사항의 검증으로 패러다임이 이동했다.",
      "AI 소프트웨어의 고유 도전(비결정론적 행동, 데이터 의존성, 블랙박스 특성)은 전통적 수동 테스트 케이스 설계를 부적합하게 만든다."
    ]
  },
  {
    "title": "Adapting TDD for Reliable AI Systems",
    "authors": ["Galileo AI Team"],
    "year": 2024,
    "type": "blog_post",
    "url": "https://galileo.ai/blog/test-driven-development-ai-systems",
    "summary": "전통적 TDD의 이진 pass/fail 구조가 AI 시스템의 확률론적 특성 앞에서 어떻게 실패하는지, 그리고 통계적 범위 검증, 다중 실행 테스트 등으로 어떻게 적응해야 하는지를 실용적으로 설명한다. TDD가 확률론적 시스템에서 무력화되는 메커니즘을 구체적 예시로 보여주므로 ch02의 '결정론 vs 확률론' 절에서 TDD 실패 사례 서술에 활용할 수 있다.",
    "key_claims": [
      "전통적 TDD는 명확한 pass/fail 결과를 가진 결정론적 테스트를 사용하며, 이 접근법은 AI 시스템의 확률론적 특성 때문에 실패한다.",
      "AI 테스팅에서는 정확한 출력을 요구하는 대신 허용 가능한 통계적 범위 안에 출력이 드는지를 검증하는 확률적 단언이 필요하다.",
      "AI의 비결정론적 출력에서는 단일 실행 테스트가 놓칠 수 있는 불일치 행동을 잡기 위해 다중 실행 테스트가 필수적이다."
    ]
  },
  {
    "title": "Beyond Deterministic Testing: Why Testing AI Systems Is Fundamentally Different",
    "authors": ["Planit Testing Team"],
    "year": 2025,
    "type": "blog_post",
    "url": "https://www.planit.com/beyond-deterministic-testing-why-testing-ai-systems-is-fundamentally-different/",
    "summary": "전통적 테스팅이 전제하는 '행동의 안정성'이 AI 시스템에서 어떻게 붕괴하는지를 RAG 시스템, 모델 버전 업그레이드 등 실제 사례로 구체화한다. '시스템은 결정론적으로 실패하는 것이 아니라 확률론적으로 실패한다'는 명제는 ch02의 핵심 논증을 뒷받침하는 현업 증거로 활용 가능하다.",
    "key_claims": [
      "전통적 테스팅은 예측 가능한 행동과 사전 정의된 기대 결과를 가정하지만, 이는 확률론적·비결정론적 AI 시스템에 대해 성립하지 않는 전제다.",
      "코드 변경 없이 커버리지가 흔들리는 새로운 형태의 회귀 불안정성이 AI 시스템에서 발생하며, 이는 전통적 회귀 테스팅의 핵심 전제(로직 변경 없으면 행동 안정)를 위반한다.",
      "AI 시스템은 결정론적으로 실패하지 않고 확률론적으로 실패하며, 이 차이가 품질 평가 방식 전체를 바꾼다."
    ]
  },
  {
    "title": "The Limitations of Test Driven Development (TDD)",
    "authors": ["219 Design Team"],
    "year": 2025,
    "type": "blog_post",
    "url": "https://219design.com/limitations-of-test-driven-development/",
    "summary": "TDD가 탄생한 역사적 맥락(XP, 1990s)과 함께 TDD가 본래 전제하는 조건(순수 로직 함수, 명확히 정의된 입·출력)을 명시한다. TDD가 잘 작동하는 영역과 작동하지 않는 영역의 경계를 설명하므로, ch02에서 '결정론적 전제'를 구체화하는 데 유용하다. 특히 'TDD는 입출력이 명확히 정의된 순수 로직 함수에서 가장 잘 작동한다'는 명제는 AI 시스템과의 대비를 선명하게 만든다.",
    "key_claims": [
      "TDD는 Extreme Programming(XP)의 관행으로 1990년대 중반에 개발되었으며, 모든 XP 관행을 함께 채택할 때 각 관행의 약점을 상호 보완한다는 전제 위에서 설계되었다.",
      "TDD는 입력과 출력이 명확히 정의된 순수 로직 함수에서 가장 잘 작동한다.",
      "테스트가 통과해도 시스템이 실세계에서 실패하는 경우(인터페이스 비결정성, 비동기 호출 등)는 TDD의 구조적 한계를 드러낸다."
    ]
  },
  {
    "title": "TDD & AI: The Giant Gap Between Claim and Practice",
    "authors": ["Marco Kotrotsos"],
    "year": 2026,
    "type": "blog_post",
    "url": "https://kotrotsos.medium.com/tdd-ai-the-giant-gap-between-claim-and-practice-8b3bfe5a3f7f",
    "summary": "TDD + AI 조합이 실제 현장에서 어떻게 작동하지 않는지를 비판적으로 분석한 최신 실무자
