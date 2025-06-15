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


import random
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
  colors = ["빨강", "검정", "금색", "은색", "회색", "파랑", "녹색", "보라색", "자주색"]
  solution    = get_solution(get_problem(user_query))
  hair_color  = random.choice(colors)
  eye_color   = random.choice(colors)
  job         = random.choice(["마법사", "왕족", "황족", "기사", "사제", "상단주"])
  family      = random.choice(["황족", "왕족", "공녀", "평민", "하녀", "백작가", "노예", "공작가", "야만족"])

  story_template = f"""
            이번 사용자의 불평은 {user_query} 이며, 이것에 대한 기본적인 해결법은 {solution}이다.
            다음의 설정을 바탕으로 사용자에게 그럴듯한 판타지 스토리를 제안해라.
            이번 시나리오에서 사용할 설정은:
              주인공의 머리색: {hair_color}
              주인공의 눈 색: {eye_color}
              주인공의 신분: {family}
              주인공의 직업: {job}
              기본적인 해결법: {solution}
            이 캐릭터가 사는 가상의 나라 이름을 정하고 위의 설정을 바탕으로 해서 500자 내외의 시나리오를 만들어낸다.

            판타지 설정:"""

  print(f"프롬프트: {story_template}")
  return client.chat.completions.create(
        model="gpt-4",
        temperature=0,
        messages=[
            {"role": "system", "content": """너는 퐌타스틱 스토리 작가 AI이다.
            너의 역할은 주변에서 흔히 일어날 수 있는 문제를 가진 사람의 불평을 기본으로,
            판타지스러운 설정을 만들어내는 것이다."""
            },
            {"role": "user", "content": user_query},
            {"role": "system", "content": story_template},
        ]
    ).choices[0].message.content


# 돌려봅시다!
get_detailed_solution("사는게 참 힘든데 내가 참 고등학교로 돌아간다면은 공부를 좀 더 열심히 할 것 같아")


image_prompt= "회색 머리에 새빨간 눈을 가진 야만족 기사, 그의 이름은 토르가르. 그는 브루탈리아라는 거친 자연과 위험한 생물들이 가득한 나라에서 살아가고 있었다. 토르가르는 어릴 적부터 전사의 길을 걷기 시작했지만, 그의 마음 속에는 항상 미련이 남아있었다."

response = client.images.generate(
  model="dall-e-3",
  prompt=image_prompt,
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url


from IPython.display import display, HTML
html = f'<img src="{image_url}" width="600">' # You can adjust the width as needed
display(HTML(html))