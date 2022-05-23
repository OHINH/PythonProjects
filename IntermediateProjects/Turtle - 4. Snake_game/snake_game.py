from turtle import Turtle, Screen, time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import random


# setup screen
screen = Screen()
screen.setup(width=600, height=700)
screen.bgcolor("black")
screen.title("Classic snake game")
screen.tracer(False)

# create a snake body, aka three white turtles
snake = Snake()
food = Food()
scoreboard = Scoreboard()

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
    
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.score += 1
        scoreboard.sc_refresh()
        snake.grow()

    if snake.head.xcor() < -290 or snake.head.xcor() > 290 or snake.head.ycor() < -300 or snake.head.ycor() > 270:
        game_is_on = False
        scoreboard.game_over()


    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            game_is_on = False
            scoreboard.game_over()

    

screen.mainloop()


# create snake food


# detect collision with food

# create a scoreboard

# detect collision with wall

# detect collision with tail














screen.exitonclick()