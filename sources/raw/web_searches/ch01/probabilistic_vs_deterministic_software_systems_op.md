# Search: probabilistic vs deterministic software systems operational challenges MLOps

검색 결과를 충분히 수집했습니다. 이제 장의 집필 목적에 맞게 자료를 선별하고 정리하겠습니다.

---

아래는 조사를 통해 찾은 참고 자료 목록입니다. 각 자료의 실제 존재 여부와 URL을 확인한 것만 포함했습니다.

---



Sculley et al.의 NeurIPS 2015 논문은 ML이 유용한 시스템을 빠르게 구축하는 강력한 도구임을 인정하면서도, 이 빠른 성과가 "공짜"가 아니라는 점을 경고하며 실제 ML 시스템에서 막대한 유지보수 비용이 발생함을 소프트웨어 기술 부채 프레임으로 논증합니다.

 

DevOps 파이프라인이 결정론적 소프트웨어용으로 설계되어, 시간이 지남에 따라 저하되는 확률론적·데이터 의존적 시스템을 단위 테스트로 잡아낼 수 없다는 점이 핵심 긴장 요소임을 실무 커뮤니티도 확인하고 있습니다.



---

```json
[
  {
    "title": "Hidden Technical Debt in Machine Learning Systems",
    "authors": ["D. Sculley", "Gary Holt", "Daniel Golovin", "Eugene Davydov", "Todd Phillips", "Dietmar Ebner", "Vinay Chaudhary", "Michael Young", "Jean-François Crespo", "Dan Dennison"],
    "year": 2015,
    "type": "academic_paper",
    "url": "https://proceedings.neurips.cc/paper_files/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html",
    "summary": "ML 시스템이 기존 소프트웨어보다 기술 부채를 더 빠르게 누적하는 이유를 시스템 수준에서 분석한 Google 연구진의 고전 논문. '데모에서 잘 작동했으나 운영에서 무너지는' 구조적 원인—경계 침식, 숨겨진 피드백 루프, 데이터 의존성—을 구체적으로 명명한다. 1장에서 '개인/모델 탓'이 아닌 '시스템 부재' 재정의를 지지하는 권위 있는 학술 근거로 활용 가능.",
    "key_claims": [
      "ML 시스템은 일반 코드 유지보수 문제에 더해 ML 고유의 기술 부채 문제를 추가로 갖는다",
      "이 부채는 코드 수준이 아닌 시스템 수준에 존재하여 탐지하기 어렵다",
      "경계 침식, 엔탱글먼트, 숨겨진 피드백 루프, 미선언 소비자, 데이터 의존성이 주요 위험 요소다",
      "재현성 부채(Reproducibility Debt): 비결정성(무작위 알고리즘, 병렬 학습)이 재현 가능한 시스템 설계를 어렵게 만든다"
    ]
  },
  {
    "title": "Challenges in Deploying Machine Learning: A Survey of Case Studies",
    "authors": ["Andrei Paleyes", "Raoul-Gabriel Urma", "Neil D. Lawrence"],
    "year": 2022,
    "type": "academic_paper",
    "url": "https://dl.acm.org/doi/full/10.1145/3533378",
    "summary": "다양한 산업의 ML 배포 사례를 체계적으로 검토하여 배포 워크플로우 각 단계에서 실무자가 직면하는 문제를 매핑한 ACM 서베이. 데모와 운영 간의 간극이 모델 성능 문제가 아닌 배포 전 과정의 구조적 문제임을 실증적으로 보여준다. 1장의 '데모 성공 ≠ 운영 성공' 주장을 다수의 실제 사례로 뒷받침하는 데 활용 가능.",
    "key_claims": [
      "ML 배포에서 실무자는 데이터 수집부터 모니터링·업데이트까지 모든 단계에서 문제를 겪는다",
      "ML은 데이터셋과 모델이라는 기존 소프트웨어 공학 도구가 그대로 적용되지 않는 고유한 아티팩트를 도입한다",
      "배포 실패의 주요 원인은 모델 알고리즘이 아닌 통합(integration), 모니터링, 갱신(updating) 단계에 집중된다",
      "학문적 환경과 실제 세계 시스템 사이에는 항상 보틀넥과 검증되지 않은 전제가 존재한다"
    ]
  },
  {
    "title": "AI Is Not a Library: Designing for Nondeterministic Dependencies",
    "authors": ["O'Reilly Radar (익명 기고)"],
    "year": 2026,
    "type": "blog_post",
    "url": "https://www.oreilly.com/radar/ai-is-not-a-library-designing-for-nondeterministic-dependencies/",
    "summary": "AI를 '더 스마트한 API'가 아닌 '비결정론적 의존성'으로 프레이밍해야 한다는 논지의 O'Reilly 블로그. 재시도(retry), 테스팅, 관찰가능성이 결정론적 소프트웨어 가정 하에 설계되어 AI 시스템에서 어떻게 무너지는지를 구체적으로 설명한다. 1장에서 '비결정성이 AI를 기존 소프트웨어와 본질적으로 다르게 만드는 이유'를 실무 엔지니어링 관점에서 설명하는 핵심 자료.",
    "key_claims": [
      "결정론적 시스템에서 재시도는 안전하지만, AI 시스템에서 재시도는 새로운 출력을 생성하여 오히려 실패를 증폭시킬 수 있다",
      "AI 관련 실패는 조용하다—시스템은 응답하고 대시보드는 녹색이지만 출력은 '수용 가능하지만 틀린(acceptable but wrong)' 상태다",
      "비결정성을 제거하려 하지 말고 '억제(containing)'하는 방향으로 설계 우선순위를 바꿔야 한다",
      "가드레일, 폴백 경로, 인간-루프-내 워크플로우가 사후 고려사항이 아닌 아키텍처 기능이 되어야 한다"
    ]
  },
  {
    "title": "Probabilistic and Deterministic Systems (Decision Matrix Substack)",
    "authors": ["Daniel Vaughan"],
    "year": 2025,
    "type": "blog_post",
    "url": "https://decisionmatrix.substack.com/p/probabilistic-and-deterministic-systems",
    "summary": "GenAI 시스템의 확률론적 특성과 결정론적 소프트웨어의 차이를 개념적으로 명확히 구분하고, 기존 단위 테스트가 확률론적 시스템에 적용될 수 없는 이유를 설명한다. 1장에서 '비결정성(Nondeterminism)이 AI를 기존 소프트웨어와 본질적으로 다르게 만드는 이유'라는 독자 인식 전환 목표에 직접 활용 가능한 입문 수준의 개념 자료.",
    "key_claims": [
      "GenAI 시스템은 확률론적이므로, 이 기술을 사용하는 모든 시스템은 그 확률론적 특성을 물려받는다",
      "전통적인 단위 테스트는 AI 어플리케이션에 작동하지 않으며, 확률론적 시스템은 단순 합격/불합격이 아닌 평가 프레임워크(evals)가 필요하다",
      "소프트웨어 개발자는 확률론적 시스템을 구축하는 데 필요한 핵심 기술이 부족하다",
      "다단계 AI 워크플로우에서 오류는 복합적으로 증폭된다"
    ]
  },
  {
    "title": "What Are Non-Deterministic AI Outputs?",
    "authors": ["Statsig 팀"],
    "year": 2024,
    "type": "blog_post",
    "url": "https://www.statsig.com/perspectives/what-are-non-deterministic-ai-outputs-",
    "summary": "비결정적 AI 출력의 특성과 이것이 개발·배포에 제기하는 고유 도전을 설명한다. 전통적 소프트웨어 테스팅(예측 가능한 반복 가능한 결과에 의존)이 어떻게 무너지는지, 그리고 운영 환경에서의 대응 전략을 다룬다. 1장에서 비결정성의 운영적 함의를 독자에게 소개하는 보조 자료로 활용 가능.",
    "key_claims": [
      "비결정적 AI를 개발·배포하는 것은 정확한 재현 가능성에 대한 기대에서 변동성을 수용하고 관리하는 마인드셋 전환이 필요하다",
      "전통적 소프트웨어 테스팅은 예측 가능하고 반복 가능한 결과에 의존하지만, 비결정적 AI에서는 단일 예상 결과가 아닌 허용 가능한 출력의 범위를 테스트해야 한다",
      "운영 환경에서 임계값 설정, 출력 분포 모니터링, 폴백 메커니즘이 필요하다"
    ]
  },
  {
    "title": "How AI-Driven Deployment Differs Between Traditional Software and ML Models (MLOps)",
    "authors": ["Semaphore 팀"],
    "year": 2026,
    "type": "blog_post",
    "url": "https://semaphore.io/how-does-ai-driven-deployment-differ-between-traditional-software-and-ml-models-mlops",
    "summary": "전통적 CI/CD(결정론적 코드 배포)와 MLOps(확률론적 동작 배포)의 차이를 아티팩트, 검증, 롤아웃, 피드백 루프 4가지 영역에서 구체적으로 대비시킨다. '행동(behavior)을 버전 관리해야 하지 코드만 버전 관리해서는 안 된다'는 핵심 명제를 제시. 1장에서 기존 소프트웨어 엔지니어링의 관행이 AI에 그대로 적용되지 않는 이유를 설명하는 실용적 자료.",
    "key_claims": [
      "전통적 CI/CD는 결정론적 코드를 배포하고, MLOps는 데이터에 의해 형성된 확률론적 행동을 배포한다—그 이후의 모든 것(테스팅, 롤아웃, 모니터링)이 여기서 비롯된다",
      "기존 도구들은 이진(binary) 게이트용으로 만들어졌기 때문에 등급이 있는(graded) 의사결정에 무너진다",
      "코드뿐 아니라 행동(behavior)을 버전 관리해야 한다는 새로운 요구사항이 생긴다",
      "MLOps에서 AI는 이미 불확실한 시스템 위에서 작동하여 위험을 복합적으로 증폭시킨다"
    ]
  },
  {
    "title": "MLOps vs DevOps: Full Comparison 2026",
    "authors": ["DiffStudy 편집팀"],
    "year": 2026,
    "type": "blog_post",
    "url": "https://diffstudy.com/mlops-vs-devops/",
    "summary": "DevOps가 결정론적 소프트웨어의 배포 문제를 해결한 것처럼, MLOps가 확률론적·데이터 의존적 시스템의 배포와 지속가능성 문제를 해결하는 방식을 대비적으로 설명한다. 시장 규모, 주요 트렌드, 실무 비교를 포함한 최신(2026) 종합 자료. 1장에서 MLOps가 왜 별도의 규율로 등장했는지를 독자에게 설명하는 컨텍스트 자료로 활용 가능.",
    "key_claims": [
      "DevOps용으로 설계된 CI/CD 파이프라인은 단위 테스트로 잡아낼 수 없는 방식으로 시간이 지남에 따라 저하되는 확률론적·데이터 의존적 시스템에 제대로 동작하지 않
