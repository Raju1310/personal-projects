# resources:
water = 1000
milk = 500
coffee = 760
balance = 0

# variables:
cost = 0.0
paid = 0.0
flag = True
lst = "espresso/latte/cappuccino".split('/')
lst.append("off")
lst.append("report")
coin_type = {"Dime": 0.10, "Nickel": 0.50, "penny": 0.10, "quarter": 0.25}


def print_report():
    print(f"""
            Water: {water}ml
            Milk: {milk}ml
            Coffee: {coffee}g
            Money: ${balance}
""")


def process_change():
    global balance
    balance += paid
    change = paid - cost
    balance -= change
    print(f"Here is your change ${paid}")


def update_resources():
    global water, milk, coffee, balance
    if prompt == "espresso":
        water -= 50
        coffee -= 18
    elif prompt == "latte":
        water -= 200
        coffee -= 24
        milk -= 150
    elif prompt == "cappuccino":
        water -= 250
        coffee -= 24
        milk -= 100
    print(f"Here is your {prompt}")


def check_resources():
    global cost
    resource_flag = True
    string_to_print = "Sorry there is not enough "
    if prompt == "espresso":
        cost = 1.50
        if water < 50:
            string_to_print += "water "
            resource_flag = False
        if coffee < 18:
            string_to_print += "Coffee Powder "
            resource_flag = False

    elif prompt == "latte":
        cost = 2.50
        if water < 200:
            string_to_print += "water "
            resource_flag = False
        if coffee < 24:
            string_to_print += "Coffee Powder "
            resource_flag = False
        if milk < 150:
            string_to_print += "Milk "
            resource_flag = False

    elif prompt == "cappuccino":
        cost = 3.00
        if water < 250:
            string_to_print += "water "
            resource_flag = False
        if coffee < 24:
            string_to_print += "Coffee Powder "
            resource_flag = False
        if milk < 100:
            string_to_print += "Milk "
            resource_flag = False

    if resource_flag:
        return resource_flag
    print(string_to_print)


def check_transaction():
    global paid
    paid = 0.0
    for i in coin_type:
        paid += coin_type[i] * (float(input(f"how many {i}")))
    print(f"you paid {paid}")
    if paid >= cost:
        return True
    return False


while flag:
    prompt = input("What would you like? (espresso/latte/cappuccino):").lower()
    if prompt not in lst:
        print("Wrong input! try again...")
        continue
    if prompt == "off":
        print("Turning off...Thank You")
        flag = False
    elif prompt == "report":
        print_report()
    elif check_resources():
        if check_transaction():
            process_change()
            update_resources()
        else:
            print(f"Transaction failed, short of {cost-paid}")
