# from the turtle module import the class turtle
from turtle import Turtle
# from the turtle module import the class screen
from turtle import Screen

# or even use:
# from turtle import *    #imports everything but confusing to use

# importing module as an alias::
# import numpy as np            #now np is short form that is used instead of full name

# if a module is not built in inside python then first install module from pipy->these r stored in .venv ie virtual environment folder...if u install using pip then chances that it will get installed at wrong location

# create object of Turtle class
timmy_turtle=Turtle()
# change shape of our turtle
timmy_turtle.shape("turtle")
# change color of turtle
timmy_turtle.color("hot pink")

# to draw a aquare using turtle:
def drawSquare():
    for _ in range(4):
        timmy_turtle.forward(50)
        timmy_turtle.right(90)
# drawSquare()


def dashedLine():
    for _ in range(15):
        timmy_turtle.pendown();
        timmy_turtle.forward(10)
        timmy_turtle.penup();
        timmy_turtle.forward(10)
# dashedLine()

def drawTriangle():
    timmy_turtle.forward(100)
    timmy_turtle.left(135)
    timmy_turtle.forward(80)
    timmy_turtle.left(97)
    timmy_turtle.forward(80)

drawTriangle()

def drawPenatgon():
    pass

# drawPenatgon()

def drawHexagon():
    pass

# drawHexagon()

def drawHeptagon():
    pass

# drawHeptagon()

def drawOctagon():
    pass

# drawOctagon()

def drawNonagon():
    pass

# drawNonagon()

def drawDecagon():
    pass

# drawDecagon()



# screen object
screen=Screen()
# close only when explicitly done
screen.exitonclick();