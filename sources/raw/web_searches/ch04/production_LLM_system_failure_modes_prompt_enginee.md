# Search: production LLM system failure modes prompt engineering limits context management session state

수집된 자료를 충분히 분석했습니다. 이제 ch04 집필에 실제로 유용한 자료들을 선별하여 JSON으로 정리하겠습니다.

---

아래는 조사 결과를 바탕으로 정리한 참고 자료 목록입니다. **실제로 존재하고 URL이 확인된 자료**만 포함하였습니다.

---

```json
[
  {
    "title": "Failure Modes in LLM Systems: A System-Level Taxonomy for Reliable AI Applications",
    "authors": ["Vaishali Vinay"],
    "year": 2025,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2511.19933",
    "summary": "프로덕션 LLM 시스템에서 반복적으로 나타나는 15가지 숨겨진 실패 유형(context-boundary degradation, version drift, cost-driven performance collapse 등)을 분류한 논문. ch04에서 '왜 각 파이프라인 구성 요소가 독립적 설계 단위가 되어야 하는가'의 근거로 활용할 수 있다. 기존 벤치마크가 안정성·재현성·드리프트를 측정하지 못한다는 점을 지적하며, 시스템 엔지니어링 관점으로 LLM 신뢰성을 접근해야 한다고 주장한다.",
    "key_claims": [
      "LLM의 프로덕션 실패 패턴은 전통적인 ML 모델과 근본적으로 다르며, 시스템 수준의 분류가 필요하다.",
      "multi-step reasoning drift, context-boundary degradation, version drift 등 15개의 숨겨진 실패 모드가 식별된다.",
      "LLM 신뢰성은 모델 중심 문제가 아니라 시스템 엔지니어링 문제로 프레이밍해야 한다."
    ]
  },
  {
    "title": "A Field Guide to LLM Failure Modes",
    "authors": ["Adnan Masood"],
    "year": 2025,
    "type": "blog_post",
    "url": "https://medium.com/@adnanmasood/a-field-guide-to-llm-failure-modes-5ffaeeb08e80",
    "summary": "프로덕션 규제 환경에서 LLM을 실제 운영한 경험 기반의 실패 사례 가이드. confident fabrication, context misuse, brittle prompts, tool call 오류 등을 실제 재현 예시와 함께 설명하며, 각 실패 유형에 대한 완화 체크리스트를 제공한다. ch04의 '각 구성 요소가 왜 필요한가'를 구체적 실패 사례로 뒷받침하는 데 활용할 수 있다.",
    "key_claims": [
      "프로덕션에서 반복되는 실패 유형은 confident fabrication, context misuse, brittle prompts, tool call 오류, 과도/과소 거부다.",
      "grounding과 검증, 규율 있는 context 구성, schema-enforced output, retrieval hygiene 등이 실제로 효과 있는 제어 수단이다.",
      "각 실패 유형은 최소 재현 코드, 사전 출하 테스트 체크리스트, 프로덕션에서 검증된 제어책의 세 항목으로 다룰 수 있다."
    ]
  },
  {
    "title": "How To Solve LLM Production Challenges & How Prompt Updates Drive Most Incidents",
    "authors": ["Deepchecks Team"],
    "year": 2025,
    "type": "blog_post",
    "url": "https://deepchecks.com/llm-production-challenges-prompt-update-incidents/",
    "summary": "프로덕션 LLM 시스템의 불안정성이 모델/인프라 장애가 아니라 프롬프트 드리프트에서 기원한다는 점을 실증적으로 설명한다. 프롬프트를 독립된 버전 관리 자산으로 취급해야 한다는 주장은, ch04에서 '프롬프트 구성'이 왜 별도의 설계 단위가 되어야 하는지를 설명할 때 직접 인용할 수 있는 근거가 된다.",
    "key_claims": [
      "모델/인프라 장애보다 관리되지 않는 프롬프트 변경 누적(prompt drift)이 프로덕션 신뢰성을 더 많이 무너뜨린다.",
      "프롬프트는 애플리케이션 로직에 하드코딩하지 말고 전용 레지스트리에 버전과 메타데이터를 포함해 관리해야 한다.",
      "프로덕션 환경은 lab에서 놓친 multi-agent 연쇄 실패, verbose response로 인한 토큰 과다 소비, 엣지케이스 안전 위반 등을 드러낸다."
    ]
  },
  {
    "title": "8 LLM Production Challenges: Problems, Solutions",
    "authors": ["Shift Asia Team"],
    "year": 2025,
    "type": "blog_post",
    "url": "https://shiftasia.com/community/8-llm-production-challenges-problems-solutions/",
    "summary": "환각, 프롬프트 인젝션, 컨텍스트 한계, 비결정성, 비용·지연, 편향, 개인정보 유출, 추론 실패라는 8가지 LLM 프로덕션 문제를 구조화한 실용 가이드. ch04의 독자가 'LLM을 블랙박스가 아닌 구성 요소의 연결로 인식'하도록 돕는 데 각 문제와 솔루션(chunking, retrieval, caching, schema enforcement 등)이 특정 파이프라인 요소와 연결됨을 보여주는 사례로 활용할 수 있다.",
    "key_claims": [
      "LLM은 확률적 특성상 '고칠' 수 없으며, 그 한계에도 불구하고 잘 동작하는 시스템을 설계해야 한다.",
      "컨텍스트 한계는 스마트 청킹·retrieval·메모리 관리로 대응해야 하며, 백만 토큰 모델도 'lost in the middle' 문제에서 자유롭지 않다.",
      "비용·지연 문제는 프롬프트 트리밍, 응답 캐싱, 계층적 모델 선택으로 해결할 수 있다."
    ]
  },
  {
    "title": "#008: Beyond Prompt Engineering: What Engineers Are Actually Using to Make LLMs Reliable in Production",
    "authors": ["Full Stack AI Engineer (Substack)"],
    "year": 2025,
    "type": "blog_post",
    "url": "https://fullstackaiengineer.substack.com/p/008-beyond-prompt-engineering-what",
    "summary": "업계가 '더 좋은 프롬프트 작성' 단계를 넘어서 LLM을 신뢰할 수 없는 외부 의존성처럼 취급하는 시스템 엔지니어링 단계로 이동했음을 실증적으로 서술한 글. ch04의 핵심 논지인 '프롬프트 엔지니어링은 충분하지 않고, 시스템 구성 요소의 분리가 필요하다'를 뒷받침하는 업계 관점의 증거로 직접 활용할 수 있다.",
    "key_claims": [
      "업계는 조용히 '더 나은 프롬프트' 단계를 지나쳤으며, 진지하게 작업하는 엔지니어들은 LLM을 신뢰할 수 없는 외부 의존성처럼 취급한다.",
      "가장 레버리지 높은 단일 변화는 LLM이 자유 형식 텍스트 대신 구조화된 데이터를 반환하도록 강제하는 것이다.",
      "신뢰할 수 있는 LLM 시스템을 구축하는 엔지니어들은 프롬프팅을 잘하는 것이 아니라 시스템 사고를 잘하는 것이다."
    ]
  },
  {
    "title": "The LLM Context Problem in 2026: Strategies for Memory, Relevance, and Scale",
    "authors": ["LogRocket Blog"],
    "year": 2026,
    "type": "blog_post",
    "url": "https://blog.logrocket.com/llm-context-problem-strategies-2026",
    "summary": "2026년 기준으로 대부분의 팀이 경험하는 LLM 컨텍스트 문제의 본질이 모델 역량이 아닌 정보 품질 관리 문제임을 설명한다. 컨텍스트 오염, 과적재, poisoning 등 4가지 프로덕션 실패 패턴을 구체적 사례와 함께 서술하며, ch04의 '상태 관리' 구성 요소가 왜 독립적으로 설계되어야 하는지를 설명하는 데 직접 활용할 수 있다.",
    "key_claims": [
      "2026년 LLM 컨텍스트 문제의 병목은 거의 모델이 아니라 모델에 무엇을 공급하는가에 있다.",
      "성공적인 프로덕션 시스템은 컨텍스트 엔지니어링을 일급 규율로 취급하며 정보를 의도적으로 필터링, 순위화, 가지치기, 요약, 격리한다.",
      "컨텍스트 poisoning은 잘못된 믿음이 컨텍스트에 진입해 시간이 지남에 따라 강화될 때 발생하며, 에이전트가 실제로 없는 아이템을 사용하려고 시간을 허비하는 결과를 낳는다."
    ]
  },
  {
    "title": "LLM Context Management: How to Improve Performance and Lower Costs",
    "authors": ["16x Eval Team"],
    "year": 2025,
    "type": "blog_post",
    "url": "https://eval.16x.engineer/blog/llm-context-management-guide",
    "summary": "LLM이 본질적으로 stateless하기 때문에 매 메시지마다 전체 대화 히스토리를 재전송해야 한다는 구조적 특성을 명확히 설명한다. 컨텍스트 bloat이 성능 저하와 비용 증가로 이어지는 메커니즘을 설명하며, ch04에서 '세션 상태 관리' 구성 요소의 필요성을 독자가 이해하도록 돕는 기초 자료로 활용할 수 있다.",
    "key_claims": [
      "LLM은 stateless하며 과거 대화에 대한 기억이 없어 매 메시지마다 전체 대화 히스토리를 모델에 재전송해야 한다.",
      "컨텍스트 창을 최대한 채우려는 시도는 나쁜 관행이며, context bloat은 성능 저하와 비용 증가를 야기한다.",
      "컨텍스트 엔지니어링은 '컨텍스트 창을 정확히 올바른 정보로 채우는 섬세한 예술이자 과학'이다(Andrej Karpathy)."
    ]
  },
  {
    "title": "Architecting Efficient Context-Aware Multi-Agent Framework for Production",
    "authors": ["Google Developers Blog"],
    "year": 2025,
    "type": "blog_post",
    "url": "https://developers.googleblog.com/architecting-efficient-context-aware-multi-agent-framework-for-production/",
    "summary": "Google ADK(Agent Development Kit)의 설계 철학을 소개하며, 컨텍스트를 'mutable string buffer'가 아닌 '풍부한 stateful 시스템 위의 compiled view'로 접근해야 한다는 핵심 개념을 제시한다. ch04에서 '상태 관리'와 '컨텍스트 구성'이 별개의 독립된 설계 단위가 되어야 하는 이유를 구조적으로 설명할 때 Google의 실제 프로덕션 설계 결정을 사례로 인용할 수 있다.",
    "key_claims": [
      "이전 세대 에이전트 프레임워크는 컨텍스트를 mutable string buffer처럼 취급했으나, ADK는 컨텍스트를 더 풍부한 stateful 시스템 위의 compiled view로 설계했다.",
      "Session은 ground truth이고 working context는 그것으로부터 파생된 일시적 표현이며, 이 분리를 통해 저장과 표현 계층을 독립적으로 최적화할 수 있다.",
      "토큰을 더 많이 넣는 것은 시간을 벌 뿐이며, 확장을 위해서는 컨텍스트 표현 방식 자체를 바꿔야 한다."
    ]
  },
  {
    "title": "Context Engineering:
