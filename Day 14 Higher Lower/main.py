from assets import logo, vs, clear, sleep
from game_data import data
from random import randint

def compare(A,B):
    if A['follower_count'] > B['follower_count']:
        return 0
    else:
        return 1


while True:
    score = 0
    clear()
    print(logo,'\n')
    A = data[randint(0,len(data)-1)]
    while True:
        while True:
            B = data[randint(0,len(data)-1)]
            if B != A:
                break
        if score >= 1:
            clear()
            print(logo)
            print(f'Your score is :{score}')
        print(f"Compare A: {A['name']}, {A['description']}, from {A['country']}")
        print(vs,'\n')
        print(f"Versus B: {B['name']}, {B['description']}, from {B['country']} \n")
        while True:
            choice = input("Who has more followers? A or B : ").lower()
            if choice != 'a' and choice !='b':
                print('Invalid input , try again')
            else:
                break
        result = compare(A,B)
        if ( result == 0 and choice == 'a' ) or (result == 1 and choice == 'b'):
            score += 1
            A = B 
        else:
            print(f'You lost , Your Score {score}')
            break
    choice = input('Press y to play again or any other key to quit').lower()
    if choice != 'y':
        break