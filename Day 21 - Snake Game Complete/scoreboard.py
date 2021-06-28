from turtle import Turtle

FONT = "Courier", 16, "bold"
ALIGN = "center"


class Scoreboard(Turtle):
    def __init__(self): # Initialize
        super().__init__() # get inheritance from Turtle
        self.score = 0
        self.color("whitesmoke")
        self.penup()
        self.goto(x=0,y=260)
        self.hideturtle()
        self.update_scoreboard()


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)


    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGN, font=FONT)