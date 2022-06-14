BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import random
import pandas
LEARNING_LANGUAGE = "French"
SPEAKING_LANGUAGE = "English"
current_card = {}
to_learn = {}

try:
    df = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = df.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_image, image=card_front)
    canvas.itemconfig(title_text, text=LEARNING_LANGUAGE, fill="black")
    canvas.itemconfig(word_text, text=current_card[LEARNING_LANGUAGE], fill="black")
    flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfig(title_text, text=SPEAKING_LANGUAGE, fill="white")
    canvas.itemconfig(word_text, text=current_card[SPEAKING_LANGUAGE], fill="white")

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()


# config the window
window = Tk()
window.title("Flashy")
window.config(background=BACKGROUND_COLOR, padx=20, pady=20)
window.geometry("+200+10")

# config the canvas
canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# config the front of a card
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front)

# config the right and wrong buttons
right = PhotoImage(file="./images/right.png")
right_button = Button(image=right, highlightthickness=0, borderwidth=0, command=is_known)
right_button.grid(row=1, column=0)
wrong = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong, highlightthickness=0, borderwidth=0, command=next_card)
wrong_button.grid(row=1, column=1)

# config the words
title_text = canvas.create_text(400, 130, text=LEARNING_LANGUAGE, font=("Georgia", 40, "italic"))
word_text = canvas.create_text(400, 270, text="Word", font=("Georgia", 60, "bold"))



# changing cards
flip_timer = window.after(ms=3000,func=flip_card) 
next_card()

window.mainloop()
