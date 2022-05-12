import random

def choose_diff():
    eh = input("Choose a difficulty. Type 'easy' or 'hard'.\n--> ")
    if eh == "easy":
        nb_attempt_left = 10
    else:
        nb_attempt_left = 5

print("Welcome to the number guessing game! \nIm thinking about a number between 1 and 100.")
NUMBER = random.randint(1,100)
guessed_number = 0
choose_diff()

MATCH = True
while MATCH is True:
    if int(guessed_number) != int(NUMBER):
        guessed_number = int(input("\nMake a guess.\n--> "))
        nb_attempt_left -= 1
        if nb_attempt_left == 0:
            print("GAME OVER.")
            break
        if guessed_number < NUMBER:
            print("Too Low.")
            print(f"Guess Again.\nYou have {nb_attempt_left} attempt(s) left.")
        elif guessed_number > NUMBER:
            print("Too high.")
            print(f"Guess Again.\nYou have {nb_attempt_left} attempt(s) left.")
    else:
        MATCH = False
        print("That's it!")