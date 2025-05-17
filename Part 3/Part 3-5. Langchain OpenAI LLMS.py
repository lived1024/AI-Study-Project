import os
from langchain_openai import OpenAI
# pip install langchain-openai

# API_KEY.txt 파일에서 API 키 읽기
# API_KEY.txt 파일은 현재 작업 디렉토리에 있어야 합니다.
# 이 코드는 현재 작업 디렉토리로 이동하여 API_KEY.txt 파일을 읽습니다.
os.chdir(os.path.dirname(__file__))
with open('API_KEY.txt', 'r') as file:
    os.environ["OPENAI_API_KEY"] = file.read().strip()

openai_api_key = os.getenv("OPENAI_API_KEY")

llm = OpenAI(openai_api_key=openai_api_key)
response = llm.generate(["넌 어떤 AI야?"])
print(response.generations[0][0].text)
