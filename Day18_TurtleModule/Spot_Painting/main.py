# using colorgram.py in pypi packages, extract colors from image.jpg
import colorgram

# Extract 6 colors from an image. 
colors = colorgram.extract('image.jpg', 12)

# colorgram.extract returns Color objects,RGB
colorExtracted=[]
for i in range(0,12):
    r=colors[i].rgb.r
    g=colors[i].rgb.g
    b=colors[i].rgb.b
    newColor=(r,g,b)
    colorExtracted.append(newColor)
# print("Colors extracted are: ")
# print(colorExtracted)
    
spotColors=[(252, 250, 247), (253, 247, 249), (237, 251, 245), (249, 228, 17), (213, 13, 9), (198, 12, 35), (231, 228, 5), (197, 69, 20), (33, 90, 188), (43, 212, 71), (234, 148, 40), (33, 30, 152)]

# create spot painting: 10 by 10 size..size of dot:20 spacing between:50paces
import turtle
from turtle import Turtle,Screen
import random
turtle.colormode(255)
timmy_turtle=Turtle();
timmy_turtle.shape('turtle')
timmy_turtle.width(2)
timmy_turtle.speed('fastest')

# start at such a place such that it does not goes off the page
timmy_turtle.penup()
timmy_turtle.setheading(220)
timmy_turtle.forward(350)
# change heading back
timmy_turtle.setheading(0)
no_of_dots=100

for dot_count in range(1,no_of_dots+1):
    # create dots here for each column
    timmy_turtle.pendown()
    timmy_turtle.dot(20,random.choice(spotColors))
    timmy_turtle.penup()
    timmy_turtle.forward(50)
    # move upwards now:
    if dot_count%10==0:
        timmy_turtle.penup()
        timmy_turtle.setheading(90)
        timmy_turtle.forward(50)
        timmy_turtle.setheading(180)
        timmy_turtle.forward(500)
        timmy_turtle.setheading(0)
        timmy_turtle.pendown()

# at end of painting-remove turtle
timmy_turtle.hideturtle()

screen=Screen()
screen.exitonclick()