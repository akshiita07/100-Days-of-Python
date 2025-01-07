from tkinter import *
window=Tk()
window.title("My GUI Program")
window.minsize(width=500, height=300) 
myLabel=Label(text="I am a Label",font=("Arial",24,"bold"))
myLabel.pack() 
def button_clicked():
    # whatever is written by user must be displayed as label text when button is clicked
    myLabel["text"]=input.get()

my_btn=Button(text="Click Me",command=button_clicked)
my_btn.pack()

input=Entry()
input.pack()
input["width"]=50
# get: to get user input as string

window.mainloop()