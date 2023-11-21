rules = print ("Welcome to Hangman! The rules are simple. I will choose a word, and you will guess the letters. You have 14 guesses. Are you ready? Good luck.")

import random

words = []

with open('sowpods.txt', 'r') as f:
  line = f.readline()
  words.append(line)
  while line: 
    line = f.readline()
    words.append(line)

print(random.choice(words))

word = ("Wonderful")
guessed = "_" * len(word)
word = list(word)
guessed = list(guessed)
listGuessed = []
letter = input("guess a letter: ")
while True:
    if letter in listGuessed:
        letter = ''
        print("Already guessed!")
    elif letter in word:
        index = word.index(letter)
        guessed[index] = letter
        word[index] = '_'
    else:
        print(''.join(guessed))
        if letter != '':
            listGuessed.append(letter)
        letter = input("guess a letter: ")

    if '_' not in guessed:
        print ("You won!")
        break