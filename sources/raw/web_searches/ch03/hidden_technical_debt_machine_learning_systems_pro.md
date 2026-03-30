# Search: "hidden technical debt" machine learning systems production failure patterns Sculley 2015

모든 자료 검색이 완료되었습니다. 이제 ch03 집필에 직접 활용할 수 있도록 JSON 형식으로 정리합니다.

---

아래는 검색을 통해 실제 존재가 확인된 자료들을 ch03 「문제는 모델이 아니라 시스템이다」의 집필 관점에서 정리한 결과입니다.

---



Sculley 2015 논문의 핵심 내용, CACE 원칙

, 

Breck 2017 ML Test Score

, 

Shankar 2022 인터뷰 연구

, 

Sambasivan 2021 Data Cascades

, 

Klaise 2020 모니터링 논문

, 

Towards Data Science 프로덕션 실패 패턴 블로그

 모두 확인 완료.

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
    "summary": "ch03의 핵심 논거를 제공하는 원전(原典). '실제 ML 시스템에서 ML 코드 자체는 극히 작은 부분에 불과하며 방대한 주변 인프라가 복잡한 부채를 만든다'는 주장은 '문제는 모델이 아니라 시스템'이라는 장의 테제를 학술적으로 뒷받침한다. CACE(Changing Anything Changes Everything) 원칙과 hidden feedback loop, entanglement, boundary erosion 등 시스템 레이어별 안티패턴 목록은 독자에게 '어느 레이어를 봐야 하는가'에 대한 구체적 진단 프레임을 제공한다.",
    "key_claims": [
      "실제 ML 시스템에서 ML 코드 자체는 전체의 극히 작은 부분이며, 방대하고 복잡한 주변 인프라가 대부분을 차지한다.",
      "CACE(Changing Anything Changes Everything) 원칙: 모델의 어떤 입력 신호를 바꾸든 나머지 모든 피처의 가중치와 중요도가 변하며, 이는 학습 방식과 무관하게 발생한다.",
      "Boundary erosion, entanglement, hidden feedback loops, undeclared consumers, data dependencies, configuration issues 등 ML 고유의 시스템 레이어 안티패턴이 운영 실패의 주원인이다.",
      "ML의 '빠른 성과(quick wins)'는 공짜가 아니며, 이를 공짜로 여기는 태도 자체가 위험하다."
    ]
  },
  {
    "title": "The ML Test Score: A Rubric for ML Production Readiness and Technical Debt Reduction",
    "authors": [
      "Eric Breck",
      "Shanqing Cai",
      "Eric Nielsen",
      "Michael Salib",
      "D. Sculley"
    ],
    "year": 2017,
    "type": "academic_paper",
    "url": "https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/",
    "summary": "Sculley 2015의 후속 연구로, 구글 내 36개 ML 팀에 실제로 적용한 28개의 프로덕션 준비 테스트 항목을 제시한다. ch03에서 '설계되지 않은 시스템'의 증거로 활용할 수 있다. 대부분의 Google 팀조차 데이터·모델 파이프라인에 대한 테스트가 없었다는 사실은 '모델 교체가 아닌 시스템 설계'의 필요성을 실증적으로 보여주는 강력한 사례다.",
    "key_claims": [
      "프로덕션 ML 시스템의 신뢰성을 확보하려면 데이터, 모델, 인프라, 모니터링 등 시스템 전 레이어에 걸친 테스트가 필요하다.",
      "실제 ML 시스템의 예측 동작은 코드가 아닌 데이터의 동적 특성과 모델 설정에 의존하므로, 일반 소프트웨어와 달리 사전에 동작을 명세하기 어렵다.",
      "구글 내부 팀들조차 데이터 및 파이프라인 테스트를 80% 이상 누락하고 있었으며, 이는 산업 전반의 ML 시스템 설계 공백을 증명한다."
    ]
  },
  {
    "title": "Operationalizing Machine Learning: An Interview Study",
    "authors": [
      "Shreya Shankar",
      "Rolando Garcia",
      "Joseph M. Hellerstein",
      "Aditya G. Parameswaran"
    ],
    "year": 2022,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2209.09125",
    "summary": "챗봇·자율주행·금융 등 다양한 도메인의 ML 엔지니어 18명을 심층 인터뷰한 정성 연구. ch03에서 '시스템이 설계되지 않았다'는 구조적 귀인의 현장 증거로 활용할 수 있다. 프로덕션 성공을 결정짓는 세 변수(Velocity, Validation, Versioning) 모두 모델 성능이 아닌 시스템 운영 설계에 관한 것이며, 실패의 원인이 대부분 파이프라인·데이터 피드백·모니터링 부재에 있음을 보여준다.",
    "key_claims": [
      "프로덕션 ML 배포의 성공을 결정짓는 세 변수는 Velocity(실험 속도), Validation(다단계 검증), Versioning(모델·데이터 버전 관리)이며, 모두 시스템 설계 영역이다.",
      "ML 엔지니어들은 잘못된 모델을 단순히 롤백하거나 더 단순한 모델로 대체하는 방식으로 프로덕션 안정성을 유지하며, 복잡한 분포 이동 대응보다 시스템 수준의 가드레일과 온콜 체계에 의존한다.",
      "ML 평가 지표는 ML 전용 지표(MAP 등)만으로는 불충분하며, 클릭률·이탈률 같은 제품 지표와 연결되어야 실제 실패를 감지할 수 있다."
    ]
  },
  {
    "title": "\"Everyone wants to do the model work, not the data work\": Data Cascades in High-Stakes AI",
    "authors": [
      "Nithya Sambasivan",
      "Shivani Kapania",
      "Hannah Highfill",
      "Diana Akrong",
      "Praveen K. Paritosh",
      "Lora Aroyo"
    ],
    "year": 2021,
    "type": "academic_paper",
    "url": "https://dl.acm.org/doi/10.1145/3411764.3445518",
    "summary": "고위험 AI 도메인의 실무자 53명 인터뷰를 통해 '데이터 캐스케이드'를 정의하고 실증한 CHI 2021 논문. ch03에서 '모델을 교체하면 나아질 것이다'는 사고 패턴이 왜 잘못된 귀인인지를 보여주는 결정적 근거로 활용할 수 있다. 92%의 실무자가 데이터 품질 문제에서 비롯된 연쇄 실패를 경험했다는 사실은 '문제는 모델 이전 레이어(데이터·파이프라인)에 있다'는 주장을 강력하게 뒷받침한다.",
    "key_claims": [
      "92%의 AI 실무자가 데이터 문제로 인한 데이터 캐스케이드(compounding failure)를 경험했으며, 이는 모델이 아닌 데이터/파이프라인 레이어에서 실패가 시작됨을 의미한다.",
      "데이터는 AI에서 가장 저평가·탈색된 영역이며, 실무자들은 모델 작업을 선호하고 데이터 작업을 회피하는 인센티브 구조 속에 있다.",
      "데이터 캐스케이드는 불투명하고 지연되어 발견이 어려우며, 뒤늦게 발견되면 프로젝트 폐기·대규모 재훈련 등 막대한 비용이 발생한다."
    ]
  },
  {
    "title": "Monitoring and Explainability of Models in Production",
    "authors": [
      "Janis Klaise",
      "Arnaud Van Looveren",
      "Clive Cox",
      "Giovanni Vacanti",
      "Alexandru Coca"
    ],
    "year": 2020,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2007.06299",
    "summary": "ML 라이프사이클이 배포 이후에도 계속된다는 점을 강조하며 모니터링·드리프트 탐지·설명가능성을 시스템 설계의 필수 구성요소로 다룬 ICML 2020 워크샵 논문. ch03에서 '시스템 레이어 중 어느 곳을 봐야 하는가'에 대한 모니터링 레이어 논의를 구체화할 때 참고할 수 있다. 모델 성능 지표만으로는 충분하지 않으며 데이터 드리프트·이상값·예측 설명 등을 포괄하는 시스템 수준 관측이 필요하다는 주장은 장의 핵심 논점을 보완한다.",
    "key_claims": [
      "ML 라이프사이클은 배포 단계에서 끝나지 않으며, 배포된 모델을 지속적으로 모니터링하는 것이 고품질 ML 서비스 제공의 필수 조건이다.",
      "모델 성능 및 데이터 모니터링, 통계적 기법을 이용한 이상값·데이터 드리프트 탐지, 과거 예측에 대한 설명 제공이 시스템 설계의 핵심 영역이다.",
      "레이블 독립적 지표(드리프트 탐지 등)와 실제 모델 성능을 직접 연결하는 것이 현재 MLOps의 핵심 미해결 연구 과제다."
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
    "summary": "Sculley 2015 NIPS 논문의 전신(前身)인 NIPS 2014 워크샵 논문. 2015년 논문보다 더 직접적으로 'ML은 기술 부채의 고금리 신용카드'라는 비유를 사용하며 시스템 레벨 부채의 위험성을 경고한다. ch03에서 '빠른 성과'에 대한 경각심과 부채가 조용히 복리로 쌓이는 메커니즘을 설명할 때 강력한 수사학적 도구로 활용할 수 있다.",
    "key_claims": [
      "ML 시스템의 기술 부채는 코드 레벨 부채를 넘어 시스템 레벨에서 숨어 복리로 증가하며, 이를 코드 리팩토링만으로 해소할 수 없다.",
      "첫 번째 ML 시스템 버전을 출시하는 것은 쉽지만, 이후 개선이 예상치 못하게 어려워지는 것이 ML 시스템의 본질적 특성이다.",
      "Hidden debt(숨겨진 부채)는 조용히 복리로 증가하기
