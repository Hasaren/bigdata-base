# 7
import random

word = ['낙하','불구덩이','몰라'] # 워드 모음
c = 1
q = random.choice(word) # 첫번째 워드 초기화
while True: # 문제 반복 시작
    
    ans = input(f"문제 {c} (종료: 0) : {q}\n")
    if ans == '0':
        break
    if q == ans:
        print('정답')
        q = random.choice(word) # 다음 문제 갱신
        c += 1 # 다음 문제 번호 갱신
    else:
        print("틀림")