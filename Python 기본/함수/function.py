def cal(num1, num2) :
  return num1 + num2

def cal(num1, num2) :
  return num1 * num2

# 위에서 동일한 함수명으로 선언해도 에러 발생 X
print(cal(3, 4))    # 12


def div(num1, num2) :
  if ( num2 == 0 ) : return 0
  return num1 / num2
print(div(3, 2))    # 1.5
print(div(3, 0))    # 0


def study(name, language='python') : 
  print(f"{name} 님은 {language} 수업 중입니다.")

study('shin')