import base64
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api_utils import load_openai_api_key

# API 키 로드 및 클라이언트 생성
client = load_openai_api_key()

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