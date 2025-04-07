todo_list = []

while True :
  print("")
  print("할 일 목록 관리자")
  print("1. 할 일 추가")
  print("2. 할 일 삭제")
  print("3. 할 일 목록 보기")
  print("4. 종료")

  choice = input("선택 : ")
  if choice == "1" :
    add_item = input("할 일 입력 : ")
    todo_list.append(add_item)
    print(f"{add_item} 추가 완료.")
    pass
  elif choice == "2" :
    del_item = input("할 일 삭제 : ")
    todo_list.remove(del_item)
    print(f"{del_item} 삭제 완료.")
    pass
  elif choice == "3" :
    print(todo_list)
    pass
  elif choice == "4" :
    print("프로그램을 종료합니다.")
    break
  else :
    print("올바른 선택이 아닙니다. 다시 시도하세요")