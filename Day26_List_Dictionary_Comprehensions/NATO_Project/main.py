# Get name:
user_input=input("Enter your name: ")
user_input=user_input.upper()       #all our letters are in uppercase

# create dictionary of alphabet:corresp_nato_alphabet
import pandas 
data=pandas.read_csv("Day26_List_Dictionary_Comprehensions/NATO_Project/nato_phonetic_alphabet.csv")
# print(data)
# print(data.to_dict())
nato_dict={row.letter:row.code for (index,row) in data.iterrows()}
# print(nato_dict)

# list of the phonetic code words from a word that the user inputs as output:
nato_list=[nato_dict[letter] for letter in user_input]
print(nato_list)