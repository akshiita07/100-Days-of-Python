# a grid layout challenge: 3rows 4 columns
from tkinter import *
window=Tk()
window.title("Miles to km converter")
# window.minsize(width=350, height=200) 
window.config(padx=20,pady=20)

equalLabel=Label(text="is equal to",font=("Arial",12))
milesLabel=Label(text="Miles",font=("Arial",12))
ansLabel=Label(text="0",font=("Arial",12,"bold"))
kmLabel=Label(text="km",font=("Arial",12))

def onBtnClick():
    # fetch input miles & convert into km
    input_miles=input.get()
    ansLabel["text"]=(int(input_miles)*1.609)
btn=Button(text="Calculate",command=onBtnClick)

input=Entry(width=10)
input.focus()

equalLabel.grid(column=0,row=1)
milesLabel.grid(column=2,row=0)
kmLabel.grid(column=2,row=2)
ansLabel.grid(column=1,row=1)
input.grid(column=1,row=0)
btn.grid(column=1,row=2)

window.mainloop()