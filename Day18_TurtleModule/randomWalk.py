from turtle import Turtle,Screen
timmy_turtle=Turtle()
import random

# array of different colors a turtle can have:
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
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
    timmy_turtle.color(random.choice(colours))
    timmy_turtle.forward(20)
    timmy_turtle.setheading(random.choice(directions))


screen=Screen()
screen.exitonclick()