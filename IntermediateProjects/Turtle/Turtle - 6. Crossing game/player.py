from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.setposition(STARTING_POSITION)
        self.shape("turtle")
        self.setheading(90)
    
    def advance(self):
        self.forward(MOVE_DISTANCE)
    
    def goto_ini(self):
        self.goto(STARTING_POSITION)