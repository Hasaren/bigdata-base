#사용자 정의 함수

# def add(number1, number2):
#     print("계산시작")
#     return number1 + number2


# result = add(50, 60)
# print(result)

# def add(num1, num2):
#     print(num1 + num2)

# def coffee():
#     print("진행중")
#     result = '아메리카노'
#     return result

# result = coffee() 
# print(result)

# def coffee():
#     print('진행중')

# coffee()

# def add_sum(n1, n2):
#     return n1 + n2, n1 - n2
# result = add_sum(60,50)
# print(result)

# print(add_sum(200,100))

# 함수 정의 --> 이름 자유
# 1부터 원하는 값까지 더해주는 함수
# 결과 변수에 return값을 담는다.
def add_up(num):
    a = 0
    for i in range(1, num+1):
        a += i
    return a

num = int(input("원하는 값: "))
result = add_up(num)
print(result)