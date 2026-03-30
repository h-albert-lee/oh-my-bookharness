# Search: LLM pipeline information flow data contract structured output parsing retry fallback design

수집된 자료를 바탕으로 ch04 집필에 활용 가능한 핵심 자료들을 정리합니다. 검색 결과에서 실제로 존재하는 자료만 선별하여 JSON 형식으로 제공합니다.

---

```json
[
  {
    "title": "Building LLM Applications for Production",
    "authors": ["Chip Huyen"],
    "year": 2023,
    "type": "blog_post",
    "url": "https://huyenchip.com/2023/04/11/llm-engineering.html",
    "summary": "LLM 파이프라인을 프로덕션 수준으로 올리는 과정에서 마주치는 핵심 도전들(출력 비결정성, 파싱 불가 응답, 제어 흐름 설계 등)을 체계적으로 분류한다. 특히 '파이프라인 내 각 태스크를 독립적으로 빌드·테스트해야 신뢰 가능한 에이전트가 된다'는 명제는 ch04의 구성 요소 분리 논거의 핵심 근거로 쓸 수 있다. 순차/병렬/조건부 제어 흐름 분류는 파이프라인 구성 요소 설명의 뼈대로 활용 가능하다.",
    "key_claims": [
      "LLM 애플리케이션을 프로덕션화하기 어려운 이유는 주로 모델 자체가 아니라 시스템 엔지니어링 리거 부족 때문이다.",
      "에이전트의 제어 흐름은 순차(sequential), 병렬(parallel), 조건(if), 반복(for loop)으로 분류할 수 있으며, 조건 자체가 LLM 프롬프팅으로 결정될 수 있다.",
      "에이전트가 신뢰 가능하려면 각 태스크를 합치기 전에 독립적으로 빌드·테스트할 수 있어야 한다."
    ]
  },
  {
    "title": "LLM Structured Outputs: Schema Validation for Real Pipelines",
    "authors": ["Collin Wilkins"],
    "year": 2026,
    "type": "blog_post",
    "url": "https://collinwilkins.com/articles/structured-output",
    "summary": "LLM 출력 처리 단계를 '데이터 생산자(data producer)'로 재정의하고, 스키마 설계·버전 관리·검증 실패 처리까지 프로덕션 파이프라인에서 구조화 출력을 다루는 실용적 패턴을 정리한다. ch04의 '출력 처리' 구성 요소가 왜 독립 설계 단위여야 하는지 논거로 쓰기 좋고, 스키마를 API 설계처럼 다뤄야 한다는 관점은 'data contract' 개념과 자연스럽게 연결된다.",
    "key_claims": [
      "구조화 출력은 LLM을 신뢰할 수 있는 '데이터 생산자'로 전환시킨다.",
      "스키마 변경은 명시적이어야 하며, schema_version과 prompt_version을 로그에 기록해야 롤백과 감사가 가능하다.",
      "검증에 실패한 출력은 다운스트림 시스템에 진입하지 않아야 하며, 이로써 '묵시적 오염'이 아닌 '처리된 오류'로 실패 모드가 바뀐다."
    ]
  },
  {
    "title": "LLM Structure Outputs: The Silent Hero of Production AI",
    "authors": ["Decoding AI (newsletter)"],
    "year": 2025,
    "type": "blog_post",
    "url": "https://www.decodingai.com/p/llm-structured-outputs-the-only-way",
    "summary": "구조화 출력을 'LLM(Software 3.0)과 애플리케이션 코드(Software 1.0) 간의 공식 계약(formal contract)'으로 정의하며, 확률적 모델과 결정론적 코드를 연결하는 개념적 인터페이스로 설명한다. ch04에서 '데이터 계약(data contract)'이 왜 LLM 파이프라인의 구성 요소 경계를 정의하는가를 설명할 때 핵심 인용 지점으로 활용할 수 있다.",
    "key_claims": [
      "구조화 출력은 LLM(Software 3.0)과 애플리케이션 코드(Software 1.0) 사이의 공식 계약으로, 확률적 LLM 출력과 결정론적 코드를 연결하는 표준 방법이다.",
      "구조화 출력이 없으면 데이터 검증, 타입 체크, 출력 형식 제어가 불가능해 프로덕션에서 취약해진다.",
      "JSON Schema는 LLM에게 어떤 데이터를 생성해야 하는지 알려주는 계약이며, 필드, 타입, 검증 규칙을 명시한다."
    ]
  },
  {
    "title": "The guide to structured outputs and function calling with LLMs",
    "authors": ["Agenta Team"],
    "year": 2025,
    "type": "blog_post",
    "url": "https://agenta.ai/blog/the-guide-to-structured-outputs-and-function-calling-with-llms",
    "summary": "구조화 출력을 얻는 방법(API native, JSON mode, Pydantic, Instructor, Outlines)을 비교 분류하고 각각의 실패 모드를 분석한다. 파싱 전략과 fallback 선택 기준을 구성 요소 수준에서 설명하므로, ch04의 '출력 처리 컴포넌트'가 왜 여러 하위 전략을 캡슐화해야 하는지 보여주는 참고 자료로 적합하다.",
    "key_claims": [
      "스키마를 한 번 정의하고 JSON Schema로 변환하여 LLM에 전달한 뒤 원래 모델로 검증하는 것이 완전한 파이프라인을 구성하는 패턴이다.",
      "비 네이티브 방식(prompt engineering + 외부 파서)은 유연하지만 LLM이 형식을 어기거나 비일관적 결과를 낼 수 있어 취약하다.",
      "프롬프트가 테스트에서 완벽히 작동하다가 모델 업데이트 후 실패하기 시작하는 것이 프로덕션의 실질적 문제다."
    ]
  },
  {
    "title": "LLM Structured Output in 2026: Stop Parsing JSON with Regex and Do It Right",
    "authors": ["Pockit Tools"],
    "year": 2026,
    "type": "blog_post",
    "url": "https://dev.to/pockit_tools/llm-structured-output-in-2026-stop-parsing-json-with-regex-and-do-it-right-34pk",
    "summary": "2026년 기준 프로덕션 LLM 시스템에서 구조화 출력이 선택이 아닌 필수임을 선언하며, OpenAI·Anthropic·Gemini 간 네이티브 구조화 출력의 차이, 거절(refusal) 처리, 잘림(truncation) 처리, fallback chain 설계를 실전 패턴으로 정리한다. ch04의 'fallback 및 retry 설계' 섹션에 직접 참조할 수 있는 최신 실무 자료다.",
    "key_claims": [
      "복잡한 스키마는 비용이 크므로 더 작은 병렬 호출로 쪼개야 한다.",
      "거절·잘림·빈 배열·enum 혼동은 프로덕션에서 반드시 처리해야 하는 엣지 케이스다.",
      "단일 프로바이더는 100% 신뢰할 수 없으므로 중요 경로에는 멀티 프로바이더 fallback chain을 구축해야 한다."
    ]
  },
  {
    "title": "Handling LLM Output Parsing Errors (Prompt Engineering for LLM Application Development, Ch.7)",
    "authors": ["APXML"],
    "year": 2024,
    "type": "documentation",
    "url": "https://apxml.com/courses/prompt-engineering-llm-application-development/chapter-7-output-parsing-validation-reliability/handling-parsing-errors",
    "summary": "파싱 오류 발생 시 '단순 재시도 → 수정 프롬프트로 재시도 → fallback' 순서로 계층화된 오류 처리 전략을 체계적으로 설명한다. 파싱 실패의 원인 유형(예상 외 콘텐츠, 잘린 생성 등)과 각 대응 전략을 구분 설명하므로, ch04의 '출력 처리 컴포넌트 내 오류 처리 설계' 섹션에 구조적 틀로 활용할 수 있다.",
    "key_claims": [
      "파싱 실패 시 대응 전략은 단순 재시도 → 수정 프롬프트(오류 메시지 포함)로 재시도 → fallback 기본값 반환의 계층 구조를 따른다.",
      "LLM의 확률적 특성, 네트워크 문제, 모델 결함이 파싱 실패를 야기할 수 있으며, 이를 무시하면 애플리케이션 크래시나 잘못된 데이터 처리로 이어진다.",
      "'오류 메시지를 포함한 수정 프롬프트'로 LLM에게 이전 출력의 문제를 알려주면 성공률을 높일 수 있다."
    ]
  },
  {
    "title": "Error Handling and Retry Strategies for LLM Applications (LLM Output Parsing and Structured Generation Guide)",
    "authors": ["Tetrate"],
    "year": 2025,
    "type": "documentation",
    "url": "https://tetrate.io/learn/ai/llm-output-parsing-structured-generation",
    "summary": "LLM 출력 파싱 파이프라인의 오류 처리 패턴—exponential backoff retry, partial success handling, fallback 동작 문서화, 모니터링/알림, 프롬프트·스키마 버전 관리—을 망라한 실용 가이드다. ch04의 '출력 처리 컴포넌트'가 왜 단순 파싱 이상의 복잡성을 가지는지, 그리고 왜 독립 설계 단위가 되어야 하는지를 뒷받침하는 논거들을 제공한다.",
    "key_claims": [
      "Exponential backoff는 반복 실패로 인한 retry storm을 방지하며, 최대 재시도 후에는 적절한 오류 메시지나 fallback으로 graceful하게 실패해야 한다.",
      "배치 처리에서 일부 아이템만 성공할 경우, 전체 배치를 거부하는 것보다 유효한 아이템을 처리하고 실패를 플래깅하는 실용적 접근이 가치를 극대화한다.",
      "프롬프트와 스키마에 명시적 버전을 부여하고 환경별 배포 버전을 추적해야 변경으로 인한 혼란을 막을 수 있다."
    ]
  },
  {
    "title": "Complex data extraction with function calling (LangGraph Retries Tutorial)",
    "authors": ["LangChain AI"],
    "year": 2024,
    "type": "documentation",
    "url": "https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/",
    "summary": "LangGraph를 활용한 구조화 데이터 추출에서 ValidationNode와 RetryStrategy(max_attempts, fallback LLM)를 결합한 retry 패턴을 코드 수준으로 설명한다. 'retry는 함수 호출 실패를 줄이는 쉬운 방법이지만, 데이터 검증은 LLM이 소프트웨어 스택의 나머지와 상호작용하는 방식을 제어하기 위해 여전히 중요하다'는 주장은 ch04의 파이프라인 경계 설계 논거로 인용 가능하다.",
    "key_claims": [
      "retry는 함수 호출 실패를 줄이는 쉬운 방법이지만, 더 강력한 LLM이 등장해도 데이터 검증은 LLM과 소프트웨어 스택 사이의 상호작용을 제어하기 위해 여전히 필수적이다.",
      "높은 retry 비율이 관찰되면, 실패 케이스를 데이터셋으로 수집하고 수정 값을 프롬프트나 스키마에 자동 반영하는 피드백 루프를 구축할 수 있다.",
      "RetryStrategy는 max_attempts, fallback LLM, 메시지 집계 함수를 파라미터로 받아 재시도 정책을 명시적으로 선언할 수
