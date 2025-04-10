# for
for i in range(5) :
  print(i)  # 0, 1, 2, 3, 4
else :
  print(f"range(5) 반복문 종료")

for i in range(1, 5) :
  print(i)  # 1, 2, 3, 4
else :
  print(f"range(1, 5) 반복문 종료")

# while
i = 0
while i < 5 :
  print(i)
  i += 1
else :
  print(f"while문 종료")



fruits = ['apple', 'strawberry', 'peach', 'banana']
for fruit in fruits :
  if fruit == 'apple' :
    print(f"사과는 맛있습니다.")

  print(f"{fruit}이(가) 과일바구니에 있습니다.")

while True :
  user_input = input(f"명령어를 입력해주세요(종료는 exit) : ")
  if user_input == "exit" :
    break;
  else :
    pass        # TODO : 차후 개발 예정


# 구구단 프로그램
for x in range(1, 10) :
  for y in range(1, 10) :
    print(f"{x} * {y} = {x * y}")
# enumerate 활용
for index, fruit in enumerate(fruits) :
  print(f"{index}번쨰 과일은 {fruit}입니다")
# 팩토리얼 구하기
num = 5
result = 1
for i in range(num, 1, -1) :
  result = result * i

print(f"팩토리얼 결과 : {result}")