# import colorgram
from turtle import Turtle, Screen
from random import choice, randint
my_screen = Screen()
my_screen.colormode(255)


# Extract 15 colors from an image. Comment out after extraction
# colors = colorgram.extract(image.jpg', 15)
# rgb_colors = []
# for color in colors:
#     # rgb_colors.append(color.rgb)
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

# Extracted Color List (From terminal code) - Removed the first  4 colors due to being almost white
rgb_colors = [(232, 52, 111), (230, 227, 81), (237, 220, 2), (17, 112, 177), (6, 196, 119), (232, 120, 171), (147, 64, 112), (225, 148, 54), (176, 194, 6), (221, 163, 216), (5, 175, 226)]

############### My Code ###########
# make a timmy object from the turtle class blueprint
tim = Turtle()      # instantiate a new turtle object called 'a'
tim.hideturtle()           # make the turtle invisible
tim.penup()                # don't draw when turtle moves
tim.speed("fastest")
# tim.pendown()              #draw when the turtle moves
# tim.shape("turtle")
# tim.color("grey20")



# TODO 1. Create a 10x10 dot grid painting
# TODO 2. Each dot is 20size spaced apart by 50
# TODO 3. Draw 100 Dots using color pallete



row_height = -170
for row in range(10):
    tim.pu()
    tim.goto(-240, row_height)
    tim.pd()
    for column in range(10):
        tim.dot(20,  choice(rgb_colors))
        tim.pu()
        tim.forward(50)
        tim.pd()
        row_height += 4

######Angela Code ########
# tim = Turtle()
# tim.color("grey20")
# tim.speed(10)
# tim.hideturtle()
#
# # Set starting Position for tim
# tim.pu()
# tim.setheading(225)
# tim.forward(300)
# tim.setheading(0)
# number_of_dots = 100
#
# for dot_count in range(1, number_of_dots+1):
#     tim.dot(20, choice(rgb_colors))
#     tim.forward(50)
#
#     if dot_count % 10 == 0:
#         tim.setheading(90)
#         tim.forward(50)
#         tim.setheading(180)
#         tim.forward(500)
#         tim.setheading(0)





my_screen.exitonclick()