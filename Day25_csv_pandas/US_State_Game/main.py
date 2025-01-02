# for turtle:
import turtle
screen=turtle.Screen()
screen.title("U.S. States Game")
# set turtle shape as background image of map of US:
image="Day25_csv_pandas/US_State_Game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# mouse click at that specific coordinates:
def get_mouse_coord(x,y):
    print(x,y)
turtle.onscreenclick(get_mouse_coord)

# for coordinate state mapping:
import pandas
data=pandas.read_csv("Day25_csv_pandas/US_State_Game/50_states.csv")
states_list=data["state"].to_list()

user_guessed_states=[]
score=0

while len(user_guessed_states)<50:
    # take input from user:
    user_input=screen.textinput(title=f"{score}/50 Guess the State",prompt="What is state's name?")
    print(f"User typed: {user_input}")
    # convert case of user input into a consistent title case(1st capital & rest small):
    user_input=user_input.title()
    
    if user_input=="Exit":
        '''
        missing_states=[]
        for state in states_list:
            if state not in user_guessed_states:
                missing_states.append(state)
        '''
        # or using list comprehension:
        missing_states=[state for state in states_list if state not in user_guessed_states]
        print(missing_states)
        # if user typed exit then generate csv file for him to learn remaining states:
        new_data=pandas.DataFrame(missing_states)
        new_data.to_csv("to_learn_states.csv")
        break
    
    # found then place it on map
    if(user_input in states_list):
        # get coordinates from pandas:
        get_row=data[data["state"]==user_input]
        x_coord=get_row["x"].values[0]      #convert series to integer
        y_coord=get_row["y"].values[0]
        # create turtle at this x & y
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x_coord,y_coord)
        t.write(user_input)
        user_guessed_states.append(user_input)
        score+=1
    # if no found then ask for input again:
    else:
        print("Oops! Not found")
        
# turtle.mainloop()       # to keep the screen open ie alternative to screen.exitonclick()
# screen.exitonclick()