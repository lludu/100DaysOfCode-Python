#This is day 4, randomization and python lists

#Exercise 2 - Who is paying for lunch:

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

names = [name.title() for name in names]

import random


random_pick = random.randint(0,(len(names)-1))
print('\nThis random pick is using random integer generated names:')
print(f'{names[random_pick]} is going to buy the meal today!\n')


# if using choice() instead of random int
random_choice = random.choice(names)
print('This random pick is using random choice generated names:')
print(f'{random_choice} is going to buy the meal today!')



#Link to Exercise
# https://replit.com/@Lludu/day-4-2-exercise#main.py
