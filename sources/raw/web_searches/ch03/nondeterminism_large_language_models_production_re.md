# Search: nondeterminism large language models production reliability system design challenges

충분한 자료를 확보했습니다. 이제 검색 결과를 바탕으로 자료를 정리하겠습니다.

---

아래는 검색 결과를 바탕으로 확인된 실존 자료들을 JSON 형식으로 정리한 것입니다.



arXiv 2408.04667: 5개 LLM에서 temperature=0 설정에도 불구하고 10회 실행 중 최대 15% 정확도 변동과 최고-최저 간 최대 70% 격차가 관찰되었으며, 이 비결정성은 컴퓨팅 자원의 효율적 활용을 위한 입력 버퍼 혼합과 관련되어 있어 쉽게 해결되지 않을 것이라고 밝혔습니다.





arXiv 2511.19933: 프로덕션 환경에서 LLM의 실패 패턴이 기존 ML 모델과 근본적으로 다르다는 전제 하에 15가지 은닉 실패 모드(추론 드리프트, 도구 오호출, 버전 드리프트 등)를 분류하고, LLM 신뢰성을 순수 모델 중심이 아닌 시스템 엔지니어링 문제로 프레이밍합니다.





arXiv 2503.13657: 멀티에이전트 LLM 시스템은 벤치마크에서의 성능 향상이 미미하며, MAST 분류체계를 통해 14가지 실패 모드를 (i) 시스템 설계 실패 (ii) 에이전트 간 정렬 실패 (iii) 태스크 검증 실패 세 범주로 분류했습니다.





Chip Huyen의 2023년 블로그: "LLM으로 멋진 것을 만들기는 쉽지만, 프로덕션 준비 상태로 만들기는 매우 어렵다"고 진단하며, LLM 한계는 자연어의 모호성과 프롬프트 엔지니어링의 공학적 엄격성 부족으로 악화된다고 지적합니다.





arXiv 2509.14404: 프롬프트 설계가 대부분 경험적이며 작은 실수가 연쇄 장애로 이어질 수 있다는 문제를 체계화하여, 프롬프트 결함을 6개 차원으로 분류한 최초의 체계적 분류체계를 제시합니다.





The Architect's Guide to LLM System Design 블로그: "PoC에서 견고한 프로덕션급 애플리케이션으로 이동하면 새로운 엔지니어링 과제가 드러난다. LLM으로 구축하는 것은 근본적으로 시스템 설계 분야이지 단순히 프롬프트 작성 연습이 아니다"라고 명시합니다.



---

