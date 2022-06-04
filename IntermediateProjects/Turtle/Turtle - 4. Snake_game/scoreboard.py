from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Georgia", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("G:\Mon Drive\CODING\Python\PythonProjects\IntermediateProjects\Turtle\Turtle - 4. Snake_game\data.txt") as file:
            self.high_score = int(file.read())
        self.goto(0, 270) 
        self.hideturtle()
        self.color("white")
        self.sc_refresh()
    
    def sc_refresh(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("G:\Mon Drive\CODING\Python\PythonProjects\IntermediateProjects\Turtle\Turtle - 4. Snake_game\data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.sc_refresh()

