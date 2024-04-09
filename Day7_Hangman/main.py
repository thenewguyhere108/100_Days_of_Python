from words import hangman, logo, words
from random import randint as rand
from os import system
from time import sleep

lives = 6
answer = words[rand(0, len(words) - 1)].lower()  # Create a random answer everytime the code is written
strips = ''
for element in answer:  # Create the strips aka _____ for the answer dynamically
    strips = strips + '_'
points = 0
Game_over = False
Result = ''
tried_letters = []


def replace_strip():  # This function replaces ___ in the strips with letters if it is found
    global strips
    strip_list = list(strips)
    for j in range(len(answer)):
        if choice == answer[j]:
            strip_list[j] = choice
    strips = ''.join([str(elem) for elem in strip_list])


def score():  # This function dynamically assigns value to the point variable tracking the number of letters in strips
    global points
    global strips
    points = 0
    for j in strips:
        if j != '_':
            points += 1


print(logo) 
sleep(0.5)
while not Game_over:  # This is our main while loop where the whole game runs ,
    system('cls | clear')
    if lives == 0:
        Result, Game_over = 'lost', True
        break
    if points == len(strips):
        Result, Game_over = 'won', False
        break
    print(logo)
    print(hangman[7-lives])  # This prints the ascii hangman art according to the players life
    print(strips)
    print(f"Guess the {len(answer)} letter word")
    if tried_letters:
        print('Tried Letters : ', end='')
        for i in tried_letters:
            print(i, '', end="")
        print('')
    choice = input('Enter a letter : ')
    choice = choice.lower()
    if choice in tried_letters:
        print("letter already tried, try again")
        sleep(2)
    elif len(choice) == 1 and choice.isalpha():
        tried_letters.append(choice)
        if choice in answer:
            replace_strip()
            score()
        else:
            lives -= 1
    else:
        print("Wrong input")
        sleep(2)        
if Result == 'won':  # Output to show if player has won
    print(logo)
    print(hangman[8])
    print(f'{answer} \nCongratulations! you {Result} the game')
    sleep(5)
if Result == 'lost':  # Output to show if player has lost
    print(hangman[7])
    print(answer)
    print(f'Game Over, you {Result} the game')
    sleep(5)
# By Sri Sandeep
