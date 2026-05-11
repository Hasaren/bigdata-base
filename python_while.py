# while <형식>
# while 조건식:
# 참이면 진행 거짓이면 탈출

# while True:
#     print('z',end='')

#=====

# year = 1
# while year <= 3:
#     print(f'서당개 {year}년')
#     year +=1
# print('풍월')

# result = None
# while result != 'y':
#     print('파이썬 좋아')
#     result = input('계속 : (종료: y): ')

# print('종료')

# 캐릭터 체력 100
# 데미지 (정수) -input

# hp = 100
# while hp > 0:
#     de = int(input('공격: '))
#     hp -= de
# print('종료')

# while True:
#     num = int(input("번호 입력(종료: 0): "))
#     if num == 0:
#         break
#     print('반복 중')

# continue 해당 차례 건너 뛰기
for x in range(1,31):
    if x % 7 != 0:
        continue
    print(f'7의 배수 {x}')