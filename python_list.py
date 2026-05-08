# 빈 리스트 생성
li = []
print(li)

li2 = list()
print(li2)


# append()
li.append('1요소')
print(li)

li.append(100)
print(li)

# 인덱싱
print(li[0])

# 슬라이싱 list[a:b:증감값(디폴트=1)]
s_li = [0,1,2,3,4,5,6,7]
print(s_li[1:4])
print(s_li[1:])
print(s_li[:6])
print(s_li[:])
print(s_li[::-1]) # 리버스

# 리스트 요소 변경
s_li[3] = '아이바오'
print(s_li)
