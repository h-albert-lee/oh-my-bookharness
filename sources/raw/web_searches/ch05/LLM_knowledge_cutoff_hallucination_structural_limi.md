# Search: LLM knowledge cutoff hallucination structural limitations retrieval augmentation survey

검색 결과를 바탕으로 각 자료를 검증하고 정리하겠습니다. 실제로 존재하는 자료들만 추려 JSON 형식으로 출력합니다.

---



아래는 수집된 자료의 출처 근거입니다. Lewis et al.(2020)은 RAG가 파라메트릭·비파라메트릭 메모리를 결합한다고 제안했고, Gao et al.(2024)은 LLM의 환각·지식 노후화 문제를 RAG로 해결한다고 정리했으며, Barnett et al.(2024)는 RAG 시스템의 7가지 실패 지점을 실증적으로 도출했습니다. Modular RAG 논문(2024)은 Naive RAG → Advanced RAG → Modular RAG의 발전 계보를 체계화했고, "Dated Data" 논문(2024)은 LLM의 knowledge cutoff가 실제로 어떻게 작동하는지 추적 연구를 수행했습니다.



```json
[
  {
    "title": "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks",
    "authors": ["Patrick Lewis", "Ethan Perez", "Aleksandra Piktus", "Fabio Petroni", "Vladimir Karpukhin", "Naman Goyal", "Heinrich Küttler", "Mike Lewis", "Wen-tau Yih", "Tim Rocktäschel", "Sebastian Riedel", "Douwe Kiela"],
    "year": 2020,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2005.11401",
    "summary": "RAG의 원 논문으로, LLM이 파라메트릭 메모리(모델 가중치)만으로는 지식 집약적 과제에서 한계를 가진다는 구조적 문제를 제기하고, 비파라메트릭 외부 메모리(검색 인덱스)와의 결합을 통해 이를 해결하는 아키텍처를 처음 제안한다. ch05의 'RAG가 왜 등장했는가'를 LLM의 구조적 한계에서 도출하는 핵심 레퍼런스로 사용할 수 있다. 파라메트릭 vs. 비파라메트릭 메모리라는 개념적 이분법은 장 전체의 논리 뼈대로 활용 가능하다.",
    "key_claims": [
      "LLM은 파라메트릭 메모리에 지식을 저장하지만, 그 지식을 정확히 접근·수정하는 능력이 제한적이며 knowledge-intensive 태스크에서 성능이 뒤처진다.",
      "RAG는 사전학습된 seq2seq 모델(파라메트릭 메모리)과 밀집 벡터 인덱스(비파라메트릭 메모리)를 결합하여 더 사실적이고 다양한 언어를 생성한다.",
      "하이브리드 모델은 지식을 직접 수정·확장하고, 접근된 지식을 검사·해석할 수 있게 해준다."
    ]
  },
  {
    "title": "Retrieval-Augmented Generation for Large Language Models: A Survey",
    "authors": ["Yunfan Gao", "Yun Xiong", "Xinyu Gao", "Kangxiang Jia", "Jinliu Pan", "Yuxi Bi", "Yi Dai", "Jiawei Sun", "Meng Wang", "Haofen Wang"],
    "year": 2024,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2312.10997",
    "summary": "Naive RAG, Advanced RAG, Modular RAG의 세 단계 패러다임 발전을 체계적으로 정리한 대표적 서베이 논문으로, RAG 파이프라인의 각 구성 요소(검색·증강·생성)가 정보 흐름 통제에서 어떤 역할을 하는지 분석하는 데 직접 활용할 수 있다. ch05에서 RAG를 단순 기능이 아닌 아키텍처로 이해시키기 위한 구조 설명의 핵심 출처다. Naive RAG의 구조적 한계를 명시함으로써 Advanced/Modular 설계가 왜 필요한지 논리적 흐름을 구성할 수 있다.",
    "key_claims": [
      "LLM은 환각, 지식 노후화, 불투명한 추론 과정이라는 구조적 한계를 가지며, RAG는 외부 데이터베이스의 지식을 통합하여 이를 해결하는 유망한 해법이다.",
      "RAG 연구 패러다임은 Naive RAG → Advanced RAG → Modular RAG의 세 단계로 진화해왔으며, 각 단계는 이전 단계의 구조적 한계를 극복하기 위해 설계되었다.",
      "RAG는 검색(Retrieval), 증강(Augmentation), 생성(Generation)이라는 삼중 기반 구조를 가진다."
    ]
  },
  {
    "title": "A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions",
    "authors": ["Lei Huang", "Weijiang Yu", "Weitao Ma", "Weihong Zhong", "Zhangyin Feng", "Haotian Wang", "Qianglong Chen", "Weihua Peng", "Xiaocheng Feng", "Bing Qin", "Ting Liu"],
    "year": 2024,
    "type": "academic_paper",
    "url": "https://dl.acm.org/doi/10.1145/3703155",
    "summary": "LLM 환각의 원인을 데이터·학습·추론 단계별로 분류하고, RAG를 환각 완화의 핵심 전략 중 하나로 다룬다. ch05에서 'RAG가 왜 등장했는가'를 LLM의 구조적 한계(환각)에서 도출하는 근거 자료로 활용할 수 있다. 동시에 RAG 자체도 환각에서 자유롭지 않다는 점을 짚어 설계 실패 패턴 논의로 연결할 수 있다.",
    "key_claims": [
      "LLM 환각은 데이터(허위정보·편향), 학습(정렬 문제), 추론(디코딩 전략) 단계의 복합적 원인에서 발생한다.",
      "RAG는 환각 완화에 효과적인 전략으로 주목받지만, 현재 RAG 시스템도 내재적 한계로 인해 환각이 발생할 수 있다.",
      "환각 완화 전략은 데이터 필터링, RAG, 디코딩 개선의 세 범주로 분류된다."
    ]
  },
  {
    "title": "Seven Failure Points When Engineering a Retrieval Augmented Generation System",
    "authors": ["Scott Barnett", "Stefanus Kurniawan", "Srikanth Thudumu", "Zach Brannelly", "Mohamed Abdelrazek"],
    "year": 2024,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2401.05856",
    "summary": "연구·교육·바이오메디컬 3개 도메인 케이스 스터디를 통해 RAG 시스템이 실제 운영에서 겪는 7가지 실패 지점(콘텐츠 누락, 검색 실패, 컨텍스트 윈도우 한계, 불량 생성, 잘못된 출력 포맷, 모호한 답변, 불완전한 답변)을 실증적으로 도출한 논문이다. ch05의 'RAG를 잘못 설계했을 때 발생하는 실패' 절의 직접적 출처로 활용할 수 있다. RAG를 기능이 아닌 아키텍처로 설계해야 하는 이유를 실패 사례로 뒷받침하는 데 적합하다.",
    "key_claims": [
      "RAG 시스템은 정보검색 시스템의 내재적 한계와 LLM 의존성에서 비롯되는 고유한 실패 지점을 가진다.",
      "RAG 시스템의 유효성 검증은 운영 중에만 가능하며, 견고성은 초기 설계가 아닌 운영 과정에서 진화한다.",
      "7가지 실패 지점: 콘텐츠 누락, 검색 실패, 컨텍스트 윈도우 한계, 불량 LLM 답변, 잘못된 출력 포맷, 모호한 답변, 불완전한 답변."
    ]
  },
  {
    "title": "Hallucination Mitigation for Retrieval-Augmented Large Language Models: A Review",
    "authors": ["(MDPI Mathematics 저자진, 2025)"],
    "year": 2025,
    "type": "academic_paper",
    "url": "https://www.mdpi.com/2227-7390/13/5/856",
    "summary": "RAG의 검색 단계와 생성 단계 각각에서 환각이 발생하는 원인을 세분화하여 분석하고, 각 단계에 대응하는 완화 기법을 체계적으로 정리한다. ch05에서 RAG 각 단계가 정보 흐름 통제의 어느 지점을 담당하는지 설명할 때, 각 단계의 실패 양상과 그 원인을 구조적으로 서술하는 데 활용할 수 있다. 쿼리-생성 정렬 문제, 검색 메커니즘 한계 등을 구체적인 설계 실패 사례로 인용할 수 있다.",
    "key_claims": [
      "RAG 내 환각은 검색 단계(쿼리-생성 정렬 불일치, 검색 메커니즘 한계)와 생성 단계의 서로 다른 하위 과제에서 각각 발생한다.",
      "검색된 지식이 쿼리 의도를 충분히 충족시키지 못하면 정보 누락이나 논리적 오류로 인해 환각이 발생한다.",
      "LLM의 능력 경계는 정밀 계산, 데이터 검색, 복잡한 논리 처리의 결함에서 주로 나타난다."
    ]
  },
  {
    "title": "Modular RAG: Transforming RAG Systems into LEGO-like Reconfigurable Frameworks",
    "authors": ["Yunfan Gao", "Yun Xiong", "Meng Wang", "Haofen Wang"],
    "year": 2024,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2407.21059",
    "summary": "Naive RAG와 Advanced RAG의 구조적 한계를 분석하고, RAG를 모듈·서브모듈·오퍼레이터의 3계층 아키텍처로 재정의하는 Modular RAG 패러다임을 제안한다. ch05에서 RAG를 '기능'이 아닌 '아키텍처'로 이해해야 한다는 핵심 주장을 뒷받침하는 이론적 기반으로 활용할 수 있다. 각 모듈이 정보 흐름 통제의 어느 지점을 담당하는지를 설명하는 구조적 프레임워크를 제공한다.",
    "key_claims": [
      "Naive RAG → Advanced RAG → Modular RAG는 상속과 발전의 관계이며, Naive RAG는 복잡한 질의와 높은 변동성의 청크에서 성능이 저하된다.",
      "Modular RAG는 RAG 시스템의 유연성과 확장성을 강화하며, 사용자가 데이터 소스와 태스크 시나리오에 따라 모듈과 오퍼레이터를 유연하게 조합할 수 있다.",
      "Naive RAG의 주요 과제는 쿼리의 얕은 이해, 검색 중복 및 노이즈로, 이 과도한 노이즈 정보는 LLM이 핵심 정보를 식별하는 것을 방해하여 오류 및 환각 생성 위험을 높인다."
    ]
  },
  {
    "title": "Retrieval-Augmented Generation: A Comprehensive Survey of Architectures, Enhancements, and Robustness Frontiers",
    "authors": ["Chaitanya Sharma", "외 다수"],
    "year": 2025,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2506.00054",
    "summary": "RAG 아키텍처를 검색기 중심(retriever-centric), 생성기 중심(generator-centric), 하이브리드, 견고성 지향의 4가지 분류 체계로 종합 정리한 최신 서베이다. ch05에서 RAG의 각 아키텍처 유형이 정보
