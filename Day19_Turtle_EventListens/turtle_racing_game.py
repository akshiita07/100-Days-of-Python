from turtle import Turtle,Screen
import random
screen=Screen()
colors=['purple','black','blue','green','yellow','orange','red']
yIndices=[-150,-100,-50,0,50,100,150]

# explicitly define screen size instead of getting default:->setup width & height
screen.setup(width=500,height=400)      #use keyword arguments

raceIsOn=False

# pop-up to ask user to make a bet on which color will win game:-> .textinput() returns string
user_bet=screen.textinput(title='Its time to BET!',prompt='Which colored turtle will win the race?')
print(f"The user's bet is on the turtle with color: {user_bet}")

allTurtles=[]       #an empty list that will ocntain all 7 turtles

# properties of turtles:
for turtles in range(0,7):
    timmy=Turtle(shape='turtle')
    timmy.penup()
    timmy.color(colors[turtles])
    # all turtles must be present at LEFT side of screen-> goto method using x,y
    # when turtle is at center coordinates r (0,0)
    timmy.goto(x=-230,y=yIndices[turtles])        #it also shows path so penup()
    # do not be too slow speed
    timmy.speed('fast')
    # add all these turltes in list
    allTurtles.append(timmy)
    
if user_bet:
    raceIsOn=True

while raceIsOn:
    for turtle in allTurtles:
        # when any one of the turtle eaches end of screen ie coordinate(x=230) (turtle size is also 40x40) then stop
        if turtle.xcor()>230:
            raceIsOn=False
            winningTurtle=turtle.pencolor()
            if user_bet==winningTurtle:
                print('You won 😊')
            else:
                print('You lost the bet😭')
            print(f'The {winningTurtle} turtle won the race.')
        # move these turtles randomly
        turtle.forward(random.randint(0,10))

# exit screen only when explicitly clicked!
screen.exitonclick()
