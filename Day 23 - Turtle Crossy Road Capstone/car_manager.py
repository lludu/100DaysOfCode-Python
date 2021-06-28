from turtle import Turtle
from random import randint, choice


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2

# CLASS THAT DEALS WITH ALL THE CARS / LOGS THAT CAN HIT PLAYER
class CarManager:
    def __init__(self):  # Initialize
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.setheading(180)
            new_car.color(choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            random_y = randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def drive(self):
        for car in self.all_cars:
            car.forward(self.car_speed)


    def next_level(self):
        self.car_speed += MOVE_INCREMENT

