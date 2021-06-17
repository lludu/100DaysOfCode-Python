from turtle import Turtle

FONT = "Courier", 16, "bold"
ALIGN = "center"

with open("data.txt") as data:
    HIGHSCORE_FROM_FILE = int(data.read())



class Scoreboard(Turtle):
    def __init__(self): # Initialize
        super().__init__() # get inheritance from Turtle
        self.score = 0
        self.color("whitesmoke")
        self.penup()
        #TODO Read High Score from data.txt
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.goto(x=0,y=260)
        self.hideturtle()
        self.update_scoreboard()


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.highscore}", align=ALIGN, font=FONT)

    def reset(self):
        if int(self.score) > int(self.highscore):
            #TODO Write High Score from data.txt
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.score))
        self.score = 0
        self.update_scoreboard()