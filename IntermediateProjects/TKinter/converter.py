from tkinter import *

window = Tk()
window.title("Converter")
window.minsize(height=200, width=300)
window.config(padx=50, pady=50)

def button_clicked():
    output = round(float(input_number.get())*1.609344, ndigits=3)
    output_label.config(text=output, font=("Georgia", 11, "bold"))

input_number = Entry(width=10)
input_number.grid(row=1, column=2)

label_miles = Label(text="Miles", font=("Georgia", 11))
label_miles.grid(row=1, column=3)

label_isequalto = Label(text="is equal to", font=("Georgia", 11))
label_isequalto.grid(row=2, column=1)

label_km = Label(text="Km", font=("Georgia", 11))
label_km.grid(row=2, column=3)

output_label = Label()
output_label.grid(row=2, column=2)

button = Button(text="Calculate", command=button_clicked)
button.grid(row=3, column=2)


window.mainloop()