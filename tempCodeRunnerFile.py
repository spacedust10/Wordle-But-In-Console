e letter is not in the actual word and not in the right spot")
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