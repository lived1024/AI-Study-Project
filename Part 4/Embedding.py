import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api_utils import load_openai_api_key

import numpy as np

# API 키 로드 및 클라이언트 생성
client = load_openai_api_key()

def get_embedding(text):
  
  return np.array(client.embeddings.create(
    model="text-embedding-ada-002",
    input=text,
    encoding_format="float"
  ).data[0].embedding)

kids_embedding = get_embedding("어린아이")
children_embedding = get_embedding("어린이")

print(len(kids_embedding))
print('----------------------------------------------------')
print(len(children_embedding))

print(type(kids_embedding)) # numpy.ndarray


# 유사도 비교 - 두 벡터가 유사한 경우 1, 유사도가 낮을수록 -1
def cosine_similarity(vector_a, vector_b):
  # Compute the dot product between the two vectors
  dot_product = np.dot(vector_a, vector_b)
  # Compute the norm(magnitude) of each vector
  norm_a = np.linalg.norm(vector_a)
  norm_b = np.linalg.norm(vector_b)
  # Compute the cosine similarity
  cosine_similarity = dot_product / (norm_a * norm_b)
  return cosine_similarity

# result = cosine_similarity(get_embedding("어린아이"), get_embedding("어린이"))      # 0.964651954216103
result = cosine_similarity(get_embedding("어린아이"), get_embedding("어린아이"))      # 1
print("Cosine Similarity: ", result)


def get_similarity(text_a, text_b):
  result = round(cosine_similarity(get_embedding(text_a), get_embedding(text_b)), 2)
  print(f"얼마나 가깝나요? {result}")

get_similarity("학교", "school")      # 0.86
get_similarity("wifi", "학원")        # 0.77
get_similarity("비행기", "항공기")     # 0.93
