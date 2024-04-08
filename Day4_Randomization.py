import random as ra

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("What do you choose? Type 0 for Rock , Type 1 for Paper, Type 2 for Scissors")
b = int(input())
if b > 3 or b < 0:
    print("You chose a wrong number. Game Over")
    exit()
a = [rock, paper, scissors]
print(a[b])
print('Computer Chose:')
choice = ra.randint(0, 2)
print(a[choice])
if b == choice:
    print("Game Draw")
elif b == 0 and choice == 2:
    print("You Win")
elif b == 1 and choice == 0:
    print("You Win")
elif b == 2 and choice == 1:
    print("You Win")
else:
    print("You Lose")
