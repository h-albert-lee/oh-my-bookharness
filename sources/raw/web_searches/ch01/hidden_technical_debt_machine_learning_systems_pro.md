# Search: hidden technical debt machine learning systems production deployment challenges paper

수집된 자료를 바탕으로 JSON 형식으로 정리합니다. 검색 결과에서 실제로 존재하고 URL이 확인된 자료만 포함합니다.

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
    "url": "https://proceedings.neurips.cc/paper_files/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf",
    "summary": "이 장의 핵심 레퍼런스. '빠른 성공'이 공짜로 오지 않는다는 주장을 통해, 데모 이후 운영에서 붕괴되는 원인을 시스템 부채(technical debt) 개념으로 설명한다. ML 시스템에서 실제 ML 코드는 극히 일부(~5%)에 불과하며 나머지는 유지보수 비용이 큰 인프라임을 시각적으로 보여주는 다이어그램과 함께, '시스템 부재'가 실패의 근원임을 논증하는 데 직접 인용 가능하다. 경계 침식, 엔탱글먼트, 히든 피드백 루프 등 ML 고유의 위험 요소 목록은 '있어야 했는데 없었던 것'을 열거하는 구조로 활용할 수 있다.",
    "key_claims": [
      "ML 시스템이 빠르게 구축될수록 막대한 유지보수 비용이 숨어서 누적된다(hidden debt compounds silently).",
      "성숙한 ML 시스템에서 실제 ML 코드는 많아야 5%, 나머지 95%는 글루 코드(glue code)다.",
      "ML 부채는 코드 수준이 아닌 시스템 수준에 존재하므로 전통적인 기술 부채 해소법으로는 대응이 불가능하다.",
      "boundary erosion, entanglement, hidden feedback loops, undeclared consumers, data dependencies, configuration issues 등 ML 고유의 위험 요소들이 운영 실패를 유발한다."
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
    "summary": "ML 엔지니어 18명을 대상으로 한 심층 인터뷰 연구로, 운영 환경에서 ML이 실패하는 현장의 목소리를 담고 있다. 프로덕션 ML 배포의 성공을 좌우하는 세 가지 변수(Velocity, Validation, Versioning)를 제시하며, 이것이 곧 '있어야 했는데 없었던 시스템 구조'임을 독자에게 보여주는 근거로 활용 가능하다. ML 평가 지표가 제품 지표와 연동되지 않을 때 프로젝트가 실패한다는 현장 증언은 '모델 성능 차이가 아닌 환경 구조 차이'라는 이 장의 핵심 명제를 뒷받침한다.",
    "key_claims": [
      "프로덕션 ML 배포의 성공을 결정하는 세 가지 변수는 Velocity(실험 속도), Validation(검증), Versioning(버전 관리)이다.",
      "많은 ML 프로젝트가 실패하는 핵심 이유는 제품 지표와 연동되지 않는 ML 지표를 사용하기 때문이다.",
      "에러는 사용자에게 노출될수록 처리 비용이 커지므로, 파이프라인 상류에서 최대한 일찍 검증하는 구조가 필요하다."
    ]
  },
  {
    "title": "The Root Causes of Failure for Artificial Intelligence Projects and How They Can Succeed: Avoiding the Anti-Patterns of AI",
    "authors": [
      "James Ryseff",
      "Brandon F. De Bruhl",
      "Sydne J. Newberry"
    ],
    "year": 2024,
    "type": "industry_report",
    "url": "https://www.rand.org/pubs/research_reports/RRA2680-1.html",
    "summary": "65명의 숙련된 데이터 과학자·엔지니어 인터뷰를 기반으로 한 RAND Corporation의 권위 있는 보고서로, AI 프로젝트 80% 이상이 실패한다는 수치를 제시한다. 이는 AI 없는 IT 프로젝트 실패율의 두 배로, 이 장의 도입부에서 '왜 AI 프로젝트는 데모 이후에 무너지는가'라는 질문을 수치로 정당화하는 데 강력한 근거가 된다. 실패 원인이 모델 자체가 아닌 문제 정의 오류, 데이터 인프라 부재, 잘못된 지표 최적화 등 시스템적 요인임을 규명하여, 이 장의 '시스템 부재로의 재정의' 논지를 직접 지지한다.",
    "key_claims": [
      "AI 프로젝트의 80% 이상이 실패하며, 이는 AI를 포함하지 않는 IT 프로젝트 실패율의 두 배다.",
      "가장 흔한 실패 원인은 해결할 문제에 대한 오해 또는 잘못된 커뮤니케이션이다.",
      "훈련된 AI 모델이 잘못된 지표에 최적화되거나 전반적인 비즈니스 워크플로우에 맞지 않는 상태로 배포되는 경우가 많다.",
      "조직이 AI 모델을 관리·배포할 적절한 인프라를 갖추지 못한 것이 주요 실패 요인이다."
    ]
  },
  {
    "title": "Hidden Technical Debt of GenAI Systems",
    "authors": [
      "Databricks Blog (Sung Won Chung et al.)"
    ],
    "year": 2024,
    "type": "blog_post",
    "url": "https://www.databricks.com/blog/hidden-technical-debt-genai-systems",
    "summary": "Sculley et al.(2015)의 논문을 생성형 AI 시대로 확장하여, 고전적 ML과 GenAI의 기술 부채 유형을 비교 분석한다. 특히 데이터 부채, 시스템 수준 부채, 외부 환경 변화에 의한 부채의 세 범주를 구체화하여 이 장의 '비결정성(nondeterminism)' 개념 도입에 활용 가능한 현대적 사례를 제공한다. GenAI에서 소프트 에러가 예측을 여전히 합리적으로 보이게 만들어 발견이 어렵다는 지적은, AI가 기존 소프트웨어와 본질적으로 다른 이유를 설명하는 데 유용하다.",
    "key_claims": [
      "GenAI는 데이터 부채, 시스템 수준 부채, 외부 환경 변화라는 세 가지 기술 부채 범주를 고전 ML보다 심화된 형태로 내포한다.",
      "소프트 에러(예: 일부 null 피처)는 예측을 여전히 합리적으로 보이게 만들어 탐지와 정량화가 어렵다.",
      "모델 드리프트(feature drift, data drift, label drift)는 시간 단위에 따라 다르게 측정되어야 하므로 모니터링 복잡도가 높다."
    ]
  },
  {
    "title": "AI Is Not a Library: Designing for Nondeterministic Dependencies",
    "authors": [
      "O'Reilly Radar"
    ],
    "year": 2026,
    "type": "blog_post",
    "url": "https://www.oreilly.com/radar/ai-is-not-a-library-designing-for-nondeterministic-dependencies/",
    "summary": "소프트웨어 엔지니어링의 오랜 전제인 '동일 입력 → 동일 출력'을 AI가 조용히 깨뜨린다는 통찰을 제시하는 실무 중심 글로, 이 장의 '비결정성이 AI를 기존 소프트웨어와 본질적으로 다르게 만드는 이유' 섹션의 핵심 논거로 활용 가능하다. 비결정성을 1등급 설계 관심사(first-class concern)로 명시적으로 문서화하고 관리하는 구조, 즉 '하네스'의 필요성을 자연스럽게 도출하는 프레임을 제공한다. 아키텍트 관점에서 쓰여 실무 독자와의 접점이 높다.",
    "key_claims": [
      "소프트웨어 공학의 핵심 전제인 결정론적 동작(같은 입력 → 같은 출력)을 AI 시스템이 조용히 깨뜨린다.",
      "AI 시스템은 라이브러리나 외부 서비스처럼 보이지만, 실제로는 결정론적 컴포넌트가 아닌 비결정론적 협력자(nondeterministic collaborator)처럼 동작한다.",
      "비결정성을 제거하려 하기보다, 그것을 명시적으로 격리하고 봉쇄(contain)하는 아키텍처 설계가 필요하다.",
      "정확성(correctness) 대신 수용 가능성(acceptability)으로 올바름의 기준을 재정의해야 한다."
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
    "summary": "2015년 NeurIPS 논문의 전신인 워크샵 페이퍼로, '성숙한 ML 시스템에서 ML 코드는 많아야 5%, 나머지 95%는 글루 코드'라는 가장 자주 인용되는 수치의 출처다. 이 장에서 '실제 모델 코드는 빙산의 일각이고 진짜 문제는 그 아래 시스템'이라는 비유를 도입할 때 1차 문헌으로 직접 인용할 수 있다. 파이프라인 정글, 글루 코드 등 구체적인 안티패턴 명칭을 처음 체계화한 문서이기도 하다.",
    "key_claims": [
      "성숙한 ML 시스템에서 실제 ML 코드는 많아야 5%, 나머지 최소 95%는 글루 코드(glue code)다.",
      "파이프라인 정글(pipeline jungle)은 새로운 데이터 소스가 점진적으로 추가되면서 자연스럽게 형성되며, 오류 감지와 복구를 극도로 어렵게 만든다.",
      "기술 부채는 감지되지 않은 채 복리로 누적되기 때문에 특히 위험하다."
    ]
  },
  {
    "title": "A Software Engineering Perspective on Engineering Machine Learning Systems: State of the Art and Challenges",
    "authors": [
      "Görkem Giray"
    ],
    "year": 2021,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2012.07919",
    "summary": "141개의 소프트웨어 공학 연구를 체계적으로 검토한 문헌 조사 논문으로, ML 시스템의 비결정론적 특성이 소프트웨어 공학의 모든 측면을 복잡하게 만든다는 것을 실증적으로 정리한다. 이 장의 '비결정성이 AI를 기존 소프트웨어와 본질적으로 다르게 만드는 이유'를 학술적으로 뒷받침하는 체계적 근거 자료로, 단순 주장이 아닌 문헌 기반 논거가 필요할 때 유용하다.",
    "key_claims": [
      "ML 시스템의 비결정론적 특성은 소프트웨어 공학의
