from assets import logo, clear
from time import sleep
auction_bids = {}


def new_bid():
    print('Welcome to the secret auction house!')
    name = input('Enter your name : ').lower().strip()
    if name in auction_bids:
        print("Name already present , price will be updated ")
    amount = int(input("Enter the amount of your bid : "))
    auction_bids[name] = amount
    print('Bid placed successfully!')
    sleep(2)


def winner():
    winner_name = ''
    winning_amount = 0
    for name, amount in auction_bids.items():
        if amount > winning_amount:
            winning_amount = amount
            winner_name = name
    print(f'Congratulations !!! \n The winner of the bid is {winner_name} with an amount of ₹{winning_amount}')


clear()
print(logo)
sleep(2)
while True:
    clear()
    print(logo)
    new_bid()
    clear()
    print(logo)
    choice = input('Is there any other bidder? : ').lower()
    if choice == 'no':
        winner()
        break