```json
[
  {
    "title": "Non-Determinism of 'Deterministic' LLM Settings",
    "authors": ["Berk Atil", "Alexa Chittams", "Liseng Fu", "Ferhan Ture", "Lixinyu Xu", "Breck Baldwin", "et al."],
    "year": 2024,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2408.04667",
    "summary": "5개 LLM에서 temperature=0 설정에도 10회 실행 간 최대 15% 정확도 변동이 관찰된다는 실증 연구. '모델을 결정론적으로 설정하면 된다'는 통념을 논파하는 핵심 증거로 활용 가능. 이 비결정성이 모델 자체가 아니라 인프라 최적화(continuous batching, prefix caching 등)에서 비롯된다는 점은 '시스템 문제'라는 장의 테제를 직접 뒷받침한다.",
    "key_claims": [
      "temperature=0 설정에도 불구하고 동일 입력·동일 설정에서 최대 15% 정확도 변동, 최고-최저 성능 간 최대 70% 격차가 발생한다.",
      "비결정성은 컴퓨팅 자원 효율화를 위한 입력 버퍼 혼합(co-mingled input buffers) 등 인프라 수준의 구조적 원인에서 비롯되며, 단기간에 해결되기 어렵다.",
      "모든 LLM은 일관된 반복 정확도를 보장하지 못하며, 단일 벤치마크 숫자 보고의 신뢰성이 근본적으로 제한된다."
    ]
  },
  {
    "title": "Failure Modes in LLM Systems: A System-Level Taxonomy for Reliable AI Applications",
    "authors": ["Vaishali Vinay"],
    "year": 2025,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2511.19933",
    "summary": "프로덕션 LLM의 실패가 모델 중심이 아닌 시스템 엔지니어링 문제임을 공식화한 핵심 논문. 추론 드리프트, 컨텍스트 경계 열화, 도구 오호출, 버전 드리프트 등 15가지 은닉 실패 모드를 분류하며, 기존 벤치마크가 안정성·재현성·워크플로 통합을 측정하지 못한다고 비판한다. 3장의 '시스템 설계 문제' 논증을 학술적으로 정당화하는 직접 근거로 사용 가능.",
    "key_claims": [
      "LLM의 프로덕션 실패 패턴은 기존 ML 모델과 근본적으로 다르며, 현재 벤치마크는 안정성·재현성·드리프트·워크플로 통합에 대한 인사이트를 거의 제공하지 못한다.",
      "많은 배포 실패가 환각이 아니라 자연어 출력과 소프트웨어 요구사항 간의 의미적 불일치(semantic mismatch)에서 비롯된다.",
      "LLM 신뢰성을 순수 모델 중심 문제가 아닌 시스템 엔지니어링 문제로 프레이밍해야 한다."
    ]
  },
  {
    "title": "Why Do Multi-Agent LLM Systems Fail?",
    "authors": ["Mert Cemri", "Melissa Z. Pan", "Shuyi Yang", "Lakshya A. Agrawal", "Bhavya Chopra", "Rishabh Tiwari", "Kurt Keutzer", "Ion Stoica", "et al."],
    "year": 2025,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2503.13657",
    "summary": "7개 멀티에이전트 프레임워크의 1,600개 이상 실행 트레이스를 분석해 14가지 실패 모드를 분류한 NeurIPS 2025 논문. 실패 원인의 상당수가 개별 모델 성능이 아니라 시스템 설계 결함(specification failure)과 에이전트 간 정렬 실패에 있음을 보인다. PART 2에서 다룰 에이전트·파이프라인 설계 필요성의 선행 동기부여 자료로 활용 가능.",
    "key_claims": [
      "멀티에이전트 시스템의 성능 개선은 더 강력한 모델보다 더 정교한 시스템 설계와 아키텍처 개선에서 나온다.",
      "실패 모드의 주요 범주는 (i) 시스템 설계 실패, (ii) 에이전트 간 정렬 실패, (iii) 태스크 검증·종료 실패로, 모두 모델 자체보다 구조적 원인을 가진다.",
      "단일 에이전트 프레임워크 대비 멀티에이전트 시스템의 벤치마크 성능 향상이 미미하며, 이는 아키텍처 설계 문제임을 시사한다."
    ]
  },
  {
    "title": "Defeating Nondeterminism in LLM Inference",
    "authors": ["Horace He", "Thinking Machines Lab"],
    "year": 2025,
    "type": "blog_post",
    "url": "https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/",
    "summary": "LLM 비결정성의 진짜 원인이 GPU 동시 실행이나 부동소수점 비결합성이 아니라 동적 배칭(dynamic batching)으로 인한 배치 크기 변동에 있음을 밝힌 Thinking Machines Lab(Mira Murati 창업)의 첫 연구 블로그. 비결정성을 '모델의 본질적 특성'이 아닌 '수정 가능한 엔지니어링 버그'로 재프레이밍한다는 점에서, '모델 탓'이라는 귀인이 왜 구조적으로 틀린지를 설명하는 강력한 사례로 활용 가능.",
    "key_claims": [
      "프로덕션 LLM 서버의 비결정성은 모델 자체나 GPU 경쟁 조건이 아니라 동적 배칭에 의한 배치 크기 변동이라는 시스템 수준의 엔지니어링 원인에서 비롯된다.",
      "LLM 비결정성은 '어차피 확률적이다'는 체념적 관점이 숨기고 있는 수정 가능한 엔지니어링 결함이다.",
      "배치 불변 커널(batch-invariant kernels) 적용으로 동적 배칭 하에서도 비트 수준 동일 재현이 가능하며, LMSYS SGLang이 이를 채택했다."
    ]
  },
  {
    "title": "Building LLM Applications for Production",
    "authors": ["Chip Huyen"],
    "year": 2023,
    "type": "blog_post",
    "url": "https://huyenchip.com/2023/04/11/llm-engineering.html",
    "summary": "LLM을 프로덕션에 적용할 때 마주치는 핵심 과제(프롬프트 모호성, 비결정성, 비용·지연, 테스트, 태스크 조합 등)를 체계적으로 정리한 가장 널리 인용되는 실무 참고 자료. 'LLM으로 멋진 것을 만들기는 쉽지만 프로덕션 준비 상태로 만들기는 매우 어렵다'는 핵심 진단은 3장의 논증을 뒷받침하는 선언적 인용구로 활용 가능.",
    "key_claims": [
      "LLM 한계는 자연어의 모호성과 프롬프트 엔지니어링의 공학적 엄격성 부족으로 인해 증폭된다.",
      "프롬프트 조건이 변경되면 코드처럼 실행은 되지만 매우 다른 출력을 낼 수 있어, 기존 소프트웨어 테스트 방법론이 적용되지 않는다.",
      "에이전트의 신뢰성을 위해서는 개별 태스크를 조합 전에 독립적으로 구축·테스트할 수 있어야 하며, 이는 시스템 설계 문제다."
    ]
  },
  {
    "title": "A Taxonomy of Prompt Defects in LLM Systems",
    "authors": ["Haoye Tian", "Chong Wang", "BoYang Yang", "Lyuye Zhang", "Yang Liu"],
    "year": 2025,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2509.14404",
    "summary": "프롬프트가 LLM의 사실상의 프로그래밍 인터페이스임에도 설계가 대부분 경험적이며 작은 실수가 연쇄 장애로 이어진다는 점을 최초로 체계화한 논문. '프롬프트를 개선하면 된다'는 통념에 반박하며, 프롬프트 결함이 6개 차원의 구조적 원인을 가진다는 것을 소프트웨어 엔지니어링 원칙으로 분석한다. '프롬프트 개선으로도 해결되지 않는 이유'를 설명하는 데 직접 활용
