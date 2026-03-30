# Search: evaluation-driven development AI systems LLM evals best practices OpenAI Anthropic Google

아래는 발견된 자료들을 ch02 집필에 활용 가능한 형태로 정리한 결과입니다. 각 자료의 실존 여부를 검색 결과로 확인한 것만 포함했습니다.

---



핵심 근거: TDD는 주어진 입력에 대해 단일하고 결정론적인 정답이 존재한다는 전제 위에 서 있지만, LLM에서는 그것이 성립하지 않는다 — 이메일 초안을 작성하라는 요청에는 수천 가지 유효한 답이 존재한다.

 이 원리가 ch02의 핵심 논증 구조입니다. 

TDD/BDD와 같은 고전 소프트웨어 엔지니어링 방법론은 안정적 명세, 실행 가능한 오라클, 사전 배포 테스트 단계를 가정하지만, LLM 에이전트는 비결정론적이고 불완전하게 정의된 목표를 추구하며 배포 이후에도 계속 적응한다.



아래 JSON 결과를 확인하십시오.

```json
[
  {
    "title": "Evaluation-Driven Development and Operations of LLM Agents: A Process Model and Reference Architecture",
    "authors": ["(arxiv 2411.13768 저자진)"],
    "year": 2025,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2411.13768",
    "summary": "EDD(평가 주도 개발)를 EDDOps라는 이름으로 공식화한 논문으로, ch02의 핵심 주제인 TDD→EDD 전환을 학술적으로 뒷받침하는 가장 직접적인 자료다. TDD/BDD가 LLM 에이전트에 왜 무력화되는지를 원리 수준에서 설명하고, 개발-운영 전 주기에 걸친 평가 루프 구조를 제시한다. 'EDD'라는 용어와 개념의 학문적 출처로 인용할 수 있다.",
    "key_claims": [
      "TDD/BDD는 안정적 명세와 실행 가능한 오라클을 전제하지만, LLM 에이전트는 비결정론적이고 불완전하게 정의된 목표를 추구하며 배포 이후에도 계속 적응한다 — 따라서 TDD만으로는 LLM 에이전트에 필요한 연속적·생애주기 전반의 평가와 거버넌스를 제공할 수 없다",
      "EDDOps는 오프라인(개발 시점)과 온라인(런타임) 평가를 하나의 닫힌 피드백 루프로 통합하며, 평가 결과가 런타임 적응과 거버넌스 기반 재개발을 모두 이끌도록 설계한다",
      "기존 평가 방법론의 공백은 생애주기 커버리지, 메트릭 설계, 시스템 통합, 적응성, 평가 기반 개선, 인간-AI 평가자 균형 등 여섯 가지 차원에서 구조적으로 존재한다"
    ]
  },
  {
    "title": "Demystifying Evals for AI Agents",
    "authors": ["Anthropic Engineering"],
    "year": 2025,
    "type": "blog_post",
    "url": "https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents",
    "summary": "Anthropic이 공식적으로 'eval-driven development(평가 주도 개발)'를 권장한다고 명시한 문서로, ch02에서 EDD를 '업계 선두 기업도 채택한 방법론'으로 소개할 때 직접 인용할 수 있는 일차 자료다. 평가를 유닛 테스트만큼 일상적인 루틴으로 삼아야 한다는 주장은 TDD와의 대비를 선명하게 만든다.",
    "key_claims": [
      "'eval-driven development를 실천할 것을 권장한다 — 에이전트가 아직 수행하지 못하는 능력을 정의하는 eval을 먼저 만들고, 에이전트가 잘 수행할 때까지 반복하라'고 Anthropic이 명시적으로 권고한다",
      "AI 제품 팀이 평가를 소유하고 반복 개선하는 일은 유닛 테스트를 유지 관리하는 것만큼 일상적인 루틴이 되어야 한다",
      "eval 작업을 정의하는 것 자체가 제품 요구사항이 구체적으로 개발을 시작할 수 있을 만큼 명확한지를 스트레스 테스트하는 가장 좋은 방법이다"
    ]
  },
  {
    "title": "Evaluation Best Practices",
    "authors": ["OpenAI"],
    "year": 2024,
    "type": "documentation",
    "url": "https://platform.openai.com/docs/guides/evaluation-best-practices",
    "summary": "OpenAI가 공식 문서에서 'eval-driven development'를 명시하며 'evaluate early and often'을 원칙으로 제시한 자료다. Anthropic과 함께 ch02에서 EDD가 이미 업계 표준으로 수렴하고 있음을 논증하는 데 활용할 수 있다. 모델 변경마다 연속 평가를 실행하는 CI/CD 통합 방식도 TDD의 테스트 자동화 개념을 AI 맥락에서 재해석한 사례로 인용 가능하다.",
    "key_claims": [
      "'eval-driven development를 채택하라: 일찍, 자주 평가하라'고 OpenAI 공식 문서가 명시한다",
      "모든 변경마다 eval을 실행하는 연속 평가(CE)를 설정하고, 앱을 모니터링해 새로운 비결정론 사례를 식별하며, 시간이 지남에 따라 eval 세트를 성장시켜야 한다",
      "LLM-as-Judge 방식은 전문가 인간 주석자보다 저렴하고 확장 가능하며, GPT-4.1 같은 강력한 LLM 판사는 인간 간 동의율과 동일한 80% 이상의 동의율을 달성할 수 있다"
    ]
  },
  {
    "title": "Eval-Driven System Design: From Prototype to Production",
    "authors": ["OpenAI Cookbook Contributors"],
    "year": 2024,
    "type": "documentation",
    "url": "https://developers.openai.com/cookbook/examples/partners/eval_driven_system_design/receipt_inspection",
    "summary": "OpenAI Cookbook에서 EDD를 구체적인 시스템 설계 방법론으로 실연한 문서로, ch02에서 EDD의 실무 적용 방식을 설명할 때 구체적 예시로 활용할 수 있다. eval 점수가 모델 개선을 이끌고, 개선된 모델이 더 많은 데이터에서 eval을 확장하는 선순환 구조가 명시되어 있다.",
    "key_claims": [
      "eval-driven iteration: eval 점수로 모델 개선을 이끌고, 개선된 모델로 더 많은 데이터에서 eval을 확장해 추가 개선 영역을 발견하는 반복적 개선 구조를 제시한다",
      "프로덕션 데이터는 평가 및 훈련 데이터셋을 진화시키는 가장 신뢰할 수 있는 출처이며, 실제 사용 사례에서 정기적으로 샘플을 수집·큐레이션해 격차와 엣지 케이스를 식별해야 한다",
      "eval은 개발 단계에만 쓰는 것이 아니다 — 프로덕션 서비스를 인스트루먼트하면 잘못된 가정을 식별하고 커버리지가 부족한 영역을 발견하는 추가적인 테스트·훈련 샘플이 시간이 지남에 따라 확보된다"
    ]
  },
  {
    "title": "Building Effective Agents",
    "authors": ["Erik Schluntz", "Barry Zhang (Anthropic)"],
    "year": 2024,
    "type": "blog_post",
    "url": "https://www.anthropic.com/research/building-effective-agents",
    "summary": "Anthropic이 수십 팀과의 실전 경험을 바탕으로 정리한 에이전트 시스템 구축 원칙으로, ch02의 '복잡성을 측정 가능한 개선이 있을 때만 추가하라'는 EDD 핵심 원칙과 직결된다. '성공의 핵심은 성능을 측정하고 반복하는 것'이라는 명제를 Anthropic 실무 경험에서 도출한 것으로, 결정론적 방법론(TDD)과의 대비를 생생하게 보여준다.",
    "key_claims": [
      "LLM 기반 기능의 성공 핵심은 성능을 측정하고 구현을 반복하는 것이다 — 복잡성은 결과를 입증 가능하게 개선할 때만 추가해야 한다",
      "단순한 프롬프트로 시작하고, 종합적인 평가로 최적화한 다음, 더 단순한 해결책이 한계에 부딪혔을 때만 멀티 스텝 에이전트 시스템을 추가하라",
      "소프트웨어 개발 공간은 코드 솔루션이 자동화된 테스트로 검증 가능하고, 에이전트가 테스트 결과를 피드백으로 사용해 반복할 수 있으며, 출력 품질을 객관적으로 측정할 수 있기 때문에 에이전트가 특히 효과적이다"
    ]
  },
  {
    "title": "A Pragmatic Guide to LLM Evals for Developers",
    "authors": ["Hamel Husain", "Shreya Shankar (The Pragmatic Engineer)"],
    "year": 2025,
    "type": "blog_post",
    "url": "https://newsletter.pragmaticengineer.com/p/evals",
    "summary": "TDD가 AI 시스템에 왜 작동하지 않는지를 '단일 결정론적 정답의 부재'라는 원리 수준에서 간결하게 설명하며, ch02의 TDD 무력화 논증을 뒷받침하는 실용적 자료다. LLM 출력은 '무한한 입력 표면'뿐만 아니라 '방대하고 주관적이며 예측 불가능한 출력 공간' 때문에 근본적으로 다르다는 주장은 결정론 vs 확률론 대비 논증에 직접 활용할 수 있다.",
    "key_claims": [
      "TDD의 순진한 적용이 실패하는 이유는, TDD는 주어진 입력에 대해 단 하나의 결정론적이고 알 수 있는 올바른 출력이 존재한다는 전제에서 작동하기 때문이다 — LLM에서는 이것이 사실이 아니다",
      "LLM 평가의 도전은 단지 '무한한 입력 표면'만이 아니라, 유효하고 주관적이며 예측 불가능한 출력의 방대한 공간에 있다",
      "'좋은 것'이 제품에 무엇을 의미하는지 정의하기 전에는 올바름을 테스트할 수 없다 — 먼저 가능한 출력의 범위를 체계적으로 관찰해야 한다"
    ]
  },
  {
    "title": "Task-Specific LLM Evals that Do & Don't Work",
    "authors": ["Eugene Yan"],
    "year": 2024,
    "type": "blog_post",
    "url": "https://eugeneyan.com/writing/evals/",
    "summary": "분류, 요약, 번역 등 태스크별로 어떤 eval 방법이 실제로 작동하고 작동하지 않는지를 실증적으로 정리한 자료로, ch02에서 EDD의 구체적 방법론을 소개할 때 근거로 활용할 수 있다. 특히 eval이 없으면 모델 업그레이드 시 성능 회귀를 탐지할 수 없다는 실제 사례(Voiceflow의 10% 성능 하락 탐지 사례)는 EDD의 필요성을 구체적으로 보여준다.",
    "key_claims": [
      "eval 하네스가 없으면 모델 버전 업그레이드 시 성능 회귀를 탐지하지 못한다 —
