# 해당 패키지(폴더) 내의 __init__.py 파일에서 __all__로 정의한 모듈만 가져온다
from calc import *

print(basic.add(3, 7))
print(advanced.div(3, 7))     # 해당 패키지(폴더) 내의 __init__.py 파일에서 __all__로 정의가 안됨