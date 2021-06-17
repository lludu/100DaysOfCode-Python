from turtle import Turtle
from random import randint


GOLD_APPLE = 240, 230, 155
FOOD_COLOR = GOLD_APPLE


class Food(Turtle):

    def __init__(self): # Initialize
        super().__init__() # get inheritance from Turtle
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # half the size of the circle
        self.speed(10)
        self.color(FOOD_COLOR)

        # Place the food
        self.refresh()

    def refresh(self):
        # Place the food
        random_x = randint(-260 ,260)
        random_y = randint(-260 ,260)
        self.goto(random_x, random_y)
