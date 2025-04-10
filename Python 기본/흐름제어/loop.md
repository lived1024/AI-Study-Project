# 반복문

## for
- 시퀀스(리스트, 튜플, 문자열 등)을 순회할 수 있음    
시퀀스 : 반복 가능한 (Next 요소가 있는) 저장공간
- 반복하여 수행될 명령은 indent로 구분
- 특이하게 for문에 else 사용 가능 : 반복문이 끝난 후 작동

  ```python
  numbers = [1, 2, 3, 4, 5]
  for num in numbers :
    print(num)
  else:
    print(("출력이 완료되었습니다."))
  ```
### range()
- range([start,], stop[, step])
- {Start}부터 {Step}만큼 증가, {Stop}까지의 숫자 목록을 생성
  ```python
  # 5회 반복(0~4), i값은 1씩 증가
  for i in range(5) :
    print(i)          # 0, 1, 2, 3, 4
  
  # range(n)       : 0 ~ (n-1) 까지의 정수
  # range(i, n)    : i ~ (n-1) 까지의 정수
  # range(i, n, x) : i ~ (n-1) 까지의 정수, x간격으로
  for i in range(1, 5, 2) :
    print(i)          # 1, 3
  ```
### enumerate()
- 시퀀스를 순회하며, 요소와 인덱스 쌍을 튜플로 반환
- 요소와 위치(순서)를 동시에 활용할 수 있음
- for loop의 시퀀스를 enumerate()로 감싸서 사용
  ```python
  fruits = ['apple', 'banana', 'cherry', 'strawberry']
  for index, fruit in enumerate(fruits, start=1) :
    print(f"{index} 번째 과일 : {fruit}")
  ```


## while
- 반복하여 수행될 명령은 indent로 구분
- 문법은 if와 유사
- break, continue 사용 가능
- 사용자 입력 대기 상황, 실시간 데이터 수집 등 특정 상황에만 활용용
  ```python
  counter = 0
  while counter < 3 :
    print(f"반복문 실행 중입니다. {counter}")
    counter += 1
  else : 
    print("반복문이 종료되었습니다.")

  # 주어진 숫자 리스트를 출력하다가 10보다 큰 값을 만나면 종료하라
  arr = [1, 3, 5, 11, 6, 15, 30]
  while i in arr :
    if i > 10 :
      break;
    else :
      print(i)
  
  # 주어진 숫자 리스트에서 10보다 큰 값을 제외하고 출력하라
  while i in arr :
    if i > 10 :
      continue
    else :
      print(i)
  ```
### pass
- 아무 작업도 수행하지 않고 코드블록을 빠져나오기 위한 예약어
- 아직 구현하지 않은 부분을 나타내거나, 차후 추가하기 위한 목적으로 활용
  ```python
  while True :
    user_input = input("원하는 작업을 선택하세요 (q로 종료) : ")
    if user_input == 'q' :
      break
    elif user_input == '1' :
      pass
    elif user_input == '2' :
      pass
  ```