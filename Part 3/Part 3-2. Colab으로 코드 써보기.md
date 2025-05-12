# Part 3-2. Colab으로 코드 써보기

## Open AI - Langchain 사용하기
```python
from langchain_openai import ChatOpenAI
llm = ChatOpenAI()
text = "웃긴 얘기 해줘"
print(llm.invoke(text).content)
```
위 사용법은 2024년 3월 기준으로 현재 바꼈을 가능성이 크다

## 링크
- [OpenAI](https://platform.openai.com/docs/overview)
- [OpenAI PlayGround](https://platform.openai.com/playground)
- [Google Colab]([https://colab.research.google.com/])

### 테스트용 코드
```python
from openai import OpenAI
client = OpenAI()

response = client.responses.create(
  model="gpt-4.1",
  input=[
    {
      "role": "system",
      "content": [
        {
          "type": "input_text",
          "text": "너는 친절한 초등학생 아이이다.\n"
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
      "id": "msg_68206159ca488191a18c0861457307b309b9e1ce5f7df6fd",
      "role": "assistant",
      "content": [
        {
          "type": "output_text",
          "text": "안녕! 무지개 색에 대해 궁금했구나. 무지개는 비가 온 뒤에 햇빛이 나올 때 하늘에 생기는 알록달록한 아치 모양이야. 빛이 공기 중에 있는 물방울에 부딪히면서 여러 색깔로 나누어져서 보여.\n\n무지개는 보통 7가지 색으로 이루어져 있어! 그 색들은 순서대로  \n빨강, 주황, 노랑, 초록, 파랑, 남색, 보라  \n야! 이렇게 외우면 좋아: \"**빨주노초파남보**\"!\n\n하나씩 살펴보면:\n- 빨강: 맨 위에 있는 강렬한 색이야.\n- 주황: 빨강과 노랑 사이, 오렌지색 같아!\n- 노랑: 해님처럼 밝고 눈에 잘 띄는 색.\n- 초록: 자연에 많은 색, 잔디나 나뭇잎 색!\n- 파랑: 푸른 하늘이나 바다를 닮았어.\n- 남색: 파랑보다 더 진한 파란색이야.\n-"
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
  max_output_tokens=256,
  top_p=1,
  store=True
)
```