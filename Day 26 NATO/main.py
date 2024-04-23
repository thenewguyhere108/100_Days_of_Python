import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}
nato_dict[" "] = "SPACE"

while True:
    word = input('Enter the word you would like to convert to NATO Code: ')
    if word == "exit":
        break
    NATO_list = []
    for a in word:
        NATO_list.append(nato_dict[a.upper()])
    print(NATO_list)
