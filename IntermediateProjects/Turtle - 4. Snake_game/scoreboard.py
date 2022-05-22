from tkinter import scrolledtext
from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Georgia", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 270)
        self.hideturtle()
        self.color("white")
        self.sc_refresh()
    
    def sc_refresh(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)
    
    def game_over(self):
        self.clear()
        self.write(arg=f"GAME OVER. Your final score is: {self.score}.", align=ALIGNMENT, font=FONT)
    



