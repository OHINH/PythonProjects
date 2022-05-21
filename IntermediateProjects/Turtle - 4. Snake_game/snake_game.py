from turtle import Turtle, Screen, time
from snake import Snake
import random

t = Turtle()

# setup screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Welcome to the snake game!")
screen.tracer(False)

# create a snake body, aka three white turtles
snake = Snake()

# control the snake
screen.listen()
screen.onkeypress(fun=snake.o, key="o")
screen.onkeypress(fun=snake.k, key="k")
screen.onkeypress(fun=snake.l, key="l")
screen.onkeypress(fun=snake.m, key="m")

# move the snake
game_is_on = True

while game_is_on: 
    screen.update()
    snake.move()  
    time.sleep(0.1)  

screen.mainloop()


# create snake food


# detect collision with food

# create a scoreboard

# detect collision with wall

# detect collision with tail














screen.exitonclick()