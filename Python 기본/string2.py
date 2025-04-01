# 문자열 변수 선언
str_var = "This is my python code."

# 쌍따옴표 3번을 하면 입력한 대로 출력된다. - 출력 시 줄바꿈 적용되어있음
# multi_line = """I'm a developer.
# I use python.
# Thank you."""

# print(str_var)
# print(multi_line)


# 문자열 더하기
# inum1 = 12
# inum2 = 34
# print(inum1 + inum2)   # 46

# snum1 = "12"
# snum2 = "34"
# print(snum1 + snum2)   # 12345

# 문자열 인덱싱
# print(str_var[11]) # p
# print(str_var[-1])
# print(str_var[-5])

# 슬라이싱
# print(str_var[11:17])   # python
# print(str_var[11:-6])   # python
# print(str_var[:10])

# isalpha 알파벳 여부
# str_test1 = "apple"
# str_test2 = "apple."
# print(str_test1.isalpha()) # True
# print(str_test2.isalpha()) # False : 마침표 또는 공백이 있으면 False

# isdecimal 숫자여부
# num_test1 = "12"
# print(num_test1.isdecimal()) # True

# upperCase, lowerCase
# print(str_var.upper())
# print(str_var.lower())

# swapcase - 대,소문자 반대로
# print(str_var.swapcase())

# replace
# print(str_var.replace("my", "your"))



# Format String
# weather = "흐림"
# temp = 15.8
# % code
# print("--------------- % code ---------------")
# print("[ %s / %f ] 오늘 날씨는 %s 입니다. 기온은 %f도 입니다." %(weather, temp, weather, temp))
# .format()    - 
# print("--------------- .format() ---------------")
# print("오늘 날씨는 {} 입니다. 기온은 {}도 입니다.".format(weather, temp))
# print("[ {0} / {1} ] 기온은 {1}도 입니다. 오늘 날씨는 {0} 입니다.".format(weather, temp))
# f""
# print("--------------- f 리터럴 ---------------")
# print(f"오늘 날씨는 {weather} 입니다. 기온은 {temp} 입니다.")

# 사용자로부터 입력받아 + 1 해서 출력
text = input("숫자를 입력해주세요.") # input 받는 값은 문자열임
num = int(text) + 1
print(f"입력받은 숫자는 {text}이고 변환된 숫자는 {num}입니다.") 