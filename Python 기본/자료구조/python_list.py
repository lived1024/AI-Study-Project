my_list = [30, 40, 50]
my_list.append(10)
my_list.append(15)
my_list.append(20)
# print(f"전체 배열 : {my_list}")     # [30, 40, 50, 10, 15, 20]
# print(f"길이 : {len(my_list)}")     # 6
# print(f"5번째 요소 : {my_list[4]}") # 15
# print(f"4번째 요소부터 슬라이스 : {my_list[3:]}")   # [10, 15, 20]


fruits = ["banana", "apple", "blueberry", "cherry"]
# print(f"바나나가 포함되어 있나요? {"banana" in fruits}")
# print(f"체리의 인덱스는 몇인가요? {fruits.index("cherry")}")
# # 참고 !! index 사용 시 자바스크립트와는 다르게 찾을 수 없다면 valueError가 발생한다.
# # print(f"오렌지의 인덱스는 몇인가요? {fruits.index("orange")}")


# 리스트의 정렬
numbers = [4, 2, 3, 1, 8, 6, 7, 5]
# print(f"정렬하지 않은 리스트 : {numbers}")
numbers.sort()
# print(f"정렬한 리스트 : {numbers}")
# 역순 정렬은 두가지 방법으로 가능하다
# numbers.reverse()
numbers.sort(reverse=True)
# print(f"역순 정렬한 리스트 : {numbers}")


# 리스트의 요소 추가 및 제거
test_list = []
test_list.append(10)
test_list.append(11)
test_list.append(12)
print(f"extend 전 : {test_list}")

test_list.extend([13,14,15])
print(f"extend 후 : {test_list}")   # list와 list를 합치는 경우 extend() 사용

# test_list.append([16,17])
# print(f"append를 이용한 배열 추가 후 : {test_list}") # 배열이 요소로 들어감

# 리스트의 연산 ( +, *)
new_list = test_list + [0,1,2]
print(f"새로운 리스트 : {new_list}") # extend()와 같이 작동함
multi_list = [0,1,3] * 3
print(f"리스트의 곱셈 연산 : {multi_list}")

# 리스트 요소 삭제
del test_list[0]        # del은 요소의 인덱스 삭제
#test_list.remove(10)    # remove는 특정 값 삭제
print(f"첫번째 요소 삭제 후 test_list : {test_list}")

# 최대값, 최소값
print(f"최대값 : {max(test_list)}")
print(f"최대값 : {min(test_list)}")