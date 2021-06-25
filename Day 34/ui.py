from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="Whitesmoke")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas()
        self.canvas.config(width=300, height=250, bg="whitesmoke")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Word",
            font=("Arial", 18, "italic"),
            fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        false_image = PhotoImage(file="images/false.png")
        self.false_btn = Button(width=100, height=97, image=false_image,
                                highlightthickness=0, bg=THEME_COLOR, command=self.false_pressed)
        self.false_btn.grid(row=2, column=0)

        true_image = PhotoImage(file="images/true.png")
        self.true_btn = Button(width=100, height=97, image=true_image,
                                  highlightthickness=0, bg=THEME_COLOR, command=self.true_pressed)
        self.true_btn.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="whitesmoke")
        self.canvas.itemconfig(self.question_text, fill=THEME_COLOR)
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text, fill=THEME_COLOR)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.true_btn.config(state=DISABLED)
            self.false_btn.config(state=DISABLED)


    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)


    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="#23AC6C")
            self.canvas.itemconfig(self.question_text, fill="whitesmoke")
        else:
            self.canvas.config(bg="#DB625D")
            self.canvas.itemconfig(self.question_text, fill="whitesmoke")

        self.window.after(1000, self.get_next_question)

