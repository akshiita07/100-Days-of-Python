from turtle import Turtle,Screen
timmy_turtle=Turtle()
timmy_turtle.pensize(3)
timmy_turtle.shape('turtle')
screen=Screen()
# listen to keystrokes on keyboard
screen.listen()     #starts listening

def move_forwards():
    timmy_turtle.forward(10)
    
# add event listen that takes fnc & key as parameter
screen.onkey(move_forwards,'space')

# exit screen only when explicitly clicked!
screen.exitonclick()
