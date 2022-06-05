import pandas

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

df = pandas.read_csv("nato_phonetic_alphabet.csv")
NATO_dict = {letter_row.letter:letter_row.code for (index, letter_row) in df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

input_word = input("What is the word you would like to convert into NATO phonetic alphabet?\n--> ").upper()
input_word_letters = [letter for letter in input_word]

output = [NATO_dict[letter] for letter in input_word_letters]
print(output)