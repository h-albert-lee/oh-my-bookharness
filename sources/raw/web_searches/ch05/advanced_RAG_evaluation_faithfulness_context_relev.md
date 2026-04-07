# Search: advanced RAG evaluation faithfulness context relevance retrieval quality metrics RAGAS

모든 검색 결과를 종합하여 아래와 같이 정리하였습니다.

---

## 조사 결과 및 출처 요약

아래는 각 자료의 핵심 내용과 ch05 집필에 어떻게 활용할 수 있는지에 대한 인용 근거입니다.

---

### 1. RAGAS 논문 (핵심 자료)



RAG 아키텍처를 평가하는 것은 여러 차원을 고려해야 하기 때문에 어렵다. 검색 시스템이 관련성 있고 집중된 컨텍스트 구절을 식별하는 능력, LLM이 이 구절을 충실하게 활용하는 능력, 그리고 생성 자체의 품질이 그 차원이다. RAGAS는 **ground truth 인간 어노테이션에 의존하지 않고** 이러한 다양한 차원을 평가할 수 있는 메트릭 집합을 제시한다.





Faithfulness는 답변이 주어진 컨텍스트에 근거해야 한다는 개념으로, 환각을 방지하고 검색된 컨텍스트가 생성된 답변의 정당성으로 작동할 수 있게 한다.





Context Relevance는 평가하기 가장 어려운 품질 차원으로 밝혀졌다. ChatGPT가 특히 긴 컨텍스트에서 핵심 문장을 선택하는 데 어려움을 겪는다는 점이 관찰되었다.



---

### 2. ARES 논문 (비교 자료)



ARES는 RAG 시스템을 Context Relevance, Answer Faithfulness, Answer Relevance 차원에서 평가하는 자동화 시스템이다. 자체적으로 합성 훈련 데이터를 생성하고, 경량 LM 판사(judge)를 파인튜닝해 개별 RAG 구성 요소의 품질을 평가하며, 예측 오류를 완화하기 위해 소량의 인간 어노테이션 데이터를 활용한다.





ARES는 Context Relevance 평가에서 RAGAS를 최대 59.3 퍼센트 포인트 능가하는 성능을 보였다.



---

### 3. Gao et al. RAG Survey (아키텍처 분류 자료)



이 논문은 Naive RAG, Advanced RAG, Modular RAG로 이어지는 RAG 패러다임의 발전을 상세히 검토하고, 검색·생성·증강 기법으로 구성된 RAG 프레임워크의 삼각 기반을 면밀히 분석한다.





Naive RAG는 검색, 생성, 증강의 세 핵심 영역에서 상당한 도전에 직면한다. 검색 품질 면에서 낮은 정밀도는 검색된 청크의 불일치를 유발하고 환각이나 mid-air drop 같은 문제를 일으킨다. 낮은 재현율은 관련 청크를 모두 검색하지 못해 LLM이 포괄적인 응답을 구성하는 능력을 저해한다.



---

### 4. RAG Evaluation Survey (Yu et al., 2024)



RAG 시스템 평가는 하이브리드 구조와 동적 지식 소스에 대한 의존성 때문에 고유한 도전을 제기한다. 이를 이해하기 위해 Auepora(A Unified Evaluation Process of RAG)를 수행하며, 현재 RAG 벤치마크 내에서 관련성(Relevance), 정확성(Accuracy), 충실도(Faithfulness) 등 검색 및 생성 구성 요소의 정량적 메트릭을 검토하고 비교한다.



---

### 5. RAG 실패 패턴 (블로그/실무 자료)



검색 품질 실패는 모델이 질문에 맞지 않는 관련 없거나 구식이거나 부정확한 문서를 충실하게 요약할 때 발생한다. 출력물은 실제 문서에 근거하기 때문에 권위 있어 보인다. 이는 표준적인 환각과는 다른 실패 모드다. 환각은 모델이 아무것도 없는 상태에서 정보를 조작할 때 발생하지만, 검색 품질 실패는 모델이 질문에 맞지 않는 문서를 충실하게 요약할 때 발생한다.





RAG는 이제 문서, 인용, 컨텍스트를 손에 들고 있는 사람처럼 말하는 모델의 어조 때문에 답변을 더 안전하게 보이게 만드는 경우가 많다. 그러나 "정보에 접근할 수 있다"는 것이 "올바른 정보를 올바르게 사용했다"는 것과 같지 않다.



---

이제 요청하신 JSON 형식으로 출력합니다:

