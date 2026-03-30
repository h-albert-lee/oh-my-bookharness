# Search: attribution error organizational teams software AI debugging blame culture

충분한 자료가 수집되었습니다. 이제 검색 결과를 바탕으로 실제로 존재하는 자료들을 정리하겠습니다.

---

## 조사 결과 요약

아래는 검색을 통해 실제 존재가 확인된 자료들을 ch03 집필에 활용 가능한 형태로 정리한 것입니다.



RAND 보고서는 AI/ML 프로젝트 실패 원인을 실증적으로 조사했으며, 80% 이상의 AI 프로젝트가 실패한다는 수치를 제시합니다.

 

PLOS ONE 연구는 AI를 인간적 마음을 가진 존재로 인식할수록 AI에 더 많은 도덕적 책임을 귀인한다는 점을 실험적으로 밝혔습니다.

 

Dekker의 연구는 사람 중심의 귀인 경향이 현대에도 강하게 남아있으며, 시스템 결함에는 상대적으로 주목하지 않는다고 지적합니다.

 

Google SRE의 포스트모템 철학은 "개인은 고칠 수 없지만 시스템은 고칠 수 있다"는 핵심 명제를 실천적으로 보여줍니다.



---

```json
[
  {
    "title": "The Root Causes of Failure for Artificial Intelligence Projects and How They Can Succeed: Avoiding the Anti-Patterns of AI",
    "authors": ["James Ryseff", "Brandon F. De Bruhl", "Sydne J. Newberry"],
    "year": 2024,
    "type": "industry_report",
    "url": "https://www.rand.org/pubs/research_reports/RRA2680-1.html",
    "summary": "65명의 AI/ML 실무자 인터뷰를 통해 도출한 5가지 AI 프로젝트 실패 근본 원인을 제시한다. '모델 자체'보다 문제 정의 오류, 데이터 부재, 기술 우선주의, 인프라 부족, 기술 과신이 실패의 원인임을 실증적으로 보여준다. ch03의 핵심 논증("모델이 아니라 시스템이 문제")을 뒷받침하는 가장 강력한 통계적·질적 근거로 활용 가능하다.",
    "key_claims": [
      "AI 프로젝트의 80% 이상이 실패하며 이는 비-AI IT 프로젝트의 2배 수준이다",
      "실패의 1위 원인은 모델 성능이 아니라 '문제 정의의 오해와 소통 부재'다",
      "성공하는 프로젝트는 기술이 아니라 해결할 문제에 레이저처럼 집중한다",
      "AI 모델이 잘못된 지표에 최적화되거나 전체 비즈니스 워크플로우에 맞지 않게 배포되는 경우가 잦다"
    ]
  },
  {
    "title": "It's the AI's fault, not mine: Mind perception increases blame attribution to AI",
    "authors": ["Minjoo Joo"],
    "year": 2024,
    "type": "academic_paper",
    "url": "https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0314559",
    "summary": "AI를 인간적 마음이 있는 존재로 인식할수록 AI에 더 많은 도덕적 책임을 귀인하고, 반대로 해당 시스템을 만든 회사나 개발자에 대한 책임 귀인은 줄어드는 현상을 3개 실험으로 실증한다. '모델 탓'이라는 귀인이 심리적으로 어떻게 작동하는지 설명하는 데 직접 활용 가능하며, AI를 의인화할수록 구조적 실패가 은폐된다는 논점을 지지한다.",
    "key_claims": [
      "AI를 인간 같은 마음을 가진 존재로 인식할수록 AI에 더 많은 도덕적 책임을 귀인한다",
      "AI에 대한 책임 귀인이 증가하면 설계자·회사에 대한 책임 귀인은 줄어든다",
      "AI는 도덕적 위반에서 스케이프고트로 오용될 수 있다"
    ]
  },
  {
    "title": "People or Systems? To Blame Is Human. The Fix Is to Engineer",
    "authors": ["Richard J. Holden"],
    "year": 2009,
    "type": "academic_paper",
    "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3115647/",
    "summary": "항공·의료 분야 사고 조사에서 전문가조차 시스템 원인보다 인간 귀인에 의존하는 경향이 있음을 분석한다. 근본귀인오류(FAE)가 산업적 규범으로도 고착화되어 있음을 논증하며, '개인 교체'가 아닌 '시스템 재설계'가 진정한 해결책임을 강조한다. ch03의 '모델 탓'이라는 귀인이 왜 구조적으로 틀린지를 역사적·심리학적으로 근거 짓는 데 활용할 수 있다.",
    "key_claims": [
      "사고 귀인을 인간 실패에 집중시키는 것은 심리적 경향인 동시에 산업적 규범이다",
      "NTSB 항공사고 조사의 74%가 '승무원 실패'를 원인으로 지목했지만 실제 원인은 시스템에 있었다",
      "인간 중심의 귀인은 시스템 재설계라는 진짜 해결책으로의 주의를 분산시킨다",
      "Dekker(2002): 인간 오류는 도구·과제·운영 환경의 특성과 체계적으로 연결되어 있다"
    ]
  },
  {
    "title": "Postmortem Culture: Learning from Failure (Google SRE Book, Chapter 15)",
    "authors": ["Google SRE Team"],
    "year": 2017,
    "type": "documentation",
    "url": "https://sre.google/sre-book/postmortem-culture/",
    "summary": "Google SRE의 블레임리스 포스트모템 철학을 기술한 공식 문서로, '개인은 고칠 수 없지만 시스템과 프로세스는 고칠 수 있다'는 핵심 원리를 실제 사례와 함께 제시한다. ch03에서 blame culture의 폐해와 시스템 사고로의 전환이 실제 현장에서 어떻게 구현되는지를 보여주는 실용적 레퍼런스로 쓸 수 있다.",
    "key_claims": [
      "포스트모템은 개인 귀인이 아닌 '왜 불완전한 정보가 주어졌는가'에 대한 시스템적 조사여야 한다",
      "blame이 있는 문화는 인시던트 은폐로 이어지고 조직에 더 큰 위험을 야기한다",
      "당신은 사람을 고칠 수 없지만, 복잡한 시스템을 설계하고 유지하는 사람들이 올바른 선택을 하도록 시스템과 프로세스를 개선할 수 있다"
    ]
  },
  {
    "title": "Fundamental Attribution Error (Wikipedia)",
    "authors": ["Wikipedia contributors"],
    "year": 2026,
    "type": "documentation",
    "url": "https://en.wikipedia.org/wiki/Fundamental_attribution_error",
    "summary": "근본귀인오류(FAE)의 정의, 이론적 배경, 관련 편향들을 정리한 참고 자료다. ch03에서 '모델 탓'이라는 귀인이 왜 FAE의 한 형태인지 설명할 때 개념 정의의 출처로 활용 가능하다.",
    "key_claims": [
      "FAE는 타인의 행동을 판단할 때 상황·환경 요인을 과소평가하고 성격·기질 요인을 과대평가하는 인지 편향이다",
      "관찰자는 '그 사람이 늦은 것은 이기적이기 때문'이라고 판단하지만 실제로는 교통체증이 원인일 수 있다",
      "Lee Ross(1977)가 명명했으며, 사회심리학의 개념적 초석으로 간주된다"
    ]
  },
  {
    "title": "The AI Attribution Error",
    "authors": ["Stephen D. Turner"],
    "year": 2025,
    "type": "blog_post",
    "url": "https://blog.stephenturner.us/p/ai-attribution-error",
    "summary": "AI 사용에서 발생하는 비대칭적 귀인 패턴('AI가 잘하면 내 프롬프트 덕, AI가 못하면 모델 탓')을 FAE의 틀로 분석한 블로그 글이다. ch03 도입부에서 독자가 공감할 만한 일상적 사례로 활용하기 좋으며, '모델 탓'이라는 귀인이 왜 편향인지를 직관적으로 전달한다.",
    "key_claims": [
      "AI가 유용한 결과를 낼 때는 자신의 모델 선택과 프롬프팅 덕분이라 귀인하고, 실패하면 모델을 탓하는 비대칭 귀인이 발생한다",
      "올바른 질문은 '이 모델이 좋은가 나쁜가'가 아니라 '내가 성공 가능성을 높이는 조건을 설정했는가'이다",
      "귀인 오류는 지저분한 과정을 올라갈 때는 미화하고 내려갈 때는 스케이프고트로 단순화한다"
    ]
  },
  {
    "title": "Fundamental Attribution Error: Why It's Always Someone Else's Fault",
    "authors": ["Leading Sapiens Editorial Team"],
    "year": 2024,
    "type": "blog_post",
    "url": "https://www.leadingsapiens.com/fundamental-attribution-error/",
    "summary": "항공 사고 조사관들도 첫 반응은 '조종사 탓'이라는 사례를 중심으로, FAE가 리더십과 조직 문화에서 어떻게 발현되는지를 분석한다. ch03에서 '조종사 탓 → 모델 탓'의 유비를 구성하는 데 활용 가능하다. Kahneman의 System 1 사고와 FAE의 연결 고리도 간결하게 설명한다.",
    "key_claims": [
      "고도로 훈련된 항공 사고 조사관조차 첫 본능은 조종사를 탓하는 것이다",
      "FAE는 복잡한 사건에 대한 단순하고 편리한 설명을 제공하기 때문에 매력적이다",
      "Kahneman의 System 1 사고는 FAE와 긴밀히 연결되어 있으며, 상황적 요인보다 인물 귀인이 인지적으로 더 쉽다",
      "올바른 질문은 '누가 잘못했나'가 아니라 '어떤 상황이 이 결과로 이어졌나'이다"
    ]
  },
  {
    "title": "How do people react to AI failure? Automation bias, algorithmic aversion, and perceived controllability",
    "authors": ["Eun Go", "Jiyeon So"],
    "year": 2022,
    "type": "academic_paper",
    "url": "https://academic.oup.com/jcmc/article/28/1/zmac029/6827859",
    "summary": "AI 실패에 대한 사용자의 반응 패턴(자동화 편향 → 알고리즘 혐오)과 귀인 구조를 분석한 JCMC 논문이다. 사용자들이 AI의 통제 불가능성을 인식할수록 책임을 프로그래머·조직·사용자에게 분산시키는 경향을 실증한다. ch03에서 '모델 탓'이라는 귀인이 실제로 어디에 착지하는지(개발자·조직)를 보여주는 학술적 근거로 활용 가능하다.",
    "key_claims": [
      "사용자는 AI의 통제 범위를 AI 밖에 있다고 인식하며, 책임을 조직·개발자·사용자에게 분산시킨다",
      "AI가 인간보다 통제력이 낮다고 인식될수록 AI 실패에 더 관대한 평가를 내린다",
      "automation bias
