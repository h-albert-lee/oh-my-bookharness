# Search: demo to production gap LLM application reliability engineering blog

검색 결과를 충분히 수집했습니다. 이제 실제로 존재하는 자료만 엄선하여 JSON 형태로 정리합니다.

---

아래는 검색 결과를 바탕으로 실제 존재가 확인된 자료만 엄선하여 정리한 JSON입니다. 각 항목에 대한 근거 인용을 함께 제공합니다.

---

### 근거 요약 (각 자료의 핵심 주장 출처)

**1. ZenML — The Agent Deployment Gap**


실제 배포 문제는 예상과 다르다. LLM이 더 잘 추론하게 만드는 것도, 올바른 프레임워크를 고르는 것도 핵심이 아니다. 엔지니어들을 밤새 깨어있게 만드는 문제는 훨씬 더 평범하고 훨씬 더 치명적이다.

 

Toqan의 사례처럼, 에이전트는 자연어를 SQL로 변환하며 "마법 같은" 순간을 보여줬지만, 프로덕션에서는 무한 루프, 58~59회 반복 응답 등 심각한 신뢰성 문제가 나타났다.



**2. ZenML — What 1,200 Production Deployments Reveal**


데모와 프로덕션 간의 격차를 줄이려면 AI를 장애를 우아하게 처리하고, 예측 가능하게 확장하며, 기존 인프라와 통합하는 시스템으로 감싸야 한다. 프로덕션에서 성공하는 팀은 깊은 시스템 엔지니어링 전문성으로 정의된다.



**3. OneUptime — How to Build Production-Ready LLM Applications**


데모를 만드는 데는 하루면 충분하다. 하지만 동일한 애플리케이션을 프로덕션에서 합리적인 비용과 예측 가능한 동작으로 안정적으로 실행하는 데는 수개월의 엔지니어링 작업이 필요하다. LLM 기반 애플리케이션의 프로토타입과 프로덕션 사이의 격차는 대부분의 팀이 예상하는 것보다 훨씬 크다.



**4. Martinfowler.com — Engineering Practices for LLM Application Development**


LLM과 프롬프트 엔지니어링은 LLM 애플리케이션을 프로덕션에 배포하는 데 필요한 것의 극히 일부에 불과하다. 그 외에도 많은 기술적 고려 사항과 제품 및 고객 경험 고려 사항이 있다.



**5. Galileo — LLM Reliability Evaluation Methods**


MMLU, TruthfulQA 같은 벤치마크에서의 높은 점수는 현실 세계 준비성에 대한 허위 확신을 줄 수 있다. 테스트 환경에서 성공한 모델이 사용자가 질문을 바꾸거나 낯선 맥락을 도입하면 자주 어려움을 겪어, 벤치마크 성능과 실제 신뢰성 간의 깊은 단절을 드러낸다.



**6. Thinking Machines Lab — Defeating Nondeterminism in LLM Inference**


재현성은 과학적 진보의 근석이다. 그러나 LLM에서 재현 가능한 결과를 얻는 것은 매우 어렵다. 예를 들어, 동일한 질문을 ChatGPT에 여러 번 해도 다른 결과가 나오는 것을 관찰할 수 있다. 이는 언어 모델의 출력을 확률 분포로 변환하고 확률적으로 토큰을 선택하는 '샘플링' 과정 때문이다.



**7. ACL Anthology — Non-Determinism of "Deterministic" LLM Settings (학술 논문)**


결정론적으로 구성된 5개의 API 기반 LLM을 8개의 다양한 태스크에 걸쳐 10회 실행하여 실험했다. 실행 간 최대 15% 정확도 편차와 최선 및 최악 성능 간 최대 70% 격차가 드러났다. 어떤 LLM도 태스크에 무관하게 동일한 출력이나 정확도를 일관되게 제공하지 않았다.



**8. Stack Overflow Blog — Reliability for Unreliable LLMs**


제너레이티브 AI 기술이 소프트웨어 제품과 워크플로우에 더 깊이 통합될수록, 그 제품과 워크플로우 자체가 LLM을 닮아간다. 덜 신뢰할 수 있고, 덜 결정론적이며, 때로는 틀리게 된다. LLM은 근본적으로 비결정론적이며, 같은 입력에 다른 응답을 생성한다. 추론 모델과 AI 에이전트를 사용하면 초기 실수가 이후 단계에서 사용될 때 오류가 복합된다.



**9. RAND Corporation — The Root Causes of Failure for Artificial Intelligence Projects**


일부 추정치에 따르면 AI 프로젝트의 80% 이상이 실패하며, 이는 AI를 포함하지 않는 IT 프로젝트 실패율의 두 배이다. 따라서 AI의 엄청난 잠재력을 구체적인 결과로 전환하는 방법을 이해하는 것이 시급한 과제로 남아 있다.



**10. Martinfowler.com — Harness Engineering**


마틴 파울러는 'harness'라는 단어가 AI 에이전트를 통제하기 위한 툴링과 실천의 집합을 묘사하는 데 적합하다고 본다. OpenAI 팀의 하네스 컴포넌트는 컨텍스트 엔지니어링, 결정론적·LLM 기반 접근 방식을 혼합한다.



