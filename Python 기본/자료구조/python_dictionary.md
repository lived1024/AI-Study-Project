# 파이썬의 자료구조

## Dictionary(딕셔너리)
- 매핑 자료구조
- Key - Value
- 해시 테이블과 유사
    ```python
    my_dict = {'one' : 1, 'two' : 2, 'three' : 3}
    my_dict['one']     # 1
    ```
- Key : 불변 타입만 사용 가능 ( List는 불가능, Tuple은 가능)
- Value : 다양한 타입 사용 가능
- Javascript의 Object와 유사사
- 활용방법
    ```python
    keys()   # key 목록
    values() # value 목록
    items()  # key, value 쌍으로 얻어오기
    ```