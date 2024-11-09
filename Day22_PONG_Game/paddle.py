from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,coordinate):
        super().__init__()
        self.shape("square")
        self.color("white")
        #width 20 & height 100
        self.shapesize(stretch_wid=4,stretch_len=1)   #default:20*20
        self.penup()        #do not draw while moving
        self.goto(coordinate,0)     #coordinate=350 for right & -350 for left
        self.speed("fastest")
        
    def up(self):
        # up by 20px
        self.goto(self.xcor(),self.ycor()+30)
        
    def down(self):
        # down by 20px
        self.goto(self.xcor(),self.ycor()-30)