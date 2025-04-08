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