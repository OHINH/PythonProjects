import pandas
import turtle as tl


screen = tl.Screen()
screen.title("US state guessing game!")
image = "blank_states_img.gif"
screen.addshape(image)
tl.shape(image)

writer = tl.Turtle()
writer.penup()
writer.hideturtle()

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()

score = 0
game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f"Guess the State - {score}/50", prompt="Type in a State name.")
    if answer_state.title() in states:
        writer.goto(int(data[answer_state.title() == data.state].x), int(data[answer_state.title() == data.state].y))
        writer.write(f"{answer_state.title()}")
        score += 1
    
    if score == 50:
        screen.textinput("You Won! Any words to say?")
        game_is_on = False
        


screen.exitonclick()