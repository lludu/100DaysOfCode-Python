#This is day 10, Functions with outputs/returns

#Exercise 1 - Days in Month

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
  if month > 12 or month < 1:
    return "invalid month"

  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if is_leap(year) and month == 2:
    return 29
  return month_days[month-1]



#🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)





#Link to Exercise
# https://replit.com/@Lludu/day-10-1-exercise#main.py

#link to Exercise Checker
# https://replit.com/@Lludu/day-10-1-test-your-code#main.py
