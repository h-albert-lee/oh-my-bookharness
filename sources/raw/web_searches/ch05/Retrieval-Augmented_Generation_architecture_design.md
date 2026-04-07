# Search: Retrieval-Augmented Generation architecture design patterns information flow control 2023 2024

모든 필요한 자료를 수집했습니다. 이제 JSON 형식으로 정리하겠습니다.

---

아래는 ch05 집필에 활용 가능한 실존 자료를 검증하여 정리한 결과입니다.



Lewis et al.(2020)의 원 논문은 LLM이 파라메트릭 메모리만으로는 지식 집약적 태스크에서 한계를 보인다는 점을 실증하며, RAG가 이 문제를 해소하기 위해 어떻게 파라메트릭·비파라메트릭 메모리를 결합했는지 보여줍니다.

 

Gao et al.(2024) 서베이는 Naive RAG→Advanced RAG→Modular RAG로의 패러다임 진화를 체계적으로 정리하며, 검색·생성·증강이라는 세 축이 정보 흐름을 어떻게 통제하는지 분석합니다.

 

Self-RAG(Asai et al., 2023)는 고정된 횟수로 무차별 검색하는 방식이 오히려 모델 유연성을 떨어뜨린다는 문제를 지적하며, 온디맨드 검색과 self-reflection 토큰으로 정보 흐름 통제를 모델 내부로 내재화했습니다.

 

Barnett et al.(2024)은 RAG 시스템의 7가지 실패 지점을 실제 사례(연구·교육·바이오메디컬)에서 도출하여, 잘못 설계된 RAG가 어떻게 무너지는지를 구체적으로 보여줍니다.



