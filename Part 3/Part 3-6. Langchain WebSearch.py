# pip install -qU duckduckgo-search langchain-community
from langchain_community.tools import DuckDuckGoSearchRun

search = DuckDuckGoSearchRun()

# result = search.invoke("Obama's first name?")
result = search.invoke("지금 대한민국의 핫이슈가 뭐야")
print(result)
