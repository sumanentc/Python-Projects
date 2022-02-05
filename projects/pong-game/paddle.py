from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(x_cor, y_cor)

    def go_up(self):
        new_ypos = self.ycor() + 20
        self.goto(self.xcor(), new_ypos)

    def go_down(self):
        new_ypos = self.ycor() - 20
        self.goto(self.xcor(), new_ypos)
