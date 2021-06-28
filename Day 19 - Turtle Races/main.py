#EXERCISE 2 - Turtle Race

from turtle import Turtle, Screen
from random import randint


def start_corner():
    turtle.pu()  # pick up pen
    turtle.goto(x=-220, y=160)  # move to upper left

# def write_name():
#     turtle.write(name)
#     turtle.forward(50)
#     turtle.showturtle()


# # # # Game
screen = Screen()
screen.setup(width=500, height=500)
colors = ["black", "blue", "green", "pink", "gray", "red", "orange"]
player_list = []
for names in range(0,7):
    player = screen.textinput(title="Enter 7 Racer's Name", prompt="Please Enter The Racer's Name")
    player_list.append(player)

user_bet = screen.textinput(title="Make your bet", prompt=f"Which turtle will win the race? Enter a name:\n\n{player_list}")
y_positions = [160, 110, 60, 10, -40, -90, -140]
turtle_list = []
screen.listen()
race_on = False


for players in range(0, 7):
    turtle = Turtle(shape="turtle")
    turtle.hideturtle()
    turtle.speed(10)
    turtle.color(colors[players])
    start_corner()
    turtle.goto(x=-220, y=y_positions[players])
    turtle.write(player_list[players])
    turtle.showturtle()
    turtle.speed(5)
    turtle.pd()
    turtle_list.append(turtle)
    turtle.name = player_list[players]

writer = Turtle()
writer.pu()
writer.hideturtle()
writer.goto(-100, 220)
writer.write(f"You bet on {user_bet}")


if user_bet:
    race_on = True


while race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 220:
            winning_turtle = turtle.name
            if winning_turtle == user_bet:
                turtle.penup()
                turtle.goto(x=-100, y=200)
                turtle.write(f"You Win ! {winning_turtle.capitalize()} Won The Race!")
                turtle.forward(180)
            else:
                turtle.penup()
                turtle.goto(x=-100, y=200)
                turtle.write(f"You Lost ! {winning_turtle.capitalize()} Won The Race!")
                turtle.forward(180)
            race_on = False

        walk_distance = randint(0, 10)
        turtle.forward(walk_distance)





















screen.exitonclick()

