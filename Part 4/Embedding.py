import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api_utils import load_openai_api_key

import numpy as np

# API 키 로드 및 클라이언트 생성
client = load_openai_api_key()

def make_embedding(text):
  
  return np.array(embedding = client.embeddings.create(
    model="text-embedding-ada-002",
    input=text,
    encoding_format="float"
  ).data[0].embedding)

kids_embedding = make_embedding("어린아이")
children_embedding = make_embedding("어린이")

print(kids_embedding)
print('----------------------------------------------------')
print(children_embedding)