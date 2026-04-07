# Search: LLM agent system architecture components model memory tools context interaction design

수집된 자료를 모두 검토하여 ch06 집필에 가장 적합한 것들을 선별·정리하겠습니다.

---

아래는 조사 결과를 바탕으로 정리한 참고 자료 목록입니다. 각 자료의 실제 존재 여부와 URL을 확인한 것만 포함했습니다.



Lilian Weng의 블로그 포스트는 LLM 기반 자율 에이전트 시스템을 Planning(서브골 분해, 반성/정제), Memory(단기·장기), Tool Use(외부 API 호출)라는 세 컴포넌트로 명확히 분류한 사실상의 레퍼런스 문서입니다.





Wang et al.의 서베이 논문은 에이전트의 핵심 컴포넌트를 profile module, memory module, planning module, action module로 분해한 통합 프레임워크를 제시합니다.





ReAct 논문은 추론 트레이스와 도구 호출 액션을 교차(interleaved)하는 방식으로 둘 사이의 시너지를 만들며, 에이전트 루프의 내부 흐름을 가장 명확하게 시각화한 논문입니다.





MemGPT는 OS의 계층적 메모리 시스템에서 영감을 얻어 virtual context management를 제안하며, 컨텍스트 윈도우를 RAM으로, 외부 저장소를 디스크로 비유하는 시스템 관점을 제시합니다.





Anthropic의 "Building Effective Agents"는 워크플로우(predefined code paths)와 에이전트(LLM이 자신의 프로세스를 동적으로 지휘)를 아키텍처 수준에서 구분하는 실용적 기준을 제공합니다.





Generative Agents 논문은 에이전트 아키텍처가 경험 기록 저장 → 메모리 상위 수준 반성 → 동적 검색 → 행동 계획이라는 순환 구조임을 ablation으로 검증합니다.





Toolformer는 LM이 스스로 외부 도구 사용법을 학습할 수 있으며, 어떤 API를 언제, 어떤 인자로 호출할지 결정하는 능력이 별도의 컴포넌트임을 보여줍니다.



---

