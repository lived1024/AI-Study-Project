import ollama
response = ollama.generate(model="deepseek-r1", prompt="Hello, how are you?")
print(response['response'])