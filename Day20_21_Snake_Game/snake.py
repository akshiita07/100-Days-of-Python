from turtle import Turtle,Screen
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]      #as a constant
MOVE_SPEED=20

class Snake:
    # constructor will run & ceate the snake for us
    def __init__(self):
        # SNAKE BODY:
        # each turtle is of 20x20pixels & first one is at (x=0,y=0)
        # y coord will stay same but x coordinate will differ
        self.segments=[]        #attribute of class so use self
        # all squares in a list
        # head of snake:
        self.createSnake()
        self.head=self.segments[0]
        
    def createSnake(self):
        for position in STARTING_POSITIONS:
            self.addSegment(position)
            
    # TO ADD SEGMENTS TO SNAKE:
    def addSegment(self,position):
        snakeBody=Turtle()
        # snakeBody.color('white')
        snakeBody.color("pink")
        snakeBody.penup()       #do not draw anything
        snakeBody.shape('square')
        snakeBody.goto(position)
        self.segments.append(snakeBody)  
        
    # TO EXTEND SNAKE WHEN IT EATS FOOD:
    def extend(self):
        self.addSegment(self.segments[-1].position())
    
    def move(self):
        # loop thru all segments from LAST to FIRST
        for i in range((len(self.segments)-1),0,-1):
            # ie range(start=2,stop=0,step=-1):
            # for turning of snake: move segment 3 to segment 2 && move segmet 2 to segment 1 && move segment1 along given dirn
            newX=self.segments[i-1].xcor()     #change second last segment
            newY=self.segments[i-1].ycor()     #change second last segment
            # last segment ie 2 must go to position of second last segment ie 1
            self.segments[i].goto(newX,newY)     #change last segment
        # after moving remaining pieces, move the first segment:
        # segments[0].left(90)
        self.segments[0].forward(MOVE_SPEED)
        
    # for keystrokes->change head of snake ie 0th segment
    def up(self):
        # if head is not down then move up
        if self.segments[0].heading()!=270:
            self.segments[0].setheading(90)

    def down(self):
        # if head is not up then move down
        if self.segments[0].heading()!=90:
            self.segments[0].setheading(270)

    def left(self):
        # if head is not right then move left
        if self.segments[0].heading()!=0:
            self.segments[0].setheading(180)

    def right(self):
        # if head is not left then move right
        if self.segments[0].heading()!=180:
            self.segments[0].setheading(0)

    def removeSnake(self):
        for segm in self.segments:
            segm.goto(1000,1000)        #cannot be seen on screen now
        self.segments.clear()
        # initilaise snake again:
        self.createSnake()
        self.head=self.segments[0]