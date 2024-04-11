from assets import logo, clear
from time import sleep


def calculate(operator, number1, number2):
    match operator:
        case '+':
            return number1 + number2
        case '-':
            return number1 - number2
        case '*':
            return number1 * number2
        case '/':
            return round(number1 / number2, 2)


n1, n2, op, result = 0, 0, '', 0

clear()
print(logo)
print('Welcome to the calculator !')
sleep(2)
n1 = float(input('Enter the number 1 : '))

while True:
    op = input('Enter the operator + , - , * , / : ')
    n2 = float(input('Enter the second number : '))
    result = calculate(op, n1, n2)
    print(f'{n1} {op} {n2} = {result}')
    choice = input(f'''press y to continue calculation with {result} or press n to do a different calculation '
                   f'\npress any other key to quit \n''')
    if choice == 'y':
        n1 = result
    elif choice == 'n':
        clear()
        n1 = float(input('Enter the number 1 : '))
    else:
        break

clear()
print('Thank you for using the calculator!')
sleep(2)
