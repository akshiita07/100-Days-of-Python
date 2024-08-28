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
        timmy_turtle.left(90)
timmy_turtle.color("blue")
drawSquare()


def dashedLine():
    for _ in range(15):
        timmy_turtle.pendown();
        timmy_turtle.forward(10)
        timmy_turtle.penup();
        timmy_turtle.forward(10)
# dashedLine()

# move 360/noOfSides for different shapes
def drawTriangle():
    # 360/3=120
    for _ in range(3):
        timmy_turtle.forward(50)
        timmy_turtle.left(120)
timmy_turtle.color("forest green")
drawTriangle()

def drawPenatgon():
    # 360/5=72
    for _ in range(5):
        timmy_turtle.forward(50)
        timmy_turtle.left(72)
timmy_turtle.color("deep pink")
drawPenatgon()

def drawHexagon():
    # 360/6=60
    for _ in range(6):
        timmy_turtle.forward(50)
        timmy_turtle.left(60)
timmy_turtle.color("light green")
drawHexagon()

def drawHeptagon():
    # 360/7=51.4
    for _ in range(7):
        timmy_turtle.forward(50)
        timmy_turtle.left(51.4)
    
timmy_turtle.color("red")
drawHeptagon()

def drawOctagon():
    # 360/8=45
    for _ in range(8):
        timmy_turtle.forward(50)
        timmy_turtle.left(45)

timmy_turtle.color("sky blue")
drawOctagon()

def drawNonagon():
    # 360/9=40
    for _ in range(9):
        timmy_turtle.forward(50)
        timmy_turtle.left(40)
    
timmy_turtle.color("saddle brown")
drawNonagon()

def drawDecagon():
    # 360/10=36
    for _ in range(10):
        timmy_turtle.forward(50)
        timmy_turtle.left(36)
    
timmy_turtle.color("cornflower blue")
drawDecagon()



# screen object
screen=Screen()
# close only when explicitly done
screen.exitonclick();