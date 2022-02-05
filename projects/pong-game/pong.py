from turtle import Screen

from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('pong')

# Turn off animation to show paddle after it has been shifted
screen.tracer(0)

right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)
ball = Ball()
score = ScoreBoard()

screen.listen()
screen.onkey(right_paddle.go_up, 'Up')
screen.onkey(right_paddle.go_down, 'Down')
screen.onkey(left_paddle.go_up, 'w')
screen.onkey(left_paddle.go_down, 's')

game_is_on = True

while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # bounce when the ball hit the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with the paddle
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or (
            ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # detect R paddle miss
    if ball.xcor() > 380:
        ball.reset_pos()
        score.increase_l_point()

    # detect L paddle miss
    if ball.xcor() < -380:
        ball.reset_pos()
        score.increase_r_point()

screen.exitonclick()
