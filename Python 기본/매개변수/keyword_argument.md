# 인자 ( Argument )

## 위치 인자 ( Positional Arguments )
- 함수 호출 시 인자(Argument)와 매개변수(Parameter)는 위치에 의해 연결됨

## 키워드 인자 ( Keyword Arguments )
- 함수 호출 시 인자에 매개변수 이름을 넣어 전달
- 인자와 매개변수의 연결을 명확히 보여줄 수 있음
- 매개변수의 순서에 영향을 받지 않으므로, 보다 유연하게 구성할 수 있음

### 활용
- 키워드 인자와 위치 인자 혼용하여 사용 ( 키워드 인자는 위치 인자 뒤에 위치 )
- 코드의 가독성을 향상시키고 함수 호출을 명확하게 함
```python
def greet(name, greeting) :
  print(greeting, name)

greet(name="Alice", greeting="Hello")     # Hello Alice
greet(greeting="Hi", name="Bob")          # Hi Bob
```

## 가변 인자 리스트 ( Arbitrary Argument List )
- 여러 인자를 유연하게 처리할 수 있게 활용
- 함수 정의에서 매개변수 이름 앞에 *를 붙여서 정의
- **튜플**로 묶여서 전달 됨
```python
def add_numbers(*args) :
  result = 0
  for num in args :
    result += num
    
  return result
```
### 가변 인자 리스트 활용
- 원하는 만큼의 인자를 전달할 수 있음
- 다른 매개변수와 함께 사용할 수 있으며, 일반 매개변수 뒤에 위치
- 하나만 정의 가능
```python
add_numbers(1)
add_numbers(1, 10, -10, 5)
add_numbers(1, 2, 3, 10 100, 50)
```

## 키워드 가변 인자 리스트 ( Keyword Arguments List )
- 여러 인자를 유연하게 처리할 수 있음
- 함수 정의에서 매개변수 이름 앞에 **를 붙여서 정의
- **딕셔너리**로 묶여서 전달 됨
```python
def print_kv(**kwargs) :
  for key, value in kwargs.items() :
    print(f"{key} : {value}")

print_kv(name = "alpha", age = 10)
print_kv(name = "beta", country = "USA")
print_kv(key = "name")
```
### 키워드 가변 인자 리스트 활용
- 다른 매개변수와 함께 사용가능
- 모든 매개변수 중 가장 뒤에 위치
```python
def display_info(name, *args, **kwargs) :
  print("Name : ", name)
  print("Known Languages : ", ', '.join(args))
  for key, value in kwargs.items() :
    print(f"{key} : {value}")
```