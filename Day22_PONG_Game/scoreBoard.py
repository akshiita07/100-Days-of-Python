from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.leftScore=0
        self.rightScore=0
        
    def updateScore(self):
        self.goto(-100,200)
        self.write(self.leftScore,align="center",font=("Arial", 24, "normal"))
        self.goto(100,200)
        self.write(self.rightScore,align="center",font=("Arial", 24, "normal"))
        
    def lPoint(self):
        self.leftScore+=1
        self.clear()        #so that no overwrites
        self.updateScore()

    def rPoint(self):
        self.rightScore+=1
        self.clear()        #so that no overwrites
        self.updateScore()

    # def printMiss(self):
    #     self.goto(0,0)
    #     self.write("Miss",align="center",font=("Arial", 18, "normal"))