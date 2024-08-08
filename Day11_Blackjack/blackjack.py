# get as close to 21 as possible
# J,K,Q-> count as 10
# A can be either 1 or 11

# HIT->TO GET ANOTHER CARD

import random;
import os;
from art import logo

endGame=False

# to find sum of all cards
def findSum(cards):
    sum=0
    for item in cards:
        sum+=item
    return sum

# to print all cards
def printCards(cards):
    # map to loop & join thru ,
    return (" , ".join(map(str, cards)))

def checkCard(userCardsSum,compCardsSum):
    if userCardsSum==compCardsSum:
        print("Its a tie! 🚀")
    elif compCardsSum==21:
        print("Computer got a blackjack. You lose 😭")
    elif userCardsSum==21:
        print("You got a blackjack. You win 😁")
    elif compCardsSum>21:
        print("Computer went over 21. You win 😁")
    elif userCardsSum>21:
        print("You went over 21. You lose 😭")
    else:
        compDiff=21-compCardsSum
        userDiff=21-userCardsSum
        # jo min  hai woh winner
        if compDiff<userDiff:
            print("Comp has a closer value to 21. You lose 😭")
        else:
            print("You have a closer value to 21. You win 😁")

def playBlackjack():
    print(logo)
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]  #13 total cards A-K
    play=True
    while play==True:
        # provide 2 cards to both comp & user randomly
        # random.randint(0,len(cards)-1)   #random no between 0 & 12
        compCards=[cards[random.randint(0,len(cards)-1)],cards[random.randint(0,len(cards)-1)]]
        compCardsSum=findSum(compCards)
        # also shows 1 of the comp cards
        print("Computer's first card: ",compCards[0])
        userCards=[cards[random.randint(0,len(cards)-1)],cards[random.randint(0,len(cards)-1)]]
        userCardsSum=findSum(userCards)
        # show ur 2 cards as: [_,_]
        print(f"Your cards: [{printCards(userCards)}], Your current score: {userCardsSum}")
        
        # check if any one of them have A+10 ie blackjack??
        if compCardsSum==21:
            print(f"Final Computer cards: [{printCards(compCards)}], Computer current score: {compCardsSum}")
            checkCard(userCardsSum,compCardsSum)
            break
        elif userCardsSum==21:
            checkCard(userCardsSum,compCardsSum)
            break
            
        askForNewCard=True
        while askForNewCard==True:
            newCard=input("Type 'y' to get another card, type 'n' to pass: ")
            if newCard=="y":
                askForNewCard=True
                # draw another new card for user
                userCards.append(cards[random.randint(0,len(cards)-1)])
                userCardsSum=findSum(userCards)
                print(f"Your new cards: [{printCards(userCards)}], Your current score: {userCardsSum}")
                
                # user has new cards
                if userCardsSum==21:
                    print("You got a blackjack. You win 😁")
                    askForNewCard=False
                    play=False
                    break
                
                # if count>21:->check if A present->no: BUST-> lost OR yes:count A as 1 instead then check if sum>21->yes:lost else:draw new card/check results
                elif userCardsSum>21:
                    if 11 in userCards:
                #       A present so count it as 1 instead
                #       replace 11 as 1
                        indexOf11=userCards.index(11)
                        userCards[indexOf11]=1
                        userCardsSum=findSum(userCards)
                        print("Converted user card A from 11 to 1.")
                        print(f"Your new cards: [{printCards(userCards)}], Your current score: {userCardsSum}")
                        if userCardsSum>21:
                #             # still greater so lost
                            print("Converted A from 11 to 1 but still BUST!! You went over. You lose 😭")
                            play=False
                            askForNewCard=False
                        # else:
                             # u can draw another card!
                    else:
                        # 11 is not in cards & sum>21
                        print("You went over 21. You lose 😭")
                        askForNewCard=False
                        play=False
                        break
                # else:
                    # ctd
            elif newCard=="n":
                askForNewCard=False
                # user does not want a new card
                
        # else: comp truen..if sum<16 then comp draws card
        if userCardsSum<=21:
            compCardsSum=findSum(compCards)
            while compCardsSum<16:
                # draw card for comp
                compCards.append(cards[random.randint(0,len(cards)-1)])
                compCardsSum=findSum(compCards)
            # normally ctd checking for total sum
            print(f"Final Computer cards: [{printCards(compCards)}], Computer current score: {compCardsSum}")
            checkCard(userCardsSum,compCardsSum)
            play=False
        
                            
while endGame==False:
    playAgainInput=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if playAgainInput=="y":
        # clear screen upar ki
        os.system('cls')
        playBlackjack()
    elif playAgainInput=="n":
        os.system('cls')
        print("Ok bye!")
        endGame=True
    else:
        print("Not a valid input 😑")