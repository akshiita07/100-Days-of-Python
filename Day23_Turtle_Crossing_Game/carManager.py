from turtle import Turtle

# constants defined here:
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

import random

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.all_cars=[]
        self.carSpeed=STARTING_MOVE_DISTANCE     
        
    def createCar(self):
        self.random_chance=random.randint(1,6)
        self.initialSpeed=0
        if self.random_chance==1:
            newCar=Turtle()
            newCar.penup()
            newCar.shape("square")
            newCar.shapesize(stretch_wid=1,stretch_len=2)     #2 times length but width same
            newCar.color(random.choice(COLORS))
            random_y_axis=random.randint(-250,250)
            newCar.goto(300,random_y_axis)
            # append in new car:
            self.all_cars.append(newCar)
        
    def moveCars(self):
        # Cars are randomly generated along the y-axis and will move from the right edge of the screen to the left edge.
        for car in self.all_cars:
            car.goto(car.xcor()-STARTING_MOVE_DISTANCE,car.ycor())
            
    def incSpeed(self):
        self.carSpeed+=MOVE_INCREMENT