#This is day 3, Control Flow & Logical operators

#Exercise 2 - BMI Calculator 2.0 - Adding Underweight, Normal, Overweight Statements:
bmi = (round(float(weight)/(float(height)**2)))

if (bmi <= 18.5):
    print(f'Your BMI is {bmi}, you are underweight.')
elif (bmi > 18.5 and bmi <= 25):
    print(f'Your BMI is {bmi}, you have a normal weight.')
elif (bmi >= 25 and bmi <= 30):
    print(f'Your BMI is {bmi}, you are slightly overweight.')
elif (bmi >= 30 and bmi < 35):
    print(f'Your BMI is {bmi}, you are obese.')
else:
    print(f'Your BMI is {bmi}, you are clinically obese.')



#link to exercise
# https://replit.com/@Lludu/day-3-2-exercise#main.py

#link to exercise checker
# https://replit.com/@Lludu/day-3-2-test-your-code#main.py