```json
[
  {
    "title": "RAGAS: Automated Evaluation of Retrieval Augmented Generation",
    "authors": ["Shahul Es", "Jithin James", "Luis Espinosa-Anke", "Steven Schockaert"],
    "year": 2024,
    "type": "academic_paper",
    "url": "https://aclanthology.org/2024.eacl-demo.16/",
    "summary": "RAG 평가의 핵심 프레임워크 논문으로, Faithfulness·Answer Relevance·Context Relevance 세 차원을 ground truth 없이 자동 평가하는 방법론을 제시한다. ch05에서 RAG의 각 구성 요소(검색기, 생성기)가 '정보 흐름 통제'의 어느 지점을 담당하는지 설명할 때, 평가 메트릭이 그 지점을 어떻게 진단하는지를 보여주는 근거 자료로 활용할 수 있다. 또한 '잘못 설계된 RAG의 실패'를 수치로 드러내는 방법의 실증 사례로도 적합하다.",
    "key_claims": [
      "RAG 평가는 검색 시스템의 관련성, LLM의 충실도(Faithfulness), 생성 품질이라는 세 차원을 독립적으로 측정해야 한다",
      "ground truth 인간 어노테이션 없이도 reference-free 평가가 가능하며, 이는 RAG 개발 사이클을 가속한다",
      "Context Relevance가 세 메트릭 중 자동 평가하기 가장 어려운 차원으로, 긴 컨텍스트에서 핵심 문장 선택이 특히 어렵다"
    ]
  },
  {
    "title": "RAGAS: Automated Evaluation of Retrieval Augmented Generation (arXiv preprint)",
    "authors": ["Shahul Es", "Jithin James", "Luis Espinosa-Anke", "Steven Schockaert"],
    "year": 2023,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2309.15217",
    "summary": "EACL 2024 발표 논문의 arXiv 원본으로, 세부 수식과 WikiEval 데이터셋 구성 방법이 포함되어 있다. Faithfulness 스코어 공식(= 컨텍스트에 의해 지지되는 클레임 수 / 전체 클레임 수)과 평가 실험 결과를 직접 인용할 때 이 버전을 참조한다. ch05의 '실패를 수치로 진단한다'는 논점의 기술적 뒷받침 자료로 적합하다.",
    "key_claims": [
      "Faithfulness는 생성된 답변이 검색된 컨텍스트에 근거하는지를 측정하여 환각을 방지하는 핵심 메트릭이다",
      "Answer Relevance는 생성된 답변이 실제 질문을 직접적으로 다루는지를 측정한다",
      "RAGAS 메트릭은 두 베이스라인(GPT Score 등)보다 인간 판단과 훨씬 더 일치하며, 특히 Faithfulness에서 높은 정확도를 보인다"
    ]
  },
  {
    "title": "ARES: An Automated Evaluation Framework for Retrieval-Augmented Generation Systems",
    "authors": ["Jon Saad-Falcon", "Omar Khattab", "Christopher Potts", "Matei Zaharia"],
    "year": 2023,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2311.09476",
    "summary": "RAGAS의 대안적 접근으로, 합성 훈련 데이터로 파인튜닝된 경량 LM 판사(judge)를 사용해 통계적 신뢰구간과 함께 RAG를 평가한다. ch05에서 RAG 평가 방법론을 비교할 때 'LLM-as-judge' 방식과 '파인튜닝된 분류기' 방식의 트레이드오프를 설명하는 비교 사례로 활용할 수 있다. 도메인 전환(domain shift) 상황에서도 평가 robustness를 유지한다는 점은 RAG 아키텍처의 일반화 가능성 논의에 유용하다.",
    "key_claims": [
      "합성 훈련 데이터를 자체 생성하여 파인튜닝된 경량 LM 판사로 Context Relevance, Answer Faithfulness, Answer Relevance를 평가한다",
      "소량의 인간 어노테이션(수백 개)으로 Context Relevance에서 RAGAS를 최대 59.3 퍼센트 포인트 능가한다",
      "도메인이 바뀌어도(쿼리 및 문서 유형 변경) 판사의 평가 정확도가 유지된다"
    ]
  },
  {
    "title": "Retrieval-Augmented Generation for Large Language Models: A Survey",
    "authors": ["Yunfan Gao", "Yun Xiong", "Xinyu Gao", "Kangxiang Jia", "Jinliu Pan", "Yuxi Bi", "Yi Dai", "Jiawei Sun", "Meng Wang", "Haofen Wang"],
    "year": 2024,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2312.10997",
    "summary": "RAG 패러다임을 Naive RAG → Advanced RAG → Modular RAG 세 단계로 분류하고, 각 단계의 구조적 한계와 발전 방향을 체계적으로 설명하는 가장 널리 인용되는 서베이 논문이다. ch05에서 'RAG가 왜 등장했는가'와 '각 단계가 정보 흐름 통제의 어느 지점을 담당하는가'를 구조적으로 설명하는 핵심 참고 문헌으로, 특히 Naive RAG의 실패(낮은 정밀도, 낮은 재현율, 구식 정보)를 구체적으로 기술한 부분을 활용할 수 있다.",
    "key_claims": [
      "Naive RAG는 검색 정밀도 부족, 환각, 컨텍스트 통합 실패라는 세 가지 핵심 문제를 가지며, Advanced RAG와 Modular RAG는 이에 대한 구조적 응답이다",
      "RAG는 LLM의 파라메트릭 지식과 방대한 외부 데이터베이스를 시너지적으로 결합하여 환각 감소, 최신 정보 접근, 도메인 특화를 가능하게 한다",
      "Modular RAG는 반복적·적응적 검색을 포함한 유연한 구조로, 파인튜닝 및 강화학습과 통합이 가능하다"
    ]
  },
  {
    "title": "Evaluation of Retrieval-Augmented Generation: A Survey",
    "authors": ["Hao Yu", "Aoran Gan", "Kai Zhang", "Shiwei Tong", "Qi Liu", "Zhaofeng Liu"],
    "year": 2024,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2405.07437",
    "summary": "RAG 평가 방법론과 벤치마크를
