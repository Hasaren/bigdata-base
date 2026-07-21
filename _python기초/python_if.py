# 회원이면 어서오세요 인사말 출력
# member = input('회원입니까? (y/n): ')
# if member == 'y':
#     print('어서오세요')
# else:
#     print('회원가입으로 이동합니다.')


# member = input('회원입니까? (y/n): ')
# if member == 'y':
#     print('어서오세요')
# elif member == 'n':
#     print('회원가입으로 이동합니다.')
# else:
#     print('잘못된 입력입니다.')

# 입장료 2만원, 6세미만 무료, 60세 미만 정가, 60세 이상 50% 할인

age = int(input("나이 : "))
price = 20000

if age < 6:
    print('입장료 무료')
elif age<60:
    print(f'입장료 {price}')
else:
    print(f'입장료 {int(price*0.5)}')