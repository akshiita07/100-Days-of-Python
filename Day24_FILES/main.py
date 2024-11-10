# TO OPEN A FILE IN PYTHON:
file=open("./DAY24_FILES/my_file.txt")
# # TO READ FILE: TURNS CONTENT OF FILE AS STRING
content=file.read()
print(content)
file.close()

# METHOD 2 OF OPENING FILES WHEN U DONT WANT TO USE CLOSE()
# the mode of opening file by default is "r" ie read-only
# mode="w" opens in write mode     #will delete everything prexisting in file  #if file does NOT exist then it creates file
# mode="a" opens in append mode     #will add at END of prexisting file
with open("./DAY24_FILES/my_file.txt",mode="a") as file:
    # content=file.read()
    # print(content)
    file.write("\nI study at TIET")  
    
with open("./DAY24_FILES/my_new_file.txt",mode="w") as file:
    # content=file.read()
    # print(content)
    file.write("This new file created in write mode when file did not pre-exist")  