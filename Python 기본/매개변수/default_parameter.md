# 기본 매개변수 ( Default Parameter )
```python
def study(name, language='python') : 
  print(f"{name} 님은 {language} 수업 중입니다.")

study('shin')             # shin 님은 python 수업 중입니다.
study('shin', )           # shin 님은 python 수업 중입니다.
study('shin', 'java')     # shin 님은 java 수업 중입니다.
```
- 함수를 호출할 때 매개변수를 제공하지 않으면, 자동으로 할당되는 값
- 매개변수 명 = 기본값 형태로 정의
- 기본 매개변수는 일반 매개변수 뒤에 위치
- 가변 객체(리스트, 딕셔너리 등)가 변조될 수 있음
  - 가변 객체를 기본 매개변수로 사용할 경우, 함수 내부에서 생성하도록 구성
    ```python
    def process_data(data, options=None) :
      if options is None :
        options = {
          "name" : "Unknown"
        }
      # options 딕셔너리를 사용하여 데이터 처리 로직을 구현
      pass
    ```