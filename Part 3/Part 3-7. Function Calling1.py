import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api_utils import load_openai_api_key

# API 키 로드 및 클라이언트 생성
client = load_openai_api_key()

# ********************** 이전 방식 - 같은 질문으로 여러번 물어볼때마다 답변이 달라짐(생성형 AI의 특성상 답변이 달라짐) **********************
# content = """다음 문장에서 색깔 정보가 있으면 그것을 추출하여 영어로 번역하고 json 포맷으로 만들어서 한글로 출력해라.
#           문장 : \"나는 빨간 사과가 좋더라\n
#           """
# response = client.chat.completions.create(
#   model="gpt-4o-mini",
#   messages=[
#     {
#       "role": "user", 
#       "content": content
#     }
#   ]
# )
# print(response.choices[0].message.content)


# ********************** 이전 방식에 schema 정보를 추가하는 경우, 같은 질문에 대한 답변의 일관성이 향상됨. **********************
# schema = {
#   "$schema": "http://json-schema.org/draft-07/schema",
#   "type": "object",
#   "properties": {
#     "color": {
#       "type": "string"
#     }
#   },
#   "required": ["color"]
# }
# content = f"""다음 문장에서 색깔 정보가 있으면 그것을 추출하여 영어로 번역하고 json 포맷으로 만들어서 출력해라.
#                문장: '나는 빨간 사과가 좋더라'
#                json schema 는 다음과 같다 : {schema}
#                색깔 정보가 없으면 no color 로 대신해라
#             """
# response = client.chat.completions.create(
#   model="gpt-4o-mini",
#   messages=[
#     {
#       "role": "user", 
#       "content": content
#     }
#   ]
# )
# print(response.choices[0].message.content)



# ********************** 새로운 방식(색깔 추출) **********************
# Function calling 방식을 쓰는 경우, 필요한 응답의 형식을 정의해서 주면 해당 형식에 맞게 응답을 줌.
# 이 방식은 같은 질문에 대한 답변의 일관성이 향상되며 최소한의 흐름을 가져갈 수 있음
# Function calling이 실패하는 경우, AttributeError: 'NoneType' object has no attribute 'arguments' 에러 발생생
# response = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[
#         {
#             "role": "user",
#             # "content": "퇴근했는데 업무 톡 날리는 양심없는 인간",       # AttributeError: 'NoneType' object has no attribute 'arguments'
#             "content": "나는 노란색이 좋더라",
#         }
#     ],  
#     functions=[
#         {
#             "name": "color_extractor",
#             "description": "사용자의 선호 색깔을 찾아서 영어로 번역하고 영어 단어를 출력함",
#             "parameters": {
#                 "type": "object",
#                 "properties": {
#                     "color": {
#                         "type": "string",
#                         "description": "색깔 정보를 빼내와서 그에 해당하는 영어 단어를 출력함",
#                     },
#                 },
#                 "required": ["color"],
#             },
#         }
#     ]    
# )
# print(response.choices[0].message.function_call.arguments)


# ********************** 새로운 방식(숫자 추출) **********************
response = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    messages=[{"role": "user", "content": "아침에 세 개 저녁에 네개"}],
    functions=[
        {
            "name": "apple_add",                              # 함수 이름
            "description": "사과 숫자를 더함",
            "parameters": {
                "type": "object",
                "properties": {
                    "quantity1": {
                        "type": "integer",
                        "description": "첫번째 숫자",
                    },
                    "quantity2": {
                        "type": "integer",
                        "description": "두번째 숫자",
                    },
                },
                "required": ["quantity1", "quantity2"],
            },
        }
    ],
    function_call="auto",
)

print(response.choices[0].message.function_call.arguments)

def apple_add(quantity1, quantity2):                          # 함수 정의
  return str(quantity1 + quantity2)

print(apple_add(3, 4))
