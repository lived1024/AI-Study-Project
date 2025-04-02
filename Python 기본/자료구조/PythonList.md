# 파이썬의 자료구조

## List(리스트)
- 열거형 자료구조
- 순서대로 값을 저장
- 배열과 유사
- <u>각 요소들이 다른 데이터 타입으로 구성될 수 있음</u>
- 문자열과 같이 index로 접근이 가능하며 slicing도 가능하다
- <u>리스트에 +, * 연산 사용 가능</u>
    ```python
    [1,2] + ['a','b']     # [1,2,'a','b']
    [1,2] * 2             # [1,2,1,2]
    ```
- len, max, min 등과 같은 기본 함수 활용 가능
- 요소 찾기
    ```python
    s = ['l','i','s','t']
    print(s.index('i'))     # 1
    print('t' in s)         # True
    print('x' not in s)     # True
    print(s.count('l'))     # 1   (일치하는 요소의 개수)
    ```
- 요소 수정
    ```python
    append()        # 추가
    insert()        # 삽입
    extend()        # 확장(list와 list를 합칠때 사용)
    del, remove()   # 제거
    pop()           # 특정 위치의 요소를 리턴하면서 제거
    sort()          # 정렬
    reverse()       # 역순 정렬
    ```