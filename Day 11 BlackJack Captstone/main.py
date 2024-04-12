from random import randint
from assets import cards, clear, sleep, logo

player_points, computer_points = 0, 0
Game_over = False

def initial_deal ():
    global player_cards, computer_cards,Game_over
    player_cards, computer_cards = [], []
    while len(player_cards) < 2:
        player_cards.append(cards[randint(0,13)])
        computer_cards.append(cards[randint(0,13)])    
    if sum(computer_cards) ==  21:
        if sum(player_cards) == 21:
            print('Both players have blackjack, Game Draw')
            Game_over = True
        else :
            print('Computer has blackjack, Computer Wins')
            Game_over = True


def calculate_score():
    global player_points, computer_points, Game_over
    player_points = sum(player_cards)
    computer_points = sum(computer_cards)
    if 11 in player_cards and player_points > 21:
        player_points -= 10
    if 11 in computer_cards and computer_points > 21:
        computer_points -= 10
    if player_points > 21 or computer_points > 21:
        Game_over = True


def deal_card(cards_list):
    cards_list.append(cards[randint(0,13)])
    calculate_score()
    return cards_list

def computer_choice():
    while sum(computer_cards) < 16:
        deal_card(computer_cards)

def winner():
    global Game_over
    winner = False
    if player_points > 21:
        print('You went over')
        winner = 'computer'
    elif computer_points > 21:
        print('Computer went over')
        winner = 'player'
    elif player_points > computer_points:
        winner = 'player'
    elif computer_points > player_points:
        winner = 'computer'
    elif player_points == computer_points:
        winner = 'draw'

    if winner == 'player':
        print('You Won 😁!!')
    if winner == 'computer':
        print('You Lost 😭!!')
    if winner == 'draw':
        print("It's a draw 😑")
    print(f'Your Cards : {player_cards} Points : {player_points}')
    print(f"Computer's cards {computer_cards} Points : {computer_points}")


def display_scores():
    print(f'Your Cards : {player_cards} Points : {player_points}')
    if not Game_over:
        print(f'Computer first card [{computer_cards[0]}]')
    else:
        print(f'Computer cards :[{computer_cards} Points : {computer_points}]')

def draw_card():
    choice = 'y'
    global Game_over
    while choice == 'y' and Game_over == False:
        choice = input('Would you like to draw a card? y / n :')
        if choice == 'y':
            deal_card(player_cards)
            computer_choice()
            calculate_score()
            display_scores()
        elif choice == 'n':
            computer_choice()
            calculate_score()
            Game_over = True
        else:
            print('Invalid input')
            choice = 'y'


while True:
    Game_over = False
    clear()
    print(logo)
    choice = input('Would you like to play a game a BlackJack? y / n : ').lower()
    if choice == 'n':
        break
    elif choice == 'y':
        initial_deal()
        calculate_score()
        display_scores()
        if not Game_over:
            while Game_over == False:
                draw_card()
            winner()
    choice = input('Would you like to play another game ? y / n : ').lower()
    if choice == 'n':
        break
    else:
        continue