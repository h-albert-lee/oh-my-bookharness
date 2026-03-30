# Search: "hidden technical debt" machine learning systems production Sculley 2015 site:papers.nips.cc OR site:arxiv.org

이제 조사된 자료를 바탕으로 충분한 정보를 확보했습니다. 검색 결과를 종합하여 ch02 집필에 참고할 JSON 형식의 자료 목록을 정리합니다.

---

아래는 검색을 통해 실제로 확인된 자료들을 ch02 집필 목적에 맞게 정리한 JSON입니다.



NeurIPS 2015에 게재된 Sculley et al.의 논문은 ML이 복잡한 예측 시스템을 빠르게 구축하는 강력한 도구이지만, 그 "빠른 성과"가 공짜로 오지 않는다고 경고하며, 실세계 ML 시스템에서 대규모의 지속적 유지보수 비용이 발생한다는 것을 소프트웨어 기술 부채 프레임워크로 분석합니다.

 

논문이 다루는 ML 특유의 위험 요소에는 boundary erosion, entanglement, hidden feedback loops, undeclared consumers, data dependencies, configuration issues, 외부 세계의 변화, 시스템 수준의 안티패턴 등이 포함됩니다.





이 논문은 ML 시스템이 기술 부채를 쌓는 특별한 능력을 가지고 있으며, 이 부채는 코드 수준이 아닌 시스템 수준에 존재하기 때문에 탐지하기 어렵고, 데이터가 ML 시스템 동작에 영향을 미쳐 전통적 추상화와 경계가 손상될 수 있으며, 코드 수준의 기술 부채 해소 방법만으로는 ML 특유의 시스템 수준 부채를 처리하기에 불충분하다고 주장합니다.





또한 구글의 선행 워크숍 논문(SE4ML 2014)은 성숙한 ML 시스템에서 실제 ML 코드가 최대 5%, 나머지 최소 95%는 glue code로 이루어질 수 있음을 지적합니다.





CACE 원칙("Changing Anything Changes Everything")에 따르면, ML 시스템에서 무엇이든 변경하면 예측 동작이 분포의 다양한 슬라이스에서 미묘하거나 극적으로 달라질 수 있습니다.





또한 후속 연구들이 지적하듯, ML에서 기술 부채 문제가 두드러지는 근본 이유는 ML의 확률론적 특성이 전통적인 비-ML 소프트웨어의 결정론적 특성과 대비되기 때문입니다.



