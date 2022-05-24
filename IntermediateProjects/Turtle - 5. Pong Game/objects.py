from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.goto(position)
        self.color("white")
        self.shapesize(4, 1)
    
    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

class Ball(Turtle):
    def __init__(self) -> None:
        super().

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
    


