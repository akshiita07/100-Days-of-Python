from tkinter import *
THEME_COLOR = "#375362"
from quiz_brain import QuizBrain

# CREATE TKINTER USER INTERFACE INSIDE A CLASS:
class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):    #to ensure that quiz_brain variable is of type QuizBrain
        self.quiz=quiz_brain    #to get quiz question input
        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(padx=30,pady=30,bg=THEME_COLOR)
        
        self.score_label=Label(text="Score:0",fg="white",bg=THEME_COLOR,font=("Arial",15,"bold"))
        self.score_label.grid(row=0,column=1)
        
        self.canvas=Canvas(width=300,height=250,bg="white",highlightthickness=0) 
        self.question_text=self.canvas.create_text(150,125,text="Question here",fill="black",width=280,font=("Arial",20,"italic"))
        self.canvas.grid(column=0,row=1,columnspan=2,pady=50)
        
        correct_img=PhotoImage(file='Day34_Quizzler/images/true.png')
        wrong_img=PhotoImage(file='Day34_Quizzler/images/false.png')
        self.correct_btn=Button(image=correct_img,highlightthickness=0,command=self.check_true_ans)
        self.correct_btn.grid(row=2,column=0)
        self.wrong_btn=Button(image=wrong_img,highlightthickness=0,command=self.check_false_ans)
        self.wrong_btn.grid(row=2,column=1)
        
        # run fnc:
        self.get_next_question()
        
        self.window.mainloop()
    
    def get_next_question(self):
        # if we still have ques remaining then:
        if self.quiz.questionsAreLeft():
            # each time new ques is displayed show white screen again:
            self.canvas.config(bg="white")
            # score tracking:
            self.score_label.config(text=f"Score:{self.quiz.score}")
            q_text=self.quiz.giveNewQues()
            # fill in question:
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="You have reached the end of the quiz!")
            # also disable the buttons
            self.canvas.config(bg="white")
            self.correct_btn.config(state="disabled")       #so that we cannot press now
            self.wrong_btn.config(state="disabled")     #so that we cannot press now            
        
    # 2 fncs for buttons to work:
    def check_true_ans(self):
        # call fnc from QuizBrain
        is_correct=self.quiz.checkAnswer("True") 
        self.give_feedback(is_correct)

    def check_false_ans(self):
        # call fnc from QuizBrain
        is_correct=self.quiz.checkAnswer("False")
        self.give_feedback(is_correct)

    def give_feedback(self,is_correct):
        if is_correct==True:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)    #after 1000ms=1s perform this fnc
