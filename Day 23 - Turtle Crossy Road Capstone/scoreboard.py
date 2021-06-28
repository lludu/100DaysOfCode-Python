from turtle import Turtle
from color import *

FONT = ("Courier", 24, "bold")

# WRITES THE SCOREBOARD ON THE LEFT AND THE GAME OVER SEQUENCE
class Scoreboard(Turtle):
    def __init__(self):  # Initialize
        super().__init__()  # get inheritance from Turtle
        self.level = 0
        self.penup()
        self.hideturtle()
        self.goto(-280, 260)
        self.next_level()


    def next_level(self):
        self.clear()
        self.level += 1
        self.color(COLOR_THEME)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Final Level: {self.level}", align="center", font=FONT)
        self.goto(0,-40)
        self.write("Game Over", align="center", font=FONT)