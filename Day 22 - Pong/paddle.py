from turtle import Turtle
from color import *

class Paddle(Turtle):
    def __init__(self, position): # Initialize
        super().__init__() # get inheritance from Turtle
        self.penup()
        self.color(COLOR_THEME)
        self.goto(position)
        self.shape("square")
        self.turtlesize(stretch_wid=5, stretch_len=1)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)