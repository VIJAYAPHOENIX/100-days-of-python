menu = {
    "espresso":{
        "ingredients":{
            "water": 50,
            "coffee":18,
        },
        "cost":1.5
    },
    "latte":{
        "ingredients":{
            "water": 200,
            "milk": 150,
            "coffee":24,
        },
        "cost":2.5
    },
    "cappuccino":{
        "ingredients":{
            "water":250,
            "milk":100,
            "coffee":24,
        },
        "cost": 3.0,
    }
}

resources ={
    "water":500,
    "milk":300,
    "coffee":100,
    "cash":0
}

def coin_counter():
    print("please insert coins.")
    try:
        quarters = int(input("how many quarters?: "))
        dimes = int(input("how many dimes?: "))
        nickles = int(input("how many nickles?: "))
        pennies = int(input("how many pennies?: "))
    except ValueError:
        print("enter a valid input")
        return 0
    total = (quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01)
    return total

def change(total,pick):
    if total == menu[pick]["cost"] or total > menu[pick]["cost"]:
        remain = total -menu[pick]["cost"]
        return f"your change {remain} cents"
    else:
        return "insufficient amount" 

def coffee_mixer(pick):
    global resources
    cwater = menu[pick]['ingredients']['water']
    cmilk = menu[pick]['ingredients'].get('milk',0)
    ccoffee = menu[pick]['ingredients']['coffee']
    if resources['coffee'] >= ccoffee and  resources['milk'] >= cmilk and resources['water'] >= cwater:
        resources['water'] -= cwater
        resources['milk']-= cmilk
        resources['coffee'] -= ccoffee
        return True
    else:
        if resources['coffee'] < ccoffee:
            return "coffee out of stock"
        if resources['milk'] < cmilk:
            return "milk is low"
        if resources['water'] < cwater:
            return "water is low"

def reports():
    return resources

is_on = True
while is_on:
    choice = input("What would you like to have ? (espresso/latte/cappuccino) : ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(reports())
    elif choice in menu:
        coffee_status = coffee_mixer(choice)
        option = menu[choice]
        print(f"select coffee {option}")
        print(option['ingredients'])
        print(f"cost {option['cost']}")
        if coffee_status != True:
            print(coffee_status)
            continue

        amount = coin_counter()
        if amount ==0:
            print("invalid amount")
        else:
            print(amount)
            print(change(amount,choice))

        if coffee_status == True and amount >= menu[choice]['cost']:
            resources['cash'] += menu[choice]['cost']

