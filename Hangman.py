from random import randint
import time


def help_menu():
    print('\nThe goal of the game is to guess the word displayed. Players guess letters, and if they are contained in t'
          + 'he answer, they will be revealed.\nIf they are not contained in the answer, a body part of a man\nhanging '
          + 'will be drawn.\nPlayers may also attempt to guess the entire word to win.\nIf the word is incorrectly'
          + ' guessed or the entire man is drawn, the player loses.')
    print('Play this game with some friends for more fun!\n\n')
    time.sleep(4)


def credit():
    print('Wordle, among other word games, follows a basic word-guessing theme. Players will guess either a letter '
          + '(hangman) or word (Wordle), \nthen the machine will return a response of what was correct/incorrect. '
          + 'Games like these have become popular recently because of the pandemic and news media popularizing these'
          + 'basic games.\nOften, these games will have a form of restraint, usually word or letter limit. This '
          + 'often encourages competition and excitement as people race to get the highest \'score\'.')


def start(ans):
    guess = []
    hangman_parts = ['( )', '( )\n      |\n      |', '( )\n     /|\n      |', '( )\n     /|\\ \n      |',
                     '( )\n     /|\\ \n      |\n     /', '( )\n     /|\\ \n      |\n     / \\']
    fails = 0
    for index in range(len(ans) - 1):
        guess += '_'
    print(' '.join(guess))
    while '_' in guess and fails < 6:
        choice = input('Enter a letter: ')
        if len(choice) > 1:
            if choice + '\n' == ans:
                print('Wow! You guessed the word correctly! The answer was ' + ans)
            else:
                print('Oh no, you didn\'t guess the word correctly. The answer was ' + ans)
        elif choice not in ans:
            fails += 1
            hangman = hangman_parts[fails - 1]
            print('Oh no, letter not in phrase.\n     ' + hangman + '\n')
            exit()
        else:
            for index in range(len(ans)):
                if choice == ans[index]:
                    guess[index] = choice
            print(' '.join(guess))
    if fails == 5:
        print('Oh no, you lost! The answer was ' + ans)
        exit()
    else:
        print(fails)
        print('Nice job, the answer was ' + ans)
        exit()


words = open('words.txt', 'r')
options = words.readlines()
answer = options[randint(0, 152)]
print('Welcome to Hangman - Plants Edition!')
mode = input('Enter \'help\' for rules, \'credits\' for CER, and anything else to start the game. ')
print('\n  loading...\n')
time.sleep(2)
if mode == 'help':
    help_menu()
    time.sleep(1)
elif mode == 'credits':
    credit()
    time.sleep(1)
start(answer)
words.close()
exit()
