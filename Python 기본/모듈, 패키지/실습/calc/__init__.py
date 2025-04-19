import calc.basic, calc.advanced

__all__ = [
  "basic"
]

# 이 파일에서 아래처럼 선언 시, 
# 해당 패키지를 사용하는 파일에서는 calc.add 와 같이 함수 명을 바로 쓸 수 있다.
from calc.basic import *
from calc.advanced import *