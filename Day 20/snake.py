from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# Color Constants
COLOR_WHITE = "whitesmoke"
COLOR_GREEN = 13, 96, 30
COLOR_SNAKE_GREEN = 108, 187, 60
COLOR_GREEN_GREY = 107, 136, 89
COLOR_REPLIT = 13, 16, 30
SNAKE_BODY = COLOR_GREEN
SNAKE_HEAD = COLOR_SNAKE_GREEN
BODY_SHAPE = "square"  # “arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake() # Create Snake Method
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segments = Turtle(shape=BODY_SHAPE)
            new_segments.color(SNAKE_BODY) # BODY COLOR BASED ON VARIABLE
            new_segments.penup()
            new_segments.speed(1)
            new_segments.goto(position)
            self.segments.append(new_segments)

        self.segments[0].color(SNAKE_HEAD)  # HEAD COLOR BASED ON VARIABLE

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):  # (start = 2, stop = 0, step = 1)
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
