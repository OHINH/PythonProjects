print("Welcome to the password generator!")

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

num_letters = int(input("What is the desired number of letters?"))
num_num = int(input("What is the desired number of numbers?"))
num_sp = int(input("What is the desired number of special characters?"))

password = ""

while num_letters+num_num+num_sp !=0:
    which = random.randint(0,2)
    if which == 0 and num_letters != 0:
        password += random.choice(letters)
        num_letters -= 1

    elif which == 1 and num_num != 0:
        password += random.choice(numbers)
        num_num -= 1

    elif which == 2 and num_sp != 0:
        password += random.choice(symbols)
        num_sp -= 1

print(password)
