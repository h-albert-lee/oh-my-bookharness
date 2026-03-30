# Search: probabilistic systems vs deterministic systems software quality assurance structural differences

조사 결과를 바탕으로 ch02 집필에 참고할 자료를 정리했습니다. 아래는 실제로 존재하는 자료만 포함한 JSON 결과입니다.

---

```json
[
  {
    "title": "Beyond deterministic testing: Why testing AI systems is fundamentally different",
    "authors": ["Planit Testing"],
    "year": 2025,
    "type": "blog_post",
    "url": "https://www.planit.com/beyond-deterministic-testing-why-testing-ai-systems-is-fundamentally-different/",
    "summary": "결정론적 시스템은 '검증(verify)'하고 확률론적 시스템은 '평가(evaluate)'해야 한다는 핵심 명제를 구조적으로 설명한다. 기존 테스트 접근법이 AI 시스템에서 구조적으로 실패하는 이유—컴포넌트 결함이 아닌 오케스트레이션에서 오류가 발생—를 논증하는 데 직접 활용 가능하다.",
    "key_claims": [
      "결정론적 시스템은 검증(verified)되고, 확률론적 시스템은 평가(evaluated)된다—불확실성을 제거하는 것이 아니라 관리하는 것이다.",
      "결정론적 테스트 모델을 확률론적 시스템에 계속 적용하면 프로덕션에서 AI를 체계적으로 과소 테스트하게 된다.",
      "각 컴포넌트가 개별적으로 '정상' 동작해도 시스템 수준 결과는 허용 불가능할 수 있으며, 실패는 개별 결함이 아닌 오케스트레이션에서 발생한다."
    ]
  },
  {
    "title": "Evaluation-Driven Development and Operations of LLM Agents: A Process Model and Reference Architecture",
    "authors": ["Busany, Nimrod", "et al."],
    "year": 2025,
    "type": "academic_paper",
    "url": "https://arxiv.org/html/2411.13768v3",
    "summary": "TDD/BDD가 결정론적 시스템에는 효과적이지만 LLM 에이전트에는 구조적으로 부적합한 이유를 4가지 한계(정적 요구사항, 이진 pass/fail, 배포 전 집중, 창발적 행동 미지원)로 체계적으로 논증한다. EDD(평가 주도 개발)가 필요한 배경을 학술적으로 뒷받침하는 핵심 논문이다.",
    "key_claims": [
      "TDD와 BDD는 결정론적 시스템에 효과적이지만, 개방형 맥락에서 적응적으로 동작하는 LLM 에이전트에는 본질적으로 적합하지 않다.",
      "전통적 단위 테스트의 pass/fail 이진 판정은 LLM 에이전트에 부적합하며, 하나의 시나리오에서 다수의 응답이 유효할 수 있다.",
      "LLM 에이전트는 배포 후에도 사용자 피드백과 환경 변화에 따라 지속적으로 진화하므로, 배포 전 검증에만 집중하는 TDD/BDD는 런타임 드리프트를 다루지 못한다."
    ]
  },
  {
    "title": "From TDD to EDD: Why Evaluation-Driven Development Is the Future of AI Engineering",
    "authors": ["Busany, Nimrod"],
    "year": 2025,
    "type": "blog_post",
    "url": "https://medium.com/@nimrodbusany_9074/from-tdd-to-edd-why-evaluation-driven-development-is-the-future-of-ai-engineering-a5e5796b2af4",
    "summary": "TDD의 'Does it work? (Yes/No)'와 EDD의 'How well does it work? (0~100%, with error bars)'의 대비를 통해 두 패러다임의 구조적 차이를 명쾌하게 설명한다. OpenAI, Microsoft Azure, Google DeepMind가 모두 eval 프레임워크를 핵심 개발 사이클로 채택했음을 사례로 제시한다.",
    "key_claims": [
      "EDD는 단순히 TDD에 단계를 추가한 것이 아니라 신뢰할 수 있는 AI 시스템을 구축하는 방식 자체를 근본적으로 재구성한 것이다.",
      "TDD는 '작동하는가(Yes/No)'를 묻지만, EDD는 '얼마나 잘 작동하는가(0~100%)'를 묻는다—이진 판정에서 통계적 측정으로의 전환이다.",
      "OpenAI, Microsoft Azure, Google DeepMind 모두 고품질 eval 구축을 개발 사이클의 핵심으로 공식화하고 있다."
    ]
  },
  {
    "title": "Probabilistic and Deterministic Systems (Decision Matrix Substack)",
    "authors": ["Vaughan, Daniel"],
    "year": 2025,
    "type": "blog_post",
    "url": "https://decisionmatrix.substack.com/p/probabilistic-and-deterministic-systems",
    "summary": "결정론적 시스템과 확률론적 시스템의 구조적 차이—특히 테스트 방식의 차이(pass/fail vs. evals)—를 명확히 설명하며, 에이전틱 워크플로우에서 오류가 복합(compound)되는 문제를 다룬다. '전통적 단위 테스트는 AI 애플리케이션에 작동하지 않는다'는 테제를 실용적으로 논증하는 데 활용할 수 있다.",
    "key_claims": [
      "GenAI 시스템은 확률론적이며 비결정론적이다—예측 가능한 출력을 생성하는 전통 소프트웨어와 달리, AI 시스템은 근본적으로 다른 빌드 및 테스트 접근법을 필요로 한다.",
      "전통적 단위 테스트는 AI 애플리케이션에 작동하지 않는다—확률론적 시스템에는 단순 pass/fail 테스트가 아닌 데이터셋, 메트릭, 반복 측정으로 구성된 평가 프레임워크가 필요하다.",
      "에이전틱 워크플로우에서는 여러 LLM이 체이닝되어 오류가 복합적으로 누적될 수 있으며, 이는 시스템 품질을 잠재적으로 크게 저하시킨다."
    ]
  },
  {
    "title": "Generative AI vs. Deterministic Testing: Why Predictability Matters",
    "authors": ["testRigor"],
    "year": 2024,
    "type": "blog_post",
    "url": "https://testrigor.com/blog/generative-ai-vs-deterministic-testing/",
    "summary": "예측 가능성이 소프트웨어 품질보증의 핵심 전제임을 설명하고, AI의 비결정론적 특성이 전통적 테스트·인증·검증 기준을 충족하지 못하게 만드는 구조적 이유를 분석한다. 'AI는 기존 소프트웨어 테스트 표준에 부합하지 않는다'는 주장의 직접적 근거로 활용 가능하다.",
    "key_claims": [
      "생성형 AI는 동일한 입력을 두 번 제공해도 다른 결과를 생성할 수 있으며, 이 비결정론적 특성은 일관된 테스트에 어려움을 야기한다.",
      "AI는 그 비결정론적·확률론적 특성으로 인해 전통적인 소프트웨어 테스트, 인증, 검증 기준에 부합하지 않는다.",
      "예측 가능성은 소프트웨어 개발의 근본 전제이며, 작성한 테스트 케이스는 모두 어떤 기대치에 대한 검증이다—이 전제가 AI에서는 성립하지 않는다."
    ]
  },
  {
    "title": "Eval-Driven Development (evaldriven.org)",
    "authors": ["evaldriven.org"],
    "year": 2026,
    "type": "documentation",
    "url": "https://evaldriven.org/",
    "summary": "TDD의 이진 pass/fail 기준이 확률론적 AI 시스템에서 왜 작동하지 않는지를 간결하게 선언하고, EDD가 이를 어떻게 대체하는지를 실천적 관점에서 정의한다. EDD 소개 섹션에서 TDD 무력화의 핵심 이유를 한 문단으로 압축하는 데 인용하기 좋다.",
    "key_claims": [
      "TDD는 결정론적 코드에 유효한 이진 pass/fail 기준을 사용하지만, AI 시스템은 확률론적이어서 실행, 모델, 프롬프트에 걸쳐 출력이 달라진다.",
      "EDD는 테스트를 작성하기 전에 '어느 정도의 점수가 충분한가'라는 성공 임계값을 먼저 정의하도록 요구하며, 이 단계를 명시적이고 필수적으로 만든다.",
      "MLOps가 '아직 작동하고 있는가?'를 묻는다면, EDD는 '애초에 작동한다는 것을 어떻게 아는가?'를 묻는다."
    ]
  },
  {
    "title": "Navigating non-determinism: Best practices for testing AI apps",
    "authors": ["Hypermode"],
    "year": 2025,
    "type": "blog_post",
    "url": "https://hypermode.com/blog/testing-ai-best-practices",
    "summary": "AI 시스템이 temperature=0으로 설정해도 왜 비결정론적인지를 기술적으로 설명하고, 전통적 exact-match 기반 테스트가 AI 검증에 실패하는 구조적 이유를 제시한다. '정확한 출력 매칭에 의존하는 전통 테스트 접근법은 AI 시스템을 효과적으로 검증하지 못한다'는 주장의 기술적 근거로 활용 가능하다.",
    "key_claims": [
      "결정론적 동작을 위해 설정된 AI 시스템도 동일한 입력에 대해 다양한 출력을 생성할 수 있으며, temperature=0으로 설정해도 미묘한 출력 차이가 발생할 수 있다.",
      "전통적 테스트 접근법—정확한 출력 매칭에 의존하는 방식—은 AI 시스템을 효과적으로 검증하지 못한다.",
      "AI는 수천 가지의 유효하고 주관적이며 예측 불가능한 출력 공간을 가지므로, 단일하고 결정론적이며 알 수 있는 정답을 전제로 하는 TDD는 근본적으로 한계를 가진다."
    ]
  },
  {
    "title": "The Challenges of Testing in a Non-Deterministic World",
    "authors": ["Carnegie Mellon University SEI"],
    "year": 2023,
    "type": "blog_post",
    "url": "https://www.sei.cmu.edu/blog/the-challenges-of-testing-in-a-non-deterministic-world/",
    "summary": "CMU 소프트웨어 엔지니어링 연구소(SEI)의 권위 있는 관점에서 비결정론적 시스템 테스팅의 구조적 문제—애매한 성공 기준, 테스트 오라클 부재, 창발적 행동—를 체계적으로 정리한다. 학문적 신뢰도가 높아 '기존 테스트 패러다임의 한계'를 입증하는 절에서 권위 있는 인용 출처로 활용 가능하다.",
    "key_claims": [
      "비결정론적 시스템 테스팅의 핵심 과제로 학습/적응 검증, 퍼지 성공 기준(pass/fail이 아닌 부분 통과·미결정 포함), 적절한 테스트 오라클 부재, 창발적 행동이 있다.",
      "비결정론적 소프트웨어는 결함이 희귀하고 재현이 어렵기 때문에 대규모 테스트 케이스 자동화가 필요하며, 이는 기존 방식으로 감당하기 어렵다.",
      "개발자와 테스터는 비결정론적 결함을 탐지하도록 설계된 테스트를 실행하지 않아 테스트가 허위 신뢰(false confidence)를 제공하고 결함이 운영 환경으로 유출된다."
    ]
  },
  {
    "title": "Adapting TDD for Reliable AI Systems",
    "authors": ["Galileo AI"],
    "year": 2024,
    "type": "blog_post",
    "url": "https://galile
