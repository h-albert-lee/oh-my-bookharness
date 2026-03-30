# Search: deterministic vs probabilistic systems software design implications "test-driven development" AI machine learning

수집된 자료를 바탕으로 ch02 집필에 실제로 참고할 수 있는 자료들을 엄선하여 JSON으로 정리했습니다. 아래는 조사 결과와 자료 목록입니다.

---

## 조사 결과 요약

수집된 자료들은 크게 **4개 클러스터**로 분류됩니다:

1. **결정론 vs. 확률론 설계 차이** — 기존 소프트웨어의 "입력→동일출력" 전제가 AI 시스템에서 무너지는 구조적 원인을 설명하는 글
2. **TDD의 한계** — TDD의 red-green-refactor 사이클이 비결정론적 AI 시스템에서 어떻게 작동 불능 상태에 빠지는지를 다루는 실무/학술 자료
3. **EDD(평가 주도 개발)의 등장** — evals가 unit test를 대체하는 논리를 구체적으로 제시하는 자료
4. **패러다임 전환의 이론적 근거** — Karpathy의 Software 2.0, Google의 ML 기술 부채 논문 등 구조적 근거를 제시하는 자료

---

```json
[
  {
    "title": "Probabilistic and Deterministic Systems",
    "authors": ["Daniel Vaughan"],
    "year": 2024,
    "type": "blog_post",
    "url": "https://decisionmatrix.substack.com/p/probabilistic-and-deterministic-systems",
    "summary": "결정론적 시스템에서 단위 테스트가 작동하는 원리를 명확히 설명한 뒤, 확률론적 GenAI 시스템에는 왜 이 접근이 실패하는지를 체계적으로 논증한다. TDD의 전제 붕괴를 직접 다루며, 대안으로서 데이터셋·지표·반복 측정 기반의 평가 프레임워크(evals)를 제시한다. ch02의 'TDD 전제 붕괴 → EDD 등장' 서사 구조와 논리 흐름이 정확히 일치한다.",
    "key_claims": [
      "GenAI 시스템은 확률론적이므로 동일 입력에 대해 출력을 확실하게 예측할 수 없다",
      "전통적 단위 테스트(pass/fail)는 확률론적 시스템에 적용할 수 없으며, 데이터셋·지표·반복 측정 기반의 평가 프레임워크가 필요하다",
      "소프트웨어 개발자는 확률론적 시스템 구축에 필요한 핵심 역량이 부족하며, AI 엔지니어링이 별도의 전문 역할로 부상한다"
    ]
  },
  {
    "title": "AI and Deterministic Testing: Predictability Is the Gold Standard",
    "authors": ["Dick Dowdell"],
    "year": 2025,
    "type": "blog_post",
    "url": "https://medium.com/nerd-for-tech/ai-and-deterministic-testing-1be8d1a0348a",
    "summary": "결정론이 소프트웨어 공학 전반의 신뢰 기반(단위 테스트, 디버깅, 검증)임을 논증하고, 생성형 AI와 에이전틱 AI가 이 기반을 어떻게 근본적으로 파괴하는지를 설명한다. '출력을 재현할 수 없으면 버그 수정도 검증할 수 없다'는 테스트 불가능성의 핵심 딜레마를 날카롭게 제시하여, ch02의 TDD 붕괴 논거로 직접 인용 가능하다.",
    "key_claims": [
      "결정론은 단위 테스트를 의미 있게 만들고 소프트웨어를 '정확하다'고 부를 수 있게 하는 기반이다",
      "생성형·에이전틱 AI는 결정론적으로 검증 가능한 소프트웨어의 기준을 절대 충족할 수 없다",
      "출력을 재현할 수 없으면 수정 사항도 검증할 수 없다 — 이것이 비결정론적 AI 테스트의 중심 딜레마다"
    ]
  },
  {
    "title": "Adapting TDD for Reliable AI Systems",
    "authors": ["Galileo AI Team"],
    "year": 2025,
    "type": "blog_post",
    "url": "https://galileo.ai/blog/test-driven-development-ai-systems",
    "summary": "전통적 TDD(pass/fail)가 AI의 확률론적 특성으로 인해 한계에 봉착하는 지점을 구체적으로 분석하고, AI용 Red-Green-Refactor-Monitor 4단계 사이클을 제안한다. 단일 테스트 실행 대신 다중 실행과 통계적 임계값 검증이 필요하다는 논거는 TDD 전제 붕괴의 실증적 사례로 활용하기에 적합하다.",
    "key_claims": [
      "전통 TDD의 명확한 pass/fail 결과는 AI 시스템의 확률론적 특성 때문에 한계에 부딪힌다",
      "AI 테스트는 정확한 출력 대신 허용 가능한 통계적 범위 내에 결과가 드는지를 검증해야 한다",
      "AI 시스템은 코드 동작뿐 아니라 훈련 데이터에도 동등하게 의존하며, 이는 TDD의 코드 중심 전제를 뒤흔든다"
    ]
  },
  {
    "title": "How to Handle TDD with AI",
    "authors": ["testRigor Team"],
    "year": 2025,
    "type": "blog_post",
    "url": "https://testrigor.com/blog/how-to-handle-tdd-with-ai/",
    "summary": "AI를 개발 프로세스에 도입하는 순간 TDD의 red-green-refactor 사이클이 '앞뒤로 오가는 루프'로 변질되는 실무 현상을 설명한다. 'AI라는 비결정론적 변수를 추가하는 순간 TDD의 본질인 제어 가능성이 무너진다'는 논거는 ch02의 TDD 붕괴 사례로 직접 인용할 수 있다.",
    "key_claims": [
      "AI를 개발에 도입하는 순간 비결정론적 변수가 추가되어 TDD의 핵심인 코드 제어권이 사라진다",
      "TDD의 red-green-refactor-repeat 사이클 대신 '개발자의 의도 vs. AI의 판단' 사이를 오가는 루프가 발생한다",
      "개발자는 AI 생성 테스트와 코드가 서로 맞지 않는 상황에 직면하며, 이는 TDD의 일관성 전제를 무너뜨린다"
    ]
  },
  {
    "title": "Beyond Traditional Testing: Addressing the Challenges of Non-Deterministic Software",
    "authors": ["AWS Dev Community"],
    "year": 2024,
    "type": "blog_post",
    "url": "https://dev.to/aws/beyond-traditional-testing-addressing-the-challenges-of-non-deterministic-software-583a",
    "summary": "비결정론적 소프트웨어 테스트의 구체적 전략(속성 기반 테스트, 시맨틱 유사도 검사, LLM 보조 검증 등)을 기술적으로 제시한다. 정확한 출력을 예측할 수 없는 시스템에서도 의미 있는 단언(assertion)을 구성할 수 있다는 관점은 EDD의 기술적 기반을 설명하는 데 활용 가능하다.",
    "key_claims": [
      "속성 기반 테스트, 반복 가능한 환경, 시맨틱 유사도 검사는 비결정론적 소프트웨어 테스트의 핵심 전략이다",
      "정확한 출력을 예측할 수 없어도 시스템 동작에 대한 의미 있는 단언은 가능하다",
      "AI 및 머신러닝을 활용해 과거 테스트 데이터를 분석하고 버그 발견 가능성이 높은 테스트 케이스를 생성할 수 있다"
    ]
  },
  {
    "title": "AI Agents, meet Test Driven Development",
    "authors": ["Anita (Vellum AI)"],
    "year": 2025,
    "type": "blog_post",
    "url": "https://www.latent.space/p/anita-tdd",
    "summary": "LLM 기반 에이전트 개발에서 TDD를 적용하려 할 때 부딪히는 근본적 어려움을 실무 관점에서 정리한다. '역사적으로 TDD에서 테스트 대상은 예측 가능했지만, AI 에이전트는 그렇지 않다'는 핵심 관찰은 ch02의 TDD 전제 붕괴 논거를 뒷받침한다. 배포 후 피드백 루프 기반의 지속적 평가-개선 사이클은 EDD의 실무 모습을 예시하는 데 유용하다.",
    "key_claims": [
      "LLM은 비결정론적이고 예측 불가능하여, AI를 올바르게 작동시키려면 많은 시행착오가 필요하다",
      "AI 에이전트의 결과는 가변적이므로 테스트에 유연성이 필요하고, 점수·등급·사용자 만족도 같은 세밀한 성공 기준이 요구된다",
      "배포 후 TDD는 '피드백 수집 → 평가 → 개선 → 회귀 확인 → 배포'의 반복 루프 형태를 띤다"
    ]
  },
  {
    "title": "Eval-Driven Development: Build Better AI Faster",
    "authors": ["Vercel Engineering Team"],
    "year": 2024,
    "type": "blog_post",
    "url": "https://vercel.com/blog/eval-driven-development-build-better-ai-faster",
    "summary": "EDD(Eval-Driven Development)의 개념을 처음으로 명시적으로 제시한 실무 문서. '코드는 예측 가능한 출력을 내지만 LLM은 그렇지 않다'는 대비를 통해 evals의 필요성을 논증하고, Vercel의 AI 제품(v0)에 EDD를 적용한 실제 사례를 제공한다. TDD가 무력화되는 이유와 EDD가 그 자리를 채우는 방식을 모두 다루어 ch02의 핵심 논증 흐름에 정확히 부합한다.",
    "key_claims": [
      "코드는 예측 가능한 출력을 내지만, LLM은 확률론적으로 작동하여 블랙박스처럼 응답을 예측하기 어렵다",
      "evals는 비결정론적 출력의 지속적 평가와 정제를 강조하는 프레임워크로, 품질·신뢰성·관찰 가능성을 확보한다",
      "Vercel의 v0 제품은 EDD로 구축되었으며, 코드 기반 검사·인간 피드백·LLM 기반 채점을 조합하여 매일 프롬프트를 반복한다"
    ]
  },
  {
    "title": "Demystifying Evals for AI Agents",
    "authors": ["Anthropic Engineering Team"],
    "year": 2025,
    "type": "documentation",
    "url": "https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents",
    "summary": "Anthropic이 내부적으로 사용하는 eval 기반 개발 방법론을 공개한 공식 엔지니어링 문서. '기능 구현 전에 eval을 먼저 작성하라'는 권고는 EDD의 핵심 원칙을 권위 있는 출처로부터 직접 인용할 수 있게 해준다. 단위 테스트 유지와 동일한 수준으로 eval을 관리해야 한다는 주장은 TDD에서 EDD로의 방법론 전환을 공식화하는 근거로 쓸 수 있다.",
    "key_claims": [
      "eval 주도 개발(eval-driven development)을 실천하라 — 에이전트가 기능을 수행할 수 있기 전에 먼저 eval을 구축하고, 에이전트가 잘 수행할 때까지 반복하라",
      "AI 제품팀에게 eval을 소유하고 반복하는 것은 단위 테스트를 유지하는 것만큼 일상적인 일이어야 한다",
      "잘 설계된 eval이 조기에 발견했을 암묵적 기대치를 충족하지 못해
