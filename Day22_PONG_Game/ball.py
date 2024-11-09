from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("pink")
        self.penup()
        # move ball to top right corner of screen:800x600pixels screen->goto(380,280)
        self.x_move=10
        self.y_move=10
        self.move_speed=0.1
        
    def move(self):
        self.goto(self.xcor()+self.x_move,self.ycor()+self.y_move)
        
    def bounce(self):       
        # bounce when ball collides with top/bottom
        self.y_move=(self.y_move*(-1))
        
    def bounceWhenPaddle(self):
        # bounce when ball collides with paddle
        self.x_move=(self.x_move*(-1))
        # to increase speed after each paddle touch
        self.move_speed*=0.9
        
    def reset_ball_pos(self):
        self.goto(0,0)
        self.x_move=(self.x_move*(-1))
        # reset speed
        self.move_speed=0.1
        