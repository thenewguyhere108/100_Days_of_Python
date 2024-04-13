from data import clear, sleep, menu, resources, logo

temp_resources = {}
balance = 0.00
change = 0.00


def check_resources(coffe_type):
    global temp_resources
    result = True
    for i in menu[coffe_type]['ingredients']:
        if menu[coffe_type]['ingredients'][i] <= resources[i]:
            temp_resources[i] = (resources[i] - menu[coffe_type]['ingredients'][i])
        else:
            print(f'Sorry there is not enough {i}')
            sleep(5)
            result = False
            break
    if not result:
        return False
    elif result:
        return True


def payment(coffe_type):
    global change
    cost = menu[coffe_type]['cost']
    print(f'{coffe_type.title()} costs ${cost}')
    quarters = int(input("Enter the amount of quarters : "))
    dimes = int(input("Enter the amount of dimes : "))
    nickles = int(input("Enter the amount of nickles : "))
    pennies = int(input("Enter the amount of pennies : "))
    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    if total >= menu[coffe_type]['cost']:
        change = round(total - menu[coffe_type]['cost'], 2)
        return True                                       
    else:
        print('Not enough money , your amount is refunded')
        sleep(5)
        return False


def complete_order(coffe_type):
    global balance
    for i in temp_resources:
        resources[i] = temp_resources[i]
    balance += menu[coffe_type]['cost']
    if change != 0:
        print(f'Here is ${change} in change')
    print(f'Here is your {coffe_type.title()} ☕ !')
    print('Have a good day !')
    sleep(5)


def report():
    print(f"Water : {resources['water']}ml")
    print(f"Milk : {resources['milk']}ml")
    print(f"Coffee : {resources['coffee']}g")
    print(f"Money : ${balance}")


while True:
    clear()
    print(logo)
    choice = input('\n What coffe would you like to have ? espresso / latte / cappuccino : ').lower()
    if choice == 'espresso' or choice == 'latte' or choice == 'cappuccino':
        if check_resources(choice) and payment(choice):
            complete_order(choice)
    elif choice == 'report':
        report()
        sleep(5)
    elif choice == 'exit':
        break
    else:
        print('Invalid input, try again')
        sleep(5)
