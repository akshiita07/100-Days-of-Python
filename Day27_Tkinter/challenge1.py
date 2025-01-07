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

window.mainloop()