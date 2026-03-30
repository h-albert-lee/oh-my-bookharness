# Search: attribution error AI project failure "model replacement" same failure pattern case study

이제 충분한 자료를 확보했습니다. 수집된 자료들을 검증하고 장의 집필 목적에 맞게 정리하겠습니다.

---

다음은 검색을 통해 실제로 확인된 자료들을 ch03의 집필 목적("문제는 모델이 아니라 시스템이다")에 맞게 정리한 결과입니다.



최신 연구들은 AI 실패가 고립된 모델 오류에서 시스템 전체 붕괴로 전이된다는 점에서, '모델 중심 위험'에서 '엔드-투-엔드 시스템 취약성'으로의 관점 전환을 강조하고 있습니다.

 

대부분의 기업은 데이터가 지저분하거나 모델이 부정확하거나 기술이 복잡하면 AI가 실패한다고 생각하지만, 실제 이유는 조직적 문제입니다.



이 맥락에서 아래 자료들이 ch03 집필에 직접 활용될 수 있습니다.

---

```json
[
  {
    "title": "Hidden Technical Debt in Machine Learning Systems",
    "authors": ["D. Sculley", "Gary Holt", "Daniel Golovin", "Eugene Davydov", "Todd Phillips", "Dietmar Ebner", "Vinay Chaudhary", "Michael Young", "Jean-François Crespo", "Dan Dennison"],
    "year": 2015,
    "type": "academic_paper",
    "url": "https://papers.neurips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems",
    "summary": "ML 시스템의 실제 코드 중 모델 코드는 극히 일부에 불과하며, 나머지는 데이터 파이프라인·설정·인프라 등 시스템 레이어임을 논증한다. '모델을 교체하면 나아질 것'이라는 귀인 오류를 직접 반박하는 구조적 근거로 활용 가능하다. 숨겨진 기술 부채가 모델 레이어가 아닌 시스템 레이어에 축적된다는 점은 ch03의 핵심 주장을 지지한다.",
    "key_claims": [
      "ML 시스템에서 실제 모델 코드의 비중은 매우 작고, 나머지는 boundary erosion·entanglement·hidden feedback loop 등 시스템 수준 문제가 지배한다.",
      "ML 기술 부채는 코드 레벨이 아닌 시스템 레벨에 존재하며, 전통적인 코드 수준 해소법으로는 ML 특유의 부채를 해결할 수 없다.",
      "ML 시스템은 데이터가 시스템 행동에 영향을 미치기 때문에 전통적 소프트웨어보다 훨씬 큰 기술 부채 위험을 내포한다."
    ]
  },
  {
    "title": "The Root Causes of Failure for Artificial Intelligence Projects and How They Can Succeed: Avoiding the Anti-Patterns of AI",
    "authors": ["James Ryseff", "Brandon F. De Bruhl", "Sydne J. Newberry"],
    "year": 2024,
    "type": "industry_report",
    "url": "https://www.rand.org/pubs/research_reports/RRA2680-1.html",
    "summary": "65명의 AI/ML 전문가 인터뷰를 통해 AI 프로젝트 실패의 5대 근본 원인을 식별한 RAND 보고서. 실패의 가장 빈번한 원인이 모델 자체가 아니라 목적 오해·인프라 부재·조직 문제임을 실증 데이터로 보여줘, '모델 귀인 오류'를 설득력 있게 반박하는 권위 있는 근거로 사용할 수 있다.",
    "key_claims": [
      "AI 프로젝트의 80% 이상이 실패하는데 이는 AI가 없는 IT 프로젝트 실패율의 두 배이다.",
      "가장 흔한 실패 원인은 프로젝트 목적과 도메인 맥락에 대한 오해·오소통이며, 이는 모델 성능 문제가 아니다.",
      "조직이 실제 문제 해결보다 최신 기술 사용에 집중하거나, 모델 배포를 지원할 인프라가 부재할 때 프로젝트가 실패한다."
    ]
  },
  {
    "title": "Failure of AI projects: understanding the critical factors",
    "authors": ["Jens Westenberger", "K. Schuler", "D. Schlegel"],
    "year": 2022,
    "type": "academic_paper",
    "url": "https://www.sciencedirect.com/science/article/pii/S1877050921022134",
    "summary": "다양한 산업의 AI 전문가 인터뷰를 통해 AI 프로젝트 실패의 12가지 요인을 5개 범주로 분류한 실증 연구. '비현실적 기대', '조직적 제약', '기술적 문제' 등이 모두 귀인 오류와 연결되며, 특히 모델 불안정성이 '모델 교체'로 해결될 수 없는 시스템 문제임을 보여주는 사례로 활용 가능하다.",
    "key_claims": [
      "AI 프로젝트 실패는 조직적·기술적 문제가 모두 원인이며, 하나의 레이어만으로 귀인하는 것은 오류이다.",
      "모델 불안정성(model instability)은 시스템 업데이트 시 결과가 달라지는 예측 불가능한 행동으로 나타나며, 이는 모델 교체로 해결되지 않는다.",
      "AI 실패 요인은 비현실적 기대, 유스케이스 관련 문제, 조직적 제약, 핵심 자원 부족, 기술적 문제의 5개 범주로 구분된다."
    ]
  },
  {
    "title": "When AI Fails, What Works? A Data-Driven Taxonomy of Real-World AI Risk Mitigation Strategies",
    "authors": ["Evgenija Popchanovska", "Ana Gjorgjevikj", "Maryan Rizinski", "Lubomir T. Chitkushev", "Irena Vodenska", "Dimitar Trajanov"],
    "year": 2026,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2603.04259",
    "summary": "9,705개의 실제 AI 사고 기사를 분석해 '모델 중심 위험'에서 '엔드-투-엔드 시스템 취약성'으로의 관점 전환을 실증한 최신 논문(2026.03). 시스템적 실패가 모델 오류를 넘어 전체 시스템 붕괴로 전이된다는 핵심 주장을 대규모 실증 데이터로 뒷받침하며, ch03의 귀인 전환 논증에 직접 사용 가능하다.",
    "key_claims": [
      "LLM이 고위험 워크플로에 내재화됨에 따라, 실패는 고립된 모델 오류가 아닌 시스템 전체의 붕괴(systemic breakdown)로 전이된다.",
      "기존 AI 위험 분류체계는 모델 개발자 중심의 이론적 관점에 치우쳐, 배포자와 최종 사용자의 실제 완화 요구를 간과한다.",
      "실제 AI 사고의 미티게이션 패턴 분석 결과 기존 분류 대비 67% 더 많은 신규 패턴이 발견됐으며, 이는 시스템적 실패 모드가 지속적으로 새롭게 등장함을 의미한다."
    ]
  },
  {
    "title": "IBM Watson for Oncology Failure Case Study ($4 Billion AI Failure)",
    "authors": ["Henrico Dolfing"],
    "year": 2024,
    "type": "blog_post",
    "url": "https://www.henricodolfing.ch/en/case-study-20-the-4-billion-ai-failure-of-ibm-watson-for-oncology/",
    "summary": "IBM 왓슨의 암 치료 추천 시스템이 40억 달러 이상을 투자하고도 실패한 사례를 시스템 설계 실패 관점에서 분석한 케이스 스터디. '모델은 좋았으나 시스템이 잘못 설계되었다'는 귀인 전환의 전형적 사례로, ch03에서 독자의 귀인 오류를 시각적으로 교정하는 앵커 사례로 활용할 수 있다.",
    "key_claims": [
      "왓슨의 실패는 모델 자체의 성능 한계가 아니라, 실제 임상 데이터 대신 가상 사례로 훈련하는 등 시스템 설계상의 근본적 결함에서 비롯되었다.",
      "시스템이 다양한 의료 시스템·자원·문화적 관행의 변이를 수용하지 못하는 경직성을 보였으며, 이는 모델 교체가 아닌 시스템 아키텍처 재설계가 필요한 문제였다.",
      "가이드라인이 변화함에 따라 훈련 데이터가 뒤처지는 구조적 문제가 발생했고, 이는 지속적 시스템 설계의 부재로 인한 실패이다."
    ]
  },
  {
    "title": "Synthesizing AI Failure Research: A Scoping Review",
    "authors": ["(Springer Nature, Business & Information Systems Engineering)"],
    "year": 2025,
    "type": "academic_paper",
    "url": "https://link.springer.com/article/10.1007/s12599-025-00970-2",
    "summary": "141개 AI 실패 연구를 메타 분석하여 기술적·상호작용적·윤리적 범주로 통합한 스코핑 리뷰. 기존 연구들이 각각 좁은 관점(기술 결함, 상호작용 문제, 윤리 문제)에 집중하는 반면, 실제 실패는 복합적 시스템 문제임을 보여줘 ch03의 '레이어를 어디서 봐야 하는가' 논의를 보강한다.",
    "key_claims": [
      "AI 실패 연구는 기술적 결함, 상호작용 붕괴, 윤리적 우려 등 좁은 관점에 분절되어 있어, 시스템 전체를 아우르는 통합 관점이 부재하다.",
      "141개 연구의 분석 결과 실패 유형·근본 원인·완화 전략을 연결하는 Subtypes-Causes-Mitigation(SCM) 프레임워크가 필요함을 발견하였다.",
      "AI 실패의 진정한 해결은 단일 레이어(모델, 데이터, 조직) 개선이 아닌 복합적 시스템 설계 관점에서만 가능하다."
    ]
  },
  {
    "title": "7 Common MLOps Challenges (and How to Solve Them)",
    "authors": ["Chalk AI Engineering Team"],
    "year": 2026,
    "type": "blog_post",
    "url": "https://chalk.ai/blog/7-common-mlops-challenges",
    "summary": "프로덕션 ML 시스템의 반복적 실패 패턴을 조직 경계와 연결하여 설명한 실무 중심 글. 특히 'train-serve skew'(훈련-서빙 불일치) 현상은 모델 교체 후에도 동일 패턴이 반복되는 이유를 명쾌하게 설명하며, '모델을 바꿔도 같은 실패가 반복된다'는 ch03의 핵심 서사를 지지하는 현장 증거로 사용할 수 있다.",
    "key_claims": [
      "많은 조직이 훈련 시와 프로덕션 서빙 시 피처를 다르게 계산하는 'train-serve skew'를 발생시키며, 이는 모델 교체 후에도 동일하게 나타난다.",
      "MLOps 과제는 순수 기술적 문제가 아니라 조직 경계(data science·engineering·MLOps 팀 분리)에 의해 증폭된다.",
      "공유된 진실의 원천(shared source of truth) 없이는 모델 성능 저하가 코드 리뷰가 아닌 인시던트로만 발견된다."
    ]
  },
  {
    "title": "From Model-Centric to System-Centric: Engineering AI That Actually Works",
    "authors": ["The AI Journal"],
    "year": 2026,
    "type": "blog_post",
    "url": "https://aijourn.com/from-model-centric-
