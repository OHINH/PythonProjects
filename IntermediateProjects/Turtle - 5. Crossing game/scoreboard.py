from turtle import Turtle
FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(-280,270)
        self.write(f"Level: {self.score}", align="left", font=FONT)
    
    def score_update(self):
        self.score += 1
        self.clear()
        self.write(f"Level: {self.score}", align="left", font=FONT)
    
    def game_over(self):
        self.goto(-20,0)
        self.write("GAME OVER.", font=FONT)

