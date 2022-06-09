from tkinter import ttk
from tkinter import *
EMAILS = ["olivierhinh@gmail.com", "olivier.hinh@azurreo.com", "olivier.hinh@edhec.com", "guest.pseudo@gmail.com"]
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data():
    website = entry_website.get()
    email = cbb_email_username.get()
    password = entry_password.get()
    with open("data.csv", "a") as data:
        data.writelines([website, " | ", email, " | ", password, "\n"])
    entry_website.delete(0, END)
    cbb_email_username.delete(0, END)
    entry_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=40, pady=40)
window.title("Password Manager")
window.geometry("+420+140")

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

text_website = Label(text="Website:")
text_website.grid(row=1, column=0)
text_email_username = Label(text="Email/Username:")
text_email_username.grid(row=2, column=0)
text_password = Label(text="Password:")
text_password.grid(row=3, column=0)


entry_website = Entry()
entry_website.grid(row=1, column=1, columnspan=2, sticky="EW")
entry_website.focus()
cbb_email_username = ttk.Combobox(window, values=EMAILS)
cbb_email_username.grid(row=2, column=1, columnspan=2, sticky="EW")
entry_password = Entry()
entry_password.grid(row=3, column=1, sticky="EW")


button_generate_password = Button(text="Generate Password")
button_generate_password.grid(row=3, column=2, sticky="EW")
button_add = Button(text="Add", command=add_data)
button_add.grid(row=4, column=1, columnspan=2, sticky="EW")



window.mainloop()