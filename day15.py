
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def create_drink(drink:str, resources: dict):
    if drink in MENU.keys():
        for key, value in MENU[drink].items():
            for ingredient, quantity in value.items():
                if quantity > resources[ingredient]:
                    print(f"Sorry there is not enough {ingredient} for your {drink}")
                    prompt_user(resources=resources)
                else:
                    for ingredient, quantity in value.items():
                        resources[ingredient] -= quantity
                    if coin_check(drink) == True:
                        report(resources=resources)
                        prompt_user(resources=resources)
                        print(f"Here is your {drink}")
                    else:
                        print('Sorry, your funds are insufficient')
                        report(resources=resources)
                        prompt_user(resources=resources)
    else:
        print('\nSorry could not find that drink, please try again')
        prompt_user(resources=resources)

def coin_check(drink: str):
    drink_cost = MENU[drink]['cost']
    quarters = int(input('Please insert quarters: '))
    dimes = int(input('Please insert dimes: '))
    nickels = int(input('Please insert nickels: '))
    pennies = int(input('Please insert pennies: '))
    coin_total = (quarters * .25) + (dimes * .10) + (nickels * .05) + (pennies * .01)
    if coin_total >= drink_cost:
        print(f'Here is your {drink}! Your change is', coin_total - MENU[drink]['cost'])
        return True
    else:
        return False
    

def report(resources):
    print('Current resources: \nWater: ' + str(resources['water']) + '\nMilk: ' + str(resources['milk']) + '\nCoffee: ' + str(resources['coffee']))


def prompt_user(resources):
    drink = input('What would you like? (espresso/latte/cappuccino): ')
    #check user input
    if drink == 'off':
        print('\nPowering off')
        pass
    else:
        create_drink(drink, resources)

report(resources=resources)
prompt_user(resources=resources)