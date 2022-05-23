from objects import Paddle, Ball, Scoreboard, Ref
from turtle import Screen, Turtle, width

# screen
## color, update
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Classic Pong Game")
screen.tracer(0)


# middle line
## refereeturtle
referee = Ref()
screen.update()


# paddle
## co
# lor, height
## moving 
paddle_left = Paddle(position="left")
paddle_right = Paddle(position="right")

while 1 > 0:
    screen.update()
# moving ball
## same moving as platform, but also on x axis
# detect collision
## ball/platform
## ball/exitscreen left and right
## score



screen.mainloop()