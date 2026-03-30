# Search: LLM nondeterminism temperature zero floating point reproducibility empirical study

검색 결과를 충분히 수집했습니다. 이제 실제로 존재하는 자료들을 검증된 정보만으로 JSON 형식으로 정리하겠습니다.

---

아래는 검색을 통해 확인된 자료들의 서지 정보 및 요약입니다. 각 자료의 실존 여부는 검색 결과로 직접 확인하였습니다.



핵심 맥락: LLM의 비결정성 문제는 "사용자가 결정론적이라고 가정하는 설정에서조차 LLM 출력이 실질적으로 불안정하다"는 것으로, 이는 "강건한 엔지니어링이 기대되는 영역에서 지나치게 큰 불확실성"을 야기한다는 것이 실증적으로 밝혀지고 있습니다.



---

```json
[
  {
    "title": "Non-Determinism of \"Deterministic\" LLM Settings",
    "authors": [
      "Berk Atil",
      "Sarp Aykent",
      "Alexa Chittams",
      "Lisheng Fu",
      "Rebecca J. Passonneau",
      "Evan Radcliffe",
      "Guru Rajan Rajagopal",
      "Adam Sloan",
      "Tomasz Tudrej",
      "Ferhan Ture",
      "et al."
    ],
    "year": 2024,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2408.04667",
    "summary": "temperature=0으로 설정해도 LLM 출력이 비결정적임을 대규모 벤치마크(MMLU, BIG-Bench Hard)에서 실증적으로 보여주는 논문. 챕터 1에서 '비결정성은 개발자의 착각에서 비롯된다'는 주장을 뒷받침하는 가장 직접적인 실증 근거로 활용 가능. 데모 단계에서는 드러나지 않다가 운영 단계에서 발현되는 시스템 불안정성의 구조적 원인을 설명하는 데 유효하다.",
    "key_claims": [
      "temperature=0을 설정해도 모델은 결정론적으로 동작하지 않으며, 동일 입력에 대해 실행마다 다른 출력이 나온다.",
      "불안정성의 정도는 모델마다, 설정마다, 태스크마다 다르게 나타나며, 이는 벤치마크 순위 자체의 신뢰성을 위협한다.",
      "현재 LLM 성능 평가에서 단일 실행 결과만 보고하는 관행은 이 분산을 무시하는 것으로, 측정 자체의 타당성을 떨어뜨린다."
    ]
  },
  {
    "title": "An Empirical Study of the Non-Determinism of ChatGPT in Code Generation",
    "authors": [
      "Shuyin Ouyang",
      "Jie M. Zhang",
      "Mark Harman",
      "Meng Wang"
    ],
    "year": 2025,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2308.02828",
    "summary": "코드 생성 태스크에서 ChatGPT의 비결정성을 829개 문제로 정량 측정한 최초의 체계적 실증 연구. 챕터 1에서 '같은 프롬프트, 다른 결과'라는 현상이 단순한 인상이 아닌 측정 가능한 공학적 현실임을 독자에게 납득시키는 구체적 수치 근거로 활용할 수 있다. LLM이 기존 소프트웨어와 본질적으로 다른 이유—같은 입력에 같은 출력을 보장하지 못함—를 실증적으로 보여준다.",
    "key_claims": [
      "ChatGPT는 동일 프롬프트에 대해 기본 설정(temperature=1)에서 코딩 태스크의 75.76%(CodeContests), 51.00%(APPS), 47.56%(HumanEval) 비율로 단 하나의 동일한 출력도 내지 못한다.",
      "temperature=0으로 설정해도 코드 생성에서 결정성은 보장되지 않으며, 단지 비결정성이 줄어들 뿐이다.",
      "비결정성은 생성 코드의 정확성과 일관성에 영향을 주고, 개발자의 LLM 신뢰를 훼손하며, LLM 기반 연구의 재현성을 낮춘다."
    ]
  },
  {
    "title": "Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference",
    "authors": [
      "Jiayi Yuan",
      "et al."
    ],
    "year": 2025,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2506.09501",
    "summary": "부동소수점 수치 정밀도(FP32/FP16/BF16)와 하드웨어 설정(GPU 종류, 배치 크기, 텐서 병렬 크기)이 LLM 출력 재현성에 미치는 영향을 최초로 체계적으로 규명한 NeurIPS 2025 Oral 논문. 챕터 1에서 비결정성의 '보이지 않는 원인'—개발자가 통제할 수 없는 인프라 변수—을 설명하는 데 핵심 레퍼런스로 쓸 수 있다. '시스템 부재'로서의 비결정성 문제를 기술적으로 뒷받침한다.",
    "key_claims": [
      "배치 크기, GPU 수, GPU 버전 등 시스템 설정 변경만으로도 LLM 출력이 유의미하게 달라지며, BF16 그리디 디코딩에서 추론 모델은 정확도가 최대 9%까지 변동할 수 있다.",
      "비결정성의 근본 원인은 제한된 수치 정밀도 하에서 부동소수점 연산의 비결합성(non-associativity)에 있다.",
      "FP32 정밀도 사용이 재현성을 크게 향상시키지만, 대부분의 평가 관행은 이를 무시하고 있어 잘못된 결론을 유발할 수 있다."
    ]
  },
  {
    "title": "Beyond Reproducibility: Token Probabilities Expose Large Language Model Nondeterminism",
    "authors": [
      "Tairan Fu",
      "Gonzalo Martínez",
      "Javier Conde",
      "Carlos Arriaga-Prieto",
      "et al."
    ],
    "year": 2026,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2601.06118",
    "summary": "생성 텍스트가 아닌 토큰 확률 분포 수준에서 LLM 비결정성을 분석한 논문으로, 비결정성의 영향이 텍스트 출력 불일치 이전에 이미 확률값 층위에서 발생함을 보여준다. 챕터 1에서 비결정성이 단순한 '글자 차이' 문제가 아니라 모델 내부의 수치 불안정성에서 기인하는 구조적 문제임을 설명하는 데 활용할 수 있다.",
    "key_claims": [
      "temperature=0과 고정 시드를 사용해도 GPU 위에서 LLM 실행은 비결정론적 결과를 낸다. 이는 부동소수점 연산의 유한 정밀도 효과 때문이며, 연산 순서는 GPU에서 동시에 실행되는 프로세스에 따라 달라진다.",
      "비결정성의 영향은 토큰 확률이 0.1~0.9 구간에 있을 때 가장 크며, 단일 추론 실행의 토큰 확률 분포를 분석함으로써 반복 실행 없이 비결정성 영향을 추정할 수 있다.",
      "비결정성은 재현성 문제를 넘어 보안·감사 측면의 함의도 있다. LLM 공급자가 모델을 낮은 비용·낮은 정밀도 버전으로 교체했는지를 출력 비교로 탐지하는 데 악용될 수 있다."
    ]
  },
  {
    "title": "Defeating Nondeterminism in LLM Inference",
    "authors": [
      "Horace He",
      "Thinking Machines Lab"
    ],
    "year": 2025,
    "type": "blog_post",
    "url": "https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/",
    "summary": "LLM 비결정성의 통념('부동소수점 + GPU 동시성')을 반박하고, 진짜 원인이 동적 배칭으로 인한 배치 비불변성(batch invariance 결여)임을 실험적으로 밝혀낸 연구 블로그 포스트. 챕터 1에서 '우리가 결정론적이라고 믿었던 것들이 실제로는 그렇지 않다'는 인식 전환의 가장 생생한 사례로 활용할 수 있다. 동일 프롬프트 1,000회 실행에서 80가지 다른 출력이 나오는 실험 결과는 독자 설득력이 매우 높다.",
    "key_claims": [
      "LLM 비결정성의 주된 원인은 GPU 동시성이나 부동소수점 비결합성 자체가 아니라, 동적 배칭(dynamic batching)으로 인해 배치 크기가 달라질 때 커널의 수치 결과가 변하는 배치 비불변성(batch non-invariance)이다.",
      "동일 프롬프트를 temperature=0으로 1,000회 실행했을 때 80가지 고유한 출력이 나왔으며, 가장 흔한 응답도 전체의 7.8%에 불과했다.",
      "배치 불변 커널(batch-invariant kernels)을 설계하면 동적 배칭 환경에서도 완전한 결정론적 추론이 가능하며, 이는 비결정성이 피할 수 없는 한계가 아니라 공학적으로 해결 가능한 문제임을 시사한다."
    ]
  },
  {
    "title": "Does Temperature 0 Guarantee Deterministic LLM Outputs?",
    "authors": [
      "Vincent Schmalbach"
    ],
    "year": 2025,
    "type": "blog_post",
    "url": "https://www.vincentschmalbach.com/does-temperature-0-guarantee-deterministic-llm-outputs/",
    "summary": "temperature=0이 결정론적 출력을 보장하지 못하는 이유를 MoE 아키텍처, 부동소수점 비결합성, GPU 병렬성, 정밀도 포맷 등 레이어별로 체계적으로 설명한 기술 블로그. 챕터 1에서 비결정성의 원인을 독자가 직관적으로 이해할 수 있도록 설명하는 보조 자료로 활용하기 좋다. OpenAI, Anthropic, Google의 공식 문서를 인용해 어떤 주요 제공자도 결정론적 출력을 보장하지 않음을 확인한다.",
    "key_claims": [
      "어떤 주요 LLM 제공자(OpenAI, Anthropic, Google)도 현재 생성 모델에 대해 완전히 결정론적 출력을 약속하지 않는다.",
      "MoE(Mixture-of-Experts) 아키텍처에서는 배치 처리 시 다른 사용자의 토큰과 전문가 자원을 경쟁하게 되어 추가적인 비결정성이 발생한다.",
      "딥러닝 프레임워크는 성능을 위해 비결정적 알고리즘을 기본으로 사용하며, 결정론적 알고리즘 강제 적용은 성능 비용을 수반한다."
    ]
  },
  {
    "title": "Why is deterministic output from LLMs nearly impossible?",
    "authors": [
      "Unstract Team"
    ],
    "year": 2025,
    "type": "blog_post",
    "url": "https://unstract.com/blog/understanding-why-deterministic-output-from-llms-is-nearly-impossible/",
    "summary": "실제 프로덕션 LLM 파이프라인(비정형 문서 구조화 추출)을 구축하는 실무자 관점에서 비결정성 문제를 다루는 글. 챕터 1에서 '데모에서는 잘 됐는데 운영에서 무너지는' 패턴의 구체적인 맥락과, OpenAI·Anthropic
