import openai
import os
import base64

# API_KEY.txt 파일에서 API 키 읽기
# API_KEY.txt 파일은 현재 작업 디렉토리에 있어야 합니다.
# 이 코드는 현재 작업 디렉토리로 이동하여 API_KEY.txt 파일을 읽습니다.
os.chdir(os.path.dirname(__file__))
with open('API_KEY.txt', 'r') as file:
    os.environ["OPENAI_API_KEY"] = file.read().strip()

openai.api_key = os.getenv("OPENAI_API_KEY")

client = openai.OpenAI()

# 이미지 분석 - URL
# response = client.chat.completions.create(
#   model="gpt-4.1-mini",
#   messages=[
#     {
#       "role": "user",
#       "content": [
#         {"type": "text", "text": "이거 설명해"},
#         {
#           "type": "image_url",
#           "image_url": {
#             "url": "https://geographical.co.uk/wp-content/uploads/shutterstock_1853507206-1.jpg",
#           },
#         },
#       ],
#     }
#   ],
#   max_tokens=300,
# )
# print(response.choices[0].message.content)

# 이미지 분석 - 파일 업로드
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


image_path = "./지브리 스타일.png"
base64_image = encode_image(image_path)

response = client.responses.create(
    model="gpt-4.1",
    input=[
        {
            "role": "user",
            "content": [
                { "type": "input_text", "text": "이거 무슨 사진이야?" },
                {
                    "type": "input_image",
                    "image_url": f"data:image/jpeg;base64,{base64_image}",
                },
            ],
        }
    ],
)

print(response.output_text)