```json
[
  {
    "title": "LLM Powered Autonomous Agents",
    "authors": ["Lilian Weng"],
    "year": 2023,
    "type": "blog_post",
    "url": "https://lilianweng.github.io/posts/2023-06-23-agent/",
    "summary": "LLM 기반 자율 에이전트 시스템을 Planning, Memory, Tool Use 세 컴포넌트로 분류하고 각각의 역할과 구현 방식을 상세히 설명한다. ch06에서 '에이전트 = 상호작용하는 컴포넌트들의 집합'이라는 핵심 프레임을 독자에게 소개할 때 가장 직접적으로 인용할 수 있는 레퍼런스다. 단기 메모리(컨텍스트 창)와 장기 메모리(벡터 DB)의 구분, 도구 호출의 의미 등을 명확한 언어로 정의하고 있다.",
    "key_claims": [
      "LLM 기반 에이전트에서 LLM은 뇌 역할을 하며, Planning·Memory·Tool Use 모듈이 이를 보완한다",
      "단기 메모리는 컨텍스트 창 내 in-context learning이고, 장기 메모리는 외부 벡터 스토어와 빠른 검색으로 구현된다",
      "에이전트는 단순 프롬프트-응답 루프가 아니라 인식-계획-행동의 반복 사이클로 동작한다"
    ]
  },
  {
    "title": "A Survey on Large Language Model based Autonomous Agents",
    "authors": ["Lei Wang", "Chen Ma", "Xueyang Feng", "Zeyu Zhang", "Hao Yang", "Jingsen Zhang", "Zhiyuan Chen", "Jiakai Tang", "Xu Chen", "Yankai Lin", "Wayne Xin Zhao", "Zhewei Wei", "Ji-Rong Wen"],
    "year": 2024,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2308.11432",
    "summary": "LLM 기반 자율 에이전트 분야의 첫 번째 공식 출판 서베이로, profile·memory·planning·action 4개 모듈로 이루어진 통합 에이전트 프레임워크를 제안한다. ch06에서 에이전트를 시스템으로 분해하는 공식 어휘와 분류 체계의 근거로 사용할 수 있다. 에이전트 구성(construction), 응용(application), 평가(evaluation)를 체계적으로 다루어 장 전체의 구조를 잡는 데 기여한다.",
    "key_claims": [
      "에이전트의 필수 컴포넌트는 profile module, memory module, planning module, action module이다",
      "LLM 기반 에이전트는 강화학습 기반 에이전트보다 포괄적인 내부 세계 지식을 보유하며, 도메인 특화 데이터 없이도 행동할 수 있다",
      "에이전트 아키텍처 설계 문제와 에이전트 능력 향상 문제는 각각 '하드웨어'와 '소프트웨어' 관점에 해당한다"
    ]
  },
  {
    "title": "ReAct: Synergizing Reasoning and Acting in Language Models",
    "authors": ["Shunyu Yao", "Jeffrey Zhao", "Dian Yu", "Nan Du", "Izhak Shafran", "Karthik Narasimhan", "Yuan Cao"],
    "year": 2023,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2210.03629",
    "summary": "추론(reasoning trace)과 액션(tool-specific action)을 교차하여 생성하는 ReAct 패턴을 제안하며, 에이전트 루프의 내부 흐름인 Thought→Action→Observation 사이클을 가장 명확하게 정형화한 논문이다. ch06에서 '단순 모델 호출 하나'처럼 보이는 에이전트가 내부적으로 어떤 반복 흐름을 갖는지 설명하는 핵심 사례로 활용 가능하다. 외부 환경(도구)과의 상호작용이 에이전트 컴포넌트 간 의존성을 만드는 방식을 실험적으로 보여준다.",
    "key_claims": [
      "추론과 행동을 교차(interleaved)하면 환각 및 오류 전파를 줄이고 인간이 해석 가능한 task-solving trajectory를 생성한다",
      "추론 트레이스는 action plan을 유도·추적·갱신하고 예외를 처리하며, 액션은 외부 소스에서 추가 정보를 수집한다",
      "기존에 추론과 행동은 별개 주제로 연구되었으나, 두 기능의 결합이 시너지를 만들어낸다"
    ]
  },
  {
    "title": "MemGPT: Towards LLMs as Operating Systems",
    "authors": ["Charles Packer", "Vivian Fang", "Shishir G. Patil", "Kevin Lin", "Sarah Wooders", "Joseph E. Gonzalez"],
    "year": 2023,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2310.08560",
    "summary": "OS의 계층적 메모리 시스템(RAM/디스크)에서 영감을 얻어, LLM의 고정된 컨텍스트 창을 main context로, 외부 저장소를 external context로 분리하는 virtual context management 아키텍처를 제안한다. ch06에서 메모리 컴포넌트가 단순 저장이 아니라 시스템 전체의 상태 관리 레이어임을 설명할 때 구체적인 구현 사례로 활용 가능하다. 컨텍스트 한계라는 고정 제약을 '컴포넌트 설계 결정'으로 다루는 시스템 관점을 명확히 보여준다.",
    "key_claims": [
      "LLM의 컨텍스트 창을 RAM에, 외부 저장소를 디스크에 비유한 2계층 메모리 구조로 사실상 무한한 컨텍스트를 구현할 수 있다",
      "function call을 통해 LLM 에이전트가 외부 데이터 소스를 읽고 쓰며 자신의 컨텍스트를 수정할 수 있다",
      "장기 대화와 긴 문서 분석 두 영역에서 고정 컨텍스트 모델의 성능 한계를 메모리 시스템 설계로 극복할 수 있다"
    ]
  },
  {
    "title": "Building Effective Agents",
    "authors": ["Erik Schluntz", "Barry Zhang"],
    "year": 2024,
    "type": "blog_post",
    "url": "https://www.anthropic.com/research/building-effective-agents",
    "summary": "Anthropic이 수십 개의 에이전트 구축 팀과의 협업 경험을 바탕으로 작성한 실용 가이드로, 워크플로우(predefined code path)와 에이전트(LLM이 동적으로 프로세스를 지휘)를 아키텍처 수준에서 구분한다. ch06의 핵심 논지인 '단순 모델 호출과 시스템의 차이'를 산업 현장의 경험 데이터로 뒷받침하는 데 최적이다. '복잡한 프레임워크보다 단순한 조합 가능한 패턴이 더 성공적'이라는 주장은 컴포넌트 교체·확장 시 설계 원칙을 논의하는 데 직접 사용할 수 있다.",
    "key_claims": [
      "가장 성공적인 에이전트 구현은 복잡한 프레임워크가 아니라 단순하고 조합 가능한(composable) 패턴을 사용한다",
      "워크플로우는 LLM과 도구가 미리 정의된 코드 경로로 조율되는 시스템이고, 에이전트는 LLM이 자신의 프로세스와 도구 사용을 동적으로 결정하는 시스템이다",
      "에이전트 시스템은 더 나은 태스크 성능을 위해 지연 시간과 비용을 트레이드오프하므로, 이 트레이드오프가 타당할 때만 구축해야 한다"
    ]
  },
  {
    "title": "Generative Agents: Interactive Simulacra of Human Behavior",
    "authors": ["Joon Sung Park", "Joseph C. O'Brien", "Carrie J. Cai", "Meredith Ringel Morris", "Percy Liang", "Michael S. Bernstein"],
    "year": 2023,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2304.03442",
    "summary": "LLM에 경험 기록 저장, 상위 수준 반성(reflection), 동적 검색 및 행동 계획을 추가한 에이전트 아키텍처를 제안하며, 각 컴포넌트(관찰·계획·반성)가 제거될 때 행동의 질이 어떻게 저하되는지 ablation으로 검증한다. ch06에서 '겉보기엔 단순해 보이는 에이전트가 내부적으로 어떤 컴포넌트 상호작용을 갖는지' 설명하는 풍부한 사례로 활용할 수 있다. 에이전트 시스템 내 메모리·계획·행동 컴포넌트 간 의존 관계를 실험적으로 보여주는 유일한 논문 중 하나다.",
    "key_claims": [
      "에이전트 아키텍처는 자연어로 경험을 저장하고, 시간에 따라 기억을 상위 수준 반성으로 합성하며, 이를 동적으로 검색하여 행동을 계획하는 구조로 이루어진다",
      "관찰(observation)·계획(planning)·반성(reflection) 세
