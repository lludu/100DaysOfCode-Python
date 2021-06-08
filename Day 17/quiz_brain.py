
#Create a quiz brain class
class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0



    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        #ask the user the question
        user_answer = input(f'Q.{self.question_number}: {current_question.text} (True or False?): ')
        self.check_answer(user_answer, current_question.answer, self.question_number)


    def still_has_questions(self):
        # if self.question_number < len(self.question_list):
        #     return True
        # else:
        #     return False

        #You can also run the if statement like this to make it shorter, but not as clear
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer, question_number):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f"That's Correct!")
            print(f"The correct answer was: {correct_answer}")
            print(f"Your current score is: {self.score}/{question_number}\n")
        else:
            print(f"That's Wrong!")
            print(f"The correct answer was: {correct_answer}")
            print(f"Your current score is: {self.score}/{question_number}\n")