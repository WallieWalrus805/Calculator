from random import randint
from colorama import Fore, Back


guess = ''


def add_line(word):
    word += '\n'
    return word


guess_count = 0
guess_limit = 6
out_of_guesses = False
mod_guess = ''
print('Welcome to Python Wordle!')
print('This Wordle has the option to feature 5 letter words or 6 letter words.\nIt is highly recommended to choose 5 ' +
      'letters if you are new to this game.\n6 letter games may be limited in word choices.\n')
a = input('Enter \'help\' for help, and anything else to start game. ')
if a == 'help':
    print('Players will enter 5 or 6 letter words into the program, and it will spit out a response.\nThe edited word '
          + 'contains colors corresponding to which letters in the word are in the word,\nwhich letters are at the '
          + 'right place, and which letters are not in the word at all.\nThe user has 6 attempts to enter words, '
          + 'trying to guess the answer with hints from each guess.\nIf an invalid word is entered, invalid characters'
          + ' are entered, or the\nword is not the given length, the program will NOT count that as an attempt.\n')
try:
    length = int(input('Enter 5 or 6 for the corresponding length of words: '))
except ValueError:
    print('Invalid input, defaulting to 5 letter word')
    length = 5

if length == 5:
    i = open('Words_Bank_5.txt', 'r')
    choices = i.readlines()
    answer = choices[randint(0, 3012)]
elif length == 6:
    i = open('Words_Bank_6.txt', 'r')
    choices = i.readlines()
    answer = choices[randint(0, 999)]
else:
    print('Number not 5 or 6, defaulting to 5 letter word.')
    length = 5
    i = open('Words_Bank_5.txt', 'r')
    choices = i.readlines()
    answer = choices[randint(0, 3012)]
i.close()
while guess != answer and not out_of_guesses:
    guess = ''
    guess_valid = False
    if guess_count < guess_limit:
        # user input guess
        guess = input(Fore.RESET + Back.RESET + 'Enter guess: ')
        guess = guess.lower()
        # detection of numbers or special characters
        if any(c.isdigit() for c in guess):
            print(Back.LIGHTRED_EX + 'Uh oh! Number detected!')
        elif any(not c.isalnum() for c in guess):
            print(Back.LIGHTRED_EX + 'Uh oh! Can\'t use special characters!')
        elif len(guess) != length:
            print(Back.LIGHTRED_EX + 'Uh oh! Word not ' + str(length) + ' letters long!')
        else:
            # most frustrating part of the code, identifying words and gibberish
            guess = add_line(guess)
            if length == 5:
                i = open('Words_Bank_5.txt', 'r')
            else:
                i = open('Words_Bank_6.txt', 'r')
            word_bank = i.read()
            if guess in word_bank:
                guess_valid = True
            else:
                pass
            if guess_valid:
                # Ok good, the answer is a valid response without numbers or special characters
                guess_count += 1
                mod_guess = ''
                # modify guess for color coding
                for index in range(length):
                    if answer[index] == guess[index]:
                        mod_guess = (mod_guess + Fore.GREEN + guess[index])
                    elif guess[index] in answer:
                        mod_guess = (mod_guess + Fore.YELLOW + guess[index])
                    else:
                        mod_guess = (mod_guess + Fore.RED + guess[index])
                # shows user the correct, containing, and incorrect letters of the guess
                print(mod_guess)
            else:
                print(Back.LIGHTRED_EX + 'Word not found')
    else:
        out_of_guesses = True
if out_of_guesses:
    # The user failed, and the answer is revealed
    print(Fore.BLACK + Back.MAGENTA + "Out of guesses! The answer was " + answer)
elif guess_count == 1:
    # if the user is super lucky and gets the Wordle first try
    print(Fore.YELLOW + Back.CYAN + 'You win in 1 try, very lucky!')
else:
    # user gets to know how many tries it took to guess
    print(Fore.RED + Back.LIGHTGREEN_EX + 'You win in ' + str(guess_count) + ' tries!')
# credits, wish others would have contributed to this project
print(Fore.RESET + Back.RESET + 'Thank you for playing this edition of Wordle, made by Alexander Lee.')
i.close()
