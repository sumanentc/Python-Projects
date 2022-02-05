from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('white')
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def increase_l_point(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def increase_r_point(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-100, 200)
        self.write(f'{self.l_score}', align='center', font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(f'{self.r_score}', align='center', font=("Courier", 80, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f'Game Over', align='center', font=("Courier", 24, "normal"))
