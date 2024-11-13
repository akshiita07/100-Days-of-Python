#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# returns all line as a list
with open("Day24_FILES/Mail_Merge_Project/Input/Names/invited_names.txt") as inv_names:
    names=inv_names.readlines()
    print("Names are: ",names)        #with \n at end
# now we get list of names:["Aang","Zuko","Appa","Katara","Sokka","Momo","Uncle" "Iroh","Toph"]


#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
with open("Day24_FILES/Mail_Merge_Project/Input/Letters/starting_letter.txt") as letter:
    letter_content=letter.read()
    for name in names:
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        # invited_names.strip()
        new_name=name.strip()
        new_letter=letter_content.replace("[name]", new_name)
        print(new_letter)
        
        with open(f"Day24_FILES/Mail_Merge_Project/Output/Ready_to_send/letter_for_{new_name}.docx",mode="w") as final_letter:
            # create new files with name as letter_for_name
            final_letter.write(new_letter)

