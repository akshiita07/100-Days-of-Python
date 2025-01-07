# a grid layout challenge: 3rows 4 columns
from tkinter import *
window=Tk()
window.title("My GUI Program")
window.minsize(width=500, height=300) 
myLabel=Label(text="Label",font=("Arial",24,"bold"))
my_btn=Button(text="Click Me")
new_btn=Button(text="Don't Click")
input=Entry()

myLabel.grid(column=0,row=0)
my_btn.grid(column=1,row=1)
new_btn.grid(column=2,row=0)
input.grid(column=3,row=3)

window.mainloop()