# Search: LLM application pipeline components design patterns prompt builder output parser state management production

수집된 자료를 충분히 검토했습니다. 이제 각 자료의 신뢰성과 ch04의 집필 목적에 대한 적합성을 평가하여 JSON으로 정리합니다.

```json
[
  {
    "title": "From Prompts to Templates: A Systematic Prompt Template Analysis for Real-world LLMapps",
    "authors": ["Yuetian Mao", "Junjie He", "Chunyang Chen"],
    "year": 2025,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2504.02052",
    "summary": "실제 오픈소스 LLMapp(Uber, Microsoft 등)에서 수집한 프롬프트 템플릿을 체계적으로 분석하여 7가지 공통 구성 요소와 자주 등장하는 co-occurrence 패턴을 분류한 논문이다. ch04에서 '프롬프트 빌더'라는 구성 요소가 왜 독립된 설계 단위가 되어야 하는지를 실증적 데이터로 뒷받침할 수 있다. LLMapp 개발자들이 현실에서 실제로 어떤 구성 요소(Role, Directive, Context, Output Format 등)를 조합하여 템플릿을 설계하는지를 보여주는 empirical 근거로 활용 가능하다.",
    "key_claims": [
      "실세계 LLMapp 프롬프트 템플릿은 Profile/Role, Directive, Context & Workflows, Output Format/Style & Constraints, Examples 등 7가지 공통 구성 요소로 분류된다",
      "LLMapp 개발자들은 응답의 내용뿐 아니라 형식(format)에도 주목하며, 구조화된 출력 포맷은 post-processing 오류를 크게 줄여준다",
      "현재의 프롬프트 설계 관행은 개인 전문성과 반복적 시행착오에 지나치게 의존하며, 체계적인 최적화 방법론이 필요하다"
    ]
  },
  {
    "title": "Prompt-Layered Architecture: A New Stack for AI-First Product Design",
    "authors": ["Savi Khatri"],
    "year": 2024,
    "type": "academic_paper",
    "url": "https://ijsrm.net/index.php/ijsrm/article/view/5670",
    "summary": "LLM 기반 제품에서 프롬프트를 일급 소프트웨어 아키텍처 구성 요소로 격상시키는 4계층 PLA(Prompt-Layered Architecture) 모델을 제안한다. ch04의 핵심 논지인 '각 구성 요소가 왜 독립된 설계 단위가 되어야 하는가'를 뒷받침하는 아키텍처 이론으로서, Prompt Composition Layer, Orchestration Layer, Response Interpretation Layer, Domain Memory Layer라는 분리된 역할 구조가 ch04의 구성 요소 분류 체계와 직접 대응된다.",
    "key_claims": [
      "현재 대부분의 AI 애플리케이션은 프롬프트 템플릿, 컨텍스트 소스, 응답 해석, 장기 메모리 간의 경계가 불분명한 단일 계층 파이프라인에 의존하며, 이는 낮은 재사용성과 관찰 가능성을 초래한다",
      "PLA는 Prompt Composition, Orchestration, Response Interpretation, Domain Memory 4계층으로 관심사를 분리하여 테스트 가능성, 재사용성, 유지보수성을 확보한다",
      "프롬프트를 ad hoc 입력이 아닌 버전 관리되는 소프트웨어 정의 모듈로 취급함으로써 AI-first 제품의 확장 가능한 설계가 가능해진다"
    ]
  },
  {
    "title": "LLM Applications: Current Paradigms and the Next Frontier",
    "authors": ["(다수 저자, arXiv 2503.04596)"],
    "year": 2025,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2503.04596",
    "summary": "LLM 기반 애플리케이션의 현재 패러다임(LLM app store, agent framework, 파이프라인 설계 등)을 포괄적으로 정리한 서베이 논문이다. ch04에서 LLM 파이프라인 개념을 설명할 때 '현재 생태계가 어떻게 구성되어 있는가'에 대한 넓은 맥락을 제공하며, LangChain·LlamaIndex·LangGraph 등 주요 프레임워크가 모듈식 추상화를 통해 파이프라인 구성 요소를 어떻게 구현하는지를 비교 설명하는 데 활용할 수 있다.",
    "key_claims": [
      "LangChain은 chains, memory, tools에 대한 모듈식 추상화를 제공하고, LangGraph는 결정론적 멀티에이전트 워크플로를 위한 그래프 기반 오케스트레이션을 도입했다",
      "plan-and-execute 패러다임은 계획(planning)과 실행(execution)을 분리함으로써 파이프라인 구성 요소 간 역할 분담의 중요성을 보여준다",
      "LLM 애플리케이션 생태계는 워크플로 기반의 모듈 조합 접근법을 채택하고 있으며, 이는 LLM이 텍스트 처리를 넘어 외부 툴과 API를 호출할 수 있게 한다"
    ]
  },
  {
    "title": "AgentForge: A Lightweight Modular Framework for Constructing Autonomous Agents Driven by Large Language Models",
    "authors": ["(다수 저자, arXiv 2601.13383)"],
    "year": 2026,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2601.13383",
    "summary": "LLM 기반 에이전트를 구성하는 데 있어 모듈화된 스킬 추상화, 통합 LLM 백엔드 인터페이스, 선언형 구성 시스템의 세 가지 핵심 설계 원칙을 제안하는 논문이다. ch04에서 '구성 요소가 왜 독립된 설계 단위가 되어야 하는가'를 설명할 때, 직접 API 통합(모놀리식, 유지보수 불가)과 과도한 프레임워크 의존(복잡성 과부하) 사이의 설계 트레이드오프를 논증하는 근거로 사용할 수 있다.",
    "key_claims": [
      "직접 API 통합 방식은 LLM 호출, 툴 실행, 상태 관리를 수동으로 오케스트레이션하여 모놀리식하고 오류가 많은 코드베이스를 낳는다",
      "모듈식 스킬 아키텍처에서 각 스킬은 잘 정의된 입출력 계약을 가진 이산적이고 재사용 가능한 단위로 캡슐화된다",
      "에이전트 로직을 구현 세부사항으로부터 분리하는 선언형 구성 시스템은 독립적 스킬 테스트, 버전 관리, 공유를 가능하게 한다"
    ]
  },
  {
    "title": "The Architect's Guide to LLM System Design: From Prompt to Production",
    "authors": ["Vi Q. Ha"],
    "year": 2025,
    "type": "blog_post",
    "url": "https://medium.com/@vi.ha.engr/the-architects-guide-to-llm-system-design-from-prompt-to-production-8be21ebac8bc",
    "summary": "LLM 시스템 설계의 표준 아키텍처 청사진을 '프롬프트에서 프로덕션까지' 관점에서 해체하여 각 구성 요소의 역할을 설명한 실무 가이드다. ch04에서 파이프라인 전체 흐름(사용자 쿼리 → 오케스트레이션 엔진 → 검색 파이프라인 → LLM 추론 → 후처리 → 응답)을 도식화하고, 각 단계가 왜 분리된 설계 단위가 되어야 하는지를 설명하는 데 직접적으로 활용할 수 있다.",
    "key_claims": [
      "LLM 시스템 설계의 핵심은 모델 자체가 아니라 데이터, 컨텍스트, 로직의 흐름을 제어하는 파이프라인이다",
      "LLM의 상품화는 경쟁 우위가 모델 접근성에서 RAG 파이프라인을 통해 활용하는 독점 데이터의 품질로 이동했음을 의미한다",
      "프롬프트를 코드에서 분리하여 버전 관리 자산으로 취급하는 프롬프트 관리 시스템이 필요하며, 이는 팀 간 협업과 안전한 반복을 가능하게 한다"
    ]
  },
  {
    "title": "How to Design LLM Applications for Production: A System Design Guide",
    "authors": ["Matt Frank"],
    "year": 2026,
    "type": "blog_post",
    "url": "https://dev.to/matt_frank_usa/how-to-design-llm-applications-for-production-a-system-design-guide-2i3h",
    "summary": "프로덕션 LLM 애플리케이션 설계를 위한 핵심 패턴(RAG 파이프라인, 벡터 DB, 챗봇 설계, 에이전트 아키텍처, 프로덕션 스케일링)을 다루는 실무 가이드다. ch04에서 LLM 시스템의 고유한 제약(비결정론적 출력, 높은 지연, 컨텍스트 윈도우 관리)이 왜 별도의 아키텍처 패턴을 요구하는지를 설명할 때 'LLM 시스템 vs. 전통적 ML 시스템'의 대비 구도로 사용할 수 있다.",
    "key_claims": [
      "프로덕션 LLM 애플리케이션 배포는 단순한 API 호출 래핑을 훨씬 넘어서며, 오케스트레이션 계층, 검색 파이프라인, 가드레일, 관찰 가능성, 비용 관리가 필요하다",
      "전통적 ML 시스템의 밀리초 단위 구조적 예측과 달리 LLM 애플리케이션은 비결정론적 출력, 높은 지연(5~60초+), 컨텍스트 윈도우 관리라는 고유한 아키텍처 도전을 안고 있다",
      "복잡한 워크플로에는 에이전트 루프, 조건부 라우팅, human-in-the-loop 패턴을 위한 상태 머신(state machine)이 필요하다"
    ]
  },
  {
    "title": "Structuring LLM Application Code",
    "authors": ["ApX Machine Learning"],
    "year": 2024,
    "type": "blog_post",
    "url": "https://apxml.com/courses/prompt-engineering-llm-application-development/chapter-8-application-development-considerations/structuring-llm-application-code",
    "summary": "LLM 애플리케이션 코드 구조화의 핵심 원칙인 관심사의 분리(Separation of Concerns)를 LLM Client Abstraction, Prompt Management, Data Handling, Configuration, Presentation/API Layer로 구체화한 실용 가이드다. ch04에서 '각 구성 요소가 왜 독립된 코드 단위가 되어야 하는가'를 소프트웨어 설계 원칙과 연결하여 설명할 때 사용할 수 있으며, 각 구성 요소의 책임 경계를 구체적인 코드 구조로 보여준다.",
    "key_claims": [
      "LLM 애플리케이션이 단순 스크립트에서 복잡한 시스템으로 진화할수록 관심사의 분리 원칙을 적용하는 것이 복잡성 관리의 핵심이 된다",
      "LLM Client Abstraction은 API 엔드포인트 선택, 재시도 로직, 파라미터 표준화, 요청/응답 로깅을 하나의 전용 모듈로 캡슐화해야 한다",
      "Prompt Management는 템플릿 파일 로딩과 플레이스홀더 치환을 담당하는 독립 컴포넌트로 분리되어야 하며, 이는 입력 처리·LLM 호출·출력 처리와 구별된다"
    ]
  },
  {
    "title": "Using Output Parsers for LLM Responses",
    "authors": ["ApX Machine Learning"],
    "year": 2
