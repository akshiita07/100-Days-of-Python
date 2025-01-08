from tkinter import *
window=Tk()
window.title("My GUI Program")
window.minsize(width=500, height=300) 

myLabel=Label(text="I am a Label",font=("Arial",24,"bold"))
myLabel.pack() 

def button_clicked():
    myLabel["text"]="Button just got clicked!"
my_btn=Button(text="Click Me",command=button_clicked)
my_btn.pack()

# 3 types of layouts manager: pack,place,grid

# 1. PACK: packs each of d widget next to each other in vaguely logical format and by default starts from top   and others below previous one...add side="" to change it...difficult  to give precise position

# 2. PLACE: about precise positioning..providing x and y value....->very specific so have to work out coordinates beforehand
# my_btn.place(x=0,y=0)       #at top left
# my_btn.place(x=100,y=0)       #at top left
my_btn.place(x=100,y=200)       #at top left

# 3. GRID: imagine entire program is grid & divide it into any no of rows - and columns | 
myLabel.grid(column=0,row=0)       #at top left

# ADDING PADDING AROUND COMPONENTS:
window.config(padx=20,pady=20)

window.mainloop()