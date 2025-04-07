# 파이썬의 자료구조

## Set
- 집합 자료구조
- 중복 불가능한 요소들로 구성
- 각 요소들이 해싱되어 저장, 순서를 가지지 않음 - 인덱스를 통한 요소 조회, 슬라이싱 불가능
- 정의 방법 : {} 또는 set()
    ```python
    my_set = {1, 2, 2, 3}     # {1, 2, 3}
    good_set = set("Good")    # {"G", "o", "d"}
    empty_set = set()
    ```
- 추가 삭제
    ```python
    add()       # 하나 추가
    update()    # 여러 값 추가
    remove()    # 값 삭제
    ```
- set은 집합에 관한 것을 처리하기 위한 데이터 타입
    - 합집합 : set1 | set2, set1.union(set2)
    - 교집합 : set1 & set2, set1.intersection(set2)
    - 차집합 : set1 - set2, set1.difference(set2)
    - 하위 집합 여부 : set1.issubset(set2)