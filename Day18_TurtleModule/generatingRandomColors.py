import turtle
from turtle import Turtle,Screen
timmy_turtle=Turtle()
import random

# do not use an array of colors
# first change color mode using turtle library
turtle.colormode(255)
def randomColor():
    # (r,g,b)
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    # generate tuple
    return (r,g,b)

directions=[0,90,180,270]

# shape of turtle
timmy_turtle.shape('turtle')
# thickness of line
timmy_turtle.pensize(10)
# speed up turtle
timmy_turtle.speed('fast')
# “fastest”,“fast”,“normal”,“slow”,“slowest”

for _ in range(100):
    # generate a random walk of same dist but any direction! !!all with diff colors!!
    timmy_turtle.color(randomColor())
    timmy_turtle.forward(20)
    timmy_turtle.setheading(random.choice(directions))


screen=Screen()
screen.exitonclick()