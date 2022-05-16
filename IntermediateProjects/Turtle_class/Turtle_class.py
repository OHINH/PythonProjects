from os import terminal_size
from turtle import Turtle as Tl, Screen

Tim = Tl("arrow")
Tim.shape("turtle")
Tim.color("teal")


for i in range(25):
    Tim.forward(10)
    if i%2 == 0:
        Tim.penup()
    else:
        Tim.pendown()















screen = Screen()
screen.exitonclick()

