import os, openai
import json
from duckpy import Client
import ast

# API_KEY.txt 파일에서 API 키 읽기
# API_KEY.txt 파일은 현재 작업 디렉토리에 있어야 합니다.
# 이 코드는 현재 작업 디렉토리로 이동하여 API_KEY.txt 파일을 읽습니다.
os.chdir(os.path.dirname(__file__))
with open('API_KEY.txt', 'r') as file:
    os.environ["OPENAI_API_KEY"] = file.read().strip()
    
openai.api_key = os.getenv("OPENAI_API_KEY")

client = openai.OpenAI()

duckduckgo_client = Client()

def duck_search(query) -> str:
    """Runs a duckduckgo search"""
    output = duckduckgo_client.search(query)
    return str(output)

# 1단계 : 한국어 질문을 영어 질문으로 변환하여 function call의 query 인자로 전달
completion = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0,
        functions=[
            {
                "name": "duck_search",
                "description": "Used to search online",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "Translate the Korean content into English input query",
                        },
                    },
                    "required": ["query"],
                },
            }
        ],
        messages=[
            {"role": "system", "content": "You must use the `duck_search` function to get information."},
            {"role": "user", "content": "조지 클루니 생일이 언제야?"},
        ]
    )

print(completion)
print("==================================================================================================================================")


# 2단계 : 영어 질문을 유튜브 검색 결과로 변환하여 function call의 content 인자로 전달
message = completion.choices[0].message
if message.function_call:
    function_name = message.function_call.name
    args = ast.literal_eval(message.function_call.arguments)
    function_response = duck_search(
        query=args.get("query"),
    )
    print(f"function_response : {function_response}")
    completion_final = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": "조지 클루니 생일이 언제야?"},
            message,
            {
                "role": "function",
                "name": function_name,
                "content": function_response,
            },
        ],
    )
    print(completion_final.choices[0].message.content)



# 이외에 참고 URL
# https://colab.research.google.com/drive/1bF0ADe3fanEh-hyv-Ujnri1i02lgqzLL?usp=sharing#scrollTo=KsQvFQWSp1Cc