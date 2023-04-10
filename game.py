import random
import sys
from termcolor import colored


def print_menu():
    print("You have 6 attempts to guess a '5 letter' word!")
    print("1. Colour "+ colored("White", 'white')+ " means: the letter is not in the actual word and not in the right spot")
    print("2. Colour "+ colored("Yellow", 'yellow')+" means: the letter is in the actual word but not in the right spot")
    print("3. Colour "+ colored("Green", 'green')+" means: the letter is in the actual word and in the right spot")
    print("Type a 5 Letter word and hit enter once done! Good Luck :) \n")

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
            print(colored(char, 'yellow'), end="")
        else: # '*'
            print(colored(char, 'green'), end="")

print_menu()
play_again = ""
while play_again != "q":
    word = read_random_word() 
    for attempt in range(1, 7):
        guess = input().lower()
        #added some input validation
        while len(guess) != 5 or not guess.isalpha(): 
            print('Incorrect input. Try again !')
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
            print(f"Congrats! You got the wordle in {attempt} trials")
            break
        elif attempt == 6:
            print(f"Sorry, the wordle was.. {word}")
    play_again = input("Want to play again? Hit 'Enter' to play again 'or' Type q and press 'Enter' to exit.").lower()