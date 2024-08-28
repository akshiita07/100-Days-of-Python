import turtle
from turtle import Turtle,Screen
timmy_turtle=Turtle()
import random

# first change color mode using turtle library
turtle.colormode(255)
def randomColor():
    # (r,g,b)
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    # generate tuple
    return (r,g,b)

# shape of turtle
timmy_turtle.shape('turtle')
# thickness of line
timmy_turtle.pensize(3)
# speed
timmy_turtle.speed('fastest')

# also stop creating circle when 1st circle coincides
def createSpirograph(step_size):
    for _ in range(int(360/step_size)):
        # generate a random walk of same dist but any direction! !!all with diff colors!!
        timmy_turtle.color(randomColor())
        # draw a circle with radius=100
        timmy_turtle.circle(100)
        # get current head position
        print(timmy_turtle.heading())
        current_head=timmy_turtle.heading()
        timmy_turtle.setheading(current_head+step_size)

createSpirograph(10)
screen=Screen()
screen.exitonclick()