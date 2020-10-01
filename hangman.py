#Imports
import sys
import random

## use "in" command for .contains

#Variables defined
wordList = ["apple", "orange", "pear", "grape", "banana"]
guessNumber = 98989
randomWord = random.choice(wordList)
wordWord = []
wordWord[:] = randomWord
encryptedWord = [' _ '] * len(randomWord)
won = False

#mainscript
print("Welcome to Hangman!")

for i in range(guessNumber):
    if won == True:
        break
    a = True

    print("\n" + str(encryptedWord))

    #guessing loop for mistakes and syntax errors in input
    while a:
        if won == True:
            break
        guess = str(input("\nMake your letter guess: "))

        #killswitch
        if guess == "app.quit()":
            sys.exit()

        #checks if less than or greater than 1
        if len(guess) > 1 or len(guess) < 1:
            print("\nPlease enter a valid input")
        else:
            #Checks if not integer
            try:
                int(guess)
                print("\nEnter a letter, not a number")
            #Checks if correct
            except:
                if (guess in randomWord):
                    print(guess + " was correct!")
                    for i in range(len(wordWord)):
                        if (wordWord[i] == guess):
                            encryptedWord.pop(i)
                            encryptedWord.insert(i, guess)
                            if encryptedWord == wordWord:
                                print("You got the word!")
                                won = True

                    a = False
                else:
                    print("You got it wrong!")
                    a = False
