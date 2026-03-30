# Search: nondeterminism large language models software testing limitations assert-based verification failure

이제 충분한 자료를 수집했습니다. 검색 결과를 바탕으로 실제로 존재하며 ch02에 직접 활용 가능한 자료들을 정리합니다.

```json
[
  {
    "title": "An Empirical Study of the Non-Determinism of ChatGPT in Code Generation",
    "authors": ["Shuyin Ouyang", "Jie M. Zhang", "Mark Harman", "Meng Wang"],
    "year": 2025,
    "type": "academic_paper",
    "url": "https://dl.acm.org/doi/10.1145/3697010",
    "summary": "LLM의 비결정성이 얼마나 심각한지를 829개 코드 생성 문제에 걸쳐 실증한 논문으로, ch02의 '결정론 vs 확률론' 대비 절에서 핵심 증거 자료로 활용할 수 있다. temperature=0으로 설정해도 결정성이 보장되지 않는다는 발견은 'TDD의 무력화' 논거를 구체적 데이터로 뒷받침한다.",
    "key_claims": [
      "ChatGPT는 기본 설정에서 코드 생성 작업의 75.76%(CodeContests), 51.00%(APPS), 47.56%(HumanEval) 비율로 동일한 출력을 전혀 생성하지 않는 높은 비결정성을 보인다.",
      "temperature=0으로 설정해도 코드 생성에서의 결정성은 보장되지 않는다.",
      "비결정성은 생성 코드의 정확성·일관성을 훼손하고, LLM에 대한 개발자 신뢰를 저하시키며, 재현 가능성을 낮춘다."
    ]
  },
  {
    "title": "Non-Determinism of 'Deterministic' LLM Settings",
    "authors": ["Atil et al."],
    "year": 2025,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2408.04667",
    "summary": "결정론적으로 설정된 5개 LLM을 8개 태스크에서 10회 반복 실행해 비결정성의 범위와 영향을 체계적으로 측정한 논문이다. ch02에서 'AI는 설정상 결정론적이어도 실제로는 확률론적으로 작동한다'는 구조적 논증의 실증 근거로 직접 인용할 수 있다. 단위 테스트의 유효성 상실을 데이터로 입증하는 핵심 자료다.",
    "key_claims": [
      "결정론적 설정을 한 LLM에서도 자연 발생적 실행 간 정확도 변동이 최대 15%, 최선-최악 성능 격차가 최대 70%에 달한다.",
      "단위 테스트의 활용은 비결정성으로 인해 제한되며, 변동성을 허용하는 회귀 테스트가 대안이 될 수 있다.",
      "비결정성은 효율적인 컴퓨팅 자원 활용(공유 입력 버퍼)에 본질적으로 연결되어 있어 단기간 내 해결이 어렵다."
    ]
  },
  {
    "title": "Challenges in Testing Large Language Model Based Software: A Faceted Taxonomy",
    "authors": ["Felix Dobslaw", "Robert Feldt", "Juyeon Yoon", "Shin Yoo"],
    "year": 2025,
    "type": "academic_paper",
    "url": "https://arxiv.org/abs/2503.00481",
    "summary": "LLM 기반 소프트웨어 테스트의 핵심 난제를 4개의 분류 체계(facet)로 정리한 논문이다. 기존의 결정론적 오라클(assert 기반 검증)이 LLM의 비결정성 앞에서 왜 무력화되는지를 이론적으로 설명하며, ch02의 'TDD 무력화 선언' 절에 학술적 근거로 활용할 수 있다.",
    "key_claims": [
      "LLM과 멀티에이전트 LLM은 전통 소프트웨어나 머신러닝 소프트웨어와 다른 방식의 비결정성을 도입하며, 단순 출력 비교나 통계적 정확도 측정을 넘어서는 새로운 정확성 검증 방식이 필요하다.",
      "전통적 소프트웨어 테스트는 결정론적 오라클에 의존하지만, LLM의 확률론적 특성은 이 전제를 무너뜨린다.",
      "원자적 오라클(단일 테스트 실행 기반의 assert)은 LLM의 고유한 변동성 앞에서 종종 불충분하며, temperature=0 설정에서도 마찬가지다."
    ]
  },
  {
    "title": "You Can't Assert Your Way Out of Non-Determinism: A Practical QA Strategy for LLM Applications",
    "authors": ["(Advisor360.com, 저자 미상)"],
    "year": 2026,
    "type": "blog_post",
    "url": "https://medium.com/advisor360-com/you-cant-assert-your-way-out-of-non-determinism-a-practical-qa-strategy-for-llm-applications-fd32e617cdec",
    "summary": "assert 기반 검증이 LLM 애플리케이션에서 실패하는 순간을 생생한 서사로 묘사한 실무 향 글이다. ch02에서 기존 TDD가 실제 현장에서 어떻게 무너지는지를 독자에게 체감시키는 도입 일화나 구체적 사례로 활용하기에 적합하다.",
    "key_claims": [
      "assert output == '...'와 같은 단언문은 LLM이 의미적으로 동일하지만 표현이 다른 출력을 생성할 경우 오탐(false failure)을 일으킨다.",
      "LLM 출력을 확률 변수로 취급하고 임계값(threshold) 기반 평가로 전환해야 하며, 단일 시점의 통과/실패가 아니라 출력 분포의 시계열 변화를 추적해야 한다.",
      "LLM 시스템에서는 불확실성을 제거하는 것이 아니라 관리하는 것이 목표가 되어야 한다."
    ]
  },
  {
    "title": "LLMs Are Facing a QA Crisis: Here's How We Could Solve It",
    "authors": ["(LogRocket Blog, 저자 미상)"],
    "year": 2025,
    "type": "blog_post",
    "url": "https://blog.logrocket.com/llms-are-facing-a-qa-crisis/",
    "summary": "결정론적 코드에서 확률론적 AI로의 전환이 QA 전체에 가져온 패러다임 충격을 명료하게 서술한 글이다. ch02에서 '기존 테스트 방식이 왜 통하지 않는가'를 독자 친화적으로 설명하는 장의 도입부나 근거 문단에 활용할 수 있다.",
    "key_claims": [
      "결정론적 코드에서 확률론적 AI로의 전환은 QA에 근본적인 위기를 초래했다. 전통적 테스트는 예측 가능한 입출력을 전제하지만 LLM은 근사와 해석의 세계에서 작동한다.",
      "동일한 프롬프트가 실행마다 극적으로 다른 응답을 생성할 수 있어 기존 테스트 프레임워크를 무용지물로 만든다.",
      "TDD는 소프트웨어가 항상 2+2=4를 만족한다는 안정성을 전제로 하지만, LLM은 이 전제 자체를 파괴한다."
    ]
  },
  {
    "title": "Beyond Traditional Testing: Addressing the Challenges of Non-Deterministic Software",
    "authors": ["(AWS / DEV Community, 저자 미상)"],
    "year": 2024,
    "type": "blog_post",
    "url": "https://dev.to/aws/beyond-traditional-testing-addressing-the-challenges-of-non-deterministic-software-583a",
    "summary": "LLM을 포함한 비결정론적 소프트웨어의 테스트 난제를 실용적으로 정리한 AWS 기고 글이다. ch02에서 비결정론적 시스템이 기존 테스트 접근법과 어떻게 근본적으로 충돌하는지를 설명하는 보충 자료로 활용할 수 있다.",
    "key_claims": [
      "비결정론적 소프트웨어는 동일한 입력에 대해 겉보기에 동일한 조건에서도 다른 출력을 생성할 수 있으며, 이 예측 불가능성은 테스트에 심각한 도전을 제기한다.",
      "LLM 통합은 매번 계산될 때마다 변할 수 있는 데이터를 도입한다.",
      "AI 기반 시스템 테스트에서는 입력 프롬프트를 의도적으로 설계해 LLM의 이해를 도전하는 적대적 테스트 방식이 유효하다."
    ]
  },
  {
    "title": "Reliability for Unreliable LLMs",
    "authors": ["(Stack Overflow Blog, 저자 미상)"],
    "year": 2025,
    "type": "blog_post",
    "url": "https://stackoverflow.blog/2025/06/30/reliability-for-unreliable-llms/",
    "summary": "LLM의 비결정성이 소프트웨어 제품 전체의 신뢰성에 미치는 영향을 산업 실무자들의 목소리로 전달하는 Stack Overflow 블로그 글이다. ch02에서 비결정론의 현실적 파급 효과와 기존 디버깅·관찰 도구의 한계를 설명하는 인용 자료로 활용할 수 있다.",
    "key_claims": [
      "LLM은 근본적으로 비결정론적이어서 동일한 입력에 대해 다른 응답을 생성하며, 이 비결정성은 버그가 아니라 LLM의 특성(feature)이다.",
      "추론 모델이나 AI 에이전트를 사용할 경우, 앞 단계의 오류가 이후 단계에 누적되어 복합적 장애로 이어진다.",
      "LLM이 왜 틀렸는지 이해하고 수정하기가 매우 어렵기 때문에, 전통 소프트웨어의 감사 가능한 실행 추적 방식은 그대로 적용되지 않는다."
    ]
  },
  {
    "title": "Defeating Nondeterminism in LLM Inference",
    "authors": ["Horace He", "Thinking Machines Lab"],
    "year": 2025,
    "type": "blog_post",
    "url": "https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/",
    "summary": "LLM 추론의 비결정성이 temperature=0에서도 왜 발생하는지 부동소수점 비결합성, 동시 실행, 배치 크기 변동 등 기술적 근원을 분석한 글이다. ch02에서 LLM의 비결정성이 단순 설정 문제가 아니라 시스템 아키텍처의 구조적 속성임을 설명하는 기술 근거로 활용할 수 있다.",
    "key_claims": [
      "temperature=0으로 이론상 결정론적 샘플링을 설정해도 LLM API는 실제로는 결정론적이지 않다.",
      "부동소수점 비결합성과 GPU 병렬 실행 순서의 비결정성이 복합적으로 작용해 같은 입력에서도 다른 결과를 만든다.",
      "사용자 관점에서 다른 동시 요청자들은 시스템의 '입력'이 아니라 비결정론적 속성으로 작용하며, 배치 크기 변화가 개별 요청 결과에 영향을 미친다."
    ]
  },
  {
    "title": "AI Agents, Meet Test Driven Development",
    "authors": ["Anita (Vellum AI)"],
    "year": 2025,
    "type": "blog_post",
    "url": "https://www.latent.space/p/anita-tdd",
    "summary": "AI 에이전트 개발에 TDD를 적용하려 할 때 전통적 TDD의 전제(예측 가능한 출력)가 어떻게 무너지는지를 실무 경험 기반으로 서술한 글이다. ch02에서 TDD의 한계를 실제 팀의 관점에서 보여주는 현장 증언 자료로 활용할 수 있다.",
    "key_claims": [
      "전통적 TDD는 '알려진 입력에서
