#This is day 3, Control Flow & Logical operators

#Exercise 4 - Pizza Order:


bill = 0

if (size == 'S'):
  bill = 15
elif (size == 'M'):
  bill = 20
else:
  bill = 25

if (add_pepperoni == 'Y'):
  if(size == 'S'):
    bill += 2
  else:
    bill += 3

if (extra_cheese == 'Y'):
  bill += 1

print(f'Your final bill is: ${bill}.')




#link to exercise
# https://replit.com/@Lludu/day-3-4-exercise#main.py

#link to exercise checker
# https://replit.com/@Lludu/day-3-4-test-your-code#main.py
