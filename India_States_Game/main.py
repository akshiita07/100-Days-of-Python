import pandas
import turtle
screen=turtle.Screen()
screen.title("India States Game")
image="India_States_Game/india_map.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(width=800, height=800)
data=pandas.read_csv("India_States_Game/india_states_coordinates.csv")
states_list=data["State"].to_list();
score=0
guessed_states=[]

# mouse click at that specific coordinates:
def get_mouse_coord(x,y):
    print(x,y)
turtle.onscreenclick(get_mouse_coord)

while len(guessed_states)<28:
    user_input=turtle.textinput(title=f"{score}/28 Guess the State",prompt="What is state's name?")
    user_input=user_input.title()
    
    if user_input=="Exit":
        break
    
    if user_input in states_list:
        score+=1;
        guessed_states.append(user_input)
        get_row=data[data["State"]==user_input]
        x_coord=get_row["X"].values[0]
        y_coord=get_row["Y"].values[0]
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x_coord,y_coord)
        t.write(user_input)
    else:
        print("OOPS! Not found")

# turtle.mainloop()