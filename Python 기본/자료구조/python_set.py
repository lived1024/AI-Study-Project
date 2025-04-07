empty_set = set()     # 빈 셋 정의 - 중괄호 {}를 이용한 정의는 dictionary에 적용된다.
my_set = {1, 2, 3, 3} # 중복된 값을 정의 시 중복된 값은 버려지게 된다.
print(my_set)         # {1, 2, 3}

# 아래 코드들을 print로 출력 시, 요소들의 순서가 보장되지 않음(출력 시 랜덤)
fruits = {'apple', 'banana', 'blueberry'}
print(fruits)
fruits.add('orange')
print(fruits)

# 요소 삭제
fruits.remove('banana')
print(fruits)


fruits1 = {'apple', 'strawberry', 'peach'}
fruits2 = {'banana', 'strawberry', 'orange'}
fruits3 = {'apple', 'peach'}
print(f"합집합 : {fruits1.union(fruits2)}")
print(f"교집합 : {fruits1.intersection(fruits2)}")
print(f"차집합1 : {fruits1.difference(fruits2)}")  # fruits1 - fruits2
print(f"차집합2 : {fruits2.difference(fruits1)}")  # fruits2 - fruits1
print(f"하위 집합 여부 : {fruits1.issubset(fruits2)}") # fruits2가 fruits1 포함여부
print(f"하위 집합 여부 : {fruits2.issubset(fruits1)}") # fruits1이 fruits2 포함여부
print(f"하위 집합 여부 : {fruits1.issubset(fruits3)}") # fruits3가 fruits1 포함여부
print(f"하위 집합 여부 : {fruits3.issubset(fruits1)}") # fruits1이 fruits3 포함여부
