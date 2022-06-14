from tkinter import messagebox, ttk
from tkinter import *
from nltk.corpus import words
import random
import pyperclip
import json

EMAILS = ["olivierhinh@gmail.com", "olivier.hinh@azurreo.com", "olivier.hinh@edhec.com", "guest.pseudo@gmail.com"]
WORDS_LIST = words.words()

# ---------------------------- SEARCH LOGIN BUTTON ------------------------------- #
def search_login():
    website = entry_website.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(fp=data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email} \npassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No website logins found for {website}")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    entry_password.delete(0, END)
    word1 = random.choice(WORDS_LIST)
    if len(word1) > 7:
        word1 = word1[0:6]
    word2 = random.choice(WORDS_LIST)
    if len(word2) > 7:
        word2 = word2[0:6]
    random_num = random.randint(11, 99)
    password = word1 + word2 + str(random_num)
    entry_password.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data():
    website = entry_website.get()
    email = cbb_email_username.get()
    password = entry_password.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0:
        messagebox.showerror(title="Website Entry error", message="You forgot to type in a website, try again.")
    elif len(email) == 0:
        messagebox.showerror(title="Email Entry error", message="You forgot to select an email, try again.")
    elif len(password) < 8:
        messagebox.showerror(title="Password Entry error", message="Your password is too short, try again.")
    
    else:

        try:    
            with open("data.json", "r") as data_file:
                # reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # update old data with new data
            data.update(new_data)
    
            with open("data.json", "w") as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)
        finally:
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
entry_website.grid(row=1, column=1, sticky="EW")
entry_website.focus()
cbb_email_username = ttk.Combobox(window, values=EMAILS)
cbb_email_username.grid(row=2, column=1, columnspan=2, sticky="EW")
entry_password = Entry()
entry_password.grid(row=3, column=1, sticky="EW")


button_generate_password = Button(text="Generate Password", command=generate_password)
button_generate_password.grid(row=3, column=2, sticky="EW")
button_add = Button(text="Add", command=add_data)
button_add.grid(row=4, column=1, columnspan=2, sticky="EW")
button_search = Button(text="Search", command=search_login)
button_search.grid(row=1, column=2, sticky=EW)



window.mainloop()