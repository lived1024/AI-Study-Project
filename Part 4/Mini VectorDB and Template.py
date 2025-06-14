import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api_utils import load_openai_api_key

import numpy as np

# API 키 로드 및 클라이언트 생성
client = load_openai_api_key()

# text-embedding-ada 불러서 임베딩 가져오는 펑션
def get_embeddings(text):
  return client.embeddings.create(
    model="text-embedding-ada-002",
    input=text,
    encoding_format="float"
  ).data[0].embedding


# from openai import OpenAI
import json
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# client = OpenAI()

# 임베딩을 만들어봅시다!
no_mon_embed      = get_embeddings("돈이 없다")
timetravel_embed  = get_embeddings("회귀")
bodysnat_embed    = get_embeddings("빙의")
reincarn_embed    = get_embeddings("환생")

# 미니 VectorDB 를 만들어봅시다..
solutions = {
    "돈이 없다": {
        "embeddings": no_mon_embed,
        "solutions": ["돈 있는 캐릭터가 된다!"]
    },
    "회귀": {
        "embeddings": timetravel_embed,
        "solutions": ["시간을 거슬러 되돌아 감!"]
    },
    "빙의": {
        "embeddings": bodysnat_embed,
        "solutions": ["소설속 캐릭터로 빙의하자!"]
    },
    "환생": {
        "embeddings": reincarn_embed,
        "solutions": ["판타지 소설의 캐릭터로 다시 태어나자!"]
    }
}
