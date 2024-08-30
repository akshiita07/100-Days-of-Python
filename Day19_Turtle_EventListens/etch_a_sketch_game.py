from turtle import Turtle,Screen
timmy_turtle=Turtle()
timmy_turtle.pensize(3)
timmy_turtle.color('hot pink')
timmy_turtle.shape('turtle')
screen=Screen()
# listen to keystrokes on keyboard
screen.listen()     #starts listening

def move_forwards():
    timmy_turtle.forward(10)

def move_backwards():
    timmy_turtle.backward(10)

def move_clockwise():
    timmy_turtle.left(90)

def move_counter_clockwise():
    timmy_turtle.right(90)

def clear_screen():
    timmy_turtle.clear()
    timmy_turtle.penup()        #as home() keeps on drawing path back to home
    # bring tutle back to center at starting point
    timmy_turtle.home()
    timmy_turtle.pendown()
    
# add event listen that takes fnc & key as parameter
screen.onkey(move_forwards,'w')
screen.onkey(move_backwards,'s')
screen.onkey(move_counter_clockwise,'a')
screen.onkey(move_clockwise,'d')
screen.onkey(clear_screen,'c')

# exit screen only when explicitly clicked!
screen.exitonclick()
