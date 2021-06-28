#This is day 3, Control Flow & Logical operators

#Exercise 3 - Is the given year a leap year:



if (year % 4 == 0):
    if(year % 100 == 0):
        if(year % 400 == 0):
            print('Leap year.')
        else:
            print('Not leap year.')
    else:
        print('Leap year.')
else:
    print('Not leap year.')




#link to exercise
# https://replit.com/@Lludu/day-3-3-exercise#main.py

#link to exercise checker
# https://replit.com/@Lludu/day-3-3-test-your-code#main.py
