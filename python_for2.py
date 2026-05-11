# 구구단 2단
# for i in range(1, 10):
    # print(f'2 * {i} = {2*i}')

# 단을 입력 받아 구구단 출력
# num = int(input('단: '))
# for i in range(1,10):
#     print(f'{num} * {i} = {num*i}')

# 구구단 전체
# for i in range(2,10):
#     print(f'====={i}단=====')
#     for j in range(1,10):
#         print(f'{i} * {j} = {i*j}')

# 중첩 for문
main = ['베이컨', '크래미']
side = ['당근','오이']
x =1 
for m in main:
    for s in side:
        print(f'{x}: {m}+{s}+계란')
        x += 1