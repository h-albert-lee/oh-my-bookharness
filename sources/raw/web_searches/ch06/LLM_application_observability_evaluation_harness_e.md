# Search: LLM application observability evaluation harness external system design patterns

수집된 자료들을 정리하여 JSON 형식으로 출력합니다.

---

```json
[
  {
    "title": "Building Effective Agents",
    "authors": ["Erik Schluntz", "Barry Zhang"],
    "year": 2024,
    "type": "blog_post",
    "url": "https://www.anthropic.com/research/building-effective-agents",
    "summary": "Anthropic가 수십 개 팀과의 실전 경험을 바탕으로 정리한 에이전트 설계 원칙. 에이전트를 '모델 호출 하나'가 아니라 workflow(예측 가능한 코드 경로)와 agent(LLM이 스스로 흐름을 결정)의 구조적 구분으로 설명하며, 가장 성공적인 구현체들이 단순하고 조합 가능한 패턴을 사용한다는 사실을 강조한다. ch06의 '에이전트는 시스템이다'라는 명제를 뒷받침하는 핵심 1차 출처로 활용 가능하다.",
    "key_claims": [
      "Workflows와 Agents는 구조적으로 다르다: Workflow는 predefined code path로 LLM을 조율하고, Agent는 LLM이 자신의 프로세스와 툴 사용을 동적으로 결정한다.",
      "가장 성공적인 에이전트 구현체들은 복잡한 프레임워크가 아닌, 단순하고 조합 가능한 패턴(prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer)을 사용한다.",
      "LLM 기반 아gentic 시스템의 기본 구성 블록은 retrieval, tools, memory로 증강된 LLM이며, 이를 '증강된 LLM(augmented LLM)'이라 부른다."
    ]
  },
  {
    "title": "LLM Readiness Harness: Evaluation, Observability, and CI Gates for LLM/RAG Applications",
    "authors": ["Alexandre Cristovão Maiorano"],
    "year": 2025,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2603.27355",
    "summary": "LLM/RAG 애플리케이션을 위한 평가 harness를 제안하며, 평가를 '배포 결정 워크플로'로 전환하는 시스템 설계를 다룬다. OpenTelemetry 기반 observability, CI 품질 게이트, 자동화 벤치마크를 하나의 API 계약 아래 묶는 방식이 ch06의 '에이전트 시스템을 운영 가능하게 만드는 외부 인프라 설계' 절에서 직접 인용할 수 있는 구체적 사례를 제공한다.",
    "key_claims": [
      "평가는 단일 품질 지표가 아니라 workflow 성공률, 정책 준수, groundedness, 검색 적중률, 비용, 지연시간을 포함한 다차원 readiness 점수로 표현되어야 한다.",
      "정책 위반 항목은 scalar 점수가 높더라도 CI 게이트에서 hard-block으로 처리해야 한다.",
      "run_id, dataset_id, 파이프라인 메타데이터, 지연시간, 토큰 사용량, 비용 추정치를 표준 필드로 강제하는 API 계약과 계측 스키마가 시스템 간 상관 관계 추적의 기반이 된다."
    ]
  },
  {
    "title": "Why Do Multi-Agent LLM Systems Fail? (MAST: Multi-Agent System Failure Taxonomy)",
    "authors": ["Mert Cemri", "Melissa Z. Pan", "Shuyi Yang", "et al."],
    "year": 2025,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2503.13657",
    "summary": "7개의 인기 있는 멀티에이전트 프레임워크에서 수집한 200개 이상의 태스크를 분석해 14가지 실패 모드를 3개 범주(사양 문제, 에이전트 간 정렬 실패, 태스크 검증 실패)로 분류한 첫 번째 체계적 실패 분류 체계(MAST)를 제시한다. ch06에서 '실패 경로'를 먼저 설계해야 한다는 논지를 실증 데이터로 뒷받침하는 데 활용할 수 있다.",
    "key_claims": [
      "멀티에이전트 시스템의 실패 모드는 (i) 사양 문제, (ii) 에이전트 간 정렬 실패, (iii) 태스크 검증 실패의 3범주 14가지로 분류된다.",
      "멀티에이전트 시스템의 인기 벤치마크 성능 향상은 단일 에이전트 대비 종종 미미하며, 이는 시스템 설계의 근본적 결함을 시사한다.",
      "프롬프트 엔지니어링과 위상학적 오케스트레이션 개선은 ChatDev에서 +14% 향상을 가져왔으나, 모든 실패 케이스를 해결하지 못했다."
    ]
  },
  {
    "title": "Where LLM Agents Fail and How They Can Learn From Failures",
    "authors": ["Kunlun Zhu", "et al."],
    "year": 2025,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2509.25370",
    "summary": "에이전트의 실패가 단일 모듈에 국한되지 않고 memory, reflection, planning, action, system-level operation 전반에 걸쳐 연쇄적으로 전파된다는 사실을 실증적으로 밝힌 논문. 에이전트를 시스템으로 이해해야 한다는 ch06의 논지를 '오류 전파(error propagation)' 개념으로 구체화하는 데 직접 활용 가능하다.",
    "key_claims": [
      "오류 전파(error propagation)가 LLM 에이전트 신뢰성의 핵심 병목이며, 초기의 작은 실수가 이후 결정 전반을 왜곡해 전체 태스크를 실패로 이끈다.",
      "AgentErrorTaxonomy는 memory, reflection, planning, action, system-level 5개 모듈에 걸친 실패 모드를 계층적으로 분류한다.",
      "단일 루트 원인 오류를 수정하는 것만으로도 실패하는 궤적을 성공으로 전환할 수 있어, 모듈 수준의 디버깅이 시스템 전체 성능 향상으로 이어진다."
    ]
  },
  {
    "title": "Harness Engineering for Coding Agent Users",
    "authors": ["Birgitta Böckeler"],
    "year": 2026,
    "type": "blog_post",
    "url": "https://martinfowler.com/articles/harness-engineering.html",
    "summary": "Martin Fowler 사이트에 게재된 이 글은 '에이전트 = 모델 + 하네스(Harness)'라는 프레임을 제시하며, 하네스를 guides(feed-forward)와 sensors(feedback)의 두 축으로 구분해 설명한다. ch06에서 에이전트 시스템의 컴포넌트를 '모델'과 '모델 바깥의 모든 것'으로 구분하는 개념적 어휘로 직접 도입할 수 있다.",
    "key_claims": [
      "'하네스(harness)'는 에이전트에서 모델 자체를 제외한 모든 것을 의미하며, Agent = Model + Harness 공식으로 표현된다.",
      "하네스의 제어 요소는 Computational(결정론적, 빠름: 테스트, 린터, 타입 체커)과 Inferential(비결정론적, 느림: LLM-as-judge, AI 코드 리뷰) 두 종류로 나뉜다.",
      "Sensors(피드백 제어)는 에이전트가 행동한 후 관찰하고 자기 수정을 돕는 반면, Guides(피드포워드 제어)는 행동 전에 규칙을 주입한다; 두 가지를 함께 사용하지 않으면 에이전트는 같은 실수를 반복하거나 규칙이 적용됐는지 알 수 없게 된다."
    ]
  },
  {
    "title": "AI Agent Observability - Evolving Standards and Best Practices",
    "authors": ["OpenTelemetry Community"],
    "year": 2025,
    "type": "documentation",
    "url": "https://opentelemetry.io/blog/2025/ai-agent-observability/",
    "summary": "OpenTelemetry의 AI 에이전트 observability 표준화 현황을 정리한 공식 블로그 포스트. GenAI Semantic Convention의 구조(traces, metrics, events)와 에이전트 프레임워크별 계측 전략의 장단점을 다루며, ch06에서 관찰 가능성을 외부 시스템 설계의 일부로 다루는 절에서 표준 참조 자료로 활용 가능하다.",
    "key_claims": [
      "AI 에이전트는 LLM 능력, 외부 세계와의 연결 도구, 고수준 추론을 결합해 목표를 달성하는 애플리케이션이며, 이를 관찰하려면 기존 APM 도구와 다른 접근이 필요하다.",
      "모든 AI 에이전트 프레임워크는 상호운용성과 일관성을 보장하기 위해 공통 AI agent framework semantic convention을 채택해야 한다.",
      "초기 AI 에이전트 semantic convention은 Google의 AI 에이전트 백서를 기반으로 하며, IBM Bee Stack, CrewAI, AutoGen, LangGraph 등 주요 프레임워크를 포함한 표준화 논의가 진행 중이다."
    ]
  },
  {
    "title": "Agent System Design Patterns (Databricks Documentation)",
    "authors": ["Databricks"],
    "year": 2025,
    "type": "documentation",
    "url": "https://docs.databricks.com/aws/en/generative-ai/guide/agent-system-design-patterns",
    "summary": "단순 LLM 호출부터 복잡한 멀티에이전트 시스템까지 GenAI 앱의 설계 패턴 스펙트럼을 결정론적 체인 → 단일 에이전트 → 멀티에이전트 순으로 단계적으로 설명한다. ch06에서 에이전트 복잡도를 단계별로 높이는 시스템 진화 경로를 독자에게 제시하는 데 활용할 수 있다.",
    "key_claims": [
      "GenAI 앱은 단순 LLM 호출부터 복잡한 멀티에이전트 시스템까지 다양한 설계 패턴으로 구현될 수 있으며, 단순한 것에서 시작해 필요할 때만 복잡성을 추가해야 한다.",
      "단일 에이전트 시스템은 LLM이 툴 사용 여부, 추가 LLM 호출 여부, 종료 여부를 스스로 결정하며 하나의 통합된 로직 흐름을 조율한다.",
      "멀티에이전트 시스템은 각자의 도메인·컨텍스트·툴셋을 가진 전문화된 에이전트들이 메시지를 교환하거나 협업하며, 별도의 조율자(supervisor)가 요청을 적절한 에이전트에게 위임한다."
    ]
  },
  {
    "title": "AI Agent Orchestration Patterns (Microsoft Azure Architecture Center)",
    "authors": ["Microsoft"],
    "year": 2026,
    "type": "documentation",
    "url": "https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns",
    "summary": "AI 에이전트 오케스트레이션 패턴(sequential, parallel fan-out/fan-in, maker-checker, magentic 등)을 분산 시스템 설계 패턴과 대응시켜 설명한다. ch06에서 에이전트를 '분산 시스템의 특수 사례'로 위치시킬 때 구체적인 패턴 명칭과 관찰 가능성·테스트 전략을 제공하는 레퍼런스로 활용 가능하다.",
    "key_claims": [
      "AI 에이전트 오케스트레이션 패턴은 기존 클라우드 설계 패턴을 확장하며, 특히 추론 능력과 비결정적 출력을 가진 컴포넌트 조율이라는 고유한 문제를 다룬다.",
      "에이전트 출력은 비결정적이므로, 통합 테스트에서 정확 일치 검증 대신 채점 루브릭 또는 LLM-as
