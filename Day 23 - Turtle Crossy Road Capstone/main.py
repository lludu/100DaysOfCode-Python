import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from color import *

screen = Screen()
screen.setup(width=600, height=600)
screen.colormode(255)
screen.bgcolor(COLOR_REPLIT)
screen.title("Turtle Crossy-road")
screen.tracer(0)

car_manager = CarManager()
scoreboard = Scoreboard()
player = Player()
screen.listen()
screen.onkeypress(player.go_up, "Up")
screen.onkeypress(player.go_up, "w")



game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    # <-------- Create the cars ---------> #
    car_manager.create_car()
    car_manager.drive()

    # <---------Detect car crash --------> #
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False


    # <--------Detect player cross / new level -------> #
    if player.crossed_road():
        player.next_level()
        car_manager.next_level()
        scoreboard.next_level()















screen.exitonclick()