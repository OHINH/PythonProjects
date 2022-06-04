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
guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"Guess the State - {len(guessed_states)}/50", prompt="Type in a State name.").title()
    if answer_state in states:
        writer.goto(int(data[answer_state == data.state].x), int(data[answer_state == data.state].y))
        writer.write(f"{answer_state}")
        guessed_states.append(answer_state)
    
    if answer_state == "Exit":
        missing_states = [state for state in states if state not in guessed_states]
        print(f"The States you haven't guessed are: {missing_states}")
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missing_states.csv")
        break
        