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

# import from snake library that we have created:
from snake import Snake     #import class Snake from snake.py
snake=Snake()
# import from food library that we have created:
from food import Food    
food=Food()
# import from scoreBoard library that we have created:
from scoreBoard import ScoreBoard    
scoreBoard=ScoreBoard()
    
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
    snake.move()        #from the snake class
    # control snake using key bindings
    
    # DETECT COLLISIONS WITH FOOD
    # compare distance of turtle with the one inside ()
    if snake.head.distance(food)<25:
        print("Collision of snake & food!")
        food.moveFoodToRandomPosition()
        # increase score board
        scoreBoard.increaseScore()
        # increase length of snake by 1:
        snake.extend()
        

    # DETECT COLLISIONS WITH WALL
    if snake.head.xcor()>285 or snake.head.xcor()<-285 or snake.head.ycor()>285 or snake.head.ycor()<-285:
        # gameIsOn=False
        scoreBoard.resetScore()
        snake.removeSnake()
    
    # DETECT COLLISIONS WITH ITS OWN TAIL
    for segment in snake.segments[1:]:
        # do not do for only 1 segment
        # if segment==snake.head:
        #     pass      
        # OR USE SLICING : [1:]
        if snake.head.distance(segment)<10:
            # gameIsOn=False
            scoreBoard.resetScore()
            snake.removeSnake()


# import from gameOver library that we have created:
# from gameOver import GameOver    
# gameOver=GameOver()
# if gameIsOn==False:
    # gameOver.giveMessage()
    
screen.exitonclick()