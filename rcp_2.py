import random

score = 0
w = "이겼습니다"
l = "졌습니다"
d = "비겼습니다"

while True:
    user = int(input("""
~ 신나는 가위바위보 ~

1. 가위
2. 바위
3. 보

원하는 선택지의 번호를 입력하세요:
    """))

    com = random.randint(1, 3)

    if user == com:
        score += 0
        print(d)
    elif user == 1:
        if com == 2:
            score += 1
            print(l)
        elif com == 3:
            score -= 1
            print(w)
    elif user == 2:
        if com == 3:
            score += 1
            print(l)
        elif com == 1:
            score -= 1
            print(w)
    else:
        if com == 1:
            score += 1
            print(l)
        elif com == 2:
            score -= 1
            print(w)

    end = input("""
게임을 더 하시겠습니까?
1. 네
2. 아니요

원하는 선택지의 번호를 입력하세요:
        """)
    if end == "2":
        break

