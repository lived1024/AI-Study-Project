# 후처리 Post-processing

## LLM 답변 받은 후의 post processing
- 윤리적 AI ( RAI )
- 관련성(relevance)
- 사실 기반(groundedness)
- cosine similarity(답변과 질문 사이의 유사도)
- 내용 검열 (moderation) API
  - 사용자 쿼리에도 적용
- Azure는?
- Google은?

## Groundedness, relevance testing
- RAGAS library : 
- 생성
  - Faithfulness : 사실인가?
  - Answer relevancy : 질문과의 관련성
- 검색
  - Context precision : 가져온 정보의 signal to noise - 랭킹
  - Context recall : 가져온 정보로 충분한가
- 그 외
  - Context relevancy : 필요한 정보만 있는가
  - Context entities recall : 가져온 정보 중 몇개를 썼는가
  - Answer semantic similarity : 답변과 ground truth 유사도