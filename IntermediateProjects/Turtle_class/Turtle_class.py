from os import terminal_size
import random
from turtle import Turtle as Tl, Screen

Tim = Tl("arrow")
Tim.shape("turtle")
Tim.color("teal")


def dashed_line():
    for i in range(25):
        Tim.forward(10)
        if i%2 == 0:
            Tim.penup()
        else:
            Tim.pendown()


colors = ["black", "yellow", "red", "blue", "grey", "teal", "medium aquamarine"]

def draw_a_polygon(nb_sides):
    angle = 360/int(nb_sides)
    for _ in range(nb_sides):
        Tim.forward(100)
        Tim.right(angle)

for i in range(3,10):
    Tim.color(random.choice(colors))
    draw_a_polygon(i)













screen = Screen()
screen.exitonclick()

