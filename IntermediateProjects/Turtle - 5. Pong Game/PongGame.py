import time
from objects import Paddle, Ball, Scoreboard, Ref
from turtle import Screen, Turtle, left, right, width


# screen
## color, update
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Classic Pong Game")
screen.tracer(0)
referee = Ref()


# paddle
## color, height
## moving 
paddle_right = Paddle(position=(350,0))
paddle_left = Paddle(position=(-350,0))

screen.listen()
screen.onkey(fun=paddle_left.move_up, key="e")
screen.onkey(fun=paddle_left.move_down, key="d")
screen.onkey(fun=paddle_right.move_up, key="o")
screen.onkey(fun=paddle_right.move_down, key="l")

game_is_on = True
while game_is_on:
    screen.update()
    
# moving ball
## same moving as platform, but also on x axis
# detect collision
## ball/platform
## ball/exitscreen left and right
## score



screen.mainloop()