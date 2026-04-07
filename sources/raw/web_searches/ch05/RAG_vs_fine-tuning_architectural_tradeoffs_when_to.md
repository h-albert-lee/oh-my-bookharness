# Search: RAG vs fine-tuning architectural tradeoffs when to use retrieval augmented generation

수집된 자료를 바탕으로, ch05 집필에 실질적으로 유용한 자료들을 엄선해 JSON 형식으로 정리합니다.

---

```json
[
  {
    "title": "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks",
    "authors": ["Patrick Lewis", "Ethan Perez", "Aleksandra Piktus", "Fabio Petroni", "Vladimir Karpukhin", "Naman Goyal", "Heinrich Küttler", "Mike Lewis", "Wen-tau Yih", "Tim Rocktäschel", "Sebastian Riedel", "Douwe Kiela"],
    "year": 2020,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2005.11401",
    "summary": "RAG 개념의 원본 논문으로, RAG가 왜 등장했는지를 LLM의 구조적 한계(파라메트릭 메모리의 지식 접근 제한, hallucination, 업데이트 불가)에서 도출하는 ch05의 핵심 논거로 활용할 수 있다. '파라메트릭 메모리(모델 내부 지식) + 비파라메트릭 메모리(외부 검색 인덱스)'의 결합이라는 이분법 프레임은 RAG를 아키텍처적 선택으로 설명하는 데 직접적으로 쓸 수 있다.",
    "key_claims": [
      "LLM은 파라메트릭 메모리에 지식을 저장하지만, 그 지식을 정밀하게 접근하거나 갱신하는 능력이 제한된다 — knowledge-intensive task에서 성능이 떨어지는 근본 원인",
      "RAG는 사전학습된 seq2seq 모델(파라메트릭 메모리)과 Wikipedia의 Dense Vector Index(비파라메트릭 메모리)를 결합하는 범용 fine-tuning 레시피다",
      "RAG 모델은 파라메트릭 전용 seq2seq 기준선보다 더 구체적이고, 다양하며, 사실적인 언어를 생성한다"
    ]
  },
  {
    "title": "RAG vs Fine-tuning: Pipelines, Tradeoffs, and a Case Study on Agriculture",
    "authors": ["Angels Balaguer", "et al."],
    "year": 2024,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2401.08406",
    "summary": "RAG와 파인튜닝의 트레이드오프를 실험적으로 측정한 논문으로, ch05에서 'RAG를 언제 선택해야 하는가'의 근거로 사용할 수 있다. Llama2-13B, GPT-3.5, GPT-4 등 복수의 LLM을 대상으로 두 접근법의 파이프라인과 성능을 비교하며, RAG와 파인튜닝의 누적 효과를 수치로 제시한다.",
    "key_claims": [
      "RAG는 외부 데이터로 프롬프트를 보강하고, 파인튜닝은 해당 지식을 모델 내부에 내재화한다 — 두 접근은 지식 통합 위치가 다른 아키텍처적 선택이다",
      "파인튜닝은 정확도를 약 6%p 향상시키고, RAG는 추가로 5%p를 향상시키며, 두 방법은 누적적이다",
      "두 접근의 장단점은 아직 충분히 이해되지 않았으며, 파이프라인 단계별 메트릭 설계가 필요하다"
    ]
  },
  {
    "title": "Retrieval-Augmented Generation for Large Language Models: A Survey",
    "authors": ["Yunfan Gao", "Yun Xiong", "Xinyu Gao", "Kangxiang Jia", "Jinliu Pan", "Yuxi Bi", "Yi Dai", "Jiawei Sun", "Meng Wang", "Haofen Wang"],
    "year": 2024,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2312.10997",
    "summary": "RAG 아키텍처를 Naive RAG → Advanced RAG → Modular RAG의 세 패러다임으로 분류하는 종합 서베이로, ch05에서 'RAG 각 단계가 정보 흐름 통제의 어느 지점을 담당하는지' 설명하는 구조적 지도로 활용할 수 있다. Retriever, Generator, Augmentation 세 구성 요소를 체계적으로 해부하고, 각 단계의 기술적 선택지를 제시한다.",
    "key_claims": [
      "RAG는 Naive RAG(인덱싱-검색-생성), Advanced RAG(사전/사후 검색 최적화), Modular RAG(유연한 구성)의 세 패러다임으로 진화했다",
      "LLM의 hallucination, 지식 노후화, 비투명한 추론 프로세스라는 세 가지 구조적 한계가 RAG 등장의 직접적 동기다",
      "RAG는 LLM의 내재적 파라메트릭 지식과 방대하고 동적인 외부 데이터베이스를 시너지적으로 결합한다"
    ]
  },
  {
    "title": "Retrieval-Augmented Generation: A Comprehensive Survey of Architectures, Enhancements, and Robustness Frontiers",
    "authors": ["(다수 저자)"],
    "year": 2025,
    "type": "academic_paper",
    "url": "https://arxiv.org/html/2506.00054v1",
    "summary": "RAG 시스템의 설계 패턴을 입력 측 쿼리 강화, 리트리버 측 적응, 검색 세분화 최적화의 세 범주로 분류하고, 노이즈·적대적 입력에 대한 robustness 문제까지 다룬다. ch05에서 'RAG를 잘못 설계했을 때 발생하는 실패' 섹션의 근거 자료로 특히 유용하다.",
    "key_claims": [
      "RAG 시스템의 설계 패턴은 쿼리 강화, 리트리버 적응, 검색 세분화 최적화의 세 유형으로 분류된다",
      "RAG는 종종 무관하거나 의미적으로 노이즈가 있는 문서를 통합하여 생성 품질을 저하시킨다 — 정보 흐름 통제 실패의 대표적 사례",
      "적대적으로 오염된 문서(BadRAG, TrojanRAG)가 베이스 모델을 수정하지 않고도 LLM 출력에서 특정 행동을 유발하는 시맨틱 백도어로 작동할 수 있다"
    ]
  },
  {
    "title": "RAG vs. Fine-Tuning vs. Hybrid: Choosing the Right AI Architecture",
    "authors": ["Actian 편집팀"],
    "year": 2025,
    "type": "blog_post",
    "url": "https://www.actian.com/blog/databases/should-you-use-rag-or-fine-tune-your-llm/",
    "summary": "RAG, 파인튜닝, 하이브리드 아키텍처를 비용·지연시간·업데이트 용이성 등 실무 관점에서 비교한다. Menlo Ventures 2024 보고서의 기업 채택 통계(RAG 51% vs 파인튜닝 9%)를 인용하여 ch05의 '왜 RAG가 지배적 패턴이 되었는가' 논증을 뒷받침할 수 있다.",
    "key_claims": [
      "RAG는 추론 시 외부 데이터를 끌어오고, 파인튜닝은 훈련 중 모델 가중치를 수정한다 — 이 구분은 프로덕션 시스템 설계에서는 불충분하다",
      "기업 AI 배포의 51%가 RAG를 사용하는 반면, 파인튜닝만 주로 사용하는 경우는 9%에 불과하다(Menlo Ventures 2024)",
      "RAG는 임베딩 생성·벡터 검색·컨텍스트 주입 등 여러 단계가 추론 파이프라인에 추가되어 응답 지연을 증가시킨다"
    ]
  },
  {
    "title": "2024: The State of Generative AI in the Enterprise",
    "authors": ["Menlo Ventures"],
    "year": 2024,
    "type": "industry_report",
    "url": "https://menlovc.com/2024-the-state-of-generative-ai-in-the-enterprise/",
    "summary": "600명의 미국 엔터프라이즈 리더를 대상으로 한 조사로, RAG 채택률이 전년 31%에서 51%로 급증한 반면 파인튜닝은 9%에 머물렀다는 산업 데이터를 제공한다. ch05에서 'RAG가 왜 지금 가장 널리 쓰이는 패턴인가'를 실증하는 맥락 설정 자료로 활용할 수 있다.",
    "key_claims": [
      "RAG 채택률이 1년 만에 31%에서 51%로 급증하며 엔터프라이즈 AI 설계 패턴의 지배적 방식이 되었다",
      "파인튜닝은 자주 언급되지만 실제 프로덕션 모델에서는 9%만이 사용하는 드문 선택이다",
      "에이전틱 아키텍처가 이미 전체 구현의 12%를 차지하며 RAG의 진화 방향을 보여준다"
    ]
  },
  {
    "title": "Retrieval Augmented Generation (RAG) — Architecture Pattern",
    "authors": ["IBM Think Architecture Team"],
    "year": 2023,
    "type": "documentation",
    "url": "https://www.ibm.com/think/architectures/patterns/genai-rag",
    "summary": "IBM이 RAG를 '기능'이 아니라 명시적으로 '아키텍처 패턴'으로 정의하고 있는 공식 문서다. ch05의 핵심 주장인 'RAG는 기능이 아닌 아키텍처'를 뒷받침하는 권위 있는 외부 사례로 직접 인용할 수 있으며, 주요 구성 요소와 정보 흐름을 명확히 다이어그램으로 제시한다.",
    "key_claims": [
      "RAG는 모델의 학습 데이터에 포함되지 않은 전문화된 또는 독점 주제에 대해 기반 모델이 사실적으로 올바른 출력을 생성할 수 있도록 하는 아키텍처 패턴이다",
      "RAG는 모델 자체를 수정하지 않고 외부 데이터 소스에서 검색된 관련 데이터로 사용자의 질문과 프롬프트를 보강한다",
      "RAG는 대규모 문서와 비즈니스 규칙이 있고 사용자가 권위 있는 답변을 제공하기 위해 참조해야 하는 모든 비즈니스 시나리오에 적합하다"
    ]
  },
  {
    "title": "Retrieval Augmented Generation: Keeping LLMs Relevant and Current",
    "authors": ["Ryan Donovan (Stack Overflow Blog)"],
    "year": 2023,
    "type": "blog_post",
    "url": "https://stackoverflow.blog/2023/10/18/retrieval-augmented-generation-keeping-llms-relevant-and-current/",
    "summary": "개발자 커뮤니티를 대상으로 RAG의 두 가지 핵심 동기(지식 노후화, hallucination)를 명확하게 설명하고, 오케스트레이션 레이어·검색 도구·벡터 스토어·ETL 파이프라인 등 RAG 구성 요소를 실무적으로 다룬다. ch05에서 LLM의 구조적 한계를 독자 친화적으로 설명하는 도입부 참고 자료로 활용할 수 있다.",
    "key_claims": [
      "LLM의 지식 문제는 두 가지로 귀결된다: 훈련 데이터의 만성적 노후화, 그리고 지식 공백이 있을 때 사실인 것처럼 들리는 거짓 진술을 자신 있게 생성하는 hallucination",
      "RAG는 외부 지식 저장소에서 검색된 정확하고 최신의 관련 정보에 LLM을 고정시키기 위해 정보 검색과 신중하게 설계된 시스템 프롬프트를 결합한다",
      "LLM 기반 전체 애플리케이션 아키텍처는 오케스트레이션 레이어, 검색 도구, 벡터 스토어, 데이터 소스로 구성된다"
    ]
  },
