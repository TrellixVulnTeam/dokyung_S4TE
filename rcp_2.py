import random


HISTORY = {
    'win': 0,
    'lost': 0,
    'draw': 0,
}


def play():
    while True:
        user_choice = get_user_input()
        result = calculate_result(user_choice)
        process_result(result)


def get_user_input():
    input_msg = "~ 신나는 가위바위보 ~\n\n" \
        + "1. 가위\n2. 바위\n3. 보\n\n" \
        + "원하는 선택지의 번호를 입력하세요.(exit=q) : "

    while True:
        print_history()
        input_str = input(input_msg)

        if input_str not in ['1', '2', '3', 'q', 'Q']:
            print("잘못 입력하였습니다. 다시 입력해주세요.")
        elif input_str in ['q', 'Q']:
            print("다음에 또 봐요~~")
            exit()
        else:
            break

    return int(input_str)


def print_history():
    msg = '\n***\nW : {0}, L : {1}, D : {2}\n***\n'.format(
        HISTORY['win'],
        HISTORY['lost'],
        HISTORY['draw']
    )
    print(msg)


def calculate_result(user_choice):
    user = user_choice
    com = random.randint(1, 3)

    if user == com:
        ret = "draw"
    elif (user % 3) == (com + 1) % 3:
        ret = "win"
    else:
        ret = "lost"

    return ret


def process_result(result):
    if result == "win":
        HISTORY['win'] += 1
        print("\n이겼습니다")

    elif result == "lost":
        HISTORY['lost'] += 1
        print("\n졌습니다")

    else:
        HISTORY['draw'] += 1
        print("\n비겼습니다")


if __name__ == '__main__':
    play()
