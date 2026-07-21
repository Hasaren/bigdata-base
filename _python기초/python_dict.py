# 딕셔너리
a = {}
print(a)

b = dict()
print(b)

# 딕셔너리 초기화 {키:내용, 키:내용}
menu = {'김밥':3000, '라면':5000}
print(menu)
print(menu['김밥'])

# 새로운 쌍 추가
menu['떡볶이'] = 4000
print(menu)

# 기존 값 수정
menu['김밥'] = 3500
print(menu)

# 키 삭제
del(menu['라면'])
print(menu)

# set 자료형 -> 중복 X, 순서 X
a = {30,20,10}
print(a)

b = set() # 빈set
print(b)

c = {40,20}
print(c)

# 교집합
print(a & c)
# 합집합
print(a|c)
# 차집합
print(a-c)
print(c-a)