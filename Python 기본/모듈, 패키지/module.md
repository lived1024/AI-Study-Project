# 모듈
- 파이썬 정의와 문장을 담고 있는 .py 파일
- 함수, 변수, 클래스 등을 포함
- 모듈을 통해 코드를 구조화하고, 유지보수하기 용이해짐
- 작성된 모듈은 다른 프로그램에서 재사용 가능

## 모듈 사용하기
- 모듈 생성 : .py파일에 정의
- 모듈을 다른 프로그램에서 가져와 사용
  - import '모듈명'
  - 모듈 내에서 다른 모듈을 가져오는 것도 가능
```python
# calc.py
def add(a, b) :
  return a + b

def sub(a, b) :
  return a - b

def mul(a, b) :
  return a *-* b

def div(a, b) :
  return a / b

# main.py
import calc

print(calc.add(3, 4))     # 7 
print(calc.sub(3, 4))     # -1
print(calc.div(3, 4))     # 0.75
```

### 모듈 가져오기 - 지역 네임스페이스(Namespace)
- 모듈을 지역 네임스페이스로 가져오기
- from '모듈명' import '개체명', '개체명2' &rarr; 해당 개체 이름을 바로 사용할 수 있음
- from '모듈명' import *
  - 모듈 내의 모든 개체를 import ( _로 시작하는 것은 제외 )
  - 가급적 지양

### 모듈 활용하기
- `모듈`로서 코드와 `메인 프로그램`으로서 코드를 어떻게 구분할 수 있을까?
  ```python
  if __name__ == "__main__" :
  ```
  - 파이썬 인터프리터로 실행한 파일은 모듈명이 `__main__`으로 고정됨