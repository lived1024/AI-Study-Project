from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import OpenAIEmbeddings                   # 임베딩 모델
from langchain_community.vectorstores import FAISS              # 벡터 저장소
from langchain.chains import RetrievalQA                        # 질문 답변 툴
from langchain_openai import ChatOpenAI                         # OpenAI 모델
from pprint import pprint                                       # 아웃풋 프린트 툴
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api_utils import load_openai_api_key

# API 키 로드
load_openai_api_key()

# 임베딩하는 툴 생성
embeddings = OpenAIEmbeddings()

# 현재 스크립트 파일과 같은 디렉토리에 있는 PDF 파일의 절대 경로 생성
# loader = PyPDFLoader("./Supabase 강의.pdf")
current_dir = os.path.dirname(os.path.abspath(__file__))
pdf_path = os.path.join(current_dir, "Supabase 강의.pdf")

loader = PyPDFLoader(pdf_path)
documents = loader.load()

db = FAISS.from_documents(documents, embeddings)
retriever = db.as_retriever()
llm = ChatOpenAI(model="gpt-4")

chain = RetrievalQA.from_chain_type(
  llm=llm,
  chain_type="stuff",
  retriever=retriever,
  return_source_documents=True
)

result = chain.invoke({"query": "어떤 내용인지 요악해서 설명해줄래? 초등학생도 이해하기 쉬운 정도로"})

pprint(result['result'])

