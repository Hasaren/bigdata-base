# 반복문
# for과 문자열
hello = '안녕하세요!'
for h in hello:
    print(h)

# for과 리스트
li = [0,1,2,3,4,5,6,7]
for i in li:
    print(i)

# for과 딕셔너리
menu = {'김밥':3000, '라면':5000, '떡볶이':4000}
for m in menu:
    print(m)
    print(menu[m])

for k, v in menu.items():
    print(f'{k} : {v}')

# for range
for i in range(5):
    print(i)

for i in range(1,5):
    print(i)

for i in range(1,31,2): #홀수만
    print(i ,end=" ")
print('\n')

for i in range(31,0, -2): #홀수만 리버스
    print(i ,end=" ")
print('\n')