import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from langchain_openai import OpenAI
from api_utils import load_openai_api_key, get_openai_api_key
# pip install langchain-openai

# API 키 로드
load_openai_api_key()
openai_api_key = get_openai_api_key()

llm = OpenAI(openai_api_key=openai_api_key)
response = llm.generate(["넌 어떤 AI야?"])
print(response.generations[0][0].text)
