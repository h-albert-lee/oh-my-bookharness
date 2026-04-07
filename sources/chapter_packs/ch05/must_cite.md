# Must-Cite Items — ch05: RAG를 기능이 아니라 아키텍처로 이해하기

---

## Tier 1 — 반드시 인용 (장의 핵심 논지를 직접 뒷받침)

---

### web_01
**Lewis et al., "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks" (2020)**

**인용 이유**
RAG 개념의 원점 논문. 이 장의 첫 번째 핵심 질문—"LLM은 왜 지식을 신뢰하기 어려운가"—에 대한 구조적 근거를 제공한다. 파라메트릭 메모리(parametric memory)와 비파라메트릭 메모리(non-parametric memory)의 구분은, "RAG는 기능이 아니라 정보 흐름을 설계하는 것"이라는 장의 핵심 주장을 개념적으로 정초하는 언어다.

**활용 포인트**
- LLM이 지식을 모델 가중치 안에 압축 저장한다는 구조적 설명 → "왜 LLM 단독으로는 지식을 신뢰하기 어려운가"의 근거
- retrieval + generation의 결합을 처음부터 단일 아키텍처 결정으로 프레이밍한 논문 → "RAG는 기능 추가가 아니라 아키텍처 선택"이라는 주장의 출발 인용

**인용 위치 제안**
장 도입부, LLM의 구조적 한계를 설명하는 절

---

### web_03
**Barnett et al., "Seven Failure Points When Engineering a Retrieval Augmented Generation System" (2024)**

**인용 이유**
이 장의 세 번째 목표—"RAG를 잘못 설계했을 때 발생하는 실패를 아키텍처 문제로 재정의한다"—를 직접 지지하는 핵심 자료. 7가지 실패 지점을 구체적으로 열거하며, 각각이 검색 버그가 아니라 파이프라인 설계 결함임을 보여준다. 실무 팀이 "검색이 이상하다"고 표현하는 문제를 설계 언어로 재기술하는 근거로 가장 직접적이다.

**활용 포인트**
- Missing content, Missed top ranked docs, Not in context, Not extracted, Wrong format, Incorrect specificity, Incomplete — 각 실패가 파이프라인의 어느 단계 설계 결함인지 매핑 가능
- 독자에게 "실패 진단 언어"를 제공하는 절에서 구체적 사례로 활용
- "RAG는 기능이다"라는 오해가 낳는 실제 비용을 보여주는 반증 사례

**인용 위치 제안**
실패 유형 분류 절, 아키텍처 문제 재정의 절

---

### web_07
**"Retrieval Augmented Generation (RAG) — Architecture Pattern"**

**인용 이유**
RAG를 단순 기능이 아니라 아키텍처 패턴으로 명시적으로 정의하는 자료. 이 장의 관점 전환—"RAG는 검색 기능이다 → RAG는 정보 흐름 통제 아키텍처다"—을 가장 직접적으로 언어화한 실무 레퍼런스. 파이프라인의 각 단계가 정보 흐름의 어느 지점을 담당하는지 구조적으로 기술하는 데 활용 가능하다.

**활용 포인트**
- RAG를 "패턴(pattern)"으로 명시하는 프레이밍 자체가 인용 가치 — 이 장의 제목 논지("기능이 아니라 아키텍처")를 외부 권위로 지지
- 각 구성 단계(인덱싱, 검색, 증강, 생성)가 수행하는 정보 통제 역할을 설명하는 절에서 구조 도식의 출처로 활용

**인용 위치 제안**
RAG 구성 단계 설명 절, 관점 전환 논지 도입 시

---

## Tier 2 — 강력 권장 인용 (장의 논지를 심화하거나 확장하는 데 필요)

---

### web_02
**"Retrieval-Augmented Generation for Large Language Models: A Survey" (2024)**

**인용 이유**
Naive RAG → Advanced RAG → Modular RAG로의 진화 계보를 체계적으로 정리한 서베이. 이 장이 RAG를 단순 기능이 아닌 설계 결정의 축적으로 설명할 때, 그 역사적·구조적 맥락을 제공한다. RAG가 왜 아키텍처로 진화할 수밖에 없었는지를 보여주는 계보 자료.

**활용 포인트**
- Naive RAG의 한계(정밀도 낮음, 컨텍스트 초과, 중복 정보)가 Advanced RAG / Modular RAG로의 구조적 진화를 강제했다는 서사 → "RAG는 설계 판단의 문제다"라는 주장의 역사적 근거
- 독자가 RAG 진화 맥락 없이 구현부터 접근하는 위험을 경고하는 절에서 활용
- 평가 프레임워크, 청킹 전략, 리랭킹 등 설계 변수의 목록 제공

