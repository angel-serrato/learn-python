# TODO: 1 - Ask user what would you like? Espresso, latte, cappuccino
# TODO: 2 - Turn off the coffee machine
# TODO: 3 - Print report
# 300 ml water, 200 ml milk, 100 g coffee
# TODO: 4 - Check resources
# espresso = 50 ml 18g, latte 200 ml 24 g 150 ml milk, cappuccino 250 ml 24 g 100 ml milk
# TODO: 5 - Process coins
# penny = 1 cent 0.01, nickel = 5 cents 0.05, dime = 10 cents 0.10  , quarter = 25 cents 0.25
# print("Please insert coins:")
# quarters = int(input("How many quarters? "))
# dimes = int(input("How many dimes? "))
# nickels = int(input("How many nickels? "))
# pennies = int(input("How many pennies? "))
# TODO: 6 - Is the transaction successful ?
# TODO: 7 - Make coffee

from resources import menu, resources

def main():
    on_off = True
    print("Welcome to the Coffee Machine! ")
    while on_off:
        print("Here is the menu:")
        contador = 1
        for item, details in menu.items():
            print(f"{contador} - {item.capitalize()} (${details["cost"]})")
            contador += 1
        user_choice = input("What would you like?\n").lower()
        if user_choice == "off":
            print("Turning off the coffee machine. Goodbye!")
            on_off = False
        elif user_choice == "1":
            change = process_coins("espresso")
            if change > 0.01:
                if update_resources("espresso"):
                    make_coffee("espresso")
                    print(f"Here is your change ${change}")
        elif user_choice == "2":
            change = process_coins("latte")
            if change > 0.01:
                if update_resources("latte"):
                    make_coffee("latte")
                    print(f"Here is your change ${change}")
        elif user_choice == "3":
            change = process_coins("cappuccino")
            if change > 0.01:
                if update_resources("cappuccino"):
                    make_coffee("cappuccino")
                    print(f"Here is your change ${change}")
        elif user_choice == "4":
            print_report()
        else:
            print(f"Sorry, that's not a valid option. Please select a number from the menu.")

def print_report():
    for item in resources:
        if item == "milk" or item == "water":
            print(f"{item.capitalize()}: {resources[item]}ml")
        else:
            print(f"{item.capitalize()}: {resources[item]}g")

def process_coins(coffee):
    print("To purchase coffee, please insert the correct amount of coins:")
    quarters = float(input("How many quarters? ")) * 0.25
    dimes = float(input("How many dimes? ")) * 0.10
    nickels = float(input("How many nickels? ")) * 0.05
    pennies = float(input("How many pennies? ")) * 0.01
    sum_coins = quarters + dimes + nickels + pennies
    change = 0
    if coffee == "espresso":
        total: float = 1.5
        if sum_coins > total:
            change = round(sum_coins - total, 2)
            return change
        elif sum_coins < total:
            print("Sorry that's not enough money. Money refunded.")
            return change
    if coffee == "latte":
        total: float = 2.5
        if sum_coins > total:
            change = round(sum_coins - total, 2)
            return change
        elif sum_coins < total:
            print("Sorry that's not enough money. Money refunded.")
            return change
    if coffee == "cappuccino":
        total: float = 3.0
        if sum_coins > total:
            change = round(sum_coins - total, 2)
            return change
        elif sum_coins < total:
            print("Sorry that's not enough money. Money refunded.")
            return change

def update_resources(coffee_name):
    ingredients = menu[coffee_name]["ingredients"]
    for ingredient, amount_needed in ingredients.items():
        if resources.get(ingredient, 0) < amount_needed:
            print(f"No hay suficiente {ingredient} para hacer {coffee_name}")
            return False
    for ingredient, amount_needed in ingredients.items():
        resources[ingredient] -= amount_needed
    print(f"Recursos actualizados para hacer {coffee_name}")
    return True

def make_coffee(coffee):
    if coffee == "espresso":
        print("Here is your espresso. Enjoy! ☕")
    elif coffee == "latte":
        print("Here is your latte. Enjoy! ☕")
    else:
        print("Here is your cappuccino. Enjoy! ☕")

main()
