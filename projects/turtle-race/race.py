from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=500)
colors = ['red', 'green', 'blue', 'orange', 'yellow', 'purple']

y_positions = [-100, -50, 0, 50, 100, 150]
is_race_on = False
all_turtles = []
winning_turtle = None

for tur_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[tur_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[tur_index])
    all_turtles.append(new_turtle)

user_bet = screen.textinput(title='Make your Bet', prompt='Which turtle will win the race? Enter your choice: '
                                                          'red | green | blue | orange| yellow | purple')
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 220:
            winning_turtle = turtle.pencolor()
            is_race_on = False
        else:
            forward_step = random.randint(0, 10)
            turtle.forward(forward_step)
timmy = Turtle()
timmy.penup()
timmy.hideturtle()
timmy.goto(x=-230, y=0)
timmy.hideturtle()
if winning_turtle:
    if winning_turtle == user_bet.lower():
        timmy.write(f'You have won! The {winning_turtle} turtle is the winner', font=("Calibri", 16, "bold"))
    else:
        timmy.write(f'You have lost! The {winning_turtle} turtle is the winner', font=("Calibri", 16, "bold"))

screen.exitonclick()
