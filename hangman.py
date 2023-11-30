rules = print ("Welcome to Hangman! The rules are simple. I will choose a word, and you will guess the letters. You have 14 guesses. Are you ready? Good luck.")

import random

words = []

with open('sowpods.txt', 'r') as f:
  line = f.readline()
  words.append(line)
  while line: 
    line = f.readline()
    words.append(line)

word = random.choice(words)
word = list(word)
cleaned_word = []
for i in word:
    if i == word[-1]:
        break
    else:
        cleaned_word.append(i)
guessed = "_" * len(cleaned_word)
guessed = list(guessed)
listGuessed = []
letter = input("guess a letter: ").upper()
num_guesses = 14
while True:
    if letter in listGuessed:
        letter = ''
        print("Already guessed!")
    elif letter in cleaned_word:
        index = cleaned_word.index(letter)
        guessed[index] = letter
        cleaned_word[index] = '_'
    else:
        print(''.join(guessed))
        if letter != '':
            listGuessed.append(letter)
        letter = input("guess a letter: ").upper()
        num_guesses -= 1

    if '_' not in guessed:
        print(''.join(guessed))
        print ("You won!")
        exit()

    if num_guesses <= 0:
        print("Sorry you've lost!")
        exit()