from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('white')
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def increase_scoreboard(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'Score: {self.score}', align='center', font=("Courier", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f'Game Over', align='center', font=("Courier", 24, "normal"))
