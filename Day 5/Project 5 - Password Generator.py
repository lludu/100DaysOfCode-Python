#This is day 5 project: Password Generator



#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

selected= ''
#Pick a random letter from the list for the amount given and store in a variable
for count in range(0, nr_letters):
  selected += random.choice(letters)

#Pick a random symbol from the list for the amount given and store in a variable
for count in range(0, nr_symbols):
  selected += random.choice(symbols)

#Pick a random number from the list for the amount given and store in a variable
for count in range(0, nr_numbers):
  selected += random.choice(numbers)



#Print the string (Easy Mode)
print('\n-----Eazy Mode - Order not randomised-----')
print(f'This is the randomly chosen password (easy-mode):\n\n{selected}\n')


#Print the shuffled string (Hard Mode)
#Shuffle the STRING by using SAMPLE method by the length of the selected string and joining
shuffle_selected = ''.join(random.sample(selected, len(selected)))
print('\n-----Hard Mode - Order of characters randomised-----')
print(f'This is the random password shuffled using string samples (hard-mode):\n\n{shuffle_selected}')




#---You can also shuffle the string by converting to a list and using SHUFFLE random method
print('\n\n\n\n-----The method below uses shuffle of list instead of using string samples-----')

#convert the string into a list
selected_password = list(selected)
print(f'\n1. These are the selected characters in a list:\n{selected_password}')

#shuffle the list
random.shuffle(selected_password)
print(f'\n2.Now shuffle the list:\n{selected_password}')

#convert the list back into a string
password = ''.join(selected_password)
print(f'\n3.Here is the shuffled list converted back to a string:\n{password}')



#Link to Day 5 project
#https://replit.com/@Lludu/password-generator#main.py
#https://replit.com/@Lludu/password-generator?v=1 spotlight
