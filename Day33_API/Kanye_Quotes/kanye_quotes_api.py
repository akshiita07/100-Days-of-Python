import requests
from tkinter import *

def get_kanye_quote():
    response=requests.get(url="https://api.kanye.rest")
    print(response.status_code)
    response.raise_for_status()     #to raise exceptions
    data=response.json()
    print(data)
    print(data["quote"])
    kanye_quote=data["quote"]
    canvas.itemconfig(kanye_text,text=kanye_quote)
    
    
# UI using TKinter:
window=Tk()
window.config(padx=30,pady=30)
canvas=Canvas(width=300,height=414)
bg=PhotoImage(file="Day33_API/Kanye_Quotes/background.png")
canvas.create_image(150,207,image=bg)

kanye_text=canvas.create_text(150,207,text="Quote here",width=250,font=("Arial",25,"bold"))

canvas.grid(column=0,row=0)

kanye_img=PhotoImage(file="Day33_API/Kanye_Quotes/kanye.png")
kanye_button=Button(image=kanye_img,command=get_kanye_quote)
kanye_button.grid(column=0,row=1)

window.mainloop()