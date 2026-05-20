# # 도서관 좌석 예약 시스템
# # 1. 회원등급 - 정회원, 우수회원 --> 예약 권한
# #               나머지 등급 --> 예약 불가
# # 2. 좌석 예약 - 좌석 번호 00 좌석이 예약이 완료되었습니다.
# # 3. main - 회원 등급 입력 -> 좌석 번호 입력 -> 1,2번에 따라 결과 도출

# def reserve_seat(seat_num):
#     """
#     매개변수(파라미터)
#     seat_num : 좌석 번호

#     입력된 좌석 번호를 화면에 보여주는 함수
    
#     """
#     print(f'{seat_num}번 좌석 예약이 완료되었습니다.')

# def check_membership(grade):
#     """
#     매개변수(파라미터)
#     grade : 회원 등급 (준회원/정회원/우수회원)

#     반환값(return) : True / False   

#     정회원, 우수회원 --> 좌석 예약 권한 부여
#     """
#     if grade == '정회원' or grade == '우수회원':
#         print('예약 권한 확인 완료')
#         return True
#     else:
#         print('예약 권한이 없습니다.')
#         return False
    
# if __name__ == '__main__':
#     grade = input('회원등급 입력하세요: ')
#     if check_membership(grade):
#         seat_num = int(input('원하는 좌석 번호: '))
#         reserve_seat(seat_num)


# 도서관
# reserved_seats = []  # 예약된 좌석 번호 목록


# def reserve_seat(grade, seat_number):
#     reserved_seats.append(seat_number)
#     print(f"🪑 [{grade}]{seat_number}번 좌석 예약 완료!")


# def show_reserved():
#     if not reserved_seats:
#         print("[현황] 예약된 좌석이 없습니다")
#     else:
#         print(f"[현황] 예약된 좌석:{sorted(reserved_seats)}")

# # ↓ 여기서부터 작성하세요

# def check_membership(grade):
#     """
#     매개변수(파라미터)
#     grade : 회원 등급 (준회원/정회원/우수회원)

#     반환값(return) : True / False   

#     정회원, 우수회원 --> 좌석 예약 권한 부여
#     """
#     if grade == '정회원' or grade == '우수회원':
#         print('예약 권한 확인 완료')
#         return True
#     else:
#         print('예약 권한이 없습니다.')
#         return False


# def check_seat(seat_number):
#     if 1<=seat_number<=50:
#         if seat_number not in reserved_seats:
#             return True
#         else:
#             print("이미 예약된 좌석입니다.")
#             show_reserved()
#             return False
#     else:
#         print("유효하지 않은 좌석입니다.")
#         return False


# if __name__ == "__main__":
#     while True:
#         print('\n--- 도서관 좌석 예약 시스템 ---\n1. 좌석 예약\n2. 예약 현황 보기\n3. 종료')
#         menu = int(input('메뉴 선택: '))

#         if menu == 3:
#             break
#         elif menu == 2:
#             show_reserved()
#         else:
#             grade = input('회원등급 입력하세요: ')
#             if check_membership(grade):
#                 seat_num = int(input('원하는 좌석 번호: '))
#                 if check_seat(seat_num):
#                     reserve_seat(grade, seat_num)

# # 카페

# menu_l = ["아메리카노", "카페라떼", "카푸치노"]
# def make_coffee(menu, quantity):
#     print(f"☕{menu}{quantity}잔 제조를 시작합니다!")


# # ↓ 여기서부터 작성하세요

# def check_menu(menu):
#     if menu in menu_l:
#         print("[메뉴확인] 주문 가능한 메뉴입니다")
#         return True
#     else:
#         print("[메뉴확인] 주문 불가능한 메뉴입니다")
#         return False


# def check_quantity(quantity):
#     if 1<=quantity<=10:
#         print("[수량확인] 주문 수량이 유효합니다")
#         return True
#     else:
#         print("[수량확인] 수량은 1잔 이상 10잔 이하만 가능합니다")
#         return False


# if __name__ == "__main__":
#     m = input('주문할 메뉴를 입력하세요: ')
#     n = int(input('수량을 입력하세요: '))
#     if check_menu(m) and check_quantity(n):
#         make_coffee(m, n)


# # 영화관
# def book_movie(title, seat):
#     print(f"🎬{title}{seat}번 좌석 예매가 완료되었습니다!")


# # ↓ 여기서부터 작성하세요

# def check_age(age):
#     if age>=15:
#         print("[나이확인] 관람 가능합니다")
#         return True
#     else:
#         print("[나이확인] 15세 미만은 관람 불가합니다")
#         return False


# def check_seat(seat):
#     if 1<=seat<=100:
#         print("[좌석확인] 유효한 좌석 번호입니다")
#         return True
#     else:
#         print("[좌석확인] 좌석 번호는 1번에서 100번 사이여야 합니다")
#         return False


# if __name__ == "__main__":
#     age = int(input('나이를 입력하세요: '))
#     seat = int(input('좌석 번호를 입력하세요: '))
#     if check_age(age) and check_seat(seat):
#         title = input('예매할 영화 제목을 입력하세요: ')
#         book_movie(title, seat)

# 헬스장

def enter_gym(name, locker):
    print(f"💪{name}님,{locker}번 락커를 사용하세요. 입장을 환영합니다!")


# ↓ 여기서부터 작성하세요

def check_membership(membership):
    if membership == '유효':
        print("[회원권확인] 입장 가능합니다")
        return True
    else:
        print("[회원권확인] 유효한 회원권이 없습니다" )
        return False


def check_locker(locker):
    if 1<=locker<=50:
        print("[락커확인] 사용 가능한 락커 번호입니다")
        return True
    else:
        print("[락커확인] 락커 번호는 1번에서 50번 사이여야 합니다")
        return False


if __name__ == "__main__":
    membership = input('회원권 상태를 입력하세요 (유효/만료): ')
    locker = int(input('락커 번호를 입력하세요: '))
    if check_membership(membership) and check_locker(locker):
        name = input('이름을 입력하세요: ')
        enter_gym(name, locker)