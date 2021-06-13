from turtle import Turtle
from color import *

SCORE_FONT = ("Courier", 60, "bold")
TITLE_FONT = ("Courier", 20, "bold")

class Scoreboard(Turtle):
    def __init__(self): # Initialize
        super().__init__() # get inheritance from Turtle
        self.penup()
        self.color(COLOR_THEME)
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(x=0, y=240)
        self.write("PONG", align="center", font=TITLE_FONT)
        self.goto(x=-100, y=200)
        self.write(self.l_score, align="center", font=SCORE_FONT)
        self.goto(x=100, y=200)
        self.write(self.r_score, align="center", font=SCORE_FONT)


    def l_point(self):
        self.l_score += 1

    def r_point(self):
        self.r_score += 1