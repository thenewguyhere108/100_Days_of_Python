from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from art import logo, clear, sleep

coffee_maker = CoffeeMaker()
money = MoneyMachine()
menu = Menu()

while True:
    clear()
    print(logo)
    choice = input(f'What would you like to have? {menu.get_items()} : ').lower().strip()
    if choice == 'report':
        coffee_maker.report()
        money.report()
        sleep(5)
    elif choice == 'exit':
        break
    else:
        chosen_item = menu.find_drink(choice)
        if chosen_item == None:
            sleep(5)
        else:
            if coffee_maker.is_resource_sufficient(chosen_item):
                print(f'The drink costs {money.CURRENCY}{chosen_item.cost}')
                if money.make_payment(chosen_item.cost):
                    coffee_maker.make_coffee(chosen_item)
                sleep(5)
            else:
                sleep(5)