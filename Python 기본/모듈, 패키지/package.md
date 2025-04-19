# 패키지
- 모듈의 계층구조를 만드는 방법
- 모듈을 계층화하고 모듈을 포함하는 디렉토리의 집합
- 디렉토리 구조를 활용하여 연관성 있는 모듈을 그룹화하고 정리할 수 있음
- 코드의 구조화와 재사용을 용이하게 만들며, 대규모 프로젝트에 필수로적으로 사용됨
```
my_package/
  __init__.py
  module1.py
  module2.py
  subpackage/
    __init__.py
    module3.py
```

## 패키지 구성
- 패키지 밖에서 모듈 임포트하기 : ``import package.module``
  - 실제 모듈 활용 시 : ``package.module.function()``
- 별칭 이용하기 : ``import package.module as alias``
  - alias.function()
- 패키지 내의 모든 모듈 임포트 : ``from package import *``
  - 허용된 모듈만 import 가능
  
## 패키지 초기화
- `__init__.py`
  - 이 디렉토리가 파이썬 패키지임을 알려주는 파일
    - 파이썬 3.3 이하 : 반드시 필요
    - 파이썬 3.3 이상 : 없어도 패키지 인식은 가능하지만 가급적 작성 권장
  - 패키지 수준에서 사용되는 변수, 함수 또는 초기화 로직이 정의됨
  - 하위 모듈을 미리 로드하거나, 전역변수를 정의
  - `__all__`을 활용하여, 참조하게 만들 모듈만 선택 가능
  ```python
  __all__ = [
    "echo",
    "surround",
    "reverse",
  ]

  def reverse(msg: str) :
    return msg[::-1]
  ```