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

prompt = "한국인 연인이 벚꽃구경을 하고 있는 모습"

result = client.images.generate(
    model="dall-e-3",
    prompt=prompt,
    size="1024x1024",
    quality="standard",
    n=1,
    response_format="b64_json"
)

image_base64 = result.data[0].b64_json
image_bytes = base64.b64decode(image_base64)

# Save the image to a file
with open("Generated_Image.png", "wb") as f:
    f.write(image_bytes)