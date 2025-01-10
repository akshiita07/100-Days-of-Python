from tkinter import *       #imports all classes & constants but not messagebox so explictly import it:
from tkinter import messagebox      
import os   #for file directory
import random   #for password generation
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# pip install pyperclip
import pyperclip

import json

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
    pyperclip.copy(password_generated)
    
# ---------------------------- SAVE & search PASSWORD ------------------------------- #
# when user clicks on add button, save data into a file called data.txt
# Format: website | email | password
def addPasswordIntoFile():
    website=website_input.get()
    email=email_input.get()
    password=password_input.get()
    
    # create new data in form of dictionary to be added in json:
    new_data={
        website:{
            "email":email,
            "password":password,
        }
    }
    
    # if any field empty then error pop up
    if (len(website)==0 or len(email)==0 or len(password)==0):
        isError=messagebox.showerror(title="Oops",message=f"Empty fields are NOT allowed")
    else:        
        # ask user if correct fields are entered or not:
        isOkay=messagebox.askokcancel(title="Check your details",message=f"Do you wish to save:\nWebsite: {website}\nEmail: {email}\nPassword: {password}")
            
        if isOkay:
            current_dir = os.getcwd()
            folder_path = os.path.join(current_dir, "Day30_Errors_Exceptions_JSON_PasswordManagerImproved/")  # Create the full file path
            file_path = os.path.join(folder_path, "data.json")  # Create the full file path

            # ADD EXCEPTION HANDLING IF FILE DOES NOT EXIST:
            try:
                with open(file_path, "r") as data_file:   #using read mode
                    # read exisiting data:
                    data=json.load(data_file)
                    # update data with new_data:
                    data.update(new_data)
                    
            except FileNotFoundError:
                # create new file
                with open(file_path, "w") as data_file:   #using write mode
                    # new file
                    json.dump(new_data,data_file,indent=4)
                    
            else:
                # write back:
                with open(file_path, "w") as data_file:   #using write mode
                    # write new data to the file:
                    json.dump(data,data_file,indent=4)
            
            # to be executed every time: 
            finally:
                # then clear input fields of website & password
                website_input.delete(0,END) 
                password_input.delete(0,END) 
                website_input.focus()
                
# add pop-ups: STANDARD DIALOGS: MESSAGE BOXES
 
def searchPassword():
    website_inp=website_input.get()
    # if no website entered
    if len(website_inp)==0:
        messagebox.showerror(title="Error",message=f"Enter website name to search")
    else:
        # check if website_input found in json data:
        current_dir = os.getcwd()
        folder_path = os.path.join(current_dir, "Day30_Errors_Exceptions_JSON_PasswordManagerImproved/")
        file_path = os.path.join(folder_path, "data.json") 
        try:
            with open(file_path, "r") as data_file:   #using read mode
                data=json.load(data_file)
                if website_inp in data:
                    fetch_email=data[website_inp]["email"]
                    fetch_password=data[website_inp]["password"]
                    messagebox.showinfo(title=f"Password for {website_input}",message=f"Email: {fetch_email}\nPassword:{fetch_password}")
                else:
                    messagebox.showerror(title="Error",message=f"No details for this {website_inp} website exists")
        except FileNotFoundError:
            messagebox.showerror(title="Error",message=f"No data file found")
        


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

search_button=Button(text="Search Password",command=searchPassword)
search_button.grid(column=2,row=1)

addPass_button=Button(text="Add",width=44,command=addPasswordIntoFile)
addPass_button.grid(column=1,row=4,columnspan=2)

# inputs:
website_input=Entry(width=33)
website_input.grid(column=1,row=1,columnspan=2, sticky="w")
website_input.focus()

email_input=Entry(width=52)
email_input.grid(column=1,row=2,columnspan=2, sticky="w")
# add default entry for email:
email_input.insert(0,"pathakshita07@gmail.com")

password_input=Entry(width=33)
password_input.grid(column=1,row=3,columnspan=1, sticky="w")



window.mainloop()