from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# TODO 1. Print Report (Completed)
#TODO 2. Check Resources
#TODO 3. Process Coins
#TODO 4. Check transaction successful
#TODO 5. Make Coffee

#Make Objects using Classes

#Coffee Maker Object
coffee_maker = CoffeeMaker()
#Money Machine Object
money_machine = MoneyMachine()
#Menu Object
menu = Menu()


#Set Flag Variable
is_on = True

while is_on:
    drink_selection = menu.get_items()
    choice = input(f"What kind of drink do you want? {drink_selection}: ")

    #Turn machine off, end program
    if choice == "off":
        is_on = False

    #Run Coffee Machine Report
    elif choice == "report":
        print(money_machine.report())
        print(coffee_maker.report())

        #Run Coffee Machine Program
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)



