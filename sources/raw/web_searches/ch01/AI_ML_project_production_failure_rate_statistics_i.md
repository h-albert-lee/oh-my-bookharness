# Search: AI ML project production failure rate statistics industry survey 2023 2024

수집된 자료를 충분히 확인했습니다. 이제 검증된 자료들을 장의 목적에 맞게 정리하여 JSON으로 출력합니다.

---

아래는 검색을 통해 실제 존재가 확인된 자료들을 ch01의 집필 목적(AI 프로젝트가 데모 이후 무너지는 이유, 시스템 부재로의 인식 전환, 하네스 개념 도입)에 맞춰 정리한 결과입니다.

---

**조사 과정에서 확인한 핵심 수치 요약 (JSON 이전 참고)**



RAND(2024): AI 프로젝트 실패율 80% 이상 — 非AI IT 프로젝트 대비 2배.




Gartner(2024): GenAI 프로젝트의 최소 30%가 PoC 이후 폐기될 것으로 예측.




Rexer Analytics(2023): '혁신적' ML 이니셔티브 중 배포 성공은 22%뿐. 43%는 80% 이상이 배포에 실패한다고 응답. 전체 ML 프로젝트 중 32%만 통상 배포 성공.




BCG(2024): 1,000명 CxO 대상 조사 — 74%가 AI에서 가시적 가치 미달성, 26%만 PoC를 넘어 실제 가치 창출.




Deloitte Q4 2024: 응답자 2/3 이상이 향후 3~6개월 내 실험의 30% 이하만 전사 확장될 것이라 예측.



---

