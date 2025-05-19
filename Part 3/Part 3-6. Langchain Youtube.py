# pip install --upgrade --quiet youtube_search
from langchain_community.tools import YouTubeSearchTool

# 유튜브 검색 툴 생성
tool = YouTubeSearchTool()
result = tool.run("IT 핫이슈")
print(result)

# pip install --upgrade --quiet youtube-transcript-api pytube faiss-cpu tiktoken langchain langchain_openai
from langchain.document_loaders import YoutubeLoader  # 유튜브 로더
from langchain.embeddings import OpenAIEmbeddings     # 임베딩 모델
from langchain.vectorstores import FAISS              # 벡터 저장소
from langchain.chains import RetrievalQA              # 질문 답변 툴
from langchain_openai import ChatOpenAI               # OpenAI 모델
from pprint import pprint                             # 아웃풋 프린트 툴
