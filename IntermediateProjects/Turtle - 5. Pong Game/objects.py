from turtle import Turtle
Init_positions_left = (-350, 0)
Init_positions_right = (350, 0)
MOVING_SPEED = 20

class Paddle(Turtle):
    
    def __init__(self, position) -> None:
        self = Turtle("square")
        self.color("white")
        self.shapesize(4, 1)
        self.penup()
        if position == "left":
            self.goto(Init_positions_left)
        elif position == "right":
            self.goto(Init_positions_right)


class Ball(Paddle):
    pass

class Scoreboard():
    pass

class Ref():
    def __init__(self) -> None:
        self = Turtle()
        self.hideturtle()
        self.pencolor("white")
        self.pensize(5)
        self.penup()
        self.goto(0, 230)
        self.setheading(270)
        for _ in range(17):
            self.forward(15)
            self.penup()
            self.forward(15)
            self.pendown()   
    


