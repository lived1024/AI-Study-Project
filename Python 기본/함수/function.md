# 함수
```python
def sum(num1, num2) :
  print(f"첫 번째 숫자 : {num1}")
  print(f"두 번째 숫자 : {num2}")

  return num1 + num2
```
- `def {function_name} (parameters) :`로 함수 정의 시작
- indent로 기존 코드와 구분
- 동일한 함수명으로 정의할 경우, 함수는 재정의됨
  - javascript처럼 동일한 함수명이 있는 경우에도 error 발생 X
- 코드 재사용성 증가
- 가독성 향상
- 유지보수성 향상