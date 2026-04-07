# Search: agentic AI system component boundaries interface contracts dependency management

아래는 조사된 자료를 바탕으로 찾은 핵심 참고 자료를 정리한 JSON입니다.



아래 자료들은 에이전트 시스템의 컴포넌트 격리, 인터페이스 계약, 의존성 관리, 실패 경로 등을 직접 다루는 최신(2025~2026) 문헌들로, ch06의 집필에 바로 활용 가능합니다.



---

```json
[
  {
    "title": "Chapter 3: Architectures for Building Agentic AI (Reliable and Responsible Generative AI, arxiv 2512.09458)",
    "authors": ["Janet (Jing) Lin", "Liangwei Zhang"],
    "year": 2025,
    "type": "academic_paper",
    "url": "https://arxiv.org/html/2512.09458v1",
    "summary": "에이전트 시스템을 컴포넌트 단위로 분해하고 각 컴포넌트 간 인터페이스를 '계약(contract)'으로 정의하는 방법을 체계적으로 설명한다. '모델이 제안하고, 아키텍처가 결정한다(models propose, architectures dispose)'라는 핵심 명제는 ch06의 주제 의식과 정확히 맞닿는다. 컴포넌트화(Componentisation)를 통한 폴트 격리, 스키마 기반 검증기, 권한 제한 도구 인터페이스 등 실천적 처방을 제공한다.",
    "key_claims": [
      "아키텍처—모델 선택이 아닌—가 신뢰할 수 있는 시스템을 만들 수 있는지를 결정한다 ('architecture, not just model choice, determines whether a powerful reasoning core becomes a dependable system')",
      "컴포넌트화는 책임을 모듈 단위로 분리하고, 스키마·검증기가 인터페이스 계약을 제공하며, 오케스트레이션이 제어 흐름을 관리한다",
      "의도(intention)를 사전조건·불변조건·사후조건을 가진 계약으로 처리하면 자유 형식의 LLM 출력이 거버넌스 대상이 된다",
      "신뢰성은 원칙적 컴포넌트화, 규율 잡힌 인터페이스, 명시적 제어 루프의 세 축으로 구성된다"
    ]
  },
  {
    "title": "AI Agent Systems: Architectures, Applications, and Evaluation (arxiv 2601.01743)",
    "authors": ["(복수 저자, JACM 2025)"],
    "year": 2026,
    "type": "academic_paper",
    "url": "https://arxiv.org/html/2601.01743v1",
    "summary": "에이전트 시스템을 '실행 루프 + 컴포넌트 집합'으로 통합 정의하는 'Agent Transformer' 추상화를 제안한다. 컴포넌트·인터페이스를 명시화하는 방법론을 제공하며, 비결정성·도구 실패·보안 위협이 어떻게 시스템 수준 실패로 연결되는지를 분석한다. ch06의 '에이전트를 시스템으로 분해하는 어휘와 프레임' 절에 직접 인용 가능하다.",
    "key_claims": [
      "현실적 과제는 여러 소스에서 정보를 수집하고, 시간에 걸쳐 상태를 유지하고, 도구를 선택하고, 제약(지연, 권한, 안전, 비용) 아래에서 다단계 행동을 실행하는 것을 포함한다",
      "에이전트 컴포넌트와 인터페이스를 명시화하는 'agent transformer' 추상화가 실제 배포를 위한 실용적 레시피를 제공한다",
      "장기 과제에서 오류 누적·비결정성·도구 변동성이 평가와 디버깅을 어렵게 만든다",
      "자율성 vs. 통제 가능성, 지연 vs. 신뢰성 등 시스템 수준 트레이드오프는 아직 도메인별로 충분히 이해되지 않았다"
    ]
  },
  {
    "title": "Why Do Multi-Agent LLM Systems Fail? (arxiv 2503.13657)",
    "authors": ["Mert Cemri", "외 12인"],
    "year": 2025,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2503.13657",
    "summary": "7개 멀티에이전트 프레임워크에서 1600개 이상의 실행 추적을 분석해 14가지 실패 모드를 분류한 MAST 분류체계를 구축했다. '시스템 설계 문제', '에이전트 간 정렬 불일치', '태스크 검증' 세 범주는 ch06의 실패 경로 분석 절에 직접 활용할 수 있는 어휘를 제공한다.",
    "key_claims": [
      "멀티에이전트 시스템의 실패는 (i) 시스템 설계 문제, (ii) 에이전트 간 정렬 불일치, (iii) 태스크 검증 부재 세 범주로 분류된다",
      "7개 프레임워크 전체에서 공통적인 실패 패턴이 반복적으로 나타난다",
      "인기 벤치마크에서의 성능 향상에도 불구하고 멀티에이전트 시스템의 실제 성능 이득은 종종 미미하다"
    ]
  },
  {
    "title": "Agentic AI Frameworks: Architectures, Protocols, and Design Challenges (arxiv 2508.10146)",
    "authors": ["(복수 저자, IEEE 2025)"],
    "year": 2025,
    "type": "academic_paper",
    "url": "https://arxiv.org/html/2508.10146v1",
    "summary": "CrewAI, LangGraph, AutoGen, Semantic Kernel, Google ADK, MetaGPT 등 주요 에이전트 프레임워크의 아키텍처 원칙, 통신 메커니즘, 메모리 관리, 안전 가드레일을 비교 분석한다. MCP, A2A, ANP 등 에이전트 간 통신 프로토콜의 계보와 한계도 다뤄 ch06의 인터페이스 계약 논의에 실증적 근거를 제공한다.",
    "key_claims": [
      "대부분의 프레임워크는 강력한 가드레일 집행을 위해 외부 로직이나 수동 설정을 필요로 하며, 표준화된 모듈식 안전 레이어가 부재하다",
      "LangChain, AutoGen 등 기존 프레임워크들은 에이전트 로직과 도구 호출의 강결합으로 인해 취약한 워크플로우를 만든다",
      "에이전트 통신 프로토콜(MCP, A2A 등)은 피어 발견, 컨텍스트 공유, 조율 행동을 가능하게 해 모듈식·탄력적 멀티에이전트 시스템의 기반이 된다"
    ]
  },
  {
    "title": "Towards a Science of AI Agent Reliability (arxiv 2602.16666)",
    "authors": ["(복수 저자)"],
    "year": 2026,
    "type": "academic_paper",
    "url": "https://arxiv.org/html/2602.16666v1",
    "summary": "내부 평가에서 합격한 에이전트가 실제 배포 환경에서 심각한 실패를 일으킨 실제 사례(Replit 데이터베이스 삭제, OpenAI Operator 무단 구매 등)를 분석하며 에이전트 신뢰성의 과학적 기반을 수립하고자 한다. ch06에서 '단순해 보이는 에이전트가 왜 실패하는가'를 독자에게 설득하는 강력한 도입부 사례로 활용 가능하다.",
    "key_claims": [
      "내부 평가에서 합리적으로 유능하다고 판단된 에이전트들이 실제 배포에서 신뢰할 수 없는 성능을 보이며 비용이 큰 실패를 초래했다",
      "에이전트 신뢰성을 체계적으로 측정·개선하기 위한 과학적 프레임워크가 필요하다"
    ]
  },
  {
    "title": "Agentic Architecture: Designing AI Agents for Enterprise Systems (Algolia Blog)",
    "authors": ["Algolia Engineering"],
    "year": 2026,
    "type": "blog_post",
    "url": "https://www.algolia.com/blog/ai/agentic-architecture",
    "summary": "에이전트 인터페이스를 API처럼 스키마·버전·계약 테스트로 관리해야 한다는 실천적 처방을 제공한다. 암묵적 계약(프롬프트 안에 숨겨진 인터페이스 기대)이 어떻게 시스템 취약성을 만드는지 명확히 설명하며, 상태 소유권·스키마 진화·중앙 감사 로그 등 ch06의 컴포넌트 교체·확장 판단 기준 절에 실무 어휘를 제공한다.",
    "key_claims": [
      "에이전트 A가 에이전트 B의 데이터에 의존한다면 그 의존성은 명시적·타입화·테스트되어야 한다 ('treat agent interfaces like APIs')",
      "프롬프트 안에 암묵적으로 인코딩된 계약은 프롬프트 최적화 시 감지하기 어려운 방식으로 깨진다",
      "거버넌스는 사후에 추가하면 에이전트 경계·데이터 접근 경로·로깅의 재설계가 필요해 비용이 크고 취약하다"
    ]
  },
  {
    "title": "The Three Layers of an Agentic AI Platform (Bain & Company)",
    "authors": ["Bain & Company"],
    "year": 2026,
    "type": "industry_report",
    "url": "https://www.bain.com/insights/the-three-layers-of-an-agentic-ai-platform/",
    "summary": "기존 엔터프라이즈 AI 플랫폼(단일 모델, 고정 API)이 왜 에이전틱 시스템의 요구를 충족하지 못하는지 설명하며, 데이터·오케스트레이션·거버넌스 세 계층의 표준화된 인터페이스 필요성을 제시한다. 스키마·데이터 계약 거버넌스, A2A·MCP 같은 표준 프로토콜의 역할을 다루어 ch06의 현실적 배경 제공에 유용하다.",
    "key_claims": [
      "단일 모델·고정 ETL 파이프라인용으로 설계된 기존 엔터프라이즈 플랫폼은 에이전트의 비결정론적·자율적 특성과 구조적 불일치를 일으킨다",
      "스키마 및 데이터 계약 거버넌스는 생산자와 소비자 간 호환성을 강제한다",
      "에이전트는 MCP, A2A 같은 표준 프로토콜을 통해 도구를 동적으로 발견하고 세션 상태와 영구 메모리를 공유한다"
    ]
  },
  {
    "title": "Choose your agentic AI architecture components (Google Cloud Architecture Center)",
    "authors": ["Google Cloud"],
    "year": 2025,
    "type": "documentation",
    "url": "https://docs.cloud.google.com/architecture/choose-agentic-ai-architecture-components",
    "summary": "에이전트 시스템을 구성하는 컴포넌트(프론트엔드, 에이전트 프레임워크, 도구, 메모리, 런타임, AI 모델, 모델 런타임)를 명확히 정의하고, MCP·AG-UI 같은 표준 인터페이스 프로토콜로 컴포넌트 간 통신을 확립하는 방법을 안내한다. ch06에서 '에이전트 = 컴포넌트들의 집합'이라는 관점 전환을 뒷받침하는 권위 있는 레퍼런스로 활용 가능하다.",
    "key_claims": [
      "에이전트 시스템 컴포넌트들이 상호작용하려면 명확한 통신 프로토콜이 필요하다",
      "MCP는 에이전트의 핵심 추론 로직을 도구의 구체적인 구현으로부터 분리한다 (표준 하드웨어 포트가 다양한 주변기기를 연결하는 것과 유사하게)",
