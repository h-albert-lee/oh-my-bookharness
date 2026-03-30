# Search: large language model system architecture separation of concerns input processing output processing error handling best practices

충분한 자료를 확보했습니다. 이제 ch04에 참고할 수 있는 실질적인 자료들을 JSON 형식으로 정리하겠습니다.

---

아래는 검색 결과를 바탕으로 **실제로 존재하는 자료**만 선별하여 정리한 결과입니다.



모듈형 LLM 파이프라인은 엔드-투-엔드 태스크를 컴포저블 스테이지로 분해하며, 모듈화의 동기는 기능 분리, 제어 가능한 평가, 타깃 확장·패치, 파이프라인 수준의 관찰 가능성에 있다는 연구들이 다수 있습니다.

 

특히 모듈형 LLM 파이프라인은 관심사의 분리(SoC) 원칙을 따라야 하며, 이를 통해 한 모듈의 변경이 다른 모듈에 영향을 주지 않아 유지보수성과 확장성이 높아집니다.



```json
[
  {
    "title": "Emerging Architectures for LLM Applications",
    "authors": ["Matt Bornstein", "Rajko Radovanovic"],
    "year": 2023,
    "type": "industry_report",
    "url": "https://a16z.com/emerging-architectures-for-llm-applications/",
    "summary": "Andreessen Horowitz가 AI 스타트업 및 기술 기업의 실무 사례를 기반으로 작성한 LLM 앱 스택 레퍼런스 아키텍처. 데이터 전처리/임베딩, 프롬프트 구성/검색, LLM 호출, 출력 처리라는 파이프라인의 각 단계를 구성 요소 단위로 명확하게 구분하여 설명한다. ch04의 '파이프라인 구성 요소를 역할 중심으로 정의'하는 논의에서 권위 있는 산업계 레퍼런스로 활용 가능하다.",
    "key_claims": [
      "LLM 앱 워크플로는 데이터 전처리/임베딩, 프롬프트 구성/검색, LLM 호출의 세 단계로 구조화할 수 있다",
      "컴파일된 프롬프트는 하드코딩된 템플릿, few-shot 예시, 외부 API 정보, 벡터 DB에서 검색된 문서 등 여러 구성 요소를 조합한 복합 객체다",
      "출력 검증(Guardrails), 프롬프트 인젝션 탐지 등 운영 도구는 별도 레이어로 분리되어야 한다"
    ]
  },
  {
    "title": "Architecting Resilient LLM Agents: A Guide to Secure Plan-then-Execute Implementations",
    "authors": ["Ron F. Del Rosario", "Klaudia Krawiecka", "Christian Schroeder de Witt"],
    "year": 2025,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2509.08646",
    "summary": "Plan-then-Execute(P-t-E) 패턴을 중심으로 LLM 에이전트 시스템에서 전략적 계획과 전술적 실행을 분리하는 것의 아키텍처적 이점을 체계적으로 분석한 논문. ch04의 '각 구성 요소가 왜 독립된 설계 단위가 되어야 하는지'를 관심사 분리 원칙으로 설명하는 핵심 이론 자료다. LangGraph, CrewAI, AutoGen 등 실제 프레임워크의 구현 사례도 포함한다.",
    "key_claims": [
      "P-t-E 패턴에서 관심사의 의도적 분리는 예측 가능성, 비용 효율성, 추론 품질 면에서 중요한 아키텍처적 이점을 제공한다",
      "플래너(Planner)와 실행기(Executor)를 별도 컴포넌트로 분리하면 외부 비신뢰 데이터로부터의 프롬프트 인젝션 공격에 대한 구조적 방어가 가능하다",
      "실행기는 현재 실행 중인 단계에 필요한 특정 도구만 동적으로 프로비저닝받아야 하며, 이는 최소 권한 원칙의 구현이다"
    ]
  },
  {
    "title": "Modular LLM Pipelines Overview",
    "authors": ["Emergent Mind Editorial"],
    "year": 2025,
    "type": "industry_report",
    "url": "https://www.emergentmind.com/topics/modular-llm-pipelines",
    "summary": "모듈형 LLM 파이프라인의 아키텍처 핵심 개념을 체계적으로 정리한 개요 문서. 각 모듈이 명시적 스키마 수준의 계약(typed JSON, YAML 등)을 통해 입출력 아티팩트를 정의해야 한다는 점을 강조하며, ch04에서 구성 요소 간 인터페이스 설계를 논의할 때 직접 인용 가능하다.",
    "key_claims": [
      "모듈형 LLM 파이프라인은 각 단계를 모듈로 캡슐화하며, 모듈은 입출력 아티팩트를 명시적 스키마 수준 계약으로 지정한다",
      "모듈화의 핵심 동기는 기능 분리, 제어 가능한 평가·제거, 타깃 확장·패치, 파이프라인 수준의 관찰 가능성이다",
      "모듈 간 상호작용은 순차, 병렬, 또는 DAG 방식의 연결로 실현되며 오케스트레이터가 실행 순서, 오류 처리, 안정성을 강제한다"
    ]
  },
  {
    "title": "How to Develop Modular LLM Pipelines?",
    "authors": ["Hakeem Abbas"],
    "year": 2024,
    "type": "blog_post",
    "url": "https://medium.com/@hakeemsyd/how-to-develop-modular-llm-pipelines-31faa8fae136",
    "summary": "LLM 파이프라인에 관심사의 분리(SoC) 원칙을 적용하는 방법을 실용적 관점에서 설명하는 글. 전처리 모듈, 추론 모듈, 후처리 모듈이 각각 독립적 추상화 레이어를 가져야 함을 코드 예시와 함께 보여준다. ch04에서 '각 구성 요소가 왜 독립적이어야 하는가'를 SoC 원칙으로 설명하는 실용적 근거로 활용 가능하다.",
    "key_claims": [
      "모듈형 LLM 파이프라인은 관심사의 분리(SoC) 원칙을 따라야 하며, 각 컴포넌트는 특정 단일 태스크만 담당해야 한다",
      "전처리 모듈은 특정 모델과 독립적으로 텍스트 변환만 처리하고, 추론 모듈은 다른 파이프라인 부분 변경 없이 LLM을 교체할 수 있어야 한다",
      "데이터 전처리는 LLM이 입력 품질에 민감하기 때문에 별도 모듈로 분리되어야 하며 plug-and-play 아키텍처를 가져야 한다"
    ]
  },
  {
    "title": "The Architecture of LLM-Powered Applications: How It Differs from Conventional Software Architecture",
    "authors": ["Craig Risi"],
    "year": 2025,
    "type": "blog_post",
    "url": "https://www.craigrisi.com/post/the-architecture-of-llm-powered-applications-how-it-differs-from-conventional-software-architecture",
    "summary": "기존 소프트웨어 아키텍처와 LLM 기반 아키텍처의 차이를 구조적으로 분석한 글. LLM 시스템에서 '로직이 코드가 아닌 모델 내부에 존재한다'는 근본적 차이를 출발점으로, 검증 레이어·필터링 레이어·후처리 레이어·폴백 메커니즘 등 LLM 주변에 구축해야 하는 보호 레이어들을 설명한다. ch04의 도입부에서 '왜 LLM 시스템은 기존 소프트웨어와 다른 설계 단위를 필요로 하는가'를 논증할 때 활용 가능하다.",
    "key_claims": [
      "기존 소프트웨어는 결정론적 로직과 모듈식 서비스 경계로 구축되지만, LLM 아키텍처는 AI 시스템의 확률론적·진화적 특성을 반영하는 새로운 레이어와 패턴을 도입한다",
      "LLM을 프로덕션에서 안전하게 사용하려면 출력 형식·정확성 검사, 유해 응답 필터링, 구조화 출력을 위한 후처리, 불확실 시의 폴백 메커니즘 등 여러 보호 레이어가 필요하다",
      "LLM 시스템에서 신뢰성은 코드 단독이 아니라 여러 확률적 컴포넌트들의 오케스트레이션에서 나온다"
    ]
  },
  {
    "title": "Enterprise LLM Architecture Patterns: RAG to Agentic Systems",
    "authors": ["DZone Editorial"],
    "year": 2026,
    "type": "blog_post",
    "url": "https://dzone.com/articles/llm-architecture-patterns-rag-to-agentic",
    "summary": "RAG부터 에이전틱 시스템까지 11개의 핵심 LLM 아키텍처 패턴을 정리한 실무 가이드. 각 패턴이 할루시네이션 제어, 피드백 루프, 워크플로 오케스트레이션 등 실제 배포 제약과 어떻게 연결되는지 설명한다. ch04에서 '구성 요소들의 조합'이 실무에서 어떤 패턴으로 발현되는지 참고할 때 유용하다.",
    "key_claims": [
      "성공적인 LLM 도입은 가장 강력한 모델 선택이 아니라 올바른 아키텍처 선택에 달려 있다",
      "고품질 LLM 애플리케이션은 견고성·관찰 가능성·거버넌스 준비를 위해 여러 패턴을 조합한다",
      "모듈형·관찰 가능·안전 인식 설계에 투자한 팀이 새 모델 적응, 운영 위험 감소, 장기적 AI 가치 실현에 가장 유리하다"
    ]
  },
  {
    "title": "Retries, Fallbacks, and Circuit Breakers in LLM Apps: A Production Guide",
    "authors": ["Maxim AI Editorial"],
    "year": 2026,
    "type": "blog_post",
    "url": "https://www.getmaxim.ai/articles/retries-fallbacks-and-circuit-breakers-in-llm-apps-a-production-guide/",
    "summary": "LLM 프로덕션 시스템에서 발생하는 장애 패턴과 이를 처리하기 위한 재시도, 폴백, 서킷 브레이커 메커니즘을 체계적으로 정리한 가이드. ch04에서 에러 처리가 왜 독립된 설계 단위가 되어야 하는지, 그리고 각 에러 처리 계층의 역할과 책임이 어떻게 분리되어야 하는지를 설명하는 실무적 근거로 활용 가능하다.",
    "key_claims": [
      "재시도(Retry), 폴백(Fallback), 서킷 브레이커(Circuit Breaker)는 신뢰할 수 있는 LLM 시스템의 기반을 이루는 세 가지 독립적 장애 처리 패턴이다",
      "프로바이더 API는 장애, 속도 제한, 가변 레이턴시를 경험하며 단일 의존성 실패가 전체 시스템에 연쇄 전파될 수 있다",
      "에러 처리 복잡성은 애플리케이션 로직이 아닌 별도 레이어(게이트웨이 수준)에서 관리해야 코드를 깔끔하게 유지할 수 있다"
    ]
  },
  {
    "title": "The Architecture of Today's LLM Applications",
    "authors": ["Alireza Goudarzi", "Albert Ziegler"],
