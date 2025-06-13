# 이 파일은 OpenAI 임베딩과 GPT-4를 활용해 사용자의 불평(문제)에 대해
# 판타지 소설 스타일의 해결책을 제안하는 예제입니다.
# 1. 네 가지 문제 유형(돈이 없다, 회귀, 빙의, 환생)에 대한 임베딩과 해결책을 저장하고,
# 2. 사용자의 입력을 임베딩 후, 가장 유사한 유형을 찾아 해결책을 선택,
# 3. GPT-4로 판타지 설정이 담긴 상세 답변을 생성합니다.
# 간단한 RAG 구조의 AI 스토리 작가 예시입니다.

# 해당 파일 내용은 Rag_Sample.py 파일과 같이 작업이 되어야함.
# 따라서 Colab 파일 참고
# https://colab.research.google.com/drive/19v_e_9IatHZEIZhksa5_Yvy9gXwvdpK7?usp=sharing


# @title
from openai import OpenAI
import json
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api_utils import load_openai_api_key

# API 키 로드 및 클라이언트 생성
client = load_openai_api_key()

# text-embedding-ada 불러서 임베딩 가져오는 펑션
def get_embeddings(text):
  return client.embeddings.create(
    model="text-embedding-ada-002",
    input=text,
    encoding_format="float"
  ).data[0].embedding


# 임베딩을 만들어봅시다!
no_mon_embed      = get_embeddings("돈이 없다")
timetravel_embed  = get_embeddings("회귀")
bodysnat_embed    = get_embeddings("빙의")
reincarn_embed    = get_embeddings("환생")

# 미니 VectorDB 를 만들어봅시다..
solutions ={
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

def get_highest_match(problem_embed):
    # 사용자의 문제를 받고, 우리의 미니 DB 에서 제일 가까운 솔루션을 찾아낼 것입니다!
    results = []
    for key, value in solutions.items():
        sim = cosine_similarity([problem_embed], [value['embeddings']])[0][0]
        results.append((key, sim, value['solutions']))

    # 유사도로 정리
    results.sort(key=lambda x: x[1], reverse=True)

    # 제일 유사한 하나만 가져오기
    return results[0]

def get_solution(problem) -> str:
    # 사용자의 문제를 임베딩으로 바꿈
    problem_embed = get_embeddings(problem)

    # 제일 가까운 카테고리의 솔루션을 가지고 옴
    solution_found = get_highest_match(problem_embed)[2][0]
    return solution_found

def get_problem(user_query):
  # 사용자의 질문을 듣고 카테고리를 선별함
  return client.chat.completions.create(
        model="gpt-4",
        temperature=0,
        messages=[
            {"role": "system", "content": """사용자의 질문을 듣고 그 문제를 해결할 수 있는 방법을 다음 다섯가지 중에서 선택해줘:
            '돈이 없다', '회귀', '빙의', '환생'
            이 중에 선택할 옵션이 없으면 그냥 아무 대답도 하지 마.
            """
            },
            {"role": "user", "content": user_query},
        ]
    ).choices[0].message.content

def get_detailed_solution(user_query):
  # 모든 자료가 모였으니 이제 마지막 답변을 생성함
  solution = get_solution(get_problem(user_query))
  return client.chat.completions.create(
        model="gpt-4",
        temperature=0,
        messages=[
            {"role": "system", "content": """너는 퐌타스틱 스토리 작가 AI이다. 너의 역할은 주변에서 흔히 일어날 수 있는 문제를 가진 사람의 불평을 기본으로,
            판타지스러운 설정을 만들어내는 것이다. 이 스토리 안에서 너는 현대인이 길에서 발견하는 작은 디바이스이며, 그 사람이 무언가에 대해 불평하면
            그 판타지스러운 설정을 제안하면 된다.

            예:
            사람: "아, 난 이번 생은 망한 것 같아."
            AI: "그렇다면 판타지 소설속의 인물로 환생하는 것은 어떨까요? 부유한 백작가의 막내 아들로 말이죠!

            """
            },
            {"role": "user", "content": user_query},
            {"role": "system", "content": f"""
            이번 사용자의 불평은 {user_query} 이며, 이것에 대한 해결법은 {solution}이다.
            이전의 예시를 참고하여 사용자에게 그럴듯한 판타지 설정을 제안해라.
            판타지 설정에는 가상의 나라, 그리고 황족, 왕족, 귀족 등의 신분, 기사나 사제, 상단주 혹은 마법사 같은 직업이 필요하다.
            머리색깔과 눈색깔도 여러가지로 설정할 수 있다. 예: 빨강, 검정, 금색, 은색, 파랑, 녹색, 보라색, 자주색, 갈색.
            주인공이 사는 가상의 나라와, 가상의 신분과, 가상의 직업과, 머리색깔과 눈색깔을 정하고, 신분과 직업에 기반한 스토리 라인을 정한다.
            기본적으로 시작할 때에는 불행하나 훌륭한 능력과 운으로 크게 성공한다는 줄거리로 200자 이상의 내용을 만들어 보낸다.

            판타지 설정:

            """
            },
        ]
    ).choices[0].message.content