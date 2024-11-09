# CREATE SCREEN
# Create & Move 2 paddle
# Create & move ball
# Detect if ball collides with TOP OR BOTTOM WALL
# Detect if ball collides with PADDLE
# SCOREBOARD for each side when paddle misses ball

# 1. CREATE SCREEN:
from turtle import Turtle,Screen
screen=Screen()
screen.bgcolor('black')     #screen background changes to color black
screen.setup(width=800,height=600)      #ie 800x600pixels screen
screen.title('My PONG game')      #changes the title of screen that apears
screen.tracer(0)        #to turn OFF screen animation

# 2. Create & Move a paddle
from paddle import Paddle
left_paddle=Paddle(-350)
right_paddle=Paddle(350)
# for keystrokes:
screen.listen()
# listen for ARROW keys: & trigger fnc using paddle class
screen.onkeypress(right_paddle.up,"Up")
screen.onkeypress(right_paddle.down,"Down")
screen.onkeypress(left_paddle.up,"w")
screen.onkeypress(left_paddle.down,"s")

# 3. Create & move ball
from ball import Ball
ball=Ball()

# 7. SCOREBOARD for each side when paddle misses ball
from scoreBoard import ScoreBoard
scoreBoard=ScoreBoard()

game_is_on=True

import time #so that we can see our ball moving

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()     #to update screen manually as animtion is turned OFF
    ball.move()         #to move the ball
    scoreBoard.updateScore()
    
    # 4.  Detect if ball collides with TOP OR BOTTOM WALL
    if ball.ycor()>290 or ball.ycor()<-290:
        # collision with top or bottom wall so bounce
        ball.bounce()
        
    # 5. Detect if ball collides with PADDLEs
    if ball.distance(right_paddle)<50 and ball.xcor()>320 or ball.distance(left_paddle)<50 and ball.xcor()<=320:
        print("Contact!")
        ball.bounceWhenPaddle()    

    # 6. Detect if ball goes out of boundary for RIGTH PADDLE:
    if ball.xcor()>380:
        # now ball recenter
        ball.reset_ball_pos()
        # move ball towards opposite player
        # count score of opp player
        scoreBoard.lPoint()
        scoreBoard.printMiss()

    # 6. Detect if ball goes out of boundary for LEFT PADDLE:
    if ball.xcor()<-380:
        # now ball recenter
        ball.reset_ball_pos()
        # move ball towards opposite player
        # count score of opp player
        scoreBoard.rPoint()
        scoreBoard.printMiss()

screen.exitonclick()

