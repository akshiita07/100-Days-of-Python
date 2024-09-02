# 1. create snake body using 3 squares on screen lined up next to each other
# 2. move snake forwards
# 3. control snake using arrow keys
# 4. Put food in screen
# 5. Detetct collsion of snake with food & create new food at random location on screen
# 6. Add scoreboard
# 7. Cases when game ends ->collides with wall ->collides with own tail ->head hits any part of body of snake

import time
from turtle import Turtle,Screen
screen=Screen()
screen.setup(width=600,height=600)      #ie 600x600pixels screen
screen.bgcolor('black')     #screen background changes to color black
screen.title('My snake game')      #changes the title of screen that apears

screen.tracer(0)        #turn off animations->now update has to be used

# import from snake library
from snake import Snake     #import class Snake from snake.py
snake=Snake()
    
gameIsOn=True

# for keystrokes:
screen.listen()
# listen for ARROW keys: & trigger fnc using snake class
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

while gameIsOn:
    screen.update()     #the screen updates after all segments r created
    time.sleep(0.1)     #add a bit of pause of 0.1s
    # move all segments
    snake.move()        #from the sanke class
    
    # control snake using key bindings

screen.exitonclick()