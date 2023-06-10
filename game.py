import random
import sys
from colorama import just_fix_windows_console
from termcolor import colored, cprint

just_fix_windows_console()
def print_menu():
    cprint("You have 6 attempts to guess a '5 letter' word!")
    cprint("1. Colour "+ colored("White", 'white')+ " means: the letter is not in the actual word and not in the right spot")
    cprint("2. Colour "+ colored("Yellow", 'yellow')+" means: the letter is in the actual word but not in the right spot")
    cprint("3. Colour "+ colored("Green", 'green')+" means: the letter is in the actual word and in the right spot")
    cprint("Type a 5 Letter word and hit enter once done! Good Luck :) \n")

def read_random_word():
    with open("words.txt") as f:
        words = f.read().splitlines()
        return random.choice(words).lower()

def eval_attempt(a, s): # a - attempt, s - word  
    result = [' '] * 5 # result as list of chars
    '''
    encoding for list elements:  
        '*' - character. is correctly placed
        '+' - character. is in the word, but wrong place
        '_' - character. is not in the word
    '''
    temp_s = list(s)      # copy of s as list of chars
    temp_a = list(a)      # copy of a as list of chars
    # mark '*' chars
    for pos, char in enumerate(a):
        if char == s[pos]:
            result[pos] = '*'
            temp_a[pos] = '0'   # mark char as "checked"
            temp_s.remove(char) # remove from temp_s
    # mark '+'', '_' chars
    for pos, char in enumerate(temp_a):
        if char != '0':    #only check chars that are not already checked
            if char in temp_s:
                result[pos] = '+'
                temp_a[pos] = '0'
                temp_s.remove(char) # remove from temp_s
            else:
                result[pos] = '_'
    # print the attempt as colored chars 
    for pos, char in enumerate(a):
        if result[pos] == '_':
            print(char, end='')
        elif result[pos] == '+':
            cprint(colored(char, 'yellow'), end="")
        else: # '*'
            cprint(colored(char, 'green'), end="")

print_menu()
play_again = ""
while play_again != "q":
    word = read_random_word() 
    for attempt in range(1, 7):
        guess = input().lower()
        #added some input validation
        while len(guess) != 5 or not guess.isalpha(): 
            cprint('Incorrect input. Try again !', color='red', attrs=['bold', 'blink'])
            guess = input().lower()
        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')
        '''
        these two statements will move the cursor up one line 
        (if possible) and clear the line, 
        effectively overwriting any text that 
        was previously on that line.
        '''
        # new evaluation function
        eval_attempt(guess, word)
        print()
        if guess == word:
            cprint(f'Congrats! You got the wordle in {attempt} trials', color='green', attrs=['blink'])
            break
        elif attempt == 6:
            cprint('Sorry, the wordle was..', color='red')
            cprint(word, color='green', attrs=['bold'])
    play_again = input("Want to play again? Hit 'Enter' to play again 'or' Type q and press 'Enter' to exit.").lower()