# Search: AI agent failure modes error propagation system reliability observability tracing

수집한 자료들을 충분히 확인했습니다. 이제 최종 JSON으로 정리합니다.

---

조사 결과를 아래와 같이 정리합니다. 각 자료는 실제로 존재하는 출처이며, ch06의 집필 방향—"AI 에이전트는 단순 프로그램이 아니라 시스템이다"—에 직접적으로 활용 가능한 것들로 선별했습니다.



MAST 논문은 7개 MAS 프레임워크를 분석해 14가지 고유 실패 모드를 세 범주(시스템 설계 이슈, 에이전트 간 불일치, 태스크 검증)로 분류한 최초의 경험적 분류 체계입니다.

 

별도의 아카이브 논문(2603.06847)은 40개 오픈소스 에이전트 저장소에서 13,602개 이슈를 수집해 실세계 결함 유형·증상·근본 원인의 분류 체계를 도출했습니다.

 

Anthropic의 "Building Effective Agents"는 증강된 LLM을 에이전트 시스템의 기본 빌딩 블록으로 정의하고, 복잡성은 필요할 때만 추가하되 워크플로우와 에이전트의 차이를 구분할 것을 권고합니다.



```json
[
  {
    "title": "Why Do Multi-Agent LLM Systems Fail?",
    "authors": ["Mert Cemri", "Melissa Z. Pan", "Shuyi Yang", "Lakshya A. Agrawal", "Bhavya Chopra", "Rishabh Tiwari", "Kurt Keutzer", "Aditya Parameswaran", "Dan Klein", "Kannan Ramchandran", "Matei Zaharia", "Joseph E. Gonzalez", "Ion Stoica"],
    "year": 2025,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2503.13657",
    "summary": "7개 MAS 프레임워크, 1,600+ 주석 실행 트레이스를 분석해 14가지 고유 실패 모드를 도출한 MAST(Multi-Agent System Failure Taxonomy)를 제시한다. ch06에서 '에이전트는 단순 모델 호출이 아닌 시스템'임을 논증하는 핵심 경험적 근거로 활용 가능하며, 시스템 설계·에이전트 간 불일치·태스크 검증이라는 3개 범주는 컴포넌트 의존 관계를 설명하는 프레임으로 직접 인용할 수 있다. Berkeley 스카이 컴퓨팅 랩에서 공개한 데이터셋·어노테이터도 함께 릴리즈되어 실습 예시로 연결하기 좋다.",
    "key_claims": [
      "멀티에이전트 시스템의 실패는 개별 에이전트 수준이 아닌 시스템 수준(스펙 이슈, 에이전트 간 불일치, 검증 부재)에서 발생한다",
      "14가지 실패 모드 중 어떤 것도 단일 에이전트 벤치마크로는 탐지되지 않는다",
      "검증 실패(FM-3.2 + FM-3.3)가 전체 관찰 실패의 13.48%를 차지하는 가장 빈번한 범주다"
    ]
  },
  {
    "title": "Characterizing Faults in Agentic AI: A Taxonomy of Types, Symptoms, and Root Causes",
    "authors": ["Mehil B. Shah", "et al."],
    "year": 2026,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2603.06847",
    "summary": "40개 오픈소스 에이전트 저장소의 13,602개 이슈·PR을 분석해 결함 유형·증상·근본 원인의 분류 체계를 경험적으로 도출한 대규모 실증 연구다. ch06의 '에이전트 내부 컴포넌트(플래닝, 메모리, 도구) 간 결함 전파 경로' 절에서 핵심 레퍼런스로 활용할 수 있으며, 약한 에러 핸들링과 불충분한 로깅이 단순 구현 실수를 진단하기 어려운 장애로 증폭시킨다는 주장은 옵저버빌리티 필요성을 뒷받침한다.",
    "key_claims": [
      "에이전트 시스템의 결함은 전통 소프트웨어나 독립 LLM 애플리케이션과는 구조적으로 다른 신뢰성 도전을 낳는다",
      "많은 결함이 확률적으로 생성된 아티팩트와 결정론적 인터페이스 제약 간의 불일치에서 비롯되며, 의존성 통합·데이터 검증·런타임 환경 처리에서 자주 발생한다",
      "약한 에러 핸들링과 제한적 로깅이 단순 구현 실수를 진단하기 어려운 장애로 전환시킨다"
    ]
  },
  {
    "title": "Building Effective Agents",
    "authors": ["Erik Schluntz", "Barry Zhang"],
    "year": 2024,
    "type": "blog_post",
    "url": "https://www.anthropic.com/research/building-effective-agents",
    "summary": "Anthropic의 실제 에이전트 구축 경험을 바탕으로 '증강된 LLM → 워크플로우 → 에이전트'의 복잡도 스펙트럼과 핵심 패턴(프롬프트 체이닝, 라우팅, 병렬화, 오케스트레이터-워커, 평가자-최적화자)을 정리한 가이드다. ch06에서 '에이전트의 기본 빌딩 블록(환경, 도구, 시스템 프롬프트)'과 '단순성을 유지하면서 컴포넌트를 어떻게 확장하는가'를 설명하는 규범적 출처로 활용 가능하다. 실패 경로를 줄이기 위해 복잡성 추가는 입증된 필요성이 있을 때만 해야 한다는 설계 원칙이 이 장의 핵심 논지와 직결된다.",
    "key_claims": [
      "에이전트 시스템의 기본 빌딩 블록은 검색·도구·메모리로 증강된 LLM이며, 이 세 컴포넌트의 조합이 다양한 에이전트 패턴을 만든다",
      "워크플로우(사전 정의된 코드 경로)와 에이전트(LLM이 직접 프로세스를 제어)를 구분해야 한다",
      "불필요한 복잡성은 신뢰성을 낮추므로, 복잡도는 입증된 성능 개선이 있을 때만 추가해야 한다"
    ]
  },
  {
    "title": "7 AI Agent Failure Modes and How To Fix Them",
    "authors": ["Galileo AI"],
    "year": 2025,
    "type": "blog_post",
    "url": "https://galileo.ai/blog/agent-failure-modes-guide",
    "summary": "100개 이상 엔터프라이즈 배포에서 수집한 수백만 에이전트 트레이스를 분석해 7가지 실패 모드와 그 탐지·수정 전략을 정리한다. ch06에서 '에러 전파가 왜 에이전트 신뢰성의 핵심 위협인가'를 설명하는 구체적 실례와 수치로 활용하기 좋다. 메모리, 반성, 플래닝, 액션, 시스템 등 모듈별 에러 출처 추적 방법론은 컴포넌트 시스템 관점 강화에 직접 기여한다.",
    "key_claims": [
      "초기 실수 하나가 이후 모든 결정에 연쇄적으로 전파되는 에러 전파가 신뢰성을 무너뜨리는 실질적 원인이다",
      "현대 옵저버빌리티 플랫폼은 하루 수백만 에이전트 트레이스를 처리하며 체계적 실패 패턴을 탐지 가능하게 한다",
      "환각된 사실은 단독으로 끝나지 않고 후속 결정의 입력이 되어 다중 시스템 인시던트로 증폭된다"
    ]
  },
  {
    "title": "AI Agent Failure Pattern Recognition: The 6 Ways Agents Fail and How to Diagnose Them",
    "authors": ["MindStudio"],
    "year": 2025,
    "type": "blog_post",
    "url": "https://www.mindstudio.ai/blog/ai-agent-failure-pattern-recognition",
    "summary": "컨텍스트 저하, 스펙 드리프트, 아첨적 확인, 도구 호출 실패, 캐스케이딩 실패, 사일런트 실패라는 6가지 에이전트 고유 실패 유형을 전통 소프트웨어 버그와 대비하여 설명한다. ch06에서 '에이전트가 전통 소프트웨어와 왜 다른가'를 독자에게 각인시키는 대조적 프레이밍에 바로 활용할 수 있다. 특히 사일런트·캐스케이딩 실패가 왜 가장 위험한지를 설명하는 대목은 시스템 경계와 컴포넌트 의존성의 중요성을 입증하는 근거가 된다.",
    "key_claims": [
      "AI 에이전트는 전통 소프트웨어와 구조적으로 다른 방식으로 실패한다—출력이 올바른 형식을 가지면서도 완전히 틀린 답을 줄 수 있다",
      "사일런트 실패와 캐스케이딩 실패가 가장 위험한데, 출력이 타당해 보이는 동안 에러가 탐지되지 않고 전파되기 때문이다",
      "멀티에이전트 시스템에서는 한 에이전트의 에러가 다운스트림 에이전트의 컨텍스트로 들어가 추적하기 점점 어려워진다"
    ]
  },
  {
    "title": "AI Agent Failure Modes: 4 Ways Your Agent Knows the Answer But Says the Wrong Thing",
    "authors": ["MindStudio"],
    "year": 2025,
    "type": "blog_post",
    "url": "https://www.mindstudio.ai/blog/ai-agent-failure-modes-reasoning-action-disconnect",
    "summary": "Mount Sinai 의과대학 연구를 인용해 추론-행동 단절, 사회적 앵커링 편향, 컨텍스트 오염, 구조화된 출력 압박이라는 4가지 실패 모드를 설명한다. ch06에서 '에이전트 실패를 모델 수준이 아닌 시스템 수준에서 사고해야 하는 이유'를 뒷받침하는 연구 사례로 활용할 수 있다. 특히 이들 실패가 표준 벤치마크에서 보이지 않고 프로덕션에서만 드러난다는 점은 실제 시스템 설계 시 관점 전환이 필요함을 강조한다.",
    "key_claims": [
      "에이전트는 올바른 정보에 접근하고 올바른 추론을 하면서도 잘못된 출력을 낼 수 있다—지식 부족이 아닌 정보 처리 실패다",
      "추론-행동 단절, 사회적 앵커링, 컨텍스트 오염, 구조화된 출력 압박의 4가지 실패 모드는 표준 벤치마크에서 거의 탐지되지 않는다",
      "신뢰할 수 있는 멀티에이전트 설계는 모델 수준이 아닌 시스템 수준에서 실패 모드를 사고해야 한다"
    ]
  },
  {
    "title": "Multi-Agent System Reliability: Failure Patterns, Root Causes, and Production Validation Strategies",
    "authors": ["Maxim AI"],
    "year": 2025,
    "type": "blog_post",
    "url": "https://www.getmaxim.ai/articles/multi-agent-system-reliability-failure-patterns-root-causes-and-production-validation-strategies/",
    "summary": "프로덕션 멀티에이전트 시스템의 실패 패턴(상태 동기화 실패, 캐스케이딩 실패 등)과 분산
