import random


class UserInterface(object):
    input_msg = "~ 신나는 가위바위보 ~\n\n" \
        + "1. 가위\n2. 바위\n3. 보\n\n" \
        + "원하는 선택지의 번호를 입력하세요.(exit=q) : "

    def get_user_input(self):
        while True:
            self.input_str = input(self.input_msg)

            if self.validate_input_str():
                break
            else:
                self.print_error_msg()

        if self.is_quit():
            print("다음에 또 봐요~~")
            exit()

        return int(self.input_str)

    def validate_input_str(self):
        return self.input_str in ['1', '2', '3', 'q', 'Q']

    def print_error_msg(self):
        print("잘못 입력하였습니다. 다시 입력해주세요.")

    def is_quit(self):
        return self.input_str in ['q', 'Q']


class ScoreBoard(object):
    win = 0
    lost = 0
    msg_format = '\n***\nW : {0}, L : {1}***\n'

    def print_score(self):
        msg = self.render_msg()
        print(msg)

    def render_msg(self):
        return self.msg_format.format(self.win, self.lost)

    def append_score(self, result):
        if result == 'win':
            self.win += 1
        elif result == 'lost':
            self.lost += 1


class DrawableScoreBoard(ScoreBoard):
    draw = 0
    msg_format = '\n***\nW : {0}, L : {1}, D : {2}\n***\n'

    def render_msg(self):
        return self.msg_format.format(self.win, self.lost, self.draw)

    def append_score(self, result):
        super().append_score(result)
        if result == 'draw':
            self.draw += 1


class RCPGameBot(object):
    user = None
    rcp = None
    result = None

    ui = UserInterface()
    score_board = DrawableScoreBoard()

    def play(self):
        while True:
            self.get_user_input()
            self.pick_rcp()
            self.calculate_result()
            self.print_result()
            self.refresh_scoreboard()
            self.print_score()

    def get_user_input(self):
        self.user = self.ui.get_user_input()

    def pick_rcp(self):
        self.rcp = random.randint(1, 3)

    def calculate_result(self):
        if self.user == self.rcp:
            self.result = "draw"
        elif (self.user % 3) == (self.rcp + 1) % 3:
            self.result = "win"
        else:
            self.result = "lost"

    def print_result(self):
        if self.result == "win":
            print("\n이겼습니다")
        elif self.result == "draw":
            print("\n비겼습니다")
        else:
            print("\n졌습니다")

    def refresh_scoreboard(self):
        self.score_board.append_score(self.result)

    def print_score(self):
        self.score_board.print_score()


if __name__ == '__main__':
    game_bot = RCPGameBot()
    game_bot.play()
