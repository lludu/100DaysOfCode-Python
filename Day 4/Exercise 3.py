#This is day 4, randomization and python lists

#Exercise 3 - Crown marks the spot (Working in Maps with Nested Arrays):

# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure?\nEnter a two digit number, 1st digit is column, 2nd is row: ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# emoji for treasure 👑
x = int(position[0]) -1
y = int(position[1]) -1
print(f'Putting Treasure at column {x+1}, row {y+1}')


map[y][x] = '👑'




#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")




#Link to Exercise
# https://replit.com/@Lludu/day-4-3-exercise#main.py
