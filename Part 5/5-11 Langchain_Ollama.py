from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="deepseek-r1")
response = llm.invoke("Hello, how are you?")
print(f"응답: {response}")