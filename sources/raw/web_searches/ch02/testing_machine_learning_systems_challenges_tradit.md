# Search: testing machine learning systems challenges traditional software testing paradigm shift site:research.google OR site:engineering.fb.com OR site:netflixtechblog.com OR site:arxiv.org

수집된 자료를 종합하여 ch02 집필에 가장 적합한 자료들을 선별하고 정리합니다.



ML 테스팅이 전통적 소프트웨어 테스팅과 다른 이유, 비교 분류표 등 핵심 구조적 차이를 정리한 포괄적 서베이

, 

ML 시스템의 기술 부채에 관한 Google의 landmark 논문

, 

ML 시스템의 테스트 명세가 사전에 정의하기 어렵다는 근본적 문제를 다룬 Google 실무 루브릭

, 

EDD 접근법에 대한 최신 논문

, 

LLM/ML 테스팅의 패러다임 전환 필요성을 서술한 분류 논문

을 핵심 자료로 확인하였습니다.

---

아래는 ch02 집필에 참고할 수 있는 자료를 요청한 JSON 형식으로 정리한 결과입니다.

```json
[
  {
    "title": "Machine Learning Testing: Survey, Landscapes and Horizons",
    "authors": ["Jie M. Zhang", "Mark Harman", "Lei Ma", "Yang Liu"],
    "year": 2020,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/1906.10742",
    "summary": "ML 테스팅과 전통 소프트웨어 테스팅의 차이를 Table 1로 체계적으로 비교 정리한 서베이 논문으로, ch02의 핵심 주장인 '왜 ML 시스템은 기존 소프트웨어와 다른가'를 뒷받침하는 가장 포괄적인 학술적 근거다. 결정론적 코드 vs. 데이터 드리븐 패러다임의 대비, 버그 위치의 차이(코드 vs. 데이터/학습 프로그램/프레임워크) 등을 명확하게 구조화한다. TDD 비교 기준점 설정 후 AI 시스템에서의 전제 붕괴를 설명하는 논증 흐름에 직접 활용 가능하다.",
    "key_claims": [
      "ML 테스팅의 도전은 기존 소프트웨어 시스템(결정론적, 덜 통계적)과 근본적으로 다른 ML 시스템의 특성에서 비롯된다.",
      "전통 소프트웨어 테스팅은 코드의 버그를 탐지하는 반면, ML 테스팅은 데이터, 학습 프로그램, 프레임워크 각각의 버그를 탐지해야 한다.",
      "ML 시스템은 훈련 데이터로부터 학습 절차를 통해 결정 로직을 획득하는 데이터 드리븐 프로그래밍 패러다임을 따른다."
    ]
  },
  {
    "title": "Hidden Technical Debt in Machine Learning Systems",
    "authors": ["D. Sculley", "Gary Holt", "Daniel Golovin", "Eugene Davydov", "Todd Phillips", "Dietmar Ebner", "Vinay Chaudhary", "Michael Young", "Jean-François Crespo", "Dan Dennison"],
    "year": 2015,
    "type": "academic_paper",
    "url": "https://proceedings.neurips.cc/paper_files/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html",
    "summary": "Google 엔지니어들이 NIPS 2015에서 발표한 이 landmark 논문은 ML 시스템이 기존 소프트웨어 공학 프레임워크(기술 부채)로는 포착되지 않는 고유한 유지보수 비용을 발생시킨다는 것을 실증한다. 경계 침식(boundary erosion), 얽힘(entanglement), 숨겨진 피드백 루프, 데이터 의존성 등 ML 특유의 위험 요인들은 기존 TDD가 전제하는 '코드를 수정하면 테스트로 검증 가능하다'는 가정을 무너뜨리는 구체적 메커니즘으로 ch02에서 활용할 수 있다.",
    "key_claims": [
      "실제 ML 시스템에서는 막대한 지속적 유지보수 비용이 발생하는 것이 일반적이며, 이는 기존 소프트웨어 기술 부채와 다른 형태다.",
      "경계 침식, 얽힘, 숨겨진 피드백 루프, 데이터 의존성, 외부 세계의 변화 등 ML 고유의 위험 요인이 존재한다.",
      "ML은 복잡한 예측 시스템을 빠르게 구축하는 강력한 도구지만, 그 빠른 성과는 공짜로 얻어지지 않는다."
    ]
  },
  {
    "title": "The ML Test Score: A Rubric for ML Production Readiness and Technical Debt Reduction",
    "authors": ["Eric Breck", "Shanqing Cai", "Eric Nielsen", "Michael Salib", "D. Sculley"],
    "year": 2017,
    "type": "academic_paper",
    "url": "https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/",
    "summary": "Google이 실제 프로덕션 ML 시스템 경험으로부터 도출한 28개의 구체적 테스트 항목을 제시하는 논문으로, ML 시스템에 대한 구체적 테스트를 '사전에 명세하기 어렵다'는 근본적 문제를 인정하는 실무적 고백을 담고 있다. EDD 필요성의 논리적 귀결 설명에서, 왜 기존 TDD 방식의 사전 명세가 ML에서 무력화되는지를 산업 현장 데이터로 지지하는 근거로 활용할 수 있다.",
    "key_claims": [
      "프로덕션 수준의 ML 시스템을 만드는 것은 작은 실험이나 오프라인 연구에는 없는 다양한 우려를 야기한다.",
      "특정 모델의 실제 예측 동작을 사전에 명세하기 어렵기 때문에 구체적 테스트를 공식화하는 것이 어렵다.",
      "테스팅과 모니터링은 ML 시스템의 프로덕션 준비 상태를 보장하고 기술 부채를 줄이기 위한 핵심 고려 사항이다."
    ]
  },
  {
    "title": "Challenges in Testing Large Language Model Based Software: A Faceted Taxonomy",
    "authors": ["Robert Feldt", "Saad Bin Abid", "Fitsum Meshesha Kifetew", "Adam Crnkovic-Friis", "Davide Fucci"],
    "year": 2025,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2503.00481",
    "summary": "전통적 소프트웨어 테스팅이 결정론적 오라클에 의존하는 반면 LLM/ML의 확률적 특성이 이 가정을 깨뜨린다는 것을 명확하게 서술하며, ML 테스팅에는 패러다임 전환이 필요하다는 주장을 체계화한다. ch02의 핵심 논지인 '결정론적 설계 가정의 붕괴'를 지지하는 최신 학술 자료로, LLM의 비결정성이 코드/모델 추론/프롬프트 엔지니어링의 조합에서 출현한다는 하이브리드 특성 설명에 활용할 수 있다.",
    "key_claims": [
      "전통적 소프트웨어 테스팅은 결정론적 오라클에 의존하지만, LLM의 확률적 특성이 이 가정에 도전한다.",
      "ML 테스팅은 패러다임 전환을 필요로 하지만, 기존 연구들은 변동성을 일급 관심사로 명시적으로 다루지 않는다.",
      "기존의 결정론적·확률론적·ML 특화 패러다임들 모두 LLM 기반 시스템의 다층적 복잡성을 다루는 데 어려움을 겪고 있다."
    ]
  },
  {
    "title": "Non-Determinism and the Lawlessness of Machine Learning Code",
    "authors": ["A. Feder Cooper", "Jonathan Frankle", "Christopher De Sa"],
    "year": 2022,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2206.11834",
    "summary": "ML 코드가 '코드는 결정론적이다'라는 기존 전제를 근본적으로 벗어남을 보이는 논문으로, 확률론(stochasticity)과 비결정성(non-determinism)을 개념적으로 구분하여 분석한다. ch02에서 TDD의 전제(동일 입력→동일 출력)가 왜 ML에서 성립하지 않는지를 철학적·기술적으로 뒷받침하는 데 직접 활용 가능하다. 동일 훈련 절차에서도 모델 결과 분포가 크게 달라질 수 있다는 실증 사례도 포함한다.",
    "key_claims": [
      "결정론적 코드는 동일 입력에 동일 출력을 보장하지만, ML의 확률론적·비결정적 특성은 유사한 훈련 절차에서도 실제로 크게 다른 결과를 낳을 수 있다.",
      "ML 코드는 '코드는 법이다'라는 사이버법의 프레임—코드가 결정론적이라는 가정—을 벗어난다.",
      "ML 출력은 단일한 결과가 아니라 가능한 결과들의 분포로 이해해야 하며, 이 분포적 관점이 비결정성의 영향을 명확히 보여준다."
    ]
  },
  {
    "title": "An Empirical Study of Testing Machine Learning in the Wild",
    "authors": ["Moses Openja", "Foutse Khomh", "Zhen Ming (Jack) Jiang"],
    "year": 2024,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2312.12604",
    "summary": "11개의 오픈소스 ML/DL 프로젝트를 분석한 실증 연구로, 실제 현장에서 ML 테스팅이 어떻게 이루어지는지(그리고 얼마나 불충분한지)를 데이터로 보여준다. 전통 소프트웨어가 연역적으로(명시적 규칙 작성) 구성되는 반면 ML/DL 시스템은 귀납적으로(훈련 데이터로부터 규칙 추론) 구성된다는 설계 차이를 명확히 기술하며, ch02의 설계 관점 분석을 실증적으로 지지한다.",
    "key_claims": [
      "전통적 소프트웨어가 명시적 규칙을 작성하는 연역적 방식으로 구축되는 것과 달리, ML/DL 시스템은 훈련 데이터로부터 규칙을 추론하는 귀납적 특성을 갖는다.",
      "ML 컴포넌트의 결함은 훈련 데이터, 프로그램 코드, 실행 환경 어디에서도 발생할 수 있어 추론과 검증이 어렵다.",
      "연구된 ML 소프트웨어 시스템의 상당수가 제한된 수의 테스팅 전략에 의존하고 있어 커버리지 공백이 생길 수 있다."
    ]
  },
  {
    "title": "Rethinking Testing of Machine Learned Models",
    "authors": ["Google Research"],
    "year": 2021,
    "type": "academic_paper",
    "url": "https://research.google/pubs/rethinking-testing-of-machine-learned-models/",
    "summary": "ML 커뮤니티의 테스팅이 주로 테스트 데이터셋 대비 예측 성능 평가에 집중되어 있으며, 이 관점이 개발자로 하여금 다른 로버스트니스 실패 원인들(코너 케이스 등)을 간과하게 만든다고 주장하는 Google Research 논문이다. 전통 소프트웨어 공학의 스트레스 테스팅 방법론과의 명시적 비교를 통해, ML 테스팅의 '평균 성능 중심 편향'이라는 패러다
