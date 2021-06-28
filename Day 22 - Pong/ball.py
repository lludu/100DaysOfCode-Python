from turtle import Turtle
from color import *

class Ball(Turtle):
    def __init__(self): # Initialize
        super().__init__() # get inheritance from Turtle
        self.penup()
        self.color(COLOR_THEME)
        self.goto(x=0, y=0)
        self.shape("circle")
        self.x_move = 5
        self.y_move = 5
        self.move_speed = 0.05

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def y_bounce(self):
        self.y_move *= -1

    def x_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.6

    def reset_ball(self):
        self.move_speed = 0.04
        self.goto(0,0)
        self.x_bounce()
