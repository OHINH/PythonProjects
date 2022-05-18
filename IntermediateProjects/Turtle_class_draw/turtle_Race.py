import random
from turtle import Turtle, Screen
import turtle

screen = Screen()
screen.setup(width=500, height=400)
colors = ["blue", "orange", "purple", "red", "brown", "grey"]

running_turtles = []
for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=150-50*i)
    running_turtles.append(new_turtle)

Referee = Turtle()
Referee.penup()
Referee.goto(x=230,y=180)
Referee.pendown()
Referee.right(90)
Referee.forward(320)
Referee.penup()
Referee.goto(0,-180)
Referee.left(180)

bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Input a color:")
is_race_on = True
while is_race_on:
    for turtle in running_turtles:
        turtle.speed(0)
        if turtle.xcor() > 200:
            winner_color = turtle.pencolor()
            is_race_on = False
        dist = 3*random.randint(0,1)
        turtle.forward(dist)

if bet == winner_color:
    print(f"The {winner_color} turtle won. You win the bet!")
else:
    print(f"The {winner_color} turtle won. You lose...")

screen.exitonclick()