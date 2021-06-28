from turtle import Turtle
from color import *

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

# CLASS FOR THE PLAYER - TURTLE THAT CROSSES ROAD
class Player(Turtle):
    def __init__(self):  # Initialize
        super().__init__()  # get inheritance from Turtle
        self.penup()
        self.setheading(90)
        self.shape("turtle")
        self.next_level()
        self.color(COLOR_THEME)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def next_level(self):
        self.goto(STARTING_POSITION)

    def crossed_road(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

        