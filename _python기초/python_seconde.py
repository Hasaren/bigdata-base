# 연산자
# 산술연산자 -> + - * / % // **
money = 10000
print(money//500)
print(money//100)
print()

price = 450
print(money//price)
print(money%price)

print()

# 대입연산자 =
# 복합 대입연산자 += -= *= /= //= %=
a=10
a+=10
print(a)

print()

# 비교 연산자 > < >= <= == !=
print(10==10)

print()

# 논리 연산자 and or not
a=10
b=60
print(a<50 and b>50)
print(a>50 or b<50)

c = a <50
print(not c)

# 문자열 연산자 +(연결) *(반복)
print('='*50)
head = '파이썬'
tail = '짱!'
print(head+tail)
print('='*50)

# in 연산자
print(head in '파이썬짱')
print(tail in '파이썬 짱 !')

print(tail not in '파이썬 짱 !')