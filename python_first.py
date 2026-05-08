# 주석처리
# 변수 만들기
hello = '안녕 파이썬'
print(hello)

# 예약어 확인
import keyword
print(keyword.kwlist)

print()

# 이름, 나이 변수에 저장 후 출력
name = "hasaren"
age = 201
print(name, age, sep='*')
print(end='*')
print(name, age)

print()

# 자료형
# 기본 자료형 : int(정수), float(실수), bool(이진 true false), str(문자열)
# 컬렉션 자료형 : list, dict, tuple, set
num = 100
print(type(num))

num = 95.5
print(num)
print(type(num))

name = '홍길동'
print(name)
print(type(name))

result = True
print(result)
print(type(result))