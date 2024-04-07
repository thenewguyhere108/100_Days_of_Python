print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."/` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You are at a cross road, where do you want to go?\n\tType 'Left' or 'right'")
choice = input().lower()
if choice == 'left':
    print("You've come to a lake.There is an island in the middle of the lake.")
    print("Type 'wait' to wait for the boat. Type 'swim' to swim across")
    choice = input().lower()
    if choice == 'swim':
        print('You were eaten alive by the crocodiles in the water. Game Over')
    elif choice == 'wait':
        print("You have successfully arrived at island unharmed.\nThere is a house with 3 doors.")
        print('One red, one yellow and one blue. Which color do you choose?')
        choice = input().lower()
        if choice == 'red':
            print('The room is full of fire , you were burned alive. Game Over')
        elif choice == 'blue':
            print("The room is full of snakes and you got bit and died. Game OVer")
        elif choice == 'yellow':
            print("Congratulations, You have found the long lost Treasure of the pirates")
else:
    print("You fell into a hole. Game Over")
