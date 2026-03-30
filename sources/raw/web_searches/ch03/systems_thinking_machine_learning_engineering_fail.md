# Search: systems thinking machine learning engineering failure modes MLOps post-mortem

충분한 자료가 확보되었습니다. 이제 검색 결과를 바탕으로 JSON 형식으로 정리하겠습니다.

---

아래는 검색을 통해 실제로 확인된 자료들을 장의 브리프에 맞게 정리한 결과입니다.



Sculley et al.(2015)의 "Hidden Technical Debt in Machine Learning Systems"는 실제 ML 시스템에서 대규모 유지보수 비용이 발생하는 것이 일반적임을 보여주며, boundary erosion, entanglement, hidden feedback loops, data dependencies 등 ML 특유의 시스템 위험 요소들을 제시합니다.





Google 프로덕션 ML 강좌에 따르면, 실제 ML 프로덕션 시스템에서 모델 코드는 전체 코드베이스의 5% 이하에 불과하며, 이는 시스템 관점 전환의 필요성을 잘 보여줍니다.





Kästner의 CMU 교재는 "모델이 벤치마크를 이기는 것이 아니라 실세계 문제를 푸는 것이 목표"임을 강조하며, "안전성은 모델 수준에서가 아니라 시스템 수준의 속성"이라고 주장합니다.





RAND 연구에 따르면, AI 프로젝트 실패의 가장 흔한 원인은 목적 및 맥락에 대한 오해·오소통이며, 학습된 모델이 잘못된 지표에 최적화되거나 전체 비즈니스 워크플로우에 맞지 않게 배포되는 경우가 많다고 합니다.



