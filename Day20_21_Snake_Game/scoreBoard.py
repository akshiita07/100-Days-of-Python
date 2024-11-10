from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        # to implement high score functionality:
        with open("./Day20_21_Snake_Game/data.txt", encoding="utf-8-sig") as file:
            self.highScore=int(file.read())
            print(self.highScore)
        self.color("white")
        self.hideturtle()       #as turtle is showing
        self.penup()
        self.goto(0,200)
        self.updateScore()
        
    def updateScore(self):
        self.clear()      #first clear previously written drawing
        self.write(f"Score: {self.score} High Score: {self.highScore}", align='center', font=('Arial', 24, 'normal'))
        
    def increaseScore(self):
        self.score+=1;
        self.updateScore()
        
    def resetScore(self):
        if self.score>self.highScore:
            self.highScore=self.score
            with open("./Day20_21_Snake_Game/data.txt",mode="w") as file:
                file.write(f"{self.highScore}")
        self.score=0
        self.updateScore()
        
        