```json
[
  {
    "title": "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks",
    "authors": ["Patrick Lewis", "Ethan Perez", "Aleksandra Piktus", "Fabio Petroni", "Vladimir Karpukhin", "Naman Goyal", "Heinrich Küttler", "Mike Lewis", "Wen-tau Yih", "Tim Rocktäschel", "Sebastian Riedel", "Douwe Kiela"],
    "year": 2020,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2005.11401",
    "summary": "RAG의 원조 논문으로, '왜 RAG가 등장했는가'를 LLM의 파라메트릭 메모리 한계에서 설명하는 데 필수적인 출처다. LLM이 지식 집약적 태스크에서 구조적으로 한계를 갖는다는 점을 실증하고, 외부 비파라메트릭 메모리(벡터 인덱스)와 생성 모델을 결합하는 아키텍처적 근거를 제시한다. ch05의 'RAG 등장 배경' 절에서 원점(origin story)으로 직접 인용할 수 있다.",
    "key_claims": [
      "LLM은 파라메트릭 지식을 저장할 수 있으나, 정밀한 지식 접근·갱신 능력이 구조적으로 제한된다(parametric memory의 한계).",
      "파라메트릭 seq2seq 모델과 비파라메트릭 밀집 벡터 인덱스를 결합한 RAG 모델이 open-domain QA에서 SOTA를 달성하며 더 구체적이고 사실적인 언어를 생성한다.",
      "검색 인덱스를 교체(hot-swap)하는 것만으로 모델 재훈련 없이 지식을 갱신할 수 있어 정보 흐름 통제의 구조적 이점을 가진다."
    ]
  },
  {
    "title": "Retrieval-Augmented Generation for Large Language Models: A Survey",
    "authors": ["Yunfan Gao", "Yun Xiong", "Xinyu Gao", "Kangxiang Jia", "Jinliu Pan", "Yuxi Bi", "Yi Dai", "Jiawei Sun", "Meng Wang", "Haofen Wang"],
    "year": 2024,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2312.10997",
    "summary": "Naive RAG → Advanced RAG → Modular RAG 세 패러다임의 진화를 체계적으로 정리한 핵심 서베이다. 각 패러다임이 정보 흐름의 어느 단계(pre-retrieval, retrieval, post-retrieval, generation)를 통제하는지 비교 분석하여, ch05의 '정보 흐름 통제 구조' 설명에 직접 활용할 수 있다. Modular RAG에서는 기능 모듈을 교체·조합할 수 있는 아키텍처적 유연성을 보여줘 'RAG는 기능이 아니라 아키텍처'라는 주장을 뒷받침한다.",
    "key_claims": [
      "RAG 패러다임은 Naive(단순 검색-읽기) → Advanced(사전/사후 검색 최적화) → Modular(독립 모듈 조합, 조건부·루핑·분기 오케스트레이션) 순으로 진화했다.",
      "Modular RAG는 검색·생성·증강을 독립적으로 교체 가능한 서브컴포넌트로 분해하여 재현성, 유연성, 제어 흐름 통합을 실현한다.",
      "Advanced RAG는 슬라이딩 윈도우, 세밀한 세그멘테이션, 메타데이터 통합 등으로 인덱싱 문제를 해결하며, Naive RAG의 정보 품질 문제를 구조적으로 보완한다."
    ]
  },
  {
    "title": "Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection",
    "authors": ["Akari Asai", "Zeqiu Wu", "Yizhong Wang", "Avirup Sil", "Hannaneh Hajishirzi"],
    "year": 2023,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2310.11511",
    "summary": "기존 RAG의 '무차별 검색'이 오히려 성능을 떨어뜨린다는 점을 지적하고, 모델이 스스로 검색 필요 여부를 판단하는 Self-RAG를 제안한다. 정보 흐름 통제를 외부 파이프라인이 아니라 모델 내부로 내재화한 설계로, ch05에서 '정보 흐름 통제의 위치'가 파이프라인 단계마다 달라질 수 있음을 보여주는 사례로 활용할 수 있다. ICLR 2024 Oral(상위 1%) 채택 논문으로 신뢰도 높다.",
    "key_claims": [
      "고정된 횟수로 무차별 검색하는 방식은 불필요하거나 관련 없는 문서를 삽입해 오히려 LLM 유연성을 저하시킨다.",
      "Self-RAG는 'reflection token'으로 검색 필요 여부·검색 문서 관련성·생성 결과 지지도를 스스로 평가하여 온디맨드 검색을 실현한다.",
      "추론 시 reflection token을 통한 커스터마이즈가 가능해, 태스크 요구사항에 따라 검색 빈도와 모델 행동을 유연하게 조정할 수 있다."
    ]
  },
  {
    "title": "Seven Failure Points When Engineering a Retrieval Augmented Generation System",
    "authors": ["Scott Barnett", "Stefanus Kurniawan", "Srikanth Thudumu", "Zach Brannelly", "Mohamed Abdelrazek"],
    "year": 2024,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2401.05856",
    "summary": "연구·교육·바이오메디컬 세 도메인의 실제 RAG 시스템 구축 경험을 바탕으로 7가지 실패 지점을 카탈로그 형태로 정리한 논문이다. ch05의 'RAG를 잘못 설계했을 때 발생하는 실패' 절에 가장 직접적으로 활용할 수 있는 자료로, 각 실패 지점이 정보 흐름의 어느 단계에서 발생하는지 연결해 설명하면 효과적이다.",
    "key_claims": [
      "RAG 시스템은 정보 검색 시스템 고유의 한계와 LLM 의존성 문제를 동시에 안고 있으며, 이 두 층위의 실패가 복합적으로 발생한다.",
      "RAG 시스템의 유효성 검증은 실제 운영 중에만 가능하며, 견고성은 처음 설계 단계보다 운영하면서 점진적으로 발전시키는 것이 현실적이다.",
      "쿼리 전처리, 청크 품질, 임베딩 매칭, 컨텍스트 윈도우 초과, LLM의 부정·모호 쿼리 처리 등이 실패 지점으로 식별된다."
    ]
  },
  {
    "title": "Retrieval-Augmented Generation: A Comprehensive Survey of Architectures, Enhancements, and Robustness Frontiers",
    "authors": ["(arXiv 2506.00054 저자진)"],
    "year": 2025,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2506.00054",
    "summary": "RAG 아키텍처를 retriever-centric, generator-centric, hybrid, robustness-oriented 네 가지로 분류한 최신 종합 서베이다. 각 아키텍처 유형이 정보 흐름의 어느 지점에 개입하는지를 명확히 구분하므로, ch05에서 '정보 흐름 통제의 각 단계' 설명에 분류 체계를 빌려올 수 있다. 동적 검색 트리거(DRAGIN, FLARE 등)와 컨텍스트 압축(FiD-Light, xRAG 등) 패턴도 정리되어 있다.",
    "key_claims": [
      "RAG 아키텍처는 retriever-centric, generator-centric, hybrid, robustness-oriented 네 범주로 분류되며, 각각 정보 흐름의 다른 지점을 최적화한다.",
      "동적 검색 트리거 시스템(DRAGIN, FLARE 등)은 생성 불확실성·태스크 복잡도에 따라 검색 시점을 조건부로 결정해 정보 흐름을 정밀 통제한다.",
      "컨텍스트 창 한계를 극복하기 위해 검색 입력을 더 조밀하거나 구조화된 형태로 최적화하는 필터링 접근(FILCO, xRAG 등)이 정보 흐름의 병목을 완화한다."
    ]
  },
  {
    "title": "Engineering the RAG Stack: A Comprehensive Review of the Architecture and Trust Frameworks for Retrieval Augmented Generation Systems",
    "authors": ["(arXiv 2601.05264 저자진)"],
    "year": 2025,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2601.05264",
    "summary": "RAG 아키텍처를 적응성·신뢰 교정·모달리티·융합 메커니즘·검색 전략 다섯 분류 차원으로 체계화한 서베이다. 기업 사례 연구에서 반복적으로 등장하는 구현 패턴과 공통 실패 모드를 분석하여 ch05의 설계 실패 사례에 활용할 수 있다. 신뢰 프레임워크와 안전 고려 사항도 다루어 실무 팀 대상 장에 현실성을 더한다.",
    "key_claims": [
      "기업 사례 연구에서 다양한 구현 패턴이 발견되지만 조직 간 지식 공유가 거의 없어, 동일한 실패 지점이 반복적으로 재발견된다.",
      "RAG 아키텍처 분류는 적응성(단일 패스 vs. 반복), 신뢰 교정, 모달리티, 융합 메커니즘, 검색 전략 다섯 차원에서 이루어질 수 있다.",
      "RAG 시스템의 신뢰 표면(trust surface)에 대한 정식 분석이 필요하며, 현재 정량적 신뢰 평가 프레임워크는 여전히 드물다."
    ]
  },
  {
    "title": "Agentic Retrieval-Augmented Generation: A Survey on Agentic RAG",
    "authors": ["(arXiv 2501.09136
