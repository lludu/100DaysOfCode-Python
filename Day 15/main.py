from data import MENU, resources

#Importing clear from Replit.com
try:
    from replit import clear #clears the screen for gameplay, code only used on replit.com
    not_replit = False
except ModuleNotFoundError:
    # Error handling
    not_replit = True
    pass



# Variable Breakdown
# choice == name of the drink
# drink == dictionary of the selected drink, access ingredients and cost
# drink["cost"] == cost of the drink

# drink["ingredients"] == ingredients of the drink
# drink["ingredients"]["water"] == water from the drink
# drink["ingredients"]["milk"] == milk from the drink
# drink["ingredients"]["coffee"] == coffee from the drink

coffer = 0
is_on = True


def wipe():
    '''Clears the screen'''
    if not_replit:
        print('\n'*2)
    else:
        clear()

def process_coins():
    '''returns the value of all the coins the user has input'''
    print("\nPlease enter coins:")
    total = float(input("How many quarters?: ")) * .25
    total += float(input("How many dimes?: ")) * .10
    total += float(input("How many nickles?: ")) * .05
    total += float(input("How many pennies?: "))  * .01
    return total

def sale_success(payment, cost_of_drink):
  
    if payment > cost_of_drink:
        coffee_made = make_drink()
        if coffee_made:
            change = round(payment - cost_of_drink, 2)
            print("\nSale Successful!")
            print(f"Here is your ${change} in change.")
            print(f"Here is your {choice.capitalize()} ☕ .")
            return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
    

def make_drink():
    for item in drink["ingredients"]:
        if int(drink["ingredients"][item]) > resources[item]:
            print(f"Sorry, we do not have enough {item.capitalize()}.")
            return False
    else:
        for item in drink["ingredients"]:
            resources[item] -= drink["ingredients"][item]
        return True





    # if resources["water"] > drink["ingredients"]["water"] and resources["milk"] > drink["ingredients"]["milk"] and resources["coffee"] > drink["ingredients"]["coffee"]:
    #     resources["water"] -= drink["ingredients"]["water"]
    #     resources["milk"] -= drink["ingredients"]["milk"]
    #     resources["coffee"] -= drink["ingredients"]["coffee"]
    #     return True
    # else:
    #     print("Sorry, we dont know have enough ingredients to make that!")
    #     return False

while is_on:
    wipe()
    choice = input("What would you like? (Espresso, Latte, or Cappuccino): ").lower()
    if choice == "off":
        print("The machine will now turn off...\n")
        is_on = False
    elif choice == "report":
        print("The machine will now enter matience mode...\n")
        print("You can restock the machine by using 'restock' at the drink selection.\n")
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${coffer:.2f}")
    
    elif choice == "restock":
        for item in resources:
            resources[item] += 500
    else:
        drink = MENU[choice] 

        payment = process_coins()
        print(f"\n\nYou have entered ${payment} to buy a {choice.capitalize()} that cost ${drink['cost']:.2f}.")

        valid_sale = sale_success(payment, drink['cost'])
        print("")
        if valid_sale:
            coffer += drink['cost']




