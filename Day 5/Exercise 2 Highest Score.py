#This is day 5, python loops

#Exercise 2 - Determine the highest score in a list:

# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores: ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
big_score = 0
for scores in student_scores:
  if (big_score < scores):
    big_score = scores

print(f'The highest score in the class is: {big_score}')



#Link to Exercise
# https://replit.com/@Lludu/day-5-2-exercise#main.py

#Link to Test
# https://replit.com/@Lludu/day-5-2-test-your-code#main.py
