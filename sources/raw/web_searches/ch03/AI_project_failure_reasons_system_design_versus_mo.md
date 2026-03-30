# Search: AI project failure reasons system design versus model performance empirical study

수집한 자료를 바탕으로 ch03의 집필에 활용할 수 있는 핵심 자료들을 정리했습니다. 아래는 JSON 형식의 최종 결과입니다.

---

```json
[
  {
    "title": "The Root Causes of Failure for Artificial Intelligence Projects and How They Can Succeed: Avoiding the Anti-Patterns of AI",
    "authors": ["James Ryseff", "Brandon F. De Bruhl", "Sydne J. Newberry"],
    "year": 2024,
    "type": "industry_report",
    "url": "https://www.rand.org/pubs/research_reports/RRA2680-1.html",
    "summary": "65명의 현업 데이터 사이언티스트·엔지니어 인터뷰를 기반으로 AI 프로젝트 실패의 5가지 근본 원인을 도출한 RAND의 경험적 연구. 가장 빈번한 실패 원인이 '모델 성능'이 아니라 '프로젝트 목적과 도메인 맥락에 대한 오해·불소통'임을 실증적으로 보여주며, 인프라 부재와 데이터 관리 미흡이 주요 구조적 문제임을 명시한다. '문제 탓이 아니라 모델 탓'이라는 귀인 오류를 반박하는 데 가장 직접적으로 활용 가능한 1차 자료.",
    "key_claims": [
      "AI 프로젝트는 일반 IT 프로젝트 대비 2배(80% 이상) 높은 실패율을 보인다",
      "가장 흔한 실패 원인은 프로젝트 목적·도메인에 대한 오해와 불소통이다",
      "성공적인 프로젝트는 기술이 아니라 해결할 문제에 집중한다",
      "데이터를 관리·배포할 인프라 부재가 실패 가능성을 높인다"
    ]
  },
  {
    "title": "Failure of AI Projects: Understanding the Critical Factors",
    "authors": ["Jens Westenberger", "Kajetan Schuler", "Dennis Schlegel"],
    "year": 2022,
    "type": "academic_paper",
    "url": "https://www.sciencedirect.com/science/article/pii/S1877050921022134",
    "summary": "다양한 산업의 AI 전문가 인터뷰를 질적 분석 방법으로 분석하여 AI 프로젝트 실패의 결정적 요인을 식별한 동료 심사 논문. 실패 원인을 '비현실적 기대', '유스케이스 문제', '조직적 제약', '핵심 자원 부족', '기술적 문제'의 5개 범주로 분류하며, 조직적·구조적 문제가 기술적 문제만큼 중요함을 실증한다. '모델 탓'이 아닌 시스템·조직 탓임을 뒷받침하는 학술적 근거로 활용 가능.",
    "key_claims": [
      "AI 프로젝트 실패는 조직적 문제와 기술적 문제 양쪽에서 기인한다",
      "비현실적 기대와 AI 역량에 대한 오해가 주요 실패 요인이다",
      "모델 불안정성(알고리즘 업데이트 시 결과 비일관성)이 프로젝트 중단을 야기한다",
      "올바르게 레이블된 훈련 데이터 확보 어려움이 핵심 실패 요인이다"
    ]
  },
  {
    "title": "Failure Factors of AI Projects: Results from Expert Interviews",
    "authors": ["Dennis Schlegel", "Kajetan Schuler", "Jens Westenberger"],
    "year": 2023,
    "type": "academic_paper",
    "url": "https://aisel.aisnet.org/ijispm/vol11/iss3/3/",
    "summary": "위 2022년 논문의 후속 확장 연구로, 더 심층적인 전문가 인터뷰를 통해 AI 실패 요인 12가지를 도출하고 5개 범주로 분류한다. 'AI 프로젝트의 실패 요인은 일반 정보시스템 프로젝트와 다르다'는 점을 강조하여, 기존의 기술 관리 프레임워크가 AI 시스템에 그대로 적용될 수 없음을 논증한다. PART 2의 설계 언어가 왜 별도로 필요한지를 정당화하는 데 유용.",
    "key_claims": [
      "모델 불안정성과 블랙박스 문제 등 기술적 요인 외에, 비기술적 요인이 더 중요한 역할을 한다",
      "AI 역량 오해와 프로젝트의 경제적 가치 부재가 주요 실패 요인이다",
      "AI 프로젝트의 실패 요인은 기존 IS 프로젝트 연구에서 도출된 것과 상이하다"
    ]
  },
  {
    "title": "Hidden Technical Debt in Machine Learning Systems",
    "authors": ["D. Sculley", "Gary Holt", "Daniel Golovin", "Eugene Davydov", "Todd Phillips", "Dietmar Ebner", "Vinay Chaudhary", "Michael Young", "Jean-François Crespo", "Dan Dennison"],
    "year": 2015,
    "type": "academic_paper",
    "url": "https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems",
    "summary": "Google 엔지니어들이 NeurIPS에 발표한 ML 시스템의 숨겨진 기술 부채를 다룬 고전적 논문. ML 시스템은 모델 코드보다 훨씬 광범위한 시스템 수준의 문제(경계 침식, 얽힘, 숨겨진 피드백 루프, 미선언 소비자, 데이터 의존성 등)를 가지며, 이러한 부채가 코드 수준이 아닌 시스템 수준에서 발생해 감지하기 어렵다고 주장한다. 'ML 코드는 전체 시스템의 작은 일부일 뿐'이라는 논거를 기술적으로 뒷받침하는 핵심 레퍼런스.",
    "key_claims": [
      "실제 ML 시스템에서는 대규모의 지속적인 유지보수 비용이 발생하는 것이 일반적이다",
      "ML 기술 부채는 코드 수준이 아니라 시스템 수준에서 존재하며, 기존 방법으로는 해소되지 않는다",
      "경계 침식, 얽힘, 숨겨진 피드백 루프, 데이터 의존성 등이 ML 고유의 위험 요인이다"
    ]
  },
  {
    "title": "The State of AI in Early 2024: Gen AI Adoption Spikes and Starts to Generate Value",
    "authors": ["Alex Singla", "Alexander Sukharevsky", "Lareina Yee", "Michael Chui"],
    "year": 2024,
    "type": "industry_report",
    "url": "https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-2024",
    "summary": "McKinsey의 1,363명 글로벌 설문 기반 AI 현황 보고서. 조직의 72%가 AI를 사용하지만 Gen AI 도입으로 의미 있는 기업 수준의 EBIT 영향을 보고하는 곳은 극소수에 불과하다는 '채택-가치 격차'를 데이터로 보여준다. AI 실패가 모델 문제가 아닌 데이터 거버넌스, 운영 모델, 스케일링 구조의 문제임을 대규모 설문으로 실증하는 자료로 활용 가능.",
    "key_claims": [
      "Gen AI를 정기적으로 사용하는 조직은 65%에 달하지만, 기업 전체 EBIT에 실질적 영향을 미치는 경우는 극소수다",
      "고성과 기업은 데이터 정의 프로세스, AI 모델 통합, 애자일 운영 모델 등 구조적 역량에서 차별화된다",
      "AI 성공의 핵심 장애물은 데이터 거버넌스 정의, 모델 통합 속도, 훈련 데이터 부족 등 시스템 문제다"
    ]
  },
  {
    "title": "Lack of AI-Ready Data Puts AI Projects at Risk",
    "authors": ["Gartner (Roxane Edjlali)"],
    "year": 2025,
    "type": "industry_report",
    "url": "https://www.gartner.com/en/newsroom/press-releases/2025-02-26-lack-of-ai-ready-data-puts-ai-projects-at-risk",
    "summary": "248명의 데이터 관리 리더를 대상으로 한 Gartner 2024년 3분기 조사 보고서. 63%의 조직이 AI에 필요한 올바른 데이터 관리 체계를 갖추지 못했으며, 2026년까지 AI 준비가 안 된 데이터로 인해 60%의 AI 프로젝트가 중단될 것이라는 예측을 제시한다. '프롬프트나 모델 교체가 아니라 데이터 파이프라인과 인프라가 문제'라는 명제의 강력한 근거로 사용 가능.",
    "key_claims": [
      "63%의 조직은 AI에 맞는 데이터 관리 체계를 갖추지 못했거나 불확실하다",
      "2026년까지 AI 준비가 안 된 데이터로 인해 60%의 AI 프로젝트가 폐기될 것으로 예측된다",
      "전통적 데이터 관리 방식은 AI 팀에게 너무 느리고 경직되어 있으며, 데이터가 사일로에 흩어져 있다"
    ]
  },
  {
    "title": "Why GenAI Projects Fail: Avoid These 5 Common Mistakes",
    "authors": ["Gartner"],
    "year": 2026,
    "type": "industry_report",
    "url": "https://www.gartner.com/en/articles/genai-project-failure",
    "summary": "Gartner가 GenAI 프로젝트의 대표 실패 패턴 5가지를 분석한 실전 가이드. 데이터 파이프라인·RAG·벡터 데이터베이스 등 AI 시스템 설계 요소를 갖추지 않으면 POC는 성공해도 프로덕션 단계에서 예산 블랙홀이 된다고 경고한다. PART 2에서 다룰 파이프라인, RAG, 가드레일의 필요성을 구체적 실패 사례로 동기부여하는 데 적합.",
    "key_claims": [
      "AI-ready 데이터 기반 없이 GenAI를 확장하면 POC 단계를 넘지 못한다",
      "RAG 데이터 파이프라인, 벡터 데이터베이스, 지식 그래프 등 시스템 설계가 선행되어야 한다",
      "기술적으로 성공한 프로젝트도 운영 비용 관리 실패로 갑작스럽게 중단될 수 있다"
    ]
  },
  {
    "title": "Why AI Projects Fail in Enterprises: Causes, Gaps, and Fixes",
    "authors": ["Futurense"],
    "year": 2026,
    "type": "blog_post",
    "url": "https://futurense.com/blog/corporate-ai-implementation-failure",
    "summary": "엔터프라이즈 AI 실패 원인을 조직 관점에서 분석한 실전 아티클. '대부분의 기업 AI 프로젝트는 모델 정확도 문제가 아니라 조직적 문제로 실패한다'고 명시하며, 워크플로 통합 부재, 소유권 부재, 비즈니스-엔지니어링 팀 불일치, 취약한 배포 계획이 핵심 원인임을 정리한다. 특히 '프롬프트 엔지니어링은 데이터 파이프라인·시스템 통합·컴플라이언스 요건·제품 전략의 결함을 고칠 수 없다'는 주장이 ch03의 핵심 논증을 직접 지지한다.",
    "key_claims": [
      "대부분의 엔터프라이즈 AI 프로젝트는 모델 정확도가 아니라 조직적 문제로 실패한다",
      "프롬프트 엔지니어링은 데이터 파이프라인, 시스템 통합, 컴플라이언스, 제품 전략 문제를 해결하지 못한다",
      "AI 실패는 실험 단계가 아니라 배포
