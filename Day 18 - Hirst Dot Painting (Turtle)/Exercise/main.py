from turtle import Turtle, Screen
from random import choice, randint
my_screen = Screen()
my_screen.colormode(255)


#make a timmy object from the turtle class blueprint
tim = Turtle()
tim.shape("classic")
tim.color("grey20")
tim.speed("fastest")
tim.pensize(2)
tim.hideturtle()


# Draw a square with loops
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# Draw a dashed line
# for _ in range(15):
#     tim.pd()
#     tim.forward(10)
#     tim.pu()
#     tim.forward(10)

# Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon
# 360 degrees / number of sides
# for shape in range(1, 8):
#     x = shape + 2
#     colors = ["DodgerBlue", "grey20", "green2", "orchid", "yellow", "sandybrown", "Slateblue"]
#     # tim.pencolor(colors[x - 3])
#     # Or Random Colors
#     tim.pencolor(choice(colors))
#     for _ in range(x):
#         tim.forward(100)
#         tim.right(360/x)


# Draw a random walk
# direction = [0, 90, 180, 270]
# colors = ["DodgerBlue", "grey20", "green2", "orchid", "yellow", "sandybrown", "Slateblue"]
#
# for _ in range(300):
#     tim.pencolor(choice(colors))
#     tim.setheading(choice(direction))
#     tim.forward(20)


# Draw a random walk with random colors using tuple
# direction = [0, 90, 180, 270]
# for _ in range(300):
#     r = randint(0, 255)
#     b = randint(0, 255)
#     g = randint(0, 255)
#     colors = (r, b, g)
#     tim.pencolor(colors)
#     tim.setheading(choice(direction))
#     tim.forward(20)

# Draw a spirograph with random colors
gap = 5
for degree in range(int(360/gap)):
    r = randint(0, 255)
    b = randint(0, 255)
    g = randint(0, 255)
    colors = (r, b, g)
    tim.pencolor(colors)
    tim.setheading(tim.heading()+gap)
    tim.circle(100)









#screen object from turtle module, keep at the bottom
my_screen.exitonclick()