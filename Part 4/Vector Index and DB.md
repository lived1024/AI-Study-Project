# Vector DB 종류
- Pinecone, Weaviate, QDrant, Milvus, Chroma 등 전용 벡터 데이터베이스 등장
- Pinecone은 서비스로서의 소프트웨어로 성공적인 사례
- Weaviate, QDrant, Milvus는 클라우드 서비스와 함께 오픈 소스로 쉽게 배포 가능
- Chroma는 SQLite와 유사해 작은 프로젝트에 적합
- FAISS
- 벡터 인덱스 지원 제품
  - Amazon    : Elasticsearch, Redis, Postgres 등 다양한 데이터베이스가 벡터 인덱스 지원.
  - Microsoft : Cognitive Search, etc

## Ranking, cutoff
- 쓸데없는 내용도 검색될 수 있음
- 검색 내용이 너무 많을 수도 있음 &rarr; 토큰 수 늘어남, 결과 부정확함
- 가장 유용한 몇 개만 가지고 와서 프롬프트 템플릿을 만들고 LLM에 보내기

## Chunking
어떻게 나누고 정리할 것인가?
- 정해진 사이즈 chunk 
  - 텍스트인 경우, 내용이 중간에 끊겨버림
- 겹치는 부분 설정
  - 문장 1개가 아닌 전체적인 맥락에 따른 의미가 있을 수도 있음
- 문단별 설정
  - 문단별 길이가 상이함
- 메타 데이터 포함
  - 처리하는 문서가 늘 비슷한 포맷이라면 적용하기 좋지만 다른 타입 문서에는 적용하기 힘듦

### Chunking 설명
- 문장별, 줄 수별, 페이지별, 문단별 등
  - 고정 크기 청킹 ( 보통 1024 토큰 )
    - 구현 간단, 예측 가능.
    - 중간에 끊어지면 의미 손실
  - 동적 크기 청킹(semantic) : 데이터의 내용에 따라 블록의 크기가 달라지는 방법
    - 유연하고 효율성 증가
    - 구현이 복잡함
- 정확도 vs 속도
  - 작은 임베딩 : 정확한 임베딩, 그러나 처리속도가 늘어남
  - 큰 임베딩 : 빠르지만 덜 정확함

### Vector Indexing, 찾기 툴 문제
- 소설정보 - 컨텍스트 없이 이해하기 힘듦
- 비슷비슷한 유사도면 뭘 선택할지?
- 토큰 1개가 결국은 비용 &rarr; 임베딩 만드는 것도 비용
- LlamaIndex
  - PDF, DB, API로도 데이터를 받아 chunking, index 만듦
  - 사용자 질문에 효과적으로 답할 수 없음
- LlamaIndex vs GPTs
- Langchain tools - text splitters
  - Splitters for - sentence, word, HTML, code, markdown..
  - UserDefined ( custom character )

### Vector Indexing, 찾기 툴 문제 해결
- 텍스트 청크 요약해서 저장하기
- Query 다시 쓰기, 쿼리 여러 개로 만들기
- 비슷비슷한 내용 합치기
- 전통적인 키워드 검색이나 메타데이터 필터링이랑 합치기
  - 메타데이터 : (이미지)날짜, 사이즈, 장소, (텍스트)태그/카테고리, 저자/소스
  - 메타데이터 만들어 저장 : "할인 품목", "인기 품목", "A 브랜드의 저렴 버전", "마진율"
  - 정확한 단어 검색이 유용할 수 있음 : 브랜드, 인용
- API/Plugin 등을 사용하여 검색