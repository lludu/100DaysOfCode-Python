#This is day 9, Dictionaries dand Nesting Dictionaries

#Exercise 1 - Grading Program

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.


#TODO-2: Write your code below to add the grades to student_grades.👇
student_grades=student_scores

for grade in student_grades:
  if student_grades[grade] > 90:
    student_grades[grade] = "Outstanding"
  elif student_grades[grade] > 80 and student_grades[grade] <= 90:
    student_grades[grade] = "Exceeds Expectations"
  elif student_grades[grade] > 70 and student_grades[grade] <= 80:
    student_grades[grade] = "Acceptable"
  else:
    student_grades[grade] = "Fail"


# 🚨 Don't change the code below 👇
print(student_grades)

#Link to Exercise
# https://replit.com/@Lludu/day-9-1-exercise#main.py

#link to Exercise Checker
# https://replit.com/@Lludu/day-9-1-test-your-code#main.py
