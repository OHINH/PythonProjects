import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00.00")
    title_label.config(text="TIMER", fg=GREEN)
    check.config(text="")
    global rep
    rep = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    window.attributes('-topmost', True)
    window.attributes('-topmost', False)
    global rep
    rep += 1
    if rep % 8 == 0:
        countdown(LONG_BREAK_MIN*60)
        title_label.config(text="BREAK", fg=RED)
    elif rep % 2 == 0:
        countdown(SHORT_BREAK_MIN*60)
        title_label.config(text="BREAK", fg=PINK)
    else:
        countdown(WORK_MIN*60)
        title_label.config(text="WORK", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)  
    else:
        global check_number
        start_timer()
        check_number = ""
        for _ in range(math.floor(rep/2)):
            check_number += "🗹"
        check.config(text=check_number)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pompodoro")
window.config(padx=40, pady=30, bg=YELLOW)
window.geometry("+460+140")

canvas = Canvas(width=200, height=260, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 130, image=image)
timer_text = canvas.create_text(100, 160, text="00.00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)


title_label = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
title_label.grid(row=0, column=1)

check = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 14, "bold"))
check.grid(row=3, column=1)

start_button = Button(text="START", command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="RESET", command=reset_timer)
reset_button.grid(row=2, column=2)



window.mainloop()