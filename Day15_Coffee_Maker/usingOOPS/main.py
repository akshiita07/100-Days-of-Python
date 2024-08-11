from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menuObj=Menu()
# menuItemObj=MenuItem()
coffeeMakerObj=CoffeeMaker()
moneyMachObj=MoneyMachine()


def coffeeMachine():
    turnOff=False
    while turnOff==False:
        user_choice=input(f"​What would you like ☕? ({menuObj.get_items()}):​")
        # lower case:
        user_choice=user_choice.lower()
        
        if user_choice in["espresso","latte","cappuccino"]:
            # check if resources sufficient
            drink=menuObj.find_drink(user_choice)
            if coffeeMakerObj.is_resource_sufficient(drink)==True:
                # resources available
                # get payment: returns true for successful payment
                if moneyMachObj.make_payment(drink.cost)==True:
                    # provide coffee
                    coffeeMakerObj.make_coffee(drink)
        elif user_choice=="report":
            # print report for all resources
            coffeeMakerObj.report()
            moneyMachObj.report()
        elif user_choice=="off":
            # end execeution
            print("Okay Bye :)")
            turnOff=True
        
coffeeMachine()