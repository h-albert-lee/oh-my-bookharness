# Search: LLM evaluation vs testing rubric-based scoring probabilistic outputs machine learning

검색 결과를 종합하여 ch02 집필에 참고할 자료를 정리합니다. 각 자료에 대한 내용을 확인하고 실제로 존재하는 자료만 포함하여 JSON 형식으로 출력합니다.

---

아래는 검색 결과를 바탕으로 확인된 자료들입니다. 각 항목이 ch02("AI 시스템은 왜 기존 소프트웨어와 다른가")의 논증 — TDD→EDD 전환, 결정론 vs. 확률론, 루브릭 기반 평가의 필요성 — 에 어떻게 기여하는지를 중심으로 정리했습니다.

---



LLM 소프트웨어는 전통적인 결정론적 소프트웨어와 근본적으로 다릅니다. 전통적 테스팅은 결정론적 오라클(oracle)에 의존하지만, LLM의 확률적 특성이 이 가정에 도전합니다. LLM은 모델 선택, 설정, 입력의 구문·의미 수준 변동으로 인해 근본적인 예측 불가능성을 보이며, 기존 테스팅 방법은 이를 감당하지 못합니다.





TDD·BDD는 미리 정의된 테스트와 고정된 요구사항에 의존하는 반면, EDD는 실시간 피드백·적응형 평가·배포 후 모니터링을 통합합니다. 고전적 소프트웨어 방법론은 결정론적 시스템에 효과적이지만, 오픈엔디드·적응형 맥락에서 작동하는 LLM 에이전트에는 본질적으로 적합하지 않습니다.



