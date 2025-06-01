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