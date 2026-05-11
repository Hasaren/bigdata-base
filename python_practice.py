# 1
# univ = input("학교:")
# dept = input("학과:")
# name = input("이름:")
# phone = input("연락처:")
# print(f'{name}{univ}{dept}{phone}')

# # 2
# name = input("이름:")
# year = int(input("출생연도:"))
# age = 2026-year+1
# print(f'{name}{age}')

# # 3
# month = int(input("월 입력: "))
# if month <= 2:
#     print(f'{month} 겨울')
# elif month <= 5:
#     print(f'{month} 봄')
# elif month <= 8:
#     print(f'{month} 여름')
# elif month <= 11:
#     print(f'{month} 가을')
# else:
#     print(f'{month} 겨울')

# # 4
# s1 = int(input("1차:"))
# s2 = int(input("2차:"))
# if ((s1+s2)/2 >=70) and (s1>=50) and (s2>=50):
#     print('합격')
# else:
#     print("불합격")

# # 5
# import random

# a = random.randint(1,31)
# ans = None
# while True:
#     ans = int(input("숫자 입력(종료: 0): "))
#     if ans == 0:
#         print('종료')
#         break
#     if a == ans:
#         print('정답')
#         break

#     if ans > a:
#         print('더 작은 수')
#     elif ans < a:
#         print('더 큰 수')

# # 6
# import random
# ans = []
# while True:
#     if len(ans)==6:
#         break
#     a = random.randint(1,46)
#     if a not in ans:
#         ans.append(a)
# print(ans)

# #sample함수 범위에서 개수만큼 중복되지 않게 추출
# lotte2 = random.sample(range(1,46),6)

# # 7
# import random

# word = ['낙하','불구덩이','몰라']
# c = 1
# q = random.choice(word)
# while True:
    
#     ans = input(f"문제 {c} (종료: 0) : {q}\n")
#     if ans == '0':
#         break
#     if q == ans:
#         print('정답')
#         q = random.choice(word)
#         c += 1
#     else:
#         print("틀림")
    

# # 8
# vote = {'대성리':0,
#         '춘천':0,
#         '을왕리':0,
#         '청평':0}

# for key in vote:
#     print(f'{key}: {vote[key]}표', end=' ')
# print('\n')

# print('MT투표')

# while True:
#     v = input("장소: ")
#     if not v:
#         break
#     else:
#         vote[v] += 1

# # m = 0
# # k = ''
# # for key in vote:
# #     print(f'{key}: {vote[key]}표', end=' ')
# #     if m < vote[key]:
# #         m = vote[key]
# #         k = key
# # print('\n')
# # print(f'최다 득표: {k} {m}표')

# for key in vote:
#     print(f'{key}: {vote[key]}표', end=' ')
# print('\n')

# max_key = max(vote, key=vote.get)

# print(f'최다 득표: {max_key} {vote[max_key]}표')

# # 10
# def price(menue):
#     m = {1: f'아메리카노: {3000:,}원',
#             2: f'카페라떼: {4000:,}원',
#             3: f'바닐라라떼: {4500:,}원'}
#     print(m[menue])

# menue=int(input("메뉴선택(1:아메리카노/2:카페라떼/3:바닐라라떼) "))
# price(menue)

# 11
files = ['re.hwp','ne','at.png','di.jpg','add.xslx']
print(list(filter(lambda x:'.jpg' in x or '.png' in x, files)))