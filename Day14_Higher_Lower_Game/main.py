import art
import random
import os
from game_data import data      #list ctg dictionary

def getRandomPerson():
    # rNo=random.randint(0,len(data)-1)
    # return data[rNo]
    rNo=random.choice(data)
    return rNo

def check(person1,person2):
    """Checks which person has more followers"""
    correctAns=-1
    if person1["follower_count"]>person2["follower_count"]:
        correctAns="A"
    else:
        correctAns="B"
        
    return correctAns

def game():
    endGame=False
    score=0
    print(art.logo)
    
    # choose A person only for 1st time
    print("Compare A: ")
    p1=getRandomPerson()

    while endGame==False:
        print((f"{p1["name"]}, {p1["description"]}, from {p1["country"]}"))
        
        print(art.vs)
        
        # choose B person
        print("Against B: ")
        p2=getRandomPerson()
        
        # both must not be same
        if p1==p2:
            p2=getRandomPerson()
            
        # print person 2
        print((f"{p2["name"]}, {p2["description"]}, from {p2["country"]}"))
        
        # ask user
        # what if user typed small case
        user_guess=input("Who has more followers? Type 'A' or 'B': ").upper()
        correctAns=check(p1,p2)
        
        if user_guess==correctAns:
            score+=1
            os.system('cls')
            print(f"You're right! Current score: {score}")
            # now give p2 as p1 & generate a new p2
            print("Compare A: ")
            p1=p2
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            endGame=True
        
    
    
game()