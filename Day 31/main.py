from tkinter import Tk, Canvas, PhotoImage, Button
from random import choice
import pandas


BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")
current_card = {}
to_learn = {}


try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")



def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    canvas.itemconfig(image_id, image=IMG_CARD_FRONT)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")
    canvas.itemconfig(image_id, image=IMG_CARD_BACK)

def is_known():
    to_learn.remove(current_card)  # removes the card from the current list of cards to learn when the user clicks the check mark

    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    



    next_card()


window = Tk()
window.title("Flashy Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)


IMG_CARD_FRONT = PhotoImage(file="images/card_front.png")
IMG_CARD_BACK = PhotoImage(file="images/card_back.png")
IMG_RIGHT = PhotoImage(file="images/right.png")
IMG_WRONG = PhotoImage(file="images/wrong.png")


canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
image_id = canvas.create_image(400, 263, image=IMG_CARD_FRONT)
canvas.grid(row=0, column=0, columnspan=2)


# ------ LABELS ------ #
title = canvas.create_text(400, 150, text="Title", font=TITLE_FONT)
word = canvas.create_text(400, 263, text="Word", font=WORD_FONT)


# ----- BUTTONS ------ #
unknown = Button(image=IMG_WRONG, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
unknown.grid(row=1, column=0)

known = Button(image=IMG_RIGHT, highlightthickness=0, bg=BACKGROUND_COLOR, command=is_known)
known.grid(row=1, column=1)









next_card()
window.mainloop()
