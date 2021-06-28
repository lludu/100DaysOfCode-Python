# # Snake Game # #
from turtle import Screen
# Turtle Doc: https://docs.python.org/3/library/turtle.html
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


# Screen Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.colormode(255)  # To Use RGB Background Colors
# screen.bgcolor(13,16,30)  # Replit Blue
screen.bgcolor(34,34,34)  # 222 Grey
screen.title("Py Snake Game")
screen.tracer(0) # Stop displacing animations until you need, no jittering


#TODO 1. Create the snake Body - Completed in snake.py
    #turtles are 20x20 pixels
    #poisition at 0x0, 0x20, 0x40
snake = Snake() # creates the snake

#TODO 3. Create snake food
food = Food() # creates the food

# TODO 5. Create a scoreboard
scoreboard = Scoreboard()

#TODO 2. Move the snake - Completed in snake.py
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()  # Updates the screen
    time.sleep(0.1)  # adds one second delay after movement

    snake.move() # move the snake

    # TODO 4. Detect collision with food - Completed
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        print("nom nom nom")

    #TODO 6. Detect collision with wall - Completed
    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -280:
        scoreboard.game_over()
        game_on = False


    #TODO 7. Detect collision with tail
    # if the head collides with the body, trigger game over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            game_on = False
            scoreboard.game_over()























screen.exitonclick()


