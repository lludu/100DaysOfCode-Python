# # Snake Game # #

from turtle import Screen, Turtle
# Turtle Doc: https://docs.python.org/3/library/turtle.html
from snake import Snake
import time

# Screen Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.colormode(255)  # To Use RGB Background Colors
# screen.bgcolor(13,16,30)  # Replit Blue
screen.bgcolor(34, 34, 34)  # 222 Grey
screen.title("Py Snake Game")
screen.tracer(0)  # Stop displacing animations until you need, no jittering

# TODO 1. Create the snake Body - Completed in snake.py
# turtles are 20x20 pixels
# poisition at 0x0, 0x20, 0x40
snake = Snake()

# TODO 2. Move the snake - Completed in snake.py
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()  # Updates the screen
    time.sleep(0.1)  # adds one second delay after movement

    snake.move()

# TODO 3. Create snake food
# TODO 4. Detect collision with food
# TODO 5. Create a scoreboard
# TODO 6. Detect collision with wall
# TODO 7. Detect collision with tail


screen.exitonclick()
