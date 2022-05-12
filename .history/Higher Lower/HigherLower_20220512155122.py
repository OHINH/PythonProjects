# import all modules
from random import randint
from random import choice
from turtle import clear
from artee import logo
from artee import vs
from HL_data import data

# variables to be initialized:
element1 = ""  # the first randomly chosen element
element2 = ""  # the second randomly chosen element
trelement = ""  # transitory element
score = 0  # initial score
truerep = True  # pour la boucle

# better notations
def format_data(element):
    name = element['name']
    desc = element['description']
    country = element['country']
    return f"{name}, a {desc}, from {country}."


# display initial game state: logo + welcome msg
print(logo + "\nWelcome to the Higher Lower game!\n")


# randomly choose two element in HL_data and make sure those choices are distinct
element1 = choice(data)
element2 = choice(data)


def generate_element2_element_distinct():
    if element1 == element2 or element1 == trelement:
        return choice(data)
    else:
        return element2


element2 = generate_element2_element_distinct()


# display choice1 + VS + choice2
print(f"Compare A: {format_data(element1)}.\n" + vs)
print(f"\nAgainst B:{format_data(element2)}.")


# ask for an input A/B, A for choice1 and B for choice2
p_choice = input(
    f"\nWho has the higher number of follower? A for {element1['name']}, B for {element2['name']}\n--> ").upper()



# define the highest number of followers between the two element


def whichismax(element1, element2):
    if element1['follower_count'] > element2['follower_count']:
        return 'A'
    elif element1['follower_count'] < element2['follower_count']:
        return 'B'


clear()
print(logo)
# if right (chose A and nbfollowers A > nbfollowers B) then
while truerep:
    if p_choice == whichismax(element1, element2):
        ## score += 1
        score += 1
        print(f"Right! your current score is {score}.\n")
# choice1 = choice2 and randomly generate choice2 (distinct from choice1)
        trelement = element1
        element1 = element2
        element2 = choice(data)
        element2 = (generate_element2_element_distinct())
# display choice1 + VS + choice2
        print(f"Compare A: {format_data(element1)}.\n" + vs)
        print(f"\nAgainst B: {format_data(element2)}.")
# ask for input A/B
        p_choice = input(
            f"\nWho has the higher number of follower? A for {element1['name']}, B for {element2['name']}\n--> ").upper()
# if wrong then
# display GAME OVER
# display the final score
# end the game
    else:
        truerep = False
        print(f"Game Over, your final score is {score}")
