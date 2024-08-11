from art import logo
# dictionary of all ☕:
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 7,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 10,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
# no of coins we have: 1,2,5

# 3 flavours: Latte, Expresso, Cappuccino ☕
# On typing REPORT-> we must see all resources we r left with
# when user orders drink-> check if resources r sufficient enough??
# Ask to insert coins-> how many pennies/dimes /etc...
# give change back/ is transaction successful?
# what u r left     

def showReport(money):
    """Shows the current resource values"""
    print(f"Water: {resources["water"]}")
    print(f"Milk: {resources["milk"]}")
    print(f"Coffee: {resources["coffee"]}")
    print(f"Money: {money}")
    
def checkResources(userChoice):
    """ Checks if there are enough resources to make the drink"""
    drink=MENU[userChoice]
    drinkIngredients=drink["ingredients"]
    
    # check wrt resources
    for item in drinkIngredients:
        if drinkIngredients[item]>resources[item]:
            print(f"Sorry there is not enough {item}.​")
            return False
    # if all ing are present then only true:
    return True
    
def deliverCoffee(user_choice):
    """Deducts resources when coffee is delivered"""
    drink=MENU[user_choice]
    drinkIngredients=drink["ingredients"]
    # give default value 0 if not present
    resources["water"]-=drinkIngredients.get("water",0)
    resources["milk"]-=drinkIngredients.get("milk",0)
    resources["coffee"]-=drinkIngredients.get("coffee",0)

def getMoney(userChoice,machine_profit):
    """Processes coins & returns change & also caluclates total profit of machine & if the transcation is successful or not"""
    drink=MENU[userChoice]
    moneyReqd=drink["cost"]
    print(f"Amount={moneyReqd}.")
    print("Please enter coins: ")
    noOf1s=int(input("Enter number of 1s: "))
    noOf2s=int(input("Enter number of 2s: "))
    noOf5s=int(input("Enter number of 5s: "))
    # check coins inserted
    money_inserted_by_user=(noOf1s*1)+(noOf2s)*2+(noOf5s)*5
    if money_inserted_by_user>=moneyReqd:
        # exact amount
        print("Transaction successful.")
        machine_profit=machine_profit+moneyReqd
        # provide change
        moneyChange=money_inserted_by_user-moneyReqd
        if moneyChange>0:
            # round up change upto 2 decimal places
            moneyChange=round(moneyChange,2)
            print(f"Here is your change: {moneyChange}")
    else:
        # less money inserted
        print("Sorry that's not enough money. Money refunded.")
        # return transaction is NOT successful
        return machine_profit,False
    # return transaction is successful
    return machine_profit,True
    

def makeDrink(userChoice,profit):
    if checkResources(userChoice)==True:
        # make drink
        print(f"I am making a {userChoice}")
        profit,success=getMoney(userChoice,profit)
        if success==True:
            deliverCoffee(userChoice)
            print(f"Here is your {userChoice}🍵. Enjoy!")
        return profit
    else:
        print("Insufficient resources :((")
        return profit
        
# START COFFEE MACHINE HERE:   
def coffeeMachine():
    turnOff=False
    profit=0
    while turnOff==False:
        print(logo)
        user_choice=input("​What would you like ☕? (espresso/latte/cappuccino):​")
        user_choice=user_choice.lower()
        if user_choice in["espresso","latte","cappuccino"]:
            profit=makeDrink(user_choice,profit)
        elif user_choice=="report":
            # show report
            showReport(profit)
        elif user_choice=="off":
            # end execeution
            print("Okay Bye :)")
            turnOff=True
        
coffeeMachine()