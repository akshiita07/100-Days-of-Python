from art import logo
import random
import os

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
COMP_NUMB=random.randint(1,100)     #take as constant
print(f"pssttt 🤫 I choose {COMP_NUMB}")

user_difficulty=input("Choose a difficulty. Type 'easy' or 'hard': ")
 
game_end=False

def checkNumber(noAttempts):
    guess_again=True
    
    while guess_again==True:
        print(f"You have {noAttempts} attempts remaining to guess the number.")
        user_guess=int(input("Make a guess: "))
        if user_guess==COMP_NUMB:
            print("You got the number! 😊")
            guess_again=False
            game_end=True
            return game_end
        elif  user_guess<COMP_NUMB:
            # chota number
            print("Too LOW!")
            noAttempts-=1
            guess_again=True
        elif  user_guess>COMP_NUMB:
            # bada number
            print("Too HIGH!")
            noAttempts-=1
            guess_again=True
            
        if noAttempts==0:
            print("All attempts over. You lost😭") 
            guess_again=False
            game_end=True

# until user has not guessed or else if attempts r left
while game_end==False:
    if user_difficulty=="easy":
        # 10 attempts for guessing
        no_of_attempts=10
        checkNumber(no_of_attempts)
        break
                  
    elif user_difficulty=="hard":
        # 5 attempts for guessing
        no_of_attempts=5
        checkNumber(no_of_attempts)
        break
        
if(game_end==True):
    os.system('cls')
    print("Ok bye")