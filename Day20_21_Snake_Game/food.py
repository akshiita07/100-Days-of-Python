# Food has to render itself on screen at random position
# When snake collides with food then food must change its position
from turtle import Turtle

# TO GET RANDOM FOOD POSIITONS:
# our screen:600x600
import random

# food class inherits from Turtle class
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")        #by default 20 by 20 px
        self.penup()        # do not draw
        # self.shapesize(stretch_len=0.5,stretch_wid=0.5)    # turn it into 10x10px: half it
        self.color("red")
        self.speed("fastest")
        self.moveFoodToRandomPosition()
        
    def moveFoodToRandomPosition(self):
        random_x=random.randint(-270,270)
        random_y=random.randint(-270,270)
        self.goto(random_x,random_y)