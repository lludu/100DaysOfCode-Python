# # # PONG # # #
from color import *
from turtle import Screen, Turtle  # https://docs.python.org/3/library/turtle.html
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# <--------------  Create game Screen -------------> #
screen = Screen()
screen.colormode(255)
screen.bgcolor(COLOR_222)
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)  # Disable the animation


# <--------------  Create Player Paddle -------------> #
r_paddle = Paddle((350, 0))  # make a new paddle on the right for the player
l_paddle = Paddle((-350, 0))  # make a new paddle on the left for the computer
# l_paddle.color(COLOR_WHITESMOKE)

# <--------------  Create Ball -------------> #
ball = Ball()
# <--------------  Create Scoreboard -------------> #
scoreboard = Scoreboard()

# <--------------  Listen to key strokes to move the paddles -------------> #
screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")

screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")


game_on = True

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()


    # <--------------  Detect Wall Collision -------------> #
    if ball.ycor() > 280 or ball.ycor() < -280:
        # Needs to bounce
        ball.y_bounce()

    # <--------------  Detect Paddle Collision -------------> #
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()



    # <--------------  Detect Right Paddle Miss (Points) -------------> #
    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.l_point()
        scoreboard.update_scoreboard()


    # <--------------  Detect Left Paddle Miss (Points) -------------> #
    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.r_point()
        scoreboard.update_scoreboard()

screen.exitonclick()
