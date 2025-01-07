import tkinter

# To create a NEW WINDOW:
window=tkinter.Tk()

# change TITLE of window:
window.title("My GUI Program")

# to change the size of window:
window.minsize(width=500, height=300)   #this is min size else it will adjust according to components added

# 1.to create a LABEL:
# text: what is displayed inside the label
# font:tuple(name_of_font,size_of_font,bold/italic)
myLabel=tkinter.Label(text="I am a Label",font=("Arial",24,"bold"))
# 2. specify how component will be laid out on the screen before it shows up
myLabel.pack()      #most imp else label is not visible on window
# myLabel.pack(side="left")      #adjusts at left
# myLabel.pack(side="bottom")      #adjusts at bottom
# myLabel.pack(expand=True)      #takes full height & width so adjusts in center
# **kw defined as argument for pack() method:

#changing text of label: using dictionary type access & using config
myLabel["text"]="New text label"
myLabel.config(text="Another new text") 

# BUTTONS:
def button_clicked():
    print("I just got clicked!")

my_btn=tkinter.Button(text="Click Me",command=button_clicked)       #DO NOT CALL FNC WITH () type only name of fnc
my_btn.pack()


# ENTRY COMPONENT FOR INPUT:
input=tkinter.Entry()
input.pack()
input["width"]=50
# get: to get user input as string
print(input.get())
# some default text to appear in input box: string=""
input.insert(tkinter.END,string="Some starting text")       #END is index

# TEXT ENTRY BOX: TO ENTER/INPUT MULTIPLE LINES OF TEXT
# heigh: no of lines
text=tkinter.Text(height=5,width=30)
# use focus so that cursor is by default placed there:
text.focus()
text.insert(tkinter.END,"Multi-line textbox")
print(text.get("1.0"),tkinter.END)       #take hold of characters starting from 1st line at the character 0
text.pack()

# SPINBOX: COUNTER THAT INCREMENTS/DECREMENTS
def spinbox_used():
    print(spinBox.get())
spinBox=tkinter.Spinbox(from_=0,to=10,command=spinbox_used)  #start from 0 to 10
spinBox.pack()

# SCALE: SLIDER THAT MOVES ALONG AXIS
def scale_used(val):
    print(val)
scale=tkinter.Scale(command=scale_used)
scale.pack()

# CHECKBOX: TICKED/NOT
def checkBox_used():
    # get variable value
    print(checkState.get())
checkState=tkinter.IntVar()
checkBox=tkinter.Checkbutton(text="On/Off",variable=checkState,command=checkBox_used)
# tie it to an integr variable to get value 0/1 for off/on resp
checkBox.pack()

# RADIOBUTTONS: TO CHOOSE 1 FROM MULTIPLE OPTIONS
def radioButton_used():
    # get variable value
    print(radioState.get())
radioState=tkinter.IntVar()
radioButton1=tkinter.Radiobutton(text="Option 1",value=1,variable=radioState,command=radioButton_used)
radioButton2=tkinter.Radiobutton(text="Option 2",value=2,variable=radioState,command=radioButton_used)
radioButton1.pack()
radioButton2.pack()

# LISTBOX: OF CHOICES TO PICK FROM
def listBox_used(event):
    print(listBox.get(listBox.curselection()))
listBox=tkinter.Listbox(height=4)
# python list:
names=["Akshita","Ritesh","Saanvi","Shaktee"]
# loop thru list:
for name in names:
    listBox.insert(names.index(name),name)
# bind fnc used to run callback fnc:
listBox.bind("<<ListboxSelect>>",listBox_used) 
listBox.pack()

# Keep window on the screen:        must be added at end
window.mainloop()