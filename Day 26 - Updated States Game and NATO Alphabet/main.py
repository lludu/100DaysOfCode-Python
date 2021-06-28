# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in dataframe.iterrows()}

import pandas as pd
data = pd.read_csv("nato_phonetic_alphabet.csv")

# print(data) # Currently is a dataframe
# new_dictionary = {letter:code for (letter, code) in data.iterrows()}
# print(new_dictionary)


#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_dict = {row.letter:row.code for (index, row) in data.iterrows()}
print(nato_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input("Enter a word: ").upper() # change to upper because dictionary keys are upper

# new_item for item in list
output_list = [nato_dict[letter] for letter in user_word]
print(output_list)