```json
[
  {
    "title": "The Root Causes of Failure for Artificial Intelligence Projects and How They Can Succeed: Avoiding the Anti-Patterns of AI",
    "authors": ["James Ryseff", "Brandon F. De Bruhl", "Sydne J. Newberry"],
    "year": 2024,
    "type": "industry_report",
    "url": "https://www.rand.org/pubs/research_reports/RRA2680-1.html",
    "summary": "65명의 현업 데이터 과학자·엔지니어 인터뷰를 기반으로 한 RAND의 정량 연구로, AI 프로젝트 실패율 80% 이상(비AI IT 프로젝트 대비 2배)이라는 핵심 수치의 가장 신뢰도 높은 출처다. '시스템 부재'가 아닌 '문제 정의 실패·데이터 인프라 부재·기술 과잉 집착' 등 구조적 원인 5가지를 도출하여, ch01의 '모델이 아닌 시스템 부재' 프레이밍에 직접 인용 가능하다. 특히 'AI 프로젝트 실패의 가장 흔한 원인은 의도·목적에 대한 오해와 소통 실패'라는 발견은 하네스 부재를 설명하는 구조적 논거로 활용할 수 있다.",
    "key_claims": [
      "AI 프로젝트는 80% 이상 실패하며, 이는 非AI IT 프로젝트 실패율의 2배다.",
      "실패의 핵심 원인 5가지: ① 문제 정의 오류·소통 실패, ② 데이터 부족, ③ 기술 자체에 집착, ④ 데이터·배포 인프라 부재, ⑤ AI가 풀기 어려운 문제에 적용.",
      "성공 프로젝트는 기술이 아닌 '해결해야 할 문제' 자체에 레이저처럼 집중한다."
    ]
  },
  {
    "title": "Survey: Machine Learning Projects Still Routinely Fail to Deploy (2023 Rexer Analytics Data Science Survey 분석)",
    "authors": ["Eric Siegel", "Karl Rexer"],
    "year": 2024,
    "type": "blog_post",
    "url": "https://www.kdnuggets.com/survey-machine-learning-projects-still-routinely-fail-to-deploy",
    "summary": "데이터 과학자 328명을 대상으로 한 2023 Rexer Analytics 설문을 분석한 글로, 현장 실무자 시점에서의 ML 배포 실패율을 정량화한 보기 드문 1차 자료다. '혁신적' ML 이니셔티브의 배포 성공률 22%, 전체 프로젝트의 배포 성공률 32%라는 수치는 ch01 도입부의 충격적 현실 묘사에 직접 사용 가능하다. 또한 기술 지표(AUC, Lift)와 비즈니스 KPI 간의 단절이 배포 실패를 야기한다는 분석은 '시스템(하네스) 부재'를 설명하는 구체적 사례로 활용할 수 있다.",
    "key_claims": [
      "'혁신적' ML 이니셔티브 중 배포 성공은 22%에 불과하며, 43%의 데이터 과학자는 자신의 프로젝트 80% 이상이 배포에 실패한다고 응답했다.",
      "전체 ML 프로젝트(기존 모델 갱신 포함)의 배포 성공률은 32%다.",
      "배포의 가장 큰 장애물 상위 2개는 기술적 문제가 아닌 '의사결정자의 지원 거부'와 '능동적 계획의 부재'였다.",
      "ML 성과를 '항상 또는 대부분 측정한다'는 응답은 48%에 불과하며, 측정 시에도 비즈니스 KPI가 아닌 기술 지표를 사용한다."
    ]
  },
  {
    "title": "Gartner Predicts 30% of Generative AI Projects Will Be Abandoned After Proof of Concept By End of 2025",
    "authors": ["Rita Sallam (Gartner)"],
    "year": 2024,
    "type": "industry_report",
    "url": "https://www.gartner.com/en/newsroom/press-releases/2024-07-29-gartner-predicts-30-percent-of-generative-ai-projects-will-be-abandoned-after-proof-of-concept-by-end-of-2025",
    "summary": "Gartner의 공식 보도자료로, GenAI 프로젝트 30% 이상이 PoC 단계 이후 폐기될 것이라는 예측을 담은 권위 있는 인용 출처다. 폐기 이유로 '데이터 품질 불량, 불충분한 리스크 통제, 비용 증가, 불분명한 비즈니스 가치'를 나열하며, 이는 모두 모델 자체가 아닌 주변 시스템(하네스)의 부재를 가리킨다. ch01에서 '데모는 성공하지만 프로덕션은 실패한다'는 명제를 뒷받침하는 가장 인용 빈도 높은 공식 출처로 활용 가능하다.",
    "key_claims": [
      "최소 30%의 GenAI 프로젝트가 2025년 말까지 PoC 이후 폐기될 것으로 예측된다.",
      "폐기 주요 원인: 데이터 품질 불량, 불충분한 리스크 통제, 비용 증가, 불분명한 비즈니스 가치.",
      "GenAI는 즉각적인 ROI보다 간접적·장기적 투자 기준에 대한 높은 내성을 요구한다."
    ]
  },
  {
    "title": "AI Adoption in 2024: 74% of Companies Struggle to Achieve and Scale Value (Where's the Value in AI?)",
    "authors": ["Boston Consulting Group (BCG)"],
    "year": 2024,
    "type": "industry_report",
    "url": "https://www.bcg.com/press/24october2024-ai-adoption-in-2024-74-of-companies-struggle-to-achieve-and-scale-value",
    "summary": "59개국 1,000명 CxO 대상 조사로, 74%의 기업이 AI에서 가시적 가치를 창출하지 못하고 있음을 정량화한 대규모 글로벌 보고서다. 오직 26%만이 PoC를 넘어 실질적 가치를 창출한다는 발견은 ch01의 '데모 성공 ≠ 운영 성공'이라는 핵심 인식 전환 논지의 강력한 통계적 근거가 된다. AI 리더들이 알고리즘 10%, 기술·데이터 20%, 사람·프로세스 70%에 자원을 배분한다는 '70-20-10 규칙'은 하네스(시스템)의 필요성을 설명하는 구체적 근거로 활용 가능하다.",
    "key_claims": [
      "74%의 기업이 AI 투자에서 가시적 가치를 창출하지 못하고 있다.",
      "오직 26%만이 PoC를 넘어 실질적 가치를 창출하는 역량을 보유하고 있다.",
      "AI 리더들은 알고리즘(10%) · 기술·데이터(20%) · 사람·프로세스(70%)에 자원을 배분한다.",
      "AI 리더들은 지난 3년간 1.5배 높은 매출 성장과 1.6배 높은 주주수익률을 달성했다."
    ]
  },
  {
    "title": "The State of Generative AI in the Enterprise: Q4 2024 (Generating a New Future)",
    "authors": ["Deloitte AI Institute"],
    "year": 2024,
    "type": "industry_report",
    "url": "https://www.deloitte.com/us/en/about/press-room/state-of-generative-ai.html",
    "summary": "14개국 2,773명의 디렉터~C레벨 리더를 대상으로 한 Deloitte의 분기별 GenAI 현황 추적 보고서(Q4, 2024년 7~9월 조사)다. 응답자의 2/3 이상이 향후 3~6개월 내 자사 실험의 30% 이하만 전사 확장될 것이라고 답한 수치는 ch01의 '프로토타입-프로덕션 갭'을 뒷받침하는 직접적 데이터다. 'GenAI 기술이 빠르게 발전해도 조직 변화는 그만큼 빠르지 않다'는 통찰은 하네스의 필요성을 기술이 아닌 구조·운영 관점에서 설명하는 데 유용하다.",
    "key_claims": [
      "응답자 2/3 이상이 자사 GenAI 실험의 30% 이하만 향후 3~6개월 내 전사 확장될 것이라고 예측했다.",
      "GenAI 기술이 빠르게 발전해도, 기업의 조직 변화 속도는 그에 미치지 못한다.",
      "배포 확장의 핵심 장애물이 Q1의 기술·인재 부족에서 Q4에는 규제·리스크 통제로 이동(10%p 증가)했다.",
      "데이터 관리 개선은 가장 선도적인 기업들에게도 최우선 과제로 남아 있다."
    ]
  },
  {
    "title": "The State of AI in Early 2024: Gen AI Adoption Spikes and Starts to Generate Value",
    "authors": ["McKinsey & Company (Alex Singla, Alexander Sukharevsky, Lareina Yee, Michael Chui 외)"],
    "year": 2024,
    "type": "industry_report",
    "url": "https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-2024",
    "summary": "전 세계 1,363명을 대상으로 한 McKinsey의 연례 AI 현황 조사로, 채택률(72%)과 실제 가치 창출 간의 극명한 격차를 정량화한다. AI를 도입한 조직의 70%가 데이터 통합 속도·거버넌스 등 데이터 관련 어려움을 경험한다는 발견은 시스템 부재를 '데이터 파이프라인 하네스 부재'로 구체화하는 데 활용 가능하다. 또한 GenAI 고성과 조직(EBIT의 11% 이상을 AI에 귀속)이 명확한 거버넌스 구조와 모델 감사 체계를 갖추고 있다는 발견은 하네스 개념의 필요성을 정당화하는 대조 사례로 사용할 수 있다.",
    "key_claims": [
      "2024년 초 기준 65%의 조직이 Gen
