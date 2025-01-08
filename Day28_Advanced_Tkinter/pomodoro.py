# 1. Decide on the TASK to be performed
# 2. Set TIMER for 25 mins
# 3. Work on task until timer rings
# 4. Take short 5 min break
# 5. A 20min break after 4 pomodoro cycles above are completed
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    
    # format time in 00:00 format:
    count_mins=math.floor(count/60)
    count_sec=count%60
    
    # if count_sec==0:
    #     count_sec="00"
    
    if count_mins<10:
        count_mins=f"0{count_mins}"
    
    if count_sec<10:
        count_sec=f"0{count_sec}"
    
    # print(count)
    canvas.itemconfig(timer_text,text=f"{count_mins}:{count_sec}")    #to update text of timer on GUI
    if count>0:     #as we don't want -ve
        global timer
        timer=window.after(1000,count_down,count-1)
    else:
        # when count 0 then call fnc again to inc reps & cnt with next rep
        fncStartBtn()
        # checkmarks:
        mark=""
        total_work_sessions=math.floor(reps/2)
        for _ in range(total_work_sessions):
            mark+="✓"
        checkMark_text["text"]=mark
        

# ---------------------------- UI SETUP ------------------------------- #
# use tkinter to create a new window
window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)      #add padding & background color

# window.after: amount of time to wait=1000ms=1s ,pass a fnc to call, pass *args ie inputs for our fnc defined
# def fnc(thing):
#     print(thing)
# window.after(1000,fnc,"hello")    

# Crete canvas widget:
canvas=Canvas(width=200,height=225,bg=YELLOW,highlightthickness=0)      #highlightthickness to remove white outline bordering the image
# adding tomato image:
tomato_img=PhotoImage(file="Day28_Advanced_Tkinter/tomato.png")
canvas.create_image(100,110,image=tomato_img)
# adding timer:
timer_text=canvas.create_text(102,130,text="00:00",fill="white",font=(FONT_NAME,30,"bold"))
canvas.grid(column=1,row=1)


# adding label text & butttons:
label_timer=Label(text="Timer",bg=YELLOW,fg=GREEN,font=(FONT_NAME,40,"bold"))
label_timer.grid(column=1,row=0)

checkMark_text=Label(text="",bg=YELLOW,fg=GREEN,font=(FONT_NAME,20,"bold"))
checkMark_text.grid(column=1,row=3)

def fncStartBtn():
    # timer fnc:
    # 1min:60sec
    # 25 mins: 25*60=1500sec
    global reps
    reps+=1 #start at first rep
    work_time=WORK_MIN*60
    short_break_time=SHORT_BREAK_MIN*60
    long_break_time=LONG_BREAK_MIN*60
    
    # 3 cases:
    if(reps==1 or reps==3 or reps==5 or reps==7):   
        count_down(work_time)
        label_timer["text"]="Work!"
    elif(reps==2 or reps==4 or reps==6):   
        count_down(short_break_time)
        label_timer["text"]="Short Break"
        label_timer["fg"]=PINK
    elif(reps==8):   
        count_down(long_break_time)
        label_timer["text"]="Long Break"
        label_timer["fg"]=RED
    
def fncResetBtn():
    # stop timer: use after cancel
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    # reset all checkmarks:
    checkMark_text["text"]=""
    # reset timer text
    label_timer["text"]="Timer"
    # reset no of reps back to 0:
    global reps
    reps=0

btn_start=Button(text="Start",command=fncStartBtn,highlightthickness=0)
btn_start.grid(column=0,row=2)

btn_reset=Button(text="Reset",command=fncResetBtn,highlightthickness=0)
btn_reset.grid(column=2,row=2)


window.mainloop()