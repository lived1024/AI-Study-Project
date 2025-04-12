# 예외처리
- try :
  - {statement} # 예외가 일어날 수 있는 코드
- except (Error / Exception) :
  - {statement} # 예외가 일어나면 실행될 코드
- else :
  - {statement} # 예외가 없을 때 실행 될 코드
- finally :
  - {statement} # 예외 발생 여부와 무관하게 마지막에 실행될 코드
```python
try :
  value = int("abc")
except ValueError : 
  print("숫자로 변환할 수 없는 문자열입니다.")
except ZeroDivisionError :
  print("0으로 나눌 수 없습니다.")
except :
  print("알 수 없는 오류입니다.")
else :
  print("변환이 완료되었습니다.")
finally :
  print("프로그램을 종료합니다.")
```
- 타 언어의 try-catch 대신 try-except 구문을 사용한다.