```json
[
  {
    "title": "Hidden Technical Debt in Machine Learning Systems",
    "authors": [
      "D. Sculley",
      "Gary Holt",
      "Daniel Golovin",
      "Eugene Davydov",
      "Todd Phillips",
      "Dietmar Ebner",
      "Vinay Chaudhary",
      "Michael Young",
      "Jean-François Crespo",
      "Dan Dennison"
    ],
    "year": 2015,
    "type": "academic_paper",
    "url": "https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems",
    "summary": "ch02의 핵심 논거 기반 논문. ML 시스템이 기존 소프트웨어와 구조적으로 다른 이유를 'technical debt' 프레임워크로 분석하며, 코드 수준이 아닌 시스템 수준에 존재하는 부채가 왜 TDD 같은 전통적 방법론으로 탐지·해소되지 않는지를 직접적으로 설명한다. 특히 CACE 원칙, boundary erosion, hidden feedback loops, data dependencies 등의 개념은 'AI 시스템이 왜 결정론적 설계 가정을 위반하는가'를 논증하는 데 직접 인용 가능하다.",
    "key_claims": [
      "ML 시스템의 기술 부채는 코드 수준이 아닌 시스템 수준에 존재하며, 데이터가 시스템 동작을 결정하므로 전통적 추상화 경계가 무력화된다(boundary erosion).",
      "CACE(Changing Anything Changes Everything) 원칙: 입력 신호, 하이퍼파라미터, 샘플링 방법 등 무엇을 바꾸든 전체 모델 동작이 예측 불가능하게 변한다 — 이는 격리(isolation)를 전제하는 단위 테스트의 근본 가정을 붕괴시킨다.",
      "실제 ML 시스템에서 ML 코드는 극히 작은 비율이며, 방대한 주변 인프라(데이터 파이프라인, 설정, 서빙, 모니터링 등)가 시스템의 대부분을 구성한다.",
      "Hidden feedback loops: 라이브 ML 시스템은 종종 자신의 미래 학습 데이터에 영향을 미쳐, 배포 전에 모델 동작을 예측하기 어렵게 만든다(분석 부채).",
      "단위 테스트와 코드 리팩터링 등 전통적 기술 부채 해소 방법은 ML 시스템 수준의 부채를 해결하기에 불충분하다."
    ]
  },
  {
    "title": "Machine Learning: The High-Interest Credit Card of Technical Debt",
    "authors": [
      "D. Sculley",
      "Gary Holt",
      "Daniel Golovin",
      "Eugene Davydov",
      "Todd Phillips",
      "Dietmar Ebner",
      "Vinay Chaudhary",
      "Michael Young"
    ],
    "year": 2014,
    "type": "academic_paper",
    "url": "https://research.google.com/pubs/archive/43146.pdf",
    "summary": "2015년 NeurIPS 논문의 선행 워크숍 버전(SE4ML @ NIPS 2014). 성숙한 ML 시스템에서 실제 ML 코드가 최대 5%, 나머지 95%가 glue code임을 명시하며, pipeline jungle 안티패턴을 구체적으로 기술한다. ch02에서 'AI 시스템이 기존 소프트웨어와 다른가'를 논증할 때 이 수치와 사례를 인용하면 독자에게 직관적 충격을 줄 수 있다.",
    "key_claims": [
      "성숙한 ML 시스템은 최대 5% ML 코드, 최소 95% glue code로 구성될 수 있다 — ML은 알고리즘 문제가 아니라 시스템 엔지니어링 문제다.",
      "Pipeline jungles: 새로운 데이터 소스가 점진적으로 추가되면서 데이터 전처리 파이프라인이 scrapes, joins, sampling 단계의 정글로 진화하고, 이를 테스트하고 오류를 복구하는 것이 극도로 어려워진다.",
      "ML 패키지에 대한 단위 테스트와 라이브러리 리팩터링은 코드 수준의 부채는 줄일 수 있지만, 시스템 수준의 숨겨진 부채는 해결하지 못한다."
    ]
  },
  {
    "title": "Hidden Technical Debts for Fair Machine Learning in Financial Services",
    "authors": [
      "Chong Huang",
      "Leid Zejnilovic",
      "Sripriya Srinivasan"
    ],
    "year": 2021,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2103.10510",
    "summary": "Sculley 2015 프레임워크를 금융권 프로덕션 환경의 공정성(fairness) 문제에 적용한 후속 연구. 개별 컴포넌트에 대한 단위 테스트는 작동하지만, 통합 시스템 전체의 누적 효과는 포착하지 못한다는 점을 실증적으로 보여준다. ch02에서 'TDD의 전제가 AI 시스템에서 어떻게 붕괴되는가'를 설명할 때 구체적 사례로 활용 가능하다.",
    "key_claims": [
      "단위 테스트는 개별 컴포넌트에는 작동하지만, 고도로 통합된 시스템에서의 집합적 효과(aggregated effects)를 포착하는 데 실패한다.",
      "프로덕션 환경에서 'glue'로 연결된 컴포넌트들은 편향된 동작의 원인을 파악하는 것을 더욱 어렵게 만든다.",
      "ML 시스템에서 기술 부채는 조용히 누적되며, 나중에 해소하는 비용이 극도로 높아질 수 있다(silent accumulation)."
    ]
  },
  {
    "title": "Analysis of Hidden Feedback Loops in Continuous Machine Learning Systems",
    "authors": [
      "Anton Khritankov"
    ],
    "year": 2021,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2101.05673",
    "summary": "Sculley 2015가 '미해결 문제'로 지적한 hidden feedback loops를 연속적 ML 시스템에서 수학적으로 모델링하고 탐지 방법을 제안한 후속 연구. ch02에서 AI 시스템이 자신의 훈련 데이터에 영향을 미쳐 동작을 사전에 예측할 수 없는 구조임을 설명할 때 구체적인 사례(주택 가격 예측 시스템의 피드백 루프 실험)를 보완 자료로 사용할 수 있다.",
    "key_claims": [
      "숨겨진 피드백 루프는 Sculley 2015가 해결되지 않은 기술 부채로 지목했으며, 가능하면 식별하고 제거하거나 모니터링으로 영향을 제한해야 한다.",
      "연속적 ML 시스템에서 양성 피드백 루프는 일시적으로 인기 있는 예측이 구조적으로 지배적 지위를 갖게 되는 등 의도하지 않은 동작 변화를 초래한다.",
      "ML 피드백 루프는 일반 소프트웨어 시스템의 피드백 루프와 달리, 눈에 보이고 관찰 가능한 것은 사용자 행동에 대한 효과뿐이어서 탐지가 근본적으로 어렵다."
    ]
  },
  {
    "title": "An Empirical Study of Self-Admitted Technical Debt in Machine Learning Software",
    "authors": [
      "Gias Uddin",
      "Anushkha Khare",
      "Yann-Gaël Guéhéneuc"
    ],
    "year": 2023,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2311.12019",
    "summary": "Sculley 2015의 이론적 주장을 2,641개 실제 ML 저장소에서 경험적으로 검증한 연구. ML 소프트웨어가 비-ML 소프트웨어보다 2.1배 더 많은 기술 부채를 축적한다는 정량적 데이터를 제공한다. ch02에서 AI 시스템의 구조적 차이가 단순한 이론적 주장이 아니라 실증적으로 확인된 사실임을 뒷받침하는 데이터로 활용 가능하다.",
    "key_claims": [
      "ML 소프트웨어는 비-ML 소프트웨어보다 2.1배 더 많은 자기 인정 기술 부채(SATD)를 축적한다.",
      "ML의 기술 부채 문제가 두드러지는 근본 이유는 ML의 확률론적(stochastic) 특성이 전통적 소프트웨어의 결정론적(deterministic) 특성과 대비되기 때문이며, 이는 품질 문제를 새로운 유형으로 만든다.",
      "ML 고유의 기술 부채는 데이터 의존성, 숨겨진 피드백 루프, 파이프라인 정글 등의 형태로 나타나며, 기존 소프트웨어에는 없는 새로운 범주의 부채다."
    ]
  }
]
```

---

## 보충 설명: 각 자료의 ch02 활용 전략



Sculley 2015가 제시하는 핵심 통찰
