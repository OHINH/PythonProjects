from tkinter import *

window = Tk()
window.title("Tkinter Screen")
window.minsize(height=700, width=700)

def button_clicked():
    print("clicked")
    new_text = my_input.get()
    my_label.config(text=new_text)


my_label = Label(text="I am a label.", font=("Georgia", 24, "bold"))
my_label.grid(row=1, column=1)


my_button = Button(text="Click me!", command=button_clicked)
my_button.grid(row=2, column=2)


my_input = Entry()
my_input.grid(row=3, column=2)


window.mainloop()