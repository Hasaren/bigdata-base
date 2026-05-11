# 람다 표현식
# 익명 함수 (이름없는 함수)
# lambda 매개변수들: 식

# def plus_five(x):
#     return x+5

# plus_five(10)


# plus_five_l = lambda x:x+5
# plus_five_l(10)

# map(함수, 시퀀스 자료형)

result = map(lambda x: x+10, [30,20,10])
print(list(result))

# filter 함수: 조건에 맞는 것만 뽑아낸다.
result2 = filter(lambda x: x<20, [30, 20,10])
print(list(result2))