from turtle import Turtle, Screen, time
import random

# setup screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Welcome to the snake game!")
screen.tracer(0)

# create a snake body, aka three white turtles
starting_pos = [(0,0), (-20,0), (-40,0)]
segments = []
for position in starting_pos:
    new_seg = Turtle("square")
    new_seg.color("white")
    new_seg.penup()
    new_seg.goto(position)
    segments.append(new_seg)

# move the snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor
        new_y = segments[seg_num - 1].ycor
        segments[seg_num].goto(new_x, new_y)
        

# create snake food

# detect collision with food

# create a scoreboard

# detect collision with wall

# detect collision with tail














screen.exitonclick()