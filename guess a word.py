rules = print ("Welcome to guess word! The rules are simple. I will choose a word, and you will guess the letters. You won't be limited to just a few guesses. Are you ready? Let's go.")

word = "awesome"
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