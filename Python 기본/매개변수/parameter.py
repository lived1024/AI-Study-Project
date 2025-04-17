# 기본 매개변수
# def welcome(name="Guest", city)      -> 에러발생!! name은 기본 매개변수로, 일반 매개변수 뒤로 가야된다.
# def welcome(city, name="Guest", room=[]) :        # 가변 변수 room는 함수 실행마다 누적됨
def welcome(city, name="Guest", room=None) :
  if room == None :                                 # 함수 실행 시 초기화를 위해 None을 이용
    room = []

  room.append(101)
  print(f"Hello, {name}! This is {city}. You can use {room}")

welcome("New York")           # Hello, Guest
welcome("Busan", "Shin")     # Hello, Shin

# 키워드 인자
def display_info(name, age, city) :
  print(f"Name : {name}, Age : {age}, City : {city}")

display_info("Alice", 30, "New York")
display_info(city="Paris", name="Bob", age=22)

# 가변 인자 리스트
def calc_sum(*args) :
  total = 0
  for arg in args :
    total += arg

  return total

print(calc_sum(1,2,3,4))
print(calc_sum(10, 100))

# 키워드 가변 인자 리스트
def print_info(**kwargs) :
  for key, value in kwargs.items() :
    print(f"{key} : {value}")

print_info(name="Eve", age=28, city="Berlin")
info = {"name" : "Charlie", "age" : 35, "City" : "Tokyo"}
print_info(**info)