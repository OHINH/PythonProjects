import random
from tkinter import N
import turtle as tl

colors = ["black", "yellow", "red", "blue", "grey", "teal", "medium aquamarine"]
directions = [0, 90, 180, 270]
tl.colormode(255)

Tim = tl.Turtle("arrow")
Tim.shape("turtle")
Tim.color("teal")


def dashed_line():
    for i in range(25):
        Tim.forward(10)
        if i%2 == 0:
            Tim.penup()
        else:
            Tim.pendown()




def random_RGB_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)

def random_direction():
    Tim.pensize(10)
    Tim.speed("fastest")
    for i in range(200):
        Tim.setheading(random.choice(directions))
        Tim.color(random_RGB_color())
        Tim.forward(20)

# random_direction()

def draw_a_circle(radius):
    Tim.speed("fastest")
    Tim.circle(radius, None, 100)

def draw_a_polygon(nb_sides):
    Tim.speed(0)
    angle = 360/int(nb_sides)
    for _ in range(nb_sides):
        Tim.forward(50)
        Tim.right(angle)

# for i in range(3,10):
#      Tim.color(r, g, b))
#      draw_a_polygon(i)

def spirograph(space_between_poly, nb_sides):
    Tim.speed(0)
    for i in range(int(360/space_between_poly)):
        Tim.color(random_RGB_color())
        draw_a_polygon(nb_sides)
        Tim.setheading(Tim.heading() + space_between_poly)





screen = tl.Screen()
screen.screensize(10000,10000)
spirograph(space_between_poly=5, nb_sides=1)
screen.screensize()
screen.exitonclick()

