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
ball = Ball()
left_scoreboard = Scoreboard(-40)
right_scoreboard = Scoreboard(40)


screen.listen()

screen.onkey(fun=paddle_left.move_up, key="e")
screen.onkey(fun=paddle_left.move_down, key="d")
screen.onkey(fun=paddle_right.move_up, key="o")
screen.onkey(fun=paddle_right.move_down, key="l")

game_is_on = True
while game_is_on:
    ball.move()
    screen.update()
    time.sleep(ball.move_speed)

    if ball.ycor() < -285 or ball.ycor() > 285:
        ball.bounce() 
    
    if (ball.distance(paddle_left) < 35 and ball.xcor() < -325) or (ball.distance(paddle_right) < 35 and ball.xcor() > 325):
        ball.bounce_on_paddle()
    
    if ball.xcor() > 380:
        left_scoreboard.score += 1
        left_scoreboard.sc_refresh()
        ball.recenter()
    if ball.xcor() < -380:
        right_scoreboard.score += 1
        right_scoreboard.sc_refresh()
        ball.recenter()
    
    
    
# moving ball
## same moving as platform, but also on x axis
# detect collision
## ball/platform
## ball/exitscreen left and right
## score



screen.mainloop()