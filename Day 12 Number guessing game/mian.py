from assets import logo, clear
from random import randint


while True:
    clear()
    print(logo)
    print('Welcome to the number guessing game !')
    print("I'm thinking of a number between 1 and 100")
    answer = randint(1,100)
    guess = 0 
    q = False
    while True:
        mode = input('Would you like to play easy or hard? ').lower()
        if mode == 'easy':
            chance = 10
            break
        if mode == 'hard':
            chance = 5
            break
        else:
            print('invalid input try again')
    while chance > 0 :
        print(f'You have {chance} chances remaining')
        guess = int(input('Enter your guess : '))
        if guess == answer:
            print(f'Congratulations , The number is {answer}')
            break
        elif guess > answer:
            print('Too high')
            chance -= 1
        elif guess < answer:
            print('Too low')
            chance -= 1
    if chance == 0:
        print('All chances lost')
    while True:
        again = input('Would you like to play again? y / n :').lower()
        if again == 'n':
            q = True
            break
        elif again == 'y':
            break
        else:
            print('Invalid input try again')
    if q:
        break
