from turtle import Turtle
import random
GAME_COLOR = "green"

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.goto(position)
        self.color(GAME_COLOR)
        self.shapesize(4, 1)
    
    def move_up(self):
        if self.ycor() < 230:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def move_down(self):
        if self.ycor() > -230:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)

class Ref():
    def __init__(self) -> None:
        self = Turtle()
        self.hideturtle()
        self.pencolor(GAME_COLOR)
        self.pensize(5)
        self.penup()
        self.goto(0, 300)
        self.setheading(270)
        for _ in range(19):
            self.forward(15)
            self.penup()
            self.forward(15)
            self.pendown()   




class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.shapesize(0.8, 0.8)
        self.color(GAME_COLOR)
        self.penup()
        self.move_speed = 0.1
        self.x_pas = 10
        self.y_pas = 10
    
    def move(self):
        new_x = self.xcor() + self.x_pas
        new_y = self.ycor() + self.y_pas
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_pas *= -1
        self.move_speed *= 0.9
    
    def bounce_on_paddle(self):
        self.x_pas *= -1
        self.move_speed *= 0.9
    
    def recenter(self):
        self.goto(0,0)
        self.move_speed = 0.1


class Scoreboard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.goto(position, 210)
        self.hideturtle()
        self.color(GAME_COLOR)
        self.sc_refresh()
    
    def sc_refresh(self):
        self.clear()
        self.write(arg=f"{self.score}", move=False, align="center", font=("Georgia", 60, "bold"))




