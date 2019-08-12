def isWordGuessed(secretWord, lettersGuessed):
    if len(lettersGuessed) == 0:
        return False
    else:      
        for k in lettersGuessed:
            if k in secretWord:
                if k == lettersGuessed[len(lettersGuessed)-1]:
                    return True
                else:
                    continue
            else:
                if k == lettersGuessed[len(lettersGuessed)-1]:
                    return False
                else:
                    continue
                
                
def getGuessedWord(secretWord, lettersGuessed):
    str = ''
    
    for k in secretWord:
        if k in lettersGuessed:
            str = str + k + ''
        else:
            str = str + '_' 
            
    return str


def getAvailableLetters(lettersGuessed):
    import string
    new_string = string.ascii_lowercase
    for k in lettersGuessed:
        if k in string.ascii_lowercase:
            new_string = new_string.replace(k, '')

    return new_string


def hangman(secretWord):
    print("Welcome to the game, Hangman!")
    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.')
    print('-------------')
    guess = []
    guessedWord = ''
    check = True
    i = 8
    while guessedWord != secretWord and i != 1:
        if not check:
            i -= 1    
            
        print('You have ' + str(i) + ' guesses left.')
        Availableletters = getAvailableLetters(guess)
        print("Available letters: " + str(Availableletters))
        x = input('Please guess a letter: ')  
        if x in guess:
            print("Oops! You've already guessed that letter: " + str(guessedWord))
        else: 
            guess.append(x)
            check = isWordGuessed(secretWord, guess)
            if check:
                guessedWord = getGuessedWord(secretWord, guess)
                print('Good guess: ' + str(guessedWord))
            else:
                print('Oops! That letter is not in my word: ' + str(getGuessedWord(secretWord, guess)))
                
        print('------------')
    
    if guessedWord == secretWord:
       print('Congratulations, you won!')     
    elif i == 1:
        print('Sorry, you ran out of guesses. The word was else.')
            
            