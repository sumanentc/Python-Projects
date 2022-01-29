import random

import colorgram
import turtle as t

tim = t.Turtle()
# It will allow us to provide custom colors
t.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()


def extract_colors(size):
    """Extract RGB Colors from the image"""
    colors = colorgram.extract('image.jpg', size)
    rgb_colors = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        rgb_colors.append(new_color)
    return rgb_colors


def initialize_painting():
    """Initialize the Painting position"""
    tim.setheading(230)
    tim.forward(380)
    tim.setheading(0)


initialize_painting()
color_list = extract_colors(50)
number_of_dots = 130
for dot_count in range(1, number_of_dots + 1):
    tim.dot(30, random.choice(color_list))
    tim.forward(50)
    # Going back to starting point
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()
