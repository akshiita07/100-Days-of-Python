from turtle import Turtle

class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()       #as turtle is showing
        self.penup()
        
    def giveMessage(self):
        self.write("Game Over!", align='center', font=('Arial', 22, 'normal'))