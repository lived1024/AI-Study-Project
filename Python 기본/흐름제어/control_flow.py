# 단일 조건 조건문

# 50보다 큰 경우 Great, 20보다 큰 경우 Big, 그렇지 않은 경우 Small
value = 51
if value > 50 :
  print("Great")
elif value <= 50 and value > 20 :
  print("Big")
else:
  print("Small")


# 날씨가 흐리고, 강수확률이 70% 이상이면 -> 비가 온다.
condition = "맑음"
rain_rate = 0.70
if condition is "흐림" and rain_rate >= 0.7 :
  print("비가 올 확률이 높습니다.")
elif condition is "흐림" :
  print("날씨가 많이 흐립니다.")
elif condition is "맑음" and rain_rate >= 0.7 :
  print("맑지만 비가 올 확률이 높습니다.")


# 사용자로부터 두 개의 값을 입력받고, 첫번째가 크면 Win, 두번째가 크면 Lose, 같으면 Draw

value1 = input("첫 번째 값을 입력하세요.")
value2 = input("두 번째 값을 입력하세요.")

num_var1 = int(value1)
num_var2 = int(value2)

if num_var1 > num_var2 :
  print("Win")
elif num_var1 < num_var2 :
  print("Lose")
else :
  print("Draw")


# 시험점수 입력받아 성적 출력 (A: 90~99, B: 80~89, C: 70~79, D: 60~69, F: ~59)
score = int(input("시험 성적을 입력하세요."))
if score >= 90 and score < 100 :
  grade = "A"
elif score >= 80 and score < 90 :
  grade = "B"
elif score >= 70 and score < 80 :
  grade = "C"
elif score >= 60 and score < 70 :
  grade = "D"
elif score >= 1 and score < 60 :
  grade = "F"
else :
  grade = "ERROR"

if grade != "ERROR" : print(f"성적은 {grade}입니다")