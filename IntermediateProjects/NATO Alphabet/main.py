import pandas


df = pandas.read_csv("nato_phonetic_alphabet.csv")
NATO_dict = {letter_row.letter:letter_row.code for (index, letter_row) in df.iterrows()}


def generate_phonetic():
    input_word = input("What is the word you would like to convert into NATO phonetic alphabet?\n--> ").upper()
    try:
        input_word_letters = [letter for letter in input_word]
        output = [NATO_dict[letter] for letter in input_word_letters]
    except KeyError:
        print("Only letters please.")
        generate_phonetic()
    else:
        print(output)

generate_phonetic()