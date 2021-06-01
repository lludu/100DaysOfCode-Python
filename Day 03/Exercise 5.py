#This is day 3, Control Flow & Logical operators

#Exercise 5 - Love Calculator:

combined_names = name1 + name2
lower_names = combined_names.lower()

t = lower_names.count('t')
r = lower_names.count('r')
u = lower_names.count('u')
e = lower_names.count('e')
l = lower_names.count('l')
o = lower_names.count('o')
v = lower_names.count('v')

true = t + r + u + e
love = l + o + v + e
occurs = int(str(true)+str(love))


if (occurs < 10 or occurs > 90):
  print(f'Your score is {occurs}, you go together like coke and mentos.')
elif (occurs>=40 and occurs<=50):
  print(f'Your score is {occurs}, you are alright together.')
else:
  print(f'Your score is {occurs}.')





#link to exercise
# https://replit.com/@Lludu/day-3-5-exercise#main.py

#link to exercise checker
# https://replit.com/@Lludu/day-3-5-test-your-code#main.py
