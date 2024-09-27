MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
coffee_machine = {
    "ingredients": {
    "water" : 300,
    "milk" : 200,
    "coffee" : 100,},
    "cost" : 0
}
def check_availability(order_drink):
    for item in order_drink:
        if coffee_machine["ingredients"][item] < order_drink[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def is_transaction_successful(received_money, drink_cost):
    if received_money < drink_cost:
        print(f"Sorry there is not enough money.Money refunded successfully")
        return False
    else:
        change = round(received_money-drink_cost,2)
        print(f"Here is your change ${change}")
        coffee_machine["cost"] += drink_cost
        return True


def make_coffee(drink_name,drink_ingredients):
    for item in drink_ingredients:
        coffee_machine["ingredients"][item]-= drink_ingredients[item]
    print(f"Your {drink_name}☕️ is ready. Enjoy!")


on_machine = True
while on_machine:
    choice = input("\n\n\nWhat would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        print("GoodBye")
        on_machine = False
    elif choice == "report":
        print(f"Water: {coffee_machine["ingredients"]["water"]}ml")
        print(f"Milk: {coffee_machine["ingredients"]["milk"]}")
        print(f"Coffee: {coffee_machine["ingredients"]["coffee"]}")
        print(f"Profit: {coffee_machine["cost"]}")
    else:
        drink = MENU[choice]
        if check_availability(drink["ingredients"]):
            payment =float(input(f"{choice} is available. Please pay ${drink["cost"]}: "))
            if is_transaction_successful(payment,drink["cost"]):
                make_coffee(choice,drink["ingredients"])





 