---

```json
[
  {
    "title": "The Agent Deployment Gap: Why Your LLM Loop Isn't Production-Ready (And What to Do About It)",
    "authors": ["ZenML Team"],
    "year": 2025,
    "type": "blog_post",
    "url": "https://www.zenml.io/blog/the-agent-deployment-gap-why-your-llm-loop-isnt-production-ready-and-what-to-do-about-it",
    "summary": "데모에서 잘 작동하던 에이전트가 프로덕션에서 무한 루프, 반복 응답 등의 심각한 신뢰성 문제에 부딪히는 구체적 사례(Toqan)를 서술한다. '데모 이후 무너지는 이유'를 설명하는 첫 장의 도입 사례로 직접 활용 가능하며, 실패 원인이 모델이 아닌 시스템 부재임을 실증한다. 또한 '진짜 문제는 모델 성능이 아니라 운영 인프라'라는 이 장의 핵심 논지를 현장 데이터로 뒷받침한다.",
    "key_claims": [
      "실제 배포 문제는 모델 추론 품질이나 프레임워크 선택이 아니라, 훨씬 평범하고 운영적인 이슈에서 비롯된다",
      "프로토타입과 프로덕션 사이의 격차는 팀이 자체 호스팅을 선택하는 순간 예상 이상의 무게로 드러난다",
      "에이전트 워크로드는 예측 불가능한 스케일링 패턴을 만들며, 전통적인 오토스케일링으로는 대응이 어렵다"
    ]
  },
  {
    "title": "What 1,200 Production Deployments Reveal About LLMOps in 2025",
    "authors": ["ZenML Team"],
    "year": 2025,
    "type": "blog_post",
    "url": "https://www.zenml.io/blog/what-1200-production-deployments-reveal-about-llmops-in-2025",
    "summary": "1,200건 이상의 실제 프로덕션 배포 사례를 분석한 대규모 실증 보고서로, 프로덕션 성공 팀과 실패 팀을 가르는 핵심 차이가 '프롬프트 품질'이 아닌 '시스템 엔지니어링 역량'임을 보여준다. 이 장에서 '시스템 부재'로의 인식 전환을 뒷받침하는 정량적 근거로 활용하기 좋다. '데모와 프로덕션의 격차를 줄이려면 AI를 시스템으로 감싸야 한다'는 하네스 개념의 당위성을 지지한다.",
    "key_claims": [
      "데모와 프로덕션 간 격차를 줄이는 것은 AI를 장애를 우아하게 처리하고 예측 가능하게 확장하는 시스템으로 래핑함으로써 가능하다",
      "프로덕션에서 성공하는 팀은 프롬프트 품질이 아닌 깊은 시스템 엔지니어링 전문성으로 정의된다",
      "가장 신뢰할 수 있는 가드레일은 프롬프트가 아닌 코드(인프라)로 구현된다"
    ]
  },
  {
    "title": "How to Build Production-Ready LLM Applications",
    "authors": ["Nawaz (OneUptime)"],
    "year": 2025,
    "type": "blog_post",
    "url": "https://oneuptime.com/blog/post/2025-09-01-production-llm-apps/view",
    "summary": "프로덕션 LLM 앱은 단순한 API 래퍼가 아니라 탄력성·관찰 가능성·비용 효율성을 갖춘 다층 시스템임을 실용적으로 설명한다. 데모를 만드는 데는 하루, 프로덕션 준비에는 수개월이 필요하다는 명확한 대비 구조는 이 장 1절의 도입 문장으로 인용하기에 적합하다. 단계를 건너뛰는 팀이 어떤 방식으로 예측 불가한 실패를 겪는지를 구체적으로 기술한다.",
    "key_claims": [
      "프로덕션 LLM 애플리케이션은 OpenAI API 호출을 웹 서버로 감싼 것 이상의 존재다—탄력성·관찰 가능성·비용 효율을 갖춘 다중 컴포넌트 시스템이다",
      "데모 제작에는 하루, 같은 앱을 프로덕션에서 안정적으로 운영하는 데는 수개월의 엔지니어링 작업이 필요하다",
      "단계를 건너뛰는 팀은 예측 불가한 방식으로 실패하고 비용도 더 많이 드는 프로덕션 서비스를 갖게 된다"
    ]
  },
  {
    "title": "Engineering Practices for LLM Application Development",
    "authors": ["David Tan", "Jessie Wang"],
    "year": 2024,
    "type": "blog_post",
    "url": "https://martinfowler.com/articles/engineering-practices-llm.html",
    "summary": "Thoughtworks 팀이 실제 LLM 애플리케이션(AI Concierge POC) 구축 경험을 바탕으로, 프롬프트 설계만으로는 부족하고 테스트·리팩터링·아키텍처 분리 등 전통적 소프트웨어 엔지니어링 실천이 필수임을 보여준다. '모델 성능이 아닌 시스템 설계 부재'라는 이 장의 핵심 인식 전환을 실무 사례로 지지하며, martinfowler.com이라는 업계 권위 있는 플랫폼의 신뢰도를 활용할 수 있다.",
    "key_claims": [
      "LLM과 프
