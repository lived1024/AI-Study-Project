# 문자열
# 특이하게도 문자열에 *(곱하기) 연산을 사용하여 반복시킬 수 있음.
strMsg = "abc"
print(strMsg * 3)

# 자바와는 다르게 문자열 자체에 인덱스를 찾을 수 있음
print(strMsg[1])

# substring을 slicing이라는 이름으로 다음과 같이 사용가능 - 시작Idx, 개수
print(strMsg[0:2])

# 문자열 만들기
weather = '맑음'
temp = 20

# %s : 문자열
# %d : 정수
# %f : 실수

# %연산자 포메팅
print("오늘 날씨는 %s 입니다. 기온은 %d도 입니다."%(weather, temp))
# format 함수
print("오늘 날씨는 {0} 입니다. 기온은 {1}도 입니다.".format(weather, temp))
# format string : 가독성 good!
print(f"오늘 날씨는 {weather}, 기온은 {temp + 1}도 입니다.")