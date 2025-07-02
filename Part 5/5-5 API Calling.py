import sys
import os
import base64
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api_utils import load_openai_api_key

import numpy as np

# API 키 로드 및 클라이언트 생성
client = load_openai_api_key()

# 이미지를 base64로 인코딩하는 함수
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# 이미지 파일 경로 (현재 스크립트와 같은 폴더)
current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, "blood inspection.jpeg")
base64_image = encode_image(image_path)

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "user",
     "content": [
       {"type": "text", "text": "이 피검사 결과를 상세하게 설명해줘. 그리고 결과에 따라 추천 조치를 제시해줘."},
       {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}},
     ]
    }
  ]
)

print(response.choices[0].message.content)