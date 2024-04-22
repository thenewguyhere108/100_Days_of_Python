with open('./Input/Letters/starting_letter.txt') as file:
    text = file.read()

with open('./Input/Names/invited_names.txt') as file:
    names = file.readlines()

for i in range(len(names)):
    names[i] = names[i].strip()

for i in names:
    letter_text = text
    letter_text = letter_text.replace('[name]', i)
    i = i.replace(' ', '_')
    file_name = './Output/ReadyToSend/Letter_to_' + i
    with open(file_name, mode='w') as file:
        file.write(letter_text)

print('Mails Merged Successfully !')
