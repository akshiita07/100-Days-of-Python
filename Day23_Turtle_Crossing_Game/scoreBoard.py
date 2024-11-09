from turtle import Turtle

# constants defined here:
FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.levelNumber=0
        self.hideturtle()
        self.goto(-200,250)       #left top
        self.updateScore()
        
    def updateScore(self):
        self.write(f"Level: {self.levelNumber}",align="center",font=FONT)
        
    def levelUp(self):
        self.levelNumber+=1
        self.clear()
        self.updateScore()
        
    def turnOff(self):
        self.goto(0,0)
        self.write("Game over",align="center",font=FONT)