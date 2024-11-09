from turtle import Turtle

# constants defined here:
MOVE_DISTANCE = 15

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.goto(0,-280)       #initially at bottom
        self.left(90)
        
    def up(self):
        # turtle can only move upwards
        self.goto(self.xcor(),self.ycor()+MOVE_DISTANCE)
        
    def resetPosition(self):
        self.goto(0,-280)