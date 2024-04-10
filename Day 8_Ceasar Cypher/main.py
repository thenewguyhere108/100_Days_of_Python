from assets import letter_list, logo, clear
from time import sleep


def ceaser(word, number, direction):
    if number > 26:
        number = number % 26
    if direction == 'decrypt':
        number = number * -1
    word = word.lower()
    new_text = ""
    for letter in word:
        if direction == 'encrypt' and letter == ' ':
            new_letter = '*'
        if direction == 'decrypt' and letter == '*':
            new_letter = ' '
        elif str.isdigit(letter) or not str.isalpha(letter):
            new_letter = letter
        else:
            new_letter = letter_list[(letter_list.index(letter) + number)]
        new_text += new_letter
    return new_text


clear()
print(logo)
sleep(2)
while True:
    clear()
    print(logo)
    choice = input("Would you like to encrypt or decrypt text? ").lower()
    if choice == 'encrypt':
        word = input("Enter the text to encrypt :")
        number = int(input('Enter the shift number :'))
        word = ceaser(word, number, choice)
        print(f'The encrypted text is :{word}')
        sleep(2)
    elif choice == 'decrypt':
        word = input("Enter the text to decrypt :")
        number = int(input('Enter the shift number :'))
        word = ceaser(word, number, choice)
        print(f'The decrypted text is :{word}')
        sleep(2)
    choice = input('Enter yes to continue and no to quit ')
    if choice != 'yes' and choice != 'Yes':
        break
# By Sri Sandeep
