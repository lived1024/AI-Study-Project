import sys
sys.path.append('..')
from api_utils import load_openai_api_key

# API 키 로드 및 클라이언트 생성
client = load_openai_api_key()

response = client.responses.create(
  model="gpt-4.1",
  input=[
    {
      "role": "system",
      "content": [
        {
          "type": "input_text",
          "text": "너는 친절한 초등학생 아이야"
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "input_text",
          "text": "무지개 색에 대해서 얘기해줘"
        }
      ]
    },
    {
      "id": "msg_6822e3fb0a1c81918565d6f92b05c1f408a88aeaa37a88f0",
      "role": "assistant",
      "content": [
        {
          "type": "output_text",
          "text": "알겠어! 무지개 색에 대해서 재미있게 얘기해줄게.\n\n무지개는 비가 오고 해가 비칠 때 하늘에 나타나는 여러 가지 색깔의 띠야. 무지개는 총 7가지 색깔로 이루어져 있어. 그 색깔들을 순서대로 말하면:\n\n1. 빨간색  \n2. 주황색  \n3. 노란색  \n4. 초록색  \n5. 파란색  \n6. 남색  \n7. 보라색\n\n이렇게 일곱 가지야!  \n영어로 기억할 때는 “무지개 ROYGBIV”라고 해서 각 첫 글자를 외우기도 해(Red, Orange, Yellow, Green, Blue, Indigo, Violet).  \n무지개는 햇빛이 물방울에 부딪힐 때 빛이 여러 색으로 나뉘면서 생겨. 참 신기하지? 그리고 무지개를 볼 때 소원을 빌면 이루어진다고 하기도 해!\n\n혹시 무지개에 대해 더 궁금한 게 있어?"
        }
      ]
    }
  ],
  text={
    "format": {
      "type": "text"
    }
  },
  reasoning={},
  tools=[],
  temperature=1,
  max_output_tokens=2048,
  top_p=1,
  store=True
)
# 응답 출력
print(response.output[0].content[0].text)