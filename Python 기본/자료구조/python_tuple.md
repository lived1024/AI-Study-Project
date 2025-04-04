# 파이썬의 자료구조

## Tuple(튜플)
- 열거형(Sequence Type) 자료구조
- 순서대로 값을 저장
- 배열과 유사
- 불변 속성(변경 X)
- 괄호를 사용하고, 각 항목은 쉼표로 구분
    ```python
    empty_tuple = ()
    single_tuple = (1, )
    my_tuple = (1, 2, 3, 4)
    ```
- 인덱스, 슬라이싱, +, * 가능
    ```python
    my_tuple = (1, 2, 3, 4)
    my_tuple[1]         # 2
    my_tuple[:2]        # (1, 2)
    ```
- len, max, min 사용 가능

### 패킹
여러 값을 하나의 튜플로 묶는 것
```python
# 아래 두 코드는 동일하게 튜플을 생성함
tp = 1, 2, 3
tp = (1, 2, 3)
```
### 언패킹
튜플의 요소를 개별적인 변수에 할당하는 것
```python
tp = (1,2,3)
x,y,z = tp
x,_,_,y,z = (1, -1, 0, 2, 5)   # 필요한 값만 변수에 할당 가능

# 언패킹 변수에 *를 붙이면 남은 요소 전체를 리스트에 담아 할당됨
values = 1, 2, 3, 4, 5
val1, val2, *vals = values              # values => [3, 4, 5]
val1, *vals, val2, val3 = values        # values => [2, 3]
```