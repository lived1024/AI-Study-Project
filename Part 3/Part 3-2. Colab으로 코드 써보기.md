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
- [OpenAI API Key](https://platform.openai.com/api-keys)
- [Google Colab](https://colab.research.google.com/)
  - [Colab을 이용한 GPT 호출 예제](https://colab.research.google.com/drive/1jQDVfGo9UaMJfzZw0LmrQAgzfmOQoeLa#scrollTo=MQ4CfYhhOtDh)