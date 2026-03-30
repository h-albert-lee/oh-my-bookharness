# Search: "system boundary" AI system design reliability observability feedback loop failure

충분한 자료를 수집했습니다. 이제 JSON 형식으로 정리합니다.

---

검색 결과를 바탕으로, **실제로 존재하고 URL이 확인된 자료**만 선별하여 ch03 집필에 활용 가능한 참고자료 목록을 아래와 같이 정리합니다.

```json
[
  {
    "title": "Hidden Technical Debt in Machine Learning Systems",
    "authors": ["D. Sculley", "Gary Holt", "Daniel Golovin", "Eugene Davydov", "Todd Phillips", "Dietmar Ebner", "Vinay Chaudhary", "Michael Young", "Jean-François Crespo", "Dan Dennison"],
    "year": 2015,
    "type": "academic_paper",
    "url": "https://proceedings.neurips.cc/paper_files/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html",
    "summary": "ML 시스템이 단순히 '모델'이 아닌 복잡한 시스템임을 보여주는 고전적 논문으로, 'boundary erosion(시스템 경계 침식)', 'entanglement(엉킴)', 'hidden feedback loops(숨겨진 피드백 루프)' 등 ML 특유의 기술 부채 개념을 소개한다. ch03의 핵심 주장인 '문제는 모델이 아니라 시스템이다'를 뒷받침하는 가장 강력한 학술적 근거로 활용 가능하다. 특히 시스템 경계가 무너질 때 유지보수 비용이 폭발적으로 증가함을 구체적으로 논증하여, 설계 부재의 구조적 귀결을 독자에게 설득력 있게 전달할 수 있다.",
    "key_claims": [
      "ML 시스템은 코드 자체보다 시스템 수준의 상호작용과 인터페이스에서 기술 부채가 급격히 누적된다 (system-level interactions and interfaces as an area where ML technical debt may rapidly accumulate)",
      "ML 모델은 추상화 경계를 조용히 침식시킨다 — 'an ML model may silently erode abstraction boundaries'",
      "외부 세계의 변화가 시스템 동작에 의도치 않은 방식으로 영향을 미치며, 모니터링 자체도 신중한 설계 없이는 어렵다",
      "숨겨진 피드백 루프(hidden feedback loops), 미선언 소비자(undeclared consumers), 데이터 의존성 등이 시스템 레벨의 안티패턴을 형성한다"
    ]
  },
  {
    "title": "Underspecification Presents Challenges for Credibility in Modern Machine Learning",
    "authors": ["Alexander D'Amour", "Katherine Heller", "Dan Moldovan", "Ben Adlam", "et al.", "D. Sculley"],
    "year": 2022,
    "type": "academic_paper",
    "url": "https://www.jmlr.org/papers/v23/20-1335.html",
    "summary": "ML 파이프라인이 훈련 도메인에서 동등한 성능을 내는 수많은 모델을 반환할 수 있는 '과소명세(underspecification)' 문제를 실증적으로 분석한다. 동일한 파이프라인에서 나온 모델들이 배포 환경에서 전혀 다르게 행동한다는 점을 보여줌으로써, '더 좋은 모델'이 문제를 해결하지 못하는 이유를 구조적으로 설명한다. ch03의 귀인 전환('모델이 나쁜 게 아니라 파이프라인/시스템이 설계되지 않았다')을 학술적으로 뒷받침하는 데 직접 활용 가능하다.",
    "key_claims": [
      "ML 시스템은 훈련 도메인 성능이 동등한 수많은 모델을 반환할 수 있으며, 이들은 배포 환경에서 매우 다르게 행동할 수 있다",
      "과소명세는 기존에 식별된 train-test 분포 불일치와는 별개의, 독립적인 실패 모드다",
      "표준 ML 파이프라인은 실제 배포 행동을 완전히 명세하지 않으며, 임의적인 선택(랜덤 시드 등)이 실세계 행동을 결정한다",
      "모델 교체나 재훈련만으로는 이 문제가 해결되지 않으며, 파이프라인 설계 자체를 명시적으로 다루어야 한다"
    ]
  },
  {
    "title": "Why Do Multi-Agent LLM Systems Fail?",
    "authors": ["Mert Cemri", "Melissa Z. Pan", "Shuyi Yang", "Lakshya A. Agrawal", "Bhavya Chopra", "Rishabh Tiwari", "Kurt Keutzer", "Aditya Parameswaran", "Dan Klein", "Kannan Ramchandran", "Matei Zaharia", "Joseph E. Gonzalez", "Ion Stoica"],
    "year": 2025,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2503.13657",
    "summary": "1600개 이상의 실제 다중 에이전트 시스템(MAS) 실행 트레이스를 분석해 최초의 MAS 실패 분류 체계(MAST)를 구축한 NeurIPS 2025 논문이다. 14가지 실패 모드가 (i) 시스템 설계 이슈, (ii) 에이전트 간 정렬 실패, (iii) 작업 검증 실패의 3범주로 묶이며, 개입 케이스 스터디를 통해 동일 모델로도 시스템 설계 개선만으로 최대 15.6% 성능 향상이 가능함을 보여준다. 'MAS 실패는 LLM 한계가 아니라 시스템 설계 문제에서 비롯된다'는 직접적 주장이 ch03의 핵심 테제와 정확히 맞닿아 있어, 최신 실증 근거로 적극 인용 가능하다.",
    "key_claims": [
      "MAS 실패는 LLM 자체의 한계나 단순한 프롬프트 문제가 아니라 시스템 설계 이슈에서 기인하는 경우가 많다",
      "동일한 기반 모델 아래에서도 시스템 설계 개선만으로 최대 15.6%의 성능 향상을 달성할 수 있다",
      "실패 이해를 위해서는 단순 오류 감지가 아니라 시스템의 동적 특성(dynamics)을 이해해야 한다",
      "에이전트 간의 복잡한 상호작용과 개별 모델 행동의 복합적 효과가 MAS 실패의 핵심 원인이다"
    ]
  },
  {
    "title": "AI Systems Don't Fail, Interface Design Is The Problem",
    "authors": ["Xite.ai Editorial"],
    "year": 2026,
    "type": "blog_post",
    "url": "https://xite.ai/blogs/ai-systems-dont-fail-interfaces-between-humans-data-and-models-do/",
    "summary": "기업 AI 운영 실패의 근본 원인이 모델 알고리즘이 아니라 인간 판단, 데이터 파이프라인, 자동화된 의사결정이 명확한 경계 없이 만나는 '인터페이스'에 있다는 주장을 전개한다. '도구는 독립적으로 평가할 수 있지만 시스템은 그럴 수 없다(Tools can be evaluated in isolation. Systems cannot)'는 핵심 명제는 ch03의 귀인 전환을 독자에게 직관적으로 전달하는 훌륭한 도입 문구로 활용 가능하다. 실패가 어떻게 시스템 경계에서 발생하는지를 실무 사례를 통해 구체적으로 설명한다.",
    "key_claims": [
      "대부분의 기업 AI 실패는 약한 모델, 편향된 알고리즘, 나쁜 프롬프트 때문이 아니라 인터페이스—인간 판단, 데이터 파이프라인, 자동화된 의사결정이 경계·책임·거버넌스 없이 만나는 지점—에서 발생한다",
      "모델은 설계된 대로 정확하게 동작하고 있을 수 있다. 실패는 그 출력이 불완전한 데이터, 모호한 의사결정 권한, 자동화를 위해 재설계되지 않은 인간 워크플로우와 교차할 때 나중에 드러난다",
      "성공 지표를 전환해야 한다: 모델이 잘 수행하는지가 아니라 시스템이 실제 조건 하에서 안정적으로 동작하는지를 평가해야 한다",
      "AI를 도구로 취급하는 많은 AI 이니셔티브가 실패한다. 도구는 독립적으로 평가할 수 있지만 시스템은 그럴 수 없다"
    ]
  },
  {
    "title": "Why Most AI Failures Aren't Model Failures — They're Integration Failures",
    "authors": ["Craigstueber"],
    "year": 2026,
    "type": "blog_post",
    "url": "https://medium.com/@craigstueber/why-most-ai-failures-arent-model-failures-they-re-integration-failures-fdec486f67ba",
    "summary": "AI 프로덕션 실패의 실체가 '통합 실패(integration failure)'임을 주장하며, 이를 'integration debt'라는 개념으로 명명한다. 모델 평가(eval)에서는 보이지 않고 프로덕션 인시던트에서만 드러나는 실패 패턴을 구체적으로 설명하며, '오류는 기술적 결함처럼 보이고, 실패는 지능의 문제로 귀인된다'는 함정을 날카롭게 지적한다. ch03의 핵심 메시지—'더 좋은 모델을 찾는 것이 아니라 시스템을 설계해야 한다'—를 실무 독자에게 전달하는 데 매우 적합한 실용 문헌이다.",
    "key_claims": [
      "대부분의 AI 위험은 모델이 생성하는 것에서 오는 것이 아니라 시스템이 그 생성물로 무엇을 하는지에서 온다",
      "모델이 통합되면 더 이상 독립적으로 작동하지 않는다: 통제하지 못하는 입력을 받고, 예상치 못한 타이밍에 호출되며, 압박 상황의 사용자에게 해석되고, 검토 없이 출력을 자동화하는 워크플로우에 내장된다",
      "'통합 부채(integration debt)'는 코드 리뷰나 백로그에 나타나지 않고 사용자, 타이밍, 동작에 대한 문서화되지 않은 기대값 속에 산다",
      "오류는 기술적 결함처럼 보이고, 실패는 지능의 문제로 귀인된다. 그래서 조직은 실제로 필요한 것(더 안전한 시스템)이 아니라 더 나은 모델을 쫓게 된다"
    ]
  },
  {
    "title": "When AI Fails, What Works? A Data-Driven Taxonomy of Real-World AI Risk Mitigation Strategies",
    "authors": ["Evgenija Popchanovska", "et al."],
    "year": 2025,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2603.04259",
    "summary": "9,705건의 실제 미디어 보고 AI 인시던트를 분석해, 실패가 고립된 모델 오류를 넘어 엔드투엔드 시스템 취약성으로 전파되는 방식을 실증적으로 보여준다. '모델 중심 위험에서 시스템 전체 취약성으로의 전환(shift from model-centric risks to end-to-end system vulnerabilities)'이라는 핵심 프레이밍은 ch03의 귀인 전환 논거를 강화하는 데 직접 활용 가능하다. 또한 '진단에서 처방으로' 이어지는 프레임워크를 제시해, 시스템 설계로 실패를 해결 가능하다는 낙관적 결론을 뒷받침한다.",
    "key_claims": [
      "LLM은 고위험 워크플로우에 점점 더 깊이 내장되고 있으며, 실패는 고립된 모델 오류를 넘어 법적 노출, 평판 손상, 실질적 재정 손실로 이어지는 시스템 붕괴로 전파된다",
