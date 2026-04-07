# Search: RAG pipeline failure modes hallucination retrieval context construction diagnosis

수집된 자료를 충분히 확보했습니다. 이제 ch05 집필에 직접 활용할 수 있도록 정리하겠습니다.

---

아래는 조사 결과를 바탕으로 실제 존재가 확인된 자료만 JSON 형식으로 정리한 결과입니다.



Lewis et al. (2020)의 RAG 원논문은 LLM이 파라메트릭 메모리만으로는 지식 집약적 태스크에서 한계를 가지며, 세계 지식의 갱신과 출처 제공이 해결되지 않은 문제임을 명시적으로 제기합니다.

 

Barnett et al. (2024)은 세 개 도메인의 실제 케이스 스터디에서 RAG 시스템의 7가지 실패 지점을 도출하고 교훈을 정리했습니다.

 

RAGEC 논문에서는 RAG 맥락에서 할루시네이션보다 검색 오류나 청킹 문제가 더 빈번하게 발생할 수 있다고 지적하며, 이들 문제가 더 많은 주목을 받아야 한다고 주장합니다.



```json
[
  {
    "title": "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks",
    "authors": ["Patrick Lewis", "Ethan Perez", "Aleksandra Piktus", "Fabio Petroni", "Vladimir Karpukhin", "Naman Goyal", "Heinrich Küttler", "Mike Lewis", "Wen-tau Yih", "Tim Rocktäschel", "Sebastian Riedel", "Douwe Kiela"],
    "year": 2020,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2005.11401",
    "summary": "RAG 개념을 최초로 정식화한 원논문으로, LLM의 파라메트릭 메모리만으로는 지식 집약적 태스크에서 정확도가 떨어지고 세계 지식 갱신이 불가능하다는 구조적 한계를 정의한다. ch05에서 'RAG가 왜 등장했는가'를 LLM의 구조적 한계에서 도출하는 논거의 1차 출처로 활용할 수 있다. 파라메트릭 메모리(모델 가중치)와 논파라메트릭 메모리(외부 검색 인덱스)의 구분은 RAG를 아키텍처적 선택으로 설명하는 핵심 프레임이 된다.",
    "key_claims": [
      "LLM은 파라메트릭 메모리에 지식을 저장하지만, 지식 집약적 태스크에서 정확한 지식 접근 및 조작 능력이 제한된다",
      "의사결정의 출처 제공(provenance)과 세계 지식 갱신은 파라메트릭 모델만으로는 해결되지 않는 열린 문제다",
      "RAG는 파라메트릭 메모리와 논파라메트릭 메모리를 결합하여, 재훈련 없이 외부 지식을 동적으로 활용하는 아키텍처적 해법이다",
      "RAG 모델은 파라메트릭 전용 seq2seq 베이스라인보다 더 구체적이고 사실에 기반한 언어를 생성한다"
    ]
  },
  {
    "title": "Seven Failure Points When Engineering a Retrieval Augmented Generation System",
    "authors": ["Scott Barnett", "Stefanus Kurniawan", "Srikanth Thudumu", "Zach Brannelly", "Mohamed Abdelrazek"],
    "year": 2024,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2401.05856",
    "summary": "연구·교육·바이오메디컬 세 도메인의 실제 RAG 시스템 케이스 스터디에서 도출한 7가지 실패 지점을 경험 보고서 형식으로 정리한다. ch05에서 'RAG를 잘못 설계했을 때 발생하는 실패'를 구체적으로 유형화하는 데 직접 활용할 수 있다. '검증은 운영 중에만 가능하다'는 결론은 RAG를 기능이 아니라 지속적으로 진화하는 아키텍처로 봐야 한다는 주제 의식과 연결된다.",
    "key_claims": [
      "RAG 시스템의 실패는 누락된 콘텐츠, 랭킹 오류, 답변 추출 실패 등 파이프라인 각 단계에서 발생한다",
      "RAG 시스템의 검증은 설계 단계가 아니라 실제 운영 중에만 가능하다",
      "RAG 시스템의 강건성은 처음부터 설계되는 것이 아니라 시간이 지나면서 진화한다",
      "RAG 시스템은 정보 검색 시스템 고유의 한계와 LLM 의존에서 오는 한계를 동시에 가진다"
    ]
  },
  {
    "title": "Classifying and Addressing the Diversity of Errors in Retrieval-Augmented Generation Systems",
    "authors": ["(저자 정보 arXiv 페이지 확인 필요)"],
    "year": 2025,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2510.13975",
    "summary": "RAG 파이프라인에서 발생하는 오류를 청킹·검색·생성·컨텍스트 오용 등 단계별로 분류한 RAGEC 프레임워크를 제시한다. ch05에서 RAG 실패를 파이프라인 단계별로 진단하는 구조적 설명에 직접 활용할 수 있다. 특히 실제 프로덕션 수준의 RAG 아키텍처를 모델로 삼아 각 단계의 오류 유형 분포를 실증 분석했다는 점에서 설득력 있는 근거가 된다.",
    "key_claims": [
      "RAG 맥락에서 할루시네이션(E10, Fabricated Content)보다 검색 오류나 청킹 문제가 더 지배적인 오류 유형이다",
      "오류 유형의 분포는 데이터셋 특성에 따라 달라지며, 이는 RAG 진단을 도메인별로 접근해야 함을 시사한다",
      "RAGEC는 복잡하고 불투명한 RAG 파이프라인 디버깅 및 개선의 진입점을 제공한다",
      "RAG 오류의 원인은 파이프라인 단계 전반에 걸쳐 다양하며, 단일 지표로는 포착하기 어렵다"
    ]
  },
  {
    "title": "RAGXplain: From Explainable Evaluation to Actionable Guidance of RAG Pipelines",
    "authors": ["(저자 정보 arXiv 페이지 확인 필요)"],
    "year": 2025,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2505.13538",
    "summary": "RAG 파이프라인의 실패를 검색 단계 실패(누락 증거, 주제 이탈 컨텍스트)와 생성 단계 실패(할루시네이션, 근거 없는 추론)로 구분하는 '단계 인식 진단' 프레임워크를 제공한다. ch05에서 정보 흐름의 어느 지점에서 실패가 발생하는지를 설명하는 구조적 논거로 활용할 수 있다. end-to-end 집계 지표만으로는 실패 위치를 판별하기 어렵다는 실용적 함의도 강조한다.",
    "key_claims": [
      "end-to-end 점수(관련성, 충실도)는 파이프라인의 어디서, 왜 실패했는지를 좀처럼 드러내지 않는다",
      "검색 단계 실패(누락 증거, 주제 이탈 컨텍스트)와 생성 단계 실패(할루시네이션, 근거 없는 추론)는 서로를 마스킹할 수 있어 진단이 어렵다",
      "컨텍스트 구성(context construction), 검색/재랭킹, 쿼리 구성, 생성이 RAG 파이프라인의 구체적인 개선 레버로 식별된다",
      "User Input-Retrieved Context-Generated Answer-Ground Truth의 '메트릭 다이아몬드' 구조가 포괄적 진단 프레임워크가 된다"
    ]
  },
  {
    "title": "Retrieval-Augmented Generation: A Comprehensive Survey of Architectures, Enhancements, and Robustness Frontiers",
    "authors": ["Chaitanya Sharma"],
    "year": 2025,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2506.00054",
    "summary": "RAG 아키텍처를 검색기 중심, 생성기 중심, 하이브리드, 강건성 중심으로 분류한 최신 종합 서베이다. ch05에서 RAG를 단순 기능이 아닌 다양한 아키텍처적 선택지의 집합으로 제시할 때 배경 지식으로 활용할 수 있다. 검색 품질·그라운딩 충실도·파이프라인 효율성·노이즈에 대한 강건성이라는 새로운 도전들을 명시적으로 정리한다.",
    "key_claims": [
      "RAG는 파라메트릭 지식 저장의 한계(사실 불일치, 도메인 경직성)를 해결하지만, 검색 품질·그라운딩 충실도·파이프라인 효율성·노이즈 강건성이라는 새로운 과제를 도입한다",
      "RAG 아키텍처는 검색기 중심, 생성기 중심, 하이브리드, 강건성 중심의 네 가지 설계 패턴으로 분류된다",
      "검색 정밀도와 생성 유연성 사이, 효율성과 충실도 사이, 모듈성과 조율 사이의 반복적인 트레이드오프가 존재한다",
      "적응형 검색 아키텍처, 실시간 검색 통합, 다중 홉 추론을 위한 구조화 추론이 미해결 과제로 남아 있다"
    ]
  },
  {
    "title": "Common Failure Modes in RAG Systems",
    "authors": ["apxml.com (저자 미상)"],
    "year": 2024,
    "type": "blog_post",
    "url": "https://apxml.com/courses/getting-started-rag/chapter-6-evaluating-improving-rag-systems/common-failure-modes",
    "summary": "RAG 실패를 검색 실패, 생성 실패, 통합 실패의 세 범주로 나누어 각각의 원인과 영향을 설명하는 교육용 자료다. ch05에서 'RAG를 잘못 설계했을 때 발생하는 실패'를 독자에게 직관적으로 설명할 때 구조적 참고 자료로 활용할 수 있다. 실패 유형별 진단 방향을 명확히 제시하여 아키텍처 관점의 서술을 보완한다.",
    "key_claims": [
      "RAG 실패는 검색 실패(잘못된 청크 반환), 생성 실패(컨텍스트가 있어도 할루시네이션), 통합 실패(두 컴포넌트 상호작용 문제)의 세 유형으로 분류된다",
      "검색이 실패하면 생성기는 처음부터 정확한 답변을 낼 가능성이 거의 없다",
      "컨텍스트가 많을 때 LLM은 중간 정보를 놓치는 'Lost in the Middle' 현상을 보인다",
      "지식베이스 자체의 오래되거나 잘못된 정보도 RAG 실패의 주요 원인이다"
    ]
  },
  {
    "title": "Retrieval-augmented generation (RAG) failure modes and how to fix them",
    "authors": ["Snorkel AI"],
    "year": 2024,
    "type": "blog_post",
    "url": "https://snorkel.ai/blog/retrieval-augmented-generation-rag-failure-modes-and-how-to-fix-them/",
    "summary": "프로덕션 RAG 파이프라인에서 가장 흔한 실패 원인으로 잘못된 청킹 전략, 불완전한 지식베이스 커버리지, 불량 프롬프트 템플릿을
