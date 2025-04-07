my_dict = {} # 딕셔너리 선언
my_dict['key'] = 'value'
print(my_dict)

person = {'name' : '홍길동', 'age' : 33, 'city' : '서울'}
print(f"나이 : {person['age']}")
person['age'] = 35
print(f"이름은 {person['name']}, 나이는 {person['age']}, 고향은 {person['city']} 입니다.")

# 아래처럼 정의되지 않은 값을 사용 시 에러 발생 ( javascript처럼 undefined가 뜨지 않고 에러 발생)
# get함수를 이용하여 nvl과 같이 이용 가능
#country = person['country']
country = person.get('country', 'unknown')
print(f"국적은 {country} 입니다.")
person['country'] = '대한민국'
country = person.get('country', 'unknown')
print(f"국적은 {country} 입니다.")


# dictionary의 update 함수를 이용하면 두 dictionary를 합친다
org_dict = {'name' : '홍길동', 'age' : 33, 'city' : '서울'}
add_dict = {'country' : '대한민국', 'married' : True}
org_dict.update(add_dict)
print(org_dict.keys())

# dictionary 키 삭제
del org_dict['married']
print(org_dict.keys())