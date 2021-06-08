from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


#Add all the questions from data into the question bank using the Question Object
question_bank =[]
for question in question_data:
    # qb_text = question["text"]
    # qb_answer = question["answer"]
    # question = Question(qb_text, qb_answer)
    new_question = Question(question["question"], question["correct_answer"])
    question_bank.append(new_question)
print(question_bank)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score is {quiz.score}/{quiz.question_number}")