**인용 위치 제안**
RAG 진화 배경 절, 설계 판단 기준 절

---

### web_04
**"Modular RAG: Transforming RAG Systems into LEGO-like Reconfigurable Frameworks" (2024)**

**인용 이유**
RAG를 고정된 파이프라인이 아니라 재구성 가능한 모듈 조합으로 프레이밍. 이 장의 "설계 판단 기준의 시작점"이라는 목표와 직결된다. Modular RAG 개념은 "RAG를 쓸지 말지, 어떤 방식으로 구성할지"라는 판단이 왜 단일한 정답이 없는지를 구조적으로 설명한다.

**활용 포인트**
- 검색(Search), 메모리(Memory), 융합(Fusion), 라우팅(Routing) 등 모듈 분해 → 각 모듈이 정보 흐름의 어느 지점을 통제하는지 설명하는 데 활용
- "RAG는 단일 패턴이 아니라 설계 공간이다"는 주장을 뒷받침
- ch05가 구현보다 설계 판단에 집중하는 이유를 정당화하는 이론적 배경

**인용 위치 제안**
RAG 구성 단계 심화 절, 설계 판단 기준 절

---

## Tier 3 — 선택적 인용 (특정 논점에만 필요하거나, 다른 Tier가 커버하면 생략 가능)

---

### web_05
**"Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection" (2023)**

**인용 이유 및 조건**
RAG 파이프라인 안에 자기 평가(self-reflection) 루프를 도입한 사례. 이 장이 "정보 흐름 통제"의 개념을 동적 제어(dynamic control)까지 확장할 경우에만 인용 가치가 있다. 장의 현재 범위(기초 구조 이해)를 넘어설 위험이 있으므로, 본문보다 각주나 "더 읽을거리" 형태 권장.

**조건부 활용 포인트**
- Retrieve, Critique, Generate의 반복 루프 → RAG가 단방향 파이프라인이 아닐 수 있다는 확장 논점
- "RAG의 각 단계가 정보 흐름을 통제한다"는 주장을 동적 피드백 루프 개념으로 심화할 때

**권장 위치**
각주, 사이드바, 또는 장 말미 "RAG의 진화 방향" 단락

---

### web_06
**"RAGAS: Automated Evaluation of Retrieval Augmented Generation" (2023)**

**인용 이유 및 조건**
RAG 시스템의 평가 프레임워크(Faithfulness, Answer Relevancy, Context Recall, Context Precision). 이 장이 실패 진단 언어를 제공하는 데 활용할 수 있으나, 평가 방법론 자체가 이 장의 주제(설계 이해)보다는 ch06이나 품질 관리 장에 더 적합하다. 단, "아키텍처 결함이 측정 가능한 품질 저하로 이어진다"는 주장의 근거로 한 문장 인용은 유효하다.

**조건부 활용 포인트**
- 설계 결함 → 측정 가능한 실패 지표로 연결되는 논리 보강
- Faithfulness 지표: 생성 결과가 검색 컨텍스트에 얼마나 충실한지 → 증강 단계 설계 결함의 정량적 표현

**권장 위치**
실패 유형 절의 보강 인용, 또는 ch06으로 이월

---

## 요약 인용 맵

| Source | Tier | 핵심 활용 절 | 인용 형태 |
|---|---|---|---|
| web_01 | **Tier 1** | 도입부, LLM 구조적 한계 절 | 개념 정의 인용 (파라메트릭 메모리) |
| web_03 | **Tier 1** | 실패 진단 언어 절, 아키텍처 재정의 절 | 사례 인용 (7가지 실패 지점) |
| web_07 | **Tier 1** | 관점 전환 논지, 구성 단계 설명 절 | 프레이밍 인용 (패턴 정의) |
| web_02 | **Tier 2** | 진화 배경 절, 설계 판단 기준 절 | 서베이 인용 (Naive→Advanced→Modular 계보) |
| web_04 | **Tier 2** | 구성 단계 심화 절, 설계 판단 절 | 모델 인용 (모듈 분해) |
| web_05 | **Tier 3** | 각주 / 확장 논점 단락 | 조건부 인용 |
| web_06 | **Tier 3** | 실패 보강 / ch06 이월 권장 | 조건부 한 문장 인용 |