```json
[
  {
    "title": "Hidden Technical Debt in Machine Learning Systems",
    "authors": ["D. Sculley", "Gary Holt", "Daniel Golovin", "Eugene Davydov", "Todd Phillips", "Dietmar Ebner", "Vinay Chaudhary", "Michael Young", "Jean-François Crespo", "Dan Dennison"],
    "year": 2015,
    "type": "academic_paper",
    "url": "https://papers.neurips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems.pdf",
    "summary": "구글 엔지니어들이 작성한 이 논문은 ML 시스템의 실패가 모델 코드가 아닌 주변 인프라(데이터 파이프라인, 피드백 루프, 설정 관리 등)에서 기인함을 보여준다. 'ML 모델 코드 자체는 시스템 전체의 극히 일부'라는 핵심 통찰은 3장의 '문제는 모델이 아니라 시스템이다' 명제를 직접 지지하는 근거 자료로 활용할 수 있다. boundary erosion, entanglement, hidden feedback loops 등 ML 특유의 시스템 부채 유형들은 모델 교체로 해결되지 않는 구조적 실패의 구체적 예시로 쓸 수 있다.",
    "key_claims": [
      "실제 ML 프로덕션 시스템에서 모델 코드는 전체 코드베이스의 5% 이하에 불과하며, 대부분은 데이터 수집·검증·모니터링 인프라 코드다",
      "ML 시스템은 boundary erosion, entanglement(뒤엉킴), hidden feedback loop, 데이터 의존성 등 소프트웨어 엔지니어링 맥락에서 인식되지 않는 특수한 기술 부채를 축적한다",
      "모델 성능 개선보다 이러한 시스템 수준의 부채를 해소하는 것이 장기적으로 훨씬 더 중요하다"
    ]
  },
  {
    "title": "Machine Learning in Production: From Models to Products",
    "authors": ["Christian Kästner"],
    "year": 2025,
    "type": "documentation",
    "url": "https://mlip-cmu.github.io/book/",
    "summary": "CMU의 'ML in Production' 과목 교재로, MIT Press에서 오픈 액세스로 출판된 이 책은 '모델만 잘 만들어서는 안 되고 전체 시스템을 설계해야 한다'는 논지를 체계적으로 전개한다. '안전성은 시스템 속성이며 신뢰할 수 없는 컴포넌트(ML 모델)를 둘러싼 가드레일 설계가 핵심'이라는 저자의 주장은 3장 및 PART 2의 설계 언어 도입을 정당화하는 데 직접 활용 가능하다. FMEA(Failure Mode and Effects Analysis)를 ML 시스템에 적용하는 방법도 다루어 시스템 관점 진단 도구로 소개할 수 있다.",
    "key_claims": [
      "안전성(safety)은 모델 수준의 속성이 아니라 시스템 수준의 속성이며, ML 모델은 항상 실수를 범하는 신뢰 불가능한 컴포넌트로 간주해야 한다",
      "전통적인 ML 교재는 모델 학습·평가에만 집중하고, MLOps 책은 배포 자동화에만 집중하지만, 둘 다 실제 가치를 전달하는 제품 구축 방법을 다루지 않는다",
      "ML 컴포넌트는 항상 실수를 범하므로, 시스템 설계 단계에서 그 실수가 실제 해악으로 이어지지 않도록 완화 전략을 미리 설계해야 한다"
    ]
  },
  {
    "title": "The Root Causes of Failure for Artificial Intelligence Projects and How They Can Succeed: Avoiding the Anti-Patterns of AI",
    "authors": ["James Ryseff", "Brandon De Bruhl", "Sydne J. Newberry"],
    "year": 2024,
    "type": "industry_report",
    "url": "https://www.rand.org/pubs/research_reports/RRA2680-1.html",
    "summary": "RAND Corporation이 65명의 데이터 과학자·엔지니어를 인터뷰하여 AI 프로젝트 실패의 근본 원인을 분석한 보고서다. AI 프로젝트의 80% 이상이 실패하며, 그 원인이 모델 성능이 아니라 목적 오해, 인프라 부재, 기술-비즈니스 워크플로우 불일치 등 구조적 문제임을 실증적으로 보여준다. 3장에서 '모델 탓'이라는 귀인이 왜 틀렸는지를 데이터로 뒷받침하는 핵심 인용 자료로 쓸 수 있다.",
    "key_claims": [
      "AI 프로젝트 실패의 가장 흔한 원인은 모델 성능 문제가 아니라 프로젝트 목적·도메인 맥락에 대한 오해와 오소통이다",
      "인프라 투자 부족(데이터 관리, 모델 배포 시스템)이 AI 프로젝트 실패의 주요 요인이며, 이를 해결하지 않으면 성능 좋은 모델도 프로덕션에서 실패한다",
      "AI 프로젝트 실패율(>80%)은 AI를 포함하지 않는 IT 프로젝트 실패율(약 40%)의 두 배이며, 이는 ML 특유의 시스템 설계 문제를 반영한다"
    ]
  },
  {
    "title": "Challenges in Deploying Machine Learning: A Survey of Case Studies",
    "authors": ["Andrei Paleyes", "Raoul-Gabriel Urma", "Neil D. Lawrence"],
    "year": 2022,
    "type": "academic_paper",
    "url": "https://dl.acm.org/doi/full/10.1145/3533378",
    "summary": "ACM Computing Surveys에 게재된 이 논문은 다양한 산업·응용 분야에서 ML 모델을 프로덕션에 배포한 사례 연구들을 체계적으로 검토하고, 배포 워크플로우의 각 단계(데이터 수집, 전처리, 모델 학습, 배포, 모니터링)에서 실패가 발생함을 보여준다. 단순한 모델 교체·파인튜닝으로 해결되지 않는 문제들이 파이프라인의 앞뒤에 걸쳐 분포한다는 것을 실증적으로 제시한다. 3장에서 AI 시스템 실패 지점의 분포를 설명할 때 핵심 근거 자료로 활용 가능하다.",
    "key_claims": [
      "ML 프로덕션 배포 실패는 모델 알고리즘 자체보다 데이터 관리, 피처 엔지니어링, 모델 서빙 인프라, 모니터링 등 주변 시스템에서 훨씬 빈번하게 발생한다",
      "학술 연구 환경에서 잘 작동하는 ML 모델이 실제 시스템에 통합될 때 실패하는 근본적 원인은 데이터 분포 불일치, 시스템 통합 문제, 환경 편향 등 시스템 설계 결함이다",
      "배포 편향(deployment bias)은 모델이 의도된 방식과 다르게 사용되거나 설계된 환경과 다른 환경에 배포될 때 발생하며, 이는 모델 성능 개선으로 해결 불가하다"
    ]
  },
  {
    "title": "Failure Modes in Machine Learning Systems",
    "authors": ["Ram Shankar Siva Kumar", "David O'Brien", "Kendra Albert", "Salome Viljoen", "Jeffrey Snover"],
    "year": 2019,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/1911.11034",
    "summary": "Microsoft AI Red Team이 작성한 이 논문은 ML 시스템의 실패를 '의도적 실패'(적대적 공격)와 '비의도적 실패'(설계상 취약점)로 분류하는 체계적 분류법을 제시한다. ML 시스템의 실패 방식이 전통적인 소프트웨어 실패와 근본적으로 다름을 강조하며, 시스템 전반적 관점의 위협 모델링 필요성을 역설한다. 3장에서 모델 중심 사고의 맹점과 시스템 수준 취약성을 논할 때 인용할 수 있다.",
    "key_claims": [
      "ML 시스템의 실패 방식은 전통적 소프트웨어 실패와 본질적으로 다르며, 이를 구분하는 공통 언어 없이는 엔지니어·법률가·정책입안자가 실패를 제대로 분석할 수 없다",
      "비의도적 실패(unintentional failures)는 모델 알고리즘의 버그가 아니라 데이터 편향, 환경 변화에 대한 취약성, 시스템 설계상의 구조적 취약점에서 비롯된다",
      "효과적인 ML 시스템 보호를 위해서는 모델 수준의 방어가 아니라 시스템 전체에 대한 위협 모델링(threat modeling)이 필요하다"
    ]
  },
  {
    "title": "Planning for Mistakes (Chapter 7) — Machine Learning in Production: From Models to Products",
    "authors": ["Christian Kästner"],
    "year": 2025,
    "type": "documentation",
    "url": "https://mlip-cmu.github.io/book/07-planning-for-mistakes.html",
    "summary": "ML 시스템의 실패를 사전에 체계적으로 설계하는 방법을 다루는 챕터로, Failure Mode and Effects Analysis(FMEA)를 ML 컴포넌트에 적용하는 방법을 구체적으로 설명한다. '모델은 항상 실수를 범한다'는 전제 하에, 시스템 설계가 그 실수의 결과를 어떻게 흡수하거나 완화할 수 있는지를 논한다. 3장의 핵심 논지인 '모델 개선으로 해결되지 않는 시스템 설계 문제'를 독자에게 납득시키는 실무 프레임워크로 직접 소개 가능하다.",
    "key_claims": [
      "ML 모델은 항상 실수를 범하며 이를 완전히 제거할 수는 없으므로, 시스템 설계 단계에서 모델 실수가 실제 피해로 이어지지 않도록 완화