```json
[
  {
    "title": "Evaluation-Driven Development and Operations of LLM Agents: A Process Model and Reference Architecture",
    "authors": ["(저자 미상, arXiv 2411.13768)"],
    "year": 2025,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2411.13768",
    "summary": "TDD/BDD가 왜 LLM 에이전트에 적용될 수 없는지를 구조적으로 논증하며, EDD(EDDOps)를 대안 방법론으로 공식화한다. ch02의 핵심 주장인 '결정론적 방법론의 무력화'와 'EDD 도입 선언'에 직접적인 이론적 근거를 제공한다. TDD/BDD와 EDDOps를 비교한 표(Table 1)는 장 내 도식 자료로도 활용 가능하다.",
    "key_claims": [
      "TDD/BDD는 사전 정의된 테스트와 결정론적 결과를 가정하지만, LLM 에이전트는 비결정론적 행동과 배포 후 진화를 특성으로 가지므로 이 방법론들이 본질적으로 부적합하다.",
      "EDD(평가 주도 개발)는 개발과 운영 전 생애주기에 걸쳐 지속적 평가를 내장함으로써, 평가를 사후 진단 도구에서 능동적 적응 메커니즘으로 전환한다.",
      "오픈엔디드·동적 맥락에서 LLM 에이전트를 운영할 때는 정적 검증(static validation)이 불충분하며, 실시간 피드백과 사후 분석을 결합한 폐쇄 피드백 루프가 필요하다."
    ]
  },
  {
    "title": "Challenges in Testing Large Language Model Based Software: A Faceted Taxonomy",
    "authors": ["(저자 미상, arXiv 2503.00481)"],
    "year": 2025,
    "type": "academic_paper",
    "url": "https://arxiv.org/html/2503.00481v1",
    "summary": "LLM 기반 소프트웨어 테스팅의 어려움을 4차원 분류 체계(소프트웨어 대상·목표·오라클·입력)로 체계화한 논문. ch02에서 '기존 테스팅 방법론이 왜 무력화되는가'를 원리 수준에서 설명하는 핵심 근거로 활용 가능하다. 특히 Atomic Oracle과 Aggregated Oracle의 구분, 프롬프트 변동이 모델 응답을 역전시킨다는 실험적 증거가 유용하다.",
    "key_claims": [
      "전통적 소프트웨어 테스팅은 결정론적 오라클에 의존하지만, LLM의 확률적 특성이 이 가정을 근본적으로 무너뜨리며 기존 패러다임들(결정론적, 확률론적, ML 특화)조차 LLM의 다층적 복잡성을 다루지 못한다.",
      "미묘한 프롬프트 변동이 고신뢰 설정에서도 모델 응답을 역전시킬 수 있으며, temperature=0 설정에서도 반복 쿼리가 불일치 결과를 낳는다.",
      "ML 테스팅은 패러다임 전환이 필요하며, LLM에서 변동성(variation)을 '1급 관심사'로 취급하는 전문 방법론이 요구된다."
    ]
  },
  {
    "title": "Rethinking Testing for LLM Applications: Characteristics, Challenges, and a Lightweight Interaction Protocol",
    "authors": ["Wei Ma", "Yixiao Yang", "Qiang Hu", "Shi Ying", "Zhi Jin", "Bo Du", "Zhenchang Xing", "Tianlin Li", "Junjie Shi", "Yang Liu", "Linxiao Jiang"],
    "year": 2025,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2508.20737",
    "summary": "LLM 애플리케이션을 세 레이어(System Shell / Prompt Orchestration / LLM Inference Core)로 분해하고, 각 레이어에서 전통적 테스팅 기법의 적용 가능성을 분석한 논문. ch02에서 'AI 시스템이 기존 소프트웨어와 구조적으로 어떻게 다른가'를 레이어별로 논증하는 데 활용할 수 있으며, 추론 코어 레이어에서 패러다임 전환이 불가피함을 보여준다.",
    "key_claims": [
      "LLM 애플리케이션의 비결정론·역동성·맥락 의존성은 품질 보증에 근본적 도전을 제기하며, 전통적 테스팅은 Shell 레이어에서만 직접 적용 가능하고 추론 코어에서는 패러다임 전환이 필수적이다.",
      "LLM 애플리케이션은 결정론적 연산에서 확률적 생성으로, 순수한 논리적 실행에서 뇌 영감 모델링 패러다임으로의 전환을 반영하며, 이는 테스팅의 단위 추상화, 평가 지표, 생애주기 관리에서 구조적 단절을 낳는다.",
      "자유형 자연어는 빠른 프로토타이핑을 가능하게 하지만 테스트 가능성을 저해한다. 모호하고, 결정론적으로 파싱하기 어려우며, 기계 가독성 맥락이 결여되어 있어 기존 테스팅 기법이 직접 이전되지 않는다."
    ]
  },
  {
    "title": "Non-Determinism of 'Deterministic' LLM Settings",
    "authors": ["Berk Atil", "Sarp Aykent", "Alexa Chittams", "Lisheng Fu", "Rebecca J. Passonneau", "Evan Radcliffe", "Guru Rajan Rajagopal", "Adam Sloan", "Tomasz Tudrej", "Ferhan Ture", "Zhe Wu", "Lixinyu Xu", "Breck Baldwin"],
    "year": 2025,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2408.04667",
    "summary": "temperature=0 등 '결정론적' 설정에서도 LLM이 실제로 비결정론적 출력을 낸다는 것을 5개 LLM·8개 태스크·10회 반복 실험으로 체계적으로 입증한 논문. ch02에서 '결정론적 테스팅이 왜 LLM에 통하지 않는가'를 실증 데이터로 뒷받침하는 핵심 증거 자료다.",
    "key_claims": [
      "결정론적으로 설정된 5개 LLM에서 자연 발생적 실행 간 정확도 변동이 최대 15%에 달하며, 최고 성능과 최저 성능 간 격차는 최대 70%에 이른다.",
      "어떤 LLM도 모든 태스크에서 반복 가능한 정확도를 일관되게 제공하지 못하며, 동일 출력 문자열은 더욱 드물다.",
      "비결정론은 컴퓨팅 자원의 효율적 사용(혼합 데이터 입력 버퍼)에 본질적으로 연결되어 있어 단기간에 해소될 문제가 아니며, 이는 단위 테스트(unit test) 기반 품질 보증의 근본적 한계를 의미한다."
    ]
  },
  {
    "title": "G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment",
    "authors": ["Yang Liu", "Dan Iter", "Yichong Xu", "Shuohang Wang", "Ruochen Xu", "Chenguang Zhu"],
    "year": 2023,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2303.16634",
    "summary": "LLM의 확률론적 출력을 평가하기 위해 루브릭·CoT·형식 채우기 패러다임을 결합한 G-Eval 프레임워크를 제안한 논문. ch02에서 '기존 결정론적 지표(BLEU, ROUGE)가 왜 LLM 평가에 실패하는가'를 보여주는 대조 사례이자, 새로운 평가 방법론의 구체적 실현으로 제시할 수 있다.",
    "key_claims": [
      "BLEU·ROUGE 같은 전통적 참조 기반 지표는 창의성·다양성이 필요한 태스크에서 인간 판단과 상관관계가 낮아, 확률론적 LLM 출력 평가에 부적합하다.",
      "GPT-4를 백본으로 한 G-Eval은 요약 태스크에서 인간과 Spearman 상관 0.514를 달성해 기존 모든 방법을 큰 폭으로 상회한다.",
      "LLM 기반 평가자는 LLM이 생성한 텍스트에 편향(bias)을 가질 수 있다는 잠재적 문제가 존재하며, 이는 평가 방법론 설계 시 반드시 고려해야 할 사항이다."
    ]
  },
  {
    "title": "LLMs-as-Judges: A Comprehensive Survey on LLM-based Evaluation Methods",
    "authors": ["Haitao Li", "Qian Dong", "Junjie Chen", "Huixue Su", "Yujia Zhou", "Qingyao Ai", "Ziyi Ye", "Yiqun Liu"],
    "year": 2024,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2412.05579",
    "summary": "LLM-as-a-Judge 패러다임을 기능·방법론·적용·메타 평가·한계 등 5개 관점에서 체계적으로 정리한 종합 서베이. ch02에서 '왜 LLM 평가는 새로운 방법론을 필요로 하는가'를 이론적으로 뒷받침하는 문헌으로, LLM 평가의 지형 전체를 한눈에 조망하는 레퍼런스로 활용 가능하다.",
    "key_claims": [
      "LLM-as-a-Judge는 자연어 응답 기반 평가자로서 효과성·범용성·해석 가능성 측면에서 학계·산업계의 주목을 받고 있으며, 기존 n-gram 지표나 의미 유사도 기반 평가를 대체하는 흐름이 형성되고 있다.",
      "평가 과정은 참조 기반(reference-based)과 참조 없는(reference-free) 방식으로 나뉘며, LLM 출력의 개방형·주관적 성격으로 인해
