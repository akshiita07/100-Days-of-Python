from tkinter import *
THEME_COLOR = "#375362"

# CREATE TKINTER USER INTERFACE INSIDE A CLASS:
class QuizInterface:
    def __init__(self):
        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(padx=30,pady=30,bg=THEME_COLOR)
        
        self.score_label=Label(text="Score:0",fg="white",bg=THEME_COLOR,font=("Arial",15,"bold"))
        self.score_label.grid(row=0,column=1)
        
        self.canvas=Canvas(width=300,height=250,bg="white",highlightthickness=0) 
        self.q_text=self.canvas.create_text(150,125,text="Question here",fill="black",font=("Arial",20,"italic"))
        self.canvas.grid(column=0,row=1,columnspan=2,pady=50)
        
        correct_img=PhotoImage(file='Day34_Quizzler/images/true.png')
        wrong_img=PhotoImage(file='Day34_Quizzler/images/false.png')
        self.correct_btn=Button(image=correct_img,highlightthickness=0)
        self.correct_btn.grid(row=2,column=0)
        self.wrong_btn=Button(image=wrong_img,highlightthickness=0)
        self.wrong_btn.grid(row=2,column=1)
        
        self.window.mainloop()
    
    
