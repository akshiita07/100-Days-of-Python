from tkinter import *       #imports all classes & constants but not messagebox so explictly import it:
from tkinter import messagebox      
import os   #for file directory
import random   #for password generation
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# pip install pyperclip
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generatePassword():
    numb_letters=random.randint(5,7)
    numb_numbers=random.randint(1,3)
    numb_symbols=random.randint(1,3)
    
    # list comprehension
    passList1=[random.choice(letters) for _ in range(numb_letters)]
    passList2=[random.choice(numbers) for _ in range(numb_numbers)]
    passList3=[random.choice(symbols) for _ in range(numb_symbols)]
    
    # combine 3lists into 1:
    passList=passList1+passList2+passList3

    random.shuffle(passList)
    password_generated="".join(passList)
    password_input.insert(0,password_generated)
    
    # directly copy this password to our clipboard:
    pyperclip.copy(password_input)
    
    

# ---------------------------- SAVE PASSWORD ------------------------------- #
# when user clicks on add button, save data into a file called data.txt
# Format: website | email | password
def addPasswordIntoFile():
    website=website_input.get()
    email=email_input.get()
    password=password_input.get()
    
    # if any field empty then error pop up
    if (len(website)==0 or len(email)==0 or len(password)==0):
        isError=messagebox.showerror(title="Oops",message=f"Empty fields are NOT allowed")
    else:        
        # ask user if correct fields are entered or not:
        isOkay=messagebox.askokcancel(title="Check your details",message=f"Do you wish to save:\nWebsite: {website}\nEmail: {email}\nPassword: {password}")
            
        if isOkay:
            current_dir = os.getcwd()
            folder_path = os.path.join(current_dir, "Day29_Password_Manager_using_Tkinter/")  # Create the full file path
            file_path = os.path.join(folder_path, "data.txt")  # Create the full file path

            with open(file_path, "a") as data_file:   #used append
                data_file.write(f"{website} | {email} | {password}\n")
            # then clear input fields of website & password
            website_input.delete(0,END) 
            password_input.delete(0,END) 
            website_input.focus()
            
            # add pop-ups: STANDARD DIALOGS: MESSAGE BOXES
    


# ---------------------------- UI SETUP ------------------------------- #
# use tkinter to create a new window
window=Tk()
window.title("Password Generator")
window.config(padx=30,pady=30)      #add padding 

# Crete canvas widget:
canvas=Canvas(width=200,height=200)

# adding logo image:
logo=PhotoImage(file="Day29_Password_Manager_using_Tkinter/logo.png")
canvas.create_image(100,102,image=logo)
# timer_text=canvas.create_text(102,130,text="00:00",fill="white",font=("Arial",30,"bold"))
canvas.grid(column=1,row=0)

# labels:
website_label=Label(text="Website:")
website_label.grid(column=0,row=1)

email_label=Label(text="Email/Username:")
email_label.grid(column=0,row=2)

password_label=Label(text="Password:")
password_label.grid(column=0,row=3)

# buttons:
genPass_button=Button(text="Generate Password",command=generatePassword)
genPass_button.grid(column=2,row=3)

addPass_button=Button(text="Add",width=44,command=addPasswordIntoFile)
addPass_button.grid(column=1,row=4,columnspan=2)

# inputs:
website_input=Entry(width=52)
website_input.grid(column=1,row=1,columnspan=2, sticky="w")
website_input.focus()

email_input=Entry(width=52)
email_input.grid(column=1,row=2,columnspan=2, sticky="w")
# add default entry for email:
email_input.insert(0,"pathakshita07@gmail.com")

password_input=Entry(width=33)
password_input.grid(column=1,row=3,columnspan=1, sticky="w")



window.mainloop()