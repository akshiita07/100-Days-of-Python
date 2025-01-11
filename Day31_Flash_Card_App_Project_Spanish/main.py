from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

# in front on flash card: WORD IN SPANISH
# in back on flash card: WORD IN ENGLISH  

# read data:

# global dictionary:
current_card={}
data_dict={}

try:
    data=pandas.read_csv("Day31_Flash_Card_App_Project_Spanish/data/words_to_learn.csv")
except FileNotFoundError:
    original_data=pandas.read_csv("Day31_Flash_Card_App_Project_Spanish/data/spanish_to_english.csv")
    data_dict=original_data.to_dict(orient="records") 
else:
    # convert pandas dataframe to dictionary
    data_dict=data.to_dict(orient="records")    #in form of ("spanish":"word","english":"word_translation")
    # print(data_dict)

# button function
def next_card():
    # generate new spanish word:
    global current_card
    global flip_timer
    global data_dict
    window.after_cancel(flip_timer)
    
    canvas.itemconfig(canvas_image,image=front_image)
    canvas.itemconfig(current_language_text,text="Spanish",fill="black")
    
    # if we ran out of cards:
    try:
        current_card=random.choice(data_dict)
    except IndexError:
        canvas.itemconfig(current_language_text,text="Well done",fill="black",font=("Ariel",40,"bold"))
        canvas.itemconfig(current_word_text,text="You've memorized every card in this set!",fill="black",font=("Ariel",20,"italic"))
    else:
        new_random_word=current_card["Spanish"]
        canvas.itemconfig(current_word_text,text=new_random_word,fill="black")
        # timer of 3s to flip card: ie 3000ms
        flip_timer=window.after(3000,func=flipCard)
    
# when we already know a word then it must be removed from the dictionary
def isKnown_card():
    global data_dict
    # remove this current_card
    if current_card in data_dict:
        data_dict.remove(current_card)
    # print(len(data_dict))
    
    # save the list to a new file:
    data=pandas.DataFrame(data_dict)
    data.to_csv("Day31_Flash_Card_App_Project_Spanish/data/words_to_learn.csv",index=False)  #we do not wish to add indices to our new list so index=false
    
    next_card()
    
    
# flip card function to show english translation:
def flipCard():
    # change background image:
    canvas.itemconfig(canvas_image,image=back_image)
    canvas.itemconfig(current_language_text,text="English",fill="white")
    meaning_word=current_card["English"]
    canvas.itemconfig(current_word_text,text=meaning_word,fill="white")
    
       
window=Tk()
window.title("Flash Card App")
window.config(padx=30,pady=30,bg=BACKGROUND_COLOR)

# import images:
right_image = PhotoImage(file="Day31_Flash_Card_App_Project_Spanish/images/right.png")
wrong_image = PhotoImage(file="Day31_Flash_Card_App_Project_Spanish/images/wrong.png")
back_image = PhotoImage(file="Day31_Flash_Card_App_Project_Spanish/images/card_back.png")
front_image = PhotoImage(file="Day31_Flash_Card_App_Project_Spanish/images/card_front.png")

# canvas:
canvas=Canvas(width=800,height=526)     #dimensions of image
canvas_image=canvas.create_image(400,263,image=front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

# canvas text:
current_language_text=canvas.create_text(400,150,text="Spanish",fill="black",font=("Ariel",40,"italic"))
current_word_text=canvas.create_text(400,263,text="word",fill="black",font=("Ariel",60,"bold"))

canvas.grid(column=0,row=0,columnspan=2)    #takes up 2 columns

# Buttons:
button_known = Button(image=right_image, highlightthickness=0,command=isKnown_card)
button_known.grid(column=1,row=1)

button_unknown = Button(image=wrong_image, highlightthickness=0,command=next_card)
button_unknown.grid(column=0,row=1)

# timer of 3s to flip card: ie 3000ms
flip_timer=window.after(3000,func=flipCard)

# run fnc here in main also for first card to appear:
next_card()

window.mainloop()