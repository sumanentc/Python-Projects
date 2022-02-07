from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('white')
        self.goto(0, 270)
        self.hideturtle()
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.update_scoreboard()

    def increase_scoreboard(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}', align='center', font=("Courier", 24, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f'{self.high_score}')
        self.score = 0
        self.update_scoreboard()
