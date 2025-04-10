# 메뉴는 아래와 같다
# 1. 성적 입력하기
# 2. 학생 조회하기
# 3. 학점 조회하기     (A: 90~99, B: 80~89, C: 70~79, D: 60~69, F: ~59)
# 0. 종료하기
# 메뉴를 입력받고, 학생의 이름과 학점을 입력받는다.
# 조회 시에는 등록된 학생의 목록을 출력
# 학점 조회 시에는 이름을 입력받아 성적 출력

score_list = []
students = {}

while True :
  print("")
  print("성적 관리 프로그램")
  print("1. 성적 입력하기")
  print("2. 학생 조회하기")
  print("3. 학점 조회하기")
  print("0. 종료하기")
  menu_number = input(f"메뉴 번호를 입력하세요 : ")

  if menu_number == "0" :
    print("프로그램이 종료되었습니다.")
    break
  elif menu_number == "1" :
    name = input("이름을 입력하세요 : ")
    score = input("성적을 입력하세요 : ")
    students[name] = int(score)
    print(f"{name}의 성적은 {students[name]}입니다.")
  elif menu_number == "2" :
    name = input("조회할 학생의 이름을 입력하세요 : ")
    if name in students.keys() :
      print(f"{name}의 점수는 {students[name]}")
    else :
      print(f"{name}은 등록되지 않았습니다.")
  elif menu_number == "3" :
    name = input("조회할 학생의 이름을 입력하세요 : ")
    if name not in students.keys() :
      print(f"{name}은 등록되지 않았습니다.")
      continue

    score = students[name]
    grade = ""
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
    print(f"{name} 학생의 학점은 {grade}입니다.")
  else :
    print(f"잘못된 메뉴가 입력되었습니다.")
    continue






