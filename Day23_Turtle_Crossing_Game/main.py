# 1. CREATE SCREEN:
from turtle import Turtle,Screen
screen=Screen()
screen.bgcolor('white')     #screen background changes to color white
screen.setup(width=600,height=600)      #ie 800x600pixels screen
screen.title('Turtle crossing game')      #changes the title of screen that apears
screen.tracer(0)        #to turn OFF screen animation

# import all files we created:
from player import Player
player=Player()
from carManager import CarManager
carManager=CarManager()
from scoreBoard import ScoreBoard
scoreBoard=ScoreBoard()

import time
game_is_on=True

# for keystrokes:
screen.listen()
# listen for ARROW keys: & trigger fnc using paddle class
screen.onkeypress(player.up,"Up")

while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    carManager.createCar()
    carManager.moveCars()
    
    # When the turtle hits the top edge of the screen, it moves back to the original position and the player levels up. On the next level, the car speed increases.
    if player.ycor()>285:
        player.resetPosition()
        scoreBoard.levelUp()
        carManager.incSpeed()
    
    # When the turtle collides with a car, it's game over and everything stops
    for car in carManager.all_cars:
        if car.distance(player)<18:
            scoreBoard.turnOff()
            game_is_on=False
    
screen.exitonclick()