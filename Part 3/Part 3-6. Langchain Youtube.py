# pip install --upgrade --quiet youtube_search
from langchain_community.tools import YouTubeSearchTool

# 유튜브 검색 툴 생성
tool = YouTubeSearchTool()
result = tool.run("IT 핫이슈")
print(result)

# pip install --upgrade --quiet youtube-transcript-api pytube faiss-cpu tiktoken langchain langchain_openai
from langchain_community.document_loaders import YoutubeLoader  # 유튜브 로더
from langchain_openai import OpenAIEmbeddings     # 임베딩 모델
from langchain_community.vectorstores import FAISS              # 벡터 저장소
from langchain.chains import RetrievalQA              # 질문 답변 툴
from langchain_openai import ChatOpenAI               # OpenAI 모델
from pprint import pprint                             # 아웃풋 프린트 툴
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api_utils import load_openai_api_key

# API 키 로드
load_openai_api_key()

# 임베딩하는 툴 생성
embeddings = OpenAIEmbeddings()

# 유튜브 링크에서 자막 내용 가지고 오기
loader = YoutubeLoader.from_youtube_url(
    "https://youtu.be/w8xG4Dzl7p0?si=63XXWtrRVSLvvjDS",
    language=['ko']  # 한국어 자막 사용 - 영어인 경우 생략 가능
)
documents = loader.load()

# 벡터 저장소
db = FAISS.from_documents(documents, embeddings)
retriever = db.as_retriever()

# 사용할 언어모델
llm = ChatOpenAI(model="gpt-4")

# RetrievalQA를 써서 "가져오는 기계" 만들기
qa = RetrievalQA.from_chain_type(
    llm=llm,
    # chain_type="stuff",
    retriever=retriever,
    return_source_documents=True
)

# 질문 정의하고 물어보기
query = "무슨 내용인지 요약해줘"
result = qa.invoke({"query": query})

pprint(result['result'])
