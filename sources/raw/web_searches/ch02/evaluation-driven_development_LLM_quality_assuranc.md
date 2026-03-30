# Search: evaluation-driven development LLM quality assurance methodology "good enough" criteria

수집된 자료들을 충분히 파악했습니다. 이제 JSON 형식으로 정리하겠습니다.

---

아래는 검색 결과를 바탕으로 확인된 실제 존재 자료만을 추려 정리한 JSON입니다.



핵심 논문인 EDDOps는 LLM 에이전트의 행동이 개방형·확률론적이며 시스템 레벨 상호작용에 의해 형성됨을 지적하고, 고정 벤치마크와 정적 테스트 스위트에 기반한 전통적 평가 방법이 창발적 행동을 포착하거나 생애주기 전반의 지속적 적응을 지원하지 못한다고 논증합니다.

 

TDD/BDD는 정적 요구사항과 결정론적 테스트 결과를 전제하는데, LLM 에이전트는 미명세된 목표를 추구하고 비결정론적 출력을 생성하며 배포 후에도 계속 적응하기 때문에, 이진적 패스/실패 단언, 사전 배포 검증 위주 관행, 창발 행동 지원 부재라는 네 가지 한계가 존재합니다.



```json
[
  {
    "title": "Evaluation-Driven Development and Operations of LLM Agents: A Process Model and Reference Architecture",
    "authors": ["Boming Xia", "Qinghua Lu", "Liming Zhu", "Zhenchang Xing", "Dehai Zhao", "Hao Zhang"],
    "year": 2025,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2411.13768",
    "summary": "ch02의 핵심 이론적 기둥이 될 논문. TDD/BDD가 결정론적 시스템 전제에 기반하고 있어 LLM 에이전트에 왜 무력화되는지를 네 가지 구체적 한계(정적 요구사항 의존, 이진 패스/실패 단언, 배포 후 드리프트 무시, 창발 행동 미지원)로 명시화한다. 그 대안으로 EDD(평가 주도 개발)의 구체적 프로세스 모델과 참조 아키텍처를 제안하므로, 장의 논증 흐름(TDD 무력화 → EDD 선언)을 뒷받침하는 직접적 학술 근거로 활용할 수 있다.",
    "key_claims": [
      "LLM 에이전트의 행동은 개방형·확률론적이며, 고정 벤치마크와 정적 테스트 스위트로는 창발적 행동을 포착하거나 지속적 적응을 지원할 수 없다",
      "TDD/BDD는 정적 요구사항과 결정론적 테스트 결과를 전제하므로, 비결정론적 출력과 배포 후 진화를 특징으로 하는 LLM 에이전트에는 구조적으로 부적합하다",
      "EDDOps는 오프라인(개발 시점) 평가와 온라인(런타임) 평가를 폐쇄적 피드백 루프로 통합하여, 평가를 최종 체크포인트가 아닌 지속적·통치적 기능으로 내재화한다",
      "평가 증거(evaluation evidence)가 런타임 적응과 재개발을 모두 주도함으로써, LLM 에이전트의 안전하고 추적 가능한 진화를 지원한다"
    ]
  },
  {
    "title": "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena",
    "authors": ["Lianmin Zheng", "Wei-Lin Chiang", "Ying Sheng", "Siyuan Zhuang", "Zhanghao Wu", "Yonghao Zhuang", "Zi Lin", "Zhuohan Li", "Dacheng Li", "Eric P. Xing", "Hao Zhang", "Joseph E. Gonzalez", "Ion Stoica"],
    "year": 2023,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2306.05685",
    "summary": "EDD의 핵심 평가 수단인 'LLM-as-a-Judge' 개념을 최초로 체계화한 NeurIPS 2023 논문. 기존 벤치마크가 인간 선호도 측정에 부적합함을 실증하고, 강력한 LLM을 평가자로 사용하면 인간 평가자 간 합의 수준인 80% 이상의 일치율을 달성함을 보여준다. 이는 '정답 일치'가 아닌 '인간 선호도 근사'라는 새로운 품질 기준 개념을 도입하여, ch02에서 'good enough 기준'의 실증적 정당성으로 직접 인용할 수 있다.",
    "key_claims": [
      "LLM 기반 챗 어시스턴트 평가는 넓은 능력 범위와 기존 벤치마크의 인간 선호도 측정 부적합성으로 인해 근본적으로 어렵다",
      "GPT-4 같은 강력한 LLM 심판은 통제된 및 크라우드소싱된 인간 선호도 모두와 80% 이상 일치율을 달성해, 인간 평가의 확장 가능하고 설명 가능한 대안이 된다",
      "LLM-as-a-Judge는 위치 편향, 장황함 편향, 자기 강화 편향 같은 한계를 가지며, 이를 완화하는 설계가 필요하다"
    ]
  },
  {
    "title": "Methodology for Quality Assurance Testing of LLM-based Multi-Agent Systems",
    "authors": ["(ACM AIMLSystems 2024 proceedings authors)"],
    "year": 2024,
    "type": "academic_paper",
    "url": "https://dl.acm.org/doi/full/10.1145/3703412.3703439",
    "summary": "LLM 기반 멀티 에이전트 시스템(MAS)에 대한 품질 보증 방법론을 실증적으로 제시한 ACM 논문. LLM의 예측 불가능성과 환각 특성이 프로덕션 배포를 방해한다는 문제를 출발점으로, 시스템 성능 모니터링과 LLM 평가 소프트웨어를 결합한 구체적 QA 방법론을 제안한다. ch02에서 '기존 방법으로는 왜 안 되는가'의 실제 사례 및 새로운 평가 방법론의 실천 사례로 활용할 수 있다.",
    "key_claims": [
      "LLM의 예측 불가능하고 환각적인 특성이 멀티 에이전트 시스템의 프로덕션 배포를 가로막는 핵심 장벽이다",
      "현재는 MAS 전체 성능을 평가·테스트할 수 있는 소프트웨어가 존재하지 않아, 새로운 QA 방법론이 필요하다",
      "관련성(relevance), 근거 충실성(groundedness), 정확성(correctness) 등의 파라미터로 개별 에이전트 및 전체 MAS 양 수준에서 품질을 평가해야 한다"
    ]
  },
  {
    "title": "Evaluation and Benchmarking of LLM Agents: A Survey",
    "authors": ["(KDD 2025 proceedings authors)"],
    "year": 2025,
    "type": "academic_paper",
    "url": "https://arxiv.org/html/2507.21504v1",
    "summary": "LLM 에이전트 평가 및 벤치마킹에 관한 포괄적 서베이 논문(KDD 2025). 평가 목표(행동·능력·신뢰성·안전성)와 평가 프로세스(상호작용 방식, 데이터셋, 지표, 툴링, 환경)를 아우르는 분류 체계를 제안하며, EDD(평가 주도 개발) 개념이 실제 에이전트 구축 현장에서 확산되고 있음을 확인한다. ch02에서 EDD가 단일 논문의 제안이 아니라 업계 전반의 실천적 움직임임을 근거짓는 데 사용할 수 있다.",
    "key_claims": [
      "평가를 개발 생애주기에 직접 통합하는 자동화·확장 가능·지속적 에이전트 평가 워크플로우를 지원하는 소프트웨어 프레임워크들이 등장하며 평가 주도 개발(EDD)이라는 움직임이 생겨나고 있다",
      "기존 서베이들이 특정 에이전트 능력에 집중하거나 전체론적 관점을 결여하고 있어, 평가 목표와 프로세스를 통합한 분류 체계가 필요하다",
      "엔터프라이즈 환경은 데이터 보안, 감사·규정 준수를 위한 고신뢰성, 복잡한 상호작용 패턴 등 기존 문헌에서 거의 다루지 않는 추가 요건을 에이전트에 부과한다"
    ]
  },
  {
    "title": "Beyond Deterministic Testing: Why Testing AI Systems Is Fundamentally Different",
    "authors": ["Planit Testing"],
    "year": 2025,
    "type": "blog_post",
    "url": "https://www.planit.com/beyond-deterministic-testing-why-testing-ai-systems-is-fundamentally-different/",
    "summary": "소프트웨어 품질 엔지니어링 관점에서 AI 시스템 테스팅이 전통적 테스팅과 어떻게 근본적으로 다른지를 설명하는 업계 실무 글. '전통적 테스팅은 예측 가능한 행동과 사전 정의된 기대 결과를 가정하지만 이는 확률론적·비결정론적 AI에는 성립하지 않는다'는 핵심 명제를 명확히 서술하며, '시스템은 결정론적으로 실패하지 않고 확률론적으로 실패한다'는 통찰을 제공한다. ch02에서 결정론 vs 확률론 대비의 구체적 사례로 인용할 수 있다.",
    "key_claims": [
      "전통적 테스팅은 예측 가능한 행동과 사전 정의된 기대 결과를 가정하는데, 이는 확률론적·비결정론적 AI·LLM 시스템에서는 성립하지 않는다",
      "AI 시스템은 결정론적으로 실패하지 않고 확률론적으로 실패하며, 이 구분이 품질 평가 방식 자체를 바꾼다",
      "단일 정답을 기대하는 회귀 테스트는 AI 시스템을 의미 있게 평가하지 못하며, 정확도가 높아도 행동 신뢰성이 보장되지 않는다"
    ]
  },
  {
    "title": "Adapting TDD for Reliable AI Systems",
    "authors": ["Galileo AI"],
    "year": 2024,
    "type": "blog_post",
    "url": "https://galileo.ai/blog/test-driven-development-ai-systems",
    "summary": "AI 시스템에 TDD를 적용할 때 발생하는 근본적 한계와 이를 극복하기 위한 적응적 접근법을 서술한 실무 중심 블로그 글. '전통적 TDD의 결정론적 패스/실패 테스트는 AI의 확률론적 특성으로 인해 부족하며, 정확한 출력 대신 허용 가능한 통계적 범위 내에 있는지를 검증해야 한다'는 핵심 전환점을 설명한다. ch02의 'TDD 무력화 메커니즘' 절에서 구체적 설명 도구로 활용할 수 있다.",
    "key_claims": [
      "전통적 TDD는 명확한 패스/실패 결과를 가진 결정론적 테스트를 사용하는데, AI 시스템의 확률론적 특성 때문에 이 방식은 부족하다",
      "AI 테스팅에서는 정확한 출력 대신 허용 가능한 통계적 범위 내에 있는지를 검증해야 하며, 다중 실행 테스팅이 필수적이다",
      "AI 시스템에 TDD를 적용하려면 비결정론적 테스트 요건을 다루는 품질 평가, 컴포넌트 테스팅, 전문화된 도구에 초점을 맞춘 근본적 적응이 필요하다"
    ]
