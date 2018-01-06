import random


info = input("""
    ~ 신나는 가위바위보 ~

    1. 가위
    2. 바위
    3. 보

    원하는 선택지의 번호를 입력하세요:
    """)
case = ['가위', '바위', '보']
com = random.choices(case)
user = int(info)
score = 0
w = "이겼습니다"
l = "졌습니다"
d = "비겼습니다"


if int(info) == 1:
    if com == case[0]:
        print(d)
    elif com == case[1]:
        score -= 1
        print(l)
    else:
        score += 1
        print(w)
elif int(info) == 2:
    if com == case[0]:
        print(w)
    elif com == case[1]:
        score -= 1
        print(d)
    else:
        score += 1
        print(l)
else:
    if com == case[0]:
        print(l)
    elif com == case[1]:
        score -= 1
        print(w)
    else:
        score += 1
        print(d)
