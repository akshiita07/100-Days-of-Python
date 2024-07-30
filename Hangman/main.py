import hangman_art as art
import hangman_words as words
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
word_list=words.word_list
import random
chosen_word=random.choice(word_list)

#add as many blanks as letters of chosen word
length_chosenWord=len(chosen_word)
blanks=[]
for length in range(1,length_chosenWord+1):
    blanks+="_"
print("The word to be guessed has the following characters:")
print(blanks)

#Testing code
print(f'\nPssst, the solution is {chosen_word}.')

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
lives=6

#Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
eog=False

#Import the logo from hangman_art.py and print it at the start of the game.
print(art.logo)

while not eog:
    user_letter=input("\nGuess a letter: ")
    user_letter=user_letter.lower()
    print(f"\nThe letter guessed by user is: {user_letter}")

    #If the user has entered a letter they've already guessed, print the letter and let them know.
    if user_letter in blanks:
        print(f"You have already guessed {user_letter}")

    #go thru list letters one by one n check if it matches guess letter
    for pos in range(length_chosenWord):
        letters_in_chosen=chosen_word[pos]
        if(user_letter==letters_in_chosen):
            #print("Matches: Right")
            #reveal that letter in the display at that position
            blanks[pos]=user_letter

    if user_letter not in chosen_word:
        #If guess is not a letter in the chosen_word,
        #Then reduce 'lives' by 1. 
        #If lives goes down to 0 then the game should stop and it should print "You lose."
        # print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
        print(f"You made a wrong guess {user_letter} so you lose a life- hangman: ")
        print(art.stages[lives])
        if lives==0:
            eog=True
            print("\nYou LOST!")
        lives=lives-1 

    print("After guess blanks are:")
    print(blanks)

    if "_" not in blanks:
        eog=True
        print("\nCongrats you win!")



