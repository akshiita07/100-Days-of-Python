from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.hideturtle()       #as turtle is showing
        self.penup()
        self.goto(0,260)
        self.write(f"Score: {self.score}", align='center', font=('Arial', 24, 'normal'))
        
    def increaseScore(self):
        self.score+=1;
        self.clear()      #first clear previously written drawing
        self.write(f"Score: {self.score}", align='center', font=('Arial', 24, 'normal'))
        
        