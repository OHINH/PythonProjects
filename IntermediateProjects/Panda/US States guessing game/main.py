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
not_guessed_states = states


while len(not_guessed_states) > 0:
    answer_state = screen.textinput(title=f"Guess the State - {len(not_guessed_states)}/50", prompt="Type in a State name.").title()
    if answer_state in states:
        writer.goto(int(data[answer_state == data.state].x), int(data[answer_state == data.state].y))
        writer.write(f"{answer_state}")
        not_guessed_states.remove(answer_state)
    
    if answer_state == "Exit":
        print(f"The States you haven't guessed are: {not_guessed_states}")
        new_data = pandas.DataFrame(not_guessed_states)
        new_data.to_csv("missing_states.csv")
        break
        