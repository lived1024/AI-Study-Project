# 빈 튜플 생성 - 튜플은 생성 후 값을 변경할 수 없다
my_tuple = (1, )

# 과일 바구니
fruits = ("apple", "banana", "blueberry")
first = fruits[0]
print(f"first : {first}")

# 패킹과 언패킹
tp = 1, 2, 3
print(f"패킹 : {tp}")
v1, v2, v3 = tp
print(f"첫번째 : {v1}, 두번째 :  {v2}, 세번째 : {v3}")

# 아래 a와 b값을 교환 시 패킹과 언패킹을 이용하여 간편하게 처리 가능
a = 10
b = 20
a, b = b, a
print(f"A : {a}, B : {b}")

# 튜플의 언패킹을 활용하면 리스트로 변환도 간편하게 할 수 있다.
test = 1, 2, 3, 4, 5, 6, 7, 8
*vals, val1 = test
vals.append(val1)
print(f"튜플 변환 결과물 : {vals}")