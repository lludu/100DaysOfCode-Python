#This is day 2 project: Tip Calculator

#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

print('Welcome to the tip calculator')
total = float(input('What was the total bill? $'))
crowd = int(input('How many people to split the bill? '))
tip = int(input('What percentage tip would you like to give? 10, 12, 15, 20? '))

split_total = total / crowd
bill = round(split_total + (split_total*(tip/100)),2)

#this line floats a zero if needed at the end to keep currency format
bill = '{:.2f}'.format(bill)


print(f'Each person should pay: ${bill}')


#Link to Day 2 project
#https://replit.com/@Lludu/tip-calculator-start#main.py
