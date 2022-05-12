import random

word_list = ("Hello", "World", "Hi", "Jack",)
print("Welcome to the hangman game!")

blank = []
word = (random.choice(word_list)).lower()
lives = 6

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

for i in range(len(word)):
    blank += "_"

print(blank)
print(stages[lives])

while "_" in blank and lives != 0:
    guess = input("Take a guess \n-->").lower()
    if guess in blank:
        print("letter already in the word, try again.")
    for position in range(len(word)):
        letter = word[position]
        if letter == guess:
            blank[position] = guess

    if guess not in word:
        lives -= 1
        if lives == 0:
            print("You lose")
        print(stages[lives])
        print("Aww, letter not in word!")
    print(blank)

if "_" not in blank:
    print("You Won!")
else:
    print("You Lose!")
