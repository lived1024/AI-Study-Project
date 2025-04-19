# 아래처럼 개별로 import할 수 있다
# import calc.basic, calc.advanced

# 단, 해당 패키지 내의 __init__.py에 미리 import해두고 package를 import하는 방법을 더 권장
import calc

print(calc.basic.add(3, 7))
print(calc.advanced.div(3, 7))