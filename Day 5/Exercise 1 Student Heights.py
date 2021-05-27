#This is day 5, python loops

#Exercise 1 - Calculate Student Heights:

# 🚨 Don't change the code below 👇3
student_heights = input("Input a list of student heights: ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
total = 0
count = 0
for height in student_heights:
  total += height
  count += 1
print(f'The average height for the students listed is: {round(total/count)}')



#Link to Exercise
# https://replit.com/@Lludu/day-5-1-exercise#main.py

#Link to Test
# https://replit.com/@Lludu/day-5-1-test-your-code#main.py
