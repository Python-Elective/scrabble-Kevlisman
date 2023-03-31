import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns the list of valid word from the word text
    """
    print("Loading word list from file...")
    # in_file: file
    in_file = open(WORDLIST_FILENAME, 'r')
    # word_list: list of strings
    word_list = []
    for line in in_file:
        word_list.append(line.strip().lower())
    print("  ", len(word_list), "words loaded.")
    return word_list

def get_frequency_dict(sequence):
    """
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#

def get_word_score(s, n):
    """
   return the score for the word input which is 's'
multiplied the score by the length and if requirement for n is used add 50 points
    """
    s = s.lower()
    score = 0
    for i in range(len(s)):
        score = score + SCRABBLE_LETTER_VALUES[s[i]] 
    score = score*len(s)
    if len(s) == n:
        score = score+50
    return(score)


def deal_hand(n):
    
    
    hand = {}
    num_vowels = n // 3

    for i in range(num_vowels):
        x = VOWELS[random.randrange(0, len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1

    for i in range(num_vowels, n):
        x = CONSONANTS[random.randrange(0, len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1

    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    try:
        assert type(hand)==dict,"hand must be dict"
        assert type(word)==str,"word must be str"
        new_hand = hand.copy()
        for i in word:
            new_hand[i] = new_hand[i] -1
        return(new_hand)

    except AssertionError as error:
        print(error)    
def display_hand(hand):
    """
    Displays the letters currently in the hand.
    For example:
    >>> display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.
    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
            print(letter, end=" ")       # print all on the same line
    print()                             # print an empty line

def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 
    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.
    Has no side effects: does not modify hand.
    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # Checking preconditions
    assert len(hand) > 0, "The hand is empty."
    assert len(word) > 0, "There was no input."
    assert type(word) == str, "The word must be a string"
    assert type(hand) == dict, "The hand must be a dictionary."
    assert word.islower() == True, "The word must be lower-case."
    # Updating the hand
    hand_copy = hand.copy()
    for letter in word:
        hand_copy[letter] -= 1
        if hand_copy[letter] == 0:
            del hand_copy[letter]
    # Check post-conditions
    assert hand_copy != hand, "The hand was changed together with the hand_copy."
    assert type(hand_copy) == dict, "The new hand is not a dictionary."
    return 

def is_valid_word(word, hand, word_list):
            """
            Returns True if word is in the word_list and is entirely
            composed of letters in the hand. Otherwise, returns False.

            Does not mutate hand or word_list.

            word: string
            hand: dictionary (string -> int)
            word_list: list of lowercase strings
            """
            try:
                assert type(hand)==dict,"hand must be dict"
                assert type(word)==str,"word must be str"
                new_hand = hand.copy()
                new_word_list = word_list.copy()
                word_letter_set = {letter: word.count(letter)  for letter in word}
                status = True
                
                if word in new_word_list:
                    for k in word_letter_set:
                        if k in new_hand and word_letter_set[k]<=new_hand[k] :
                            status = status
                        else:
                            status = False
                    if status == True:
                        return(True)
                    else:
                        return(False)
                else:
                    return(False)

            except AssertionError as error:
                print(error)
                def display_hand(hand):
             
                    for letter in hand.keys():
                        for j in range(hand[letter]):
                            print(letter, end=" ")       # print all on the same line
            print()                             # print an empty line

        #
        # Problem #2: Make sure you understand how this function works and what it does!
        #

def calculate_hand_len(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    hand: dictionary (string-> int)
    returns: integer
    """
    assert type(hand) == dict, "The hand must be a dictionary." 
    return sum(hand.values())
def play_hand(hand, word_list, n):
    """
    Allows the user to play the given hand, as follows:
    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."
      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    hand_copy = hand.copy()
    # Keep track of the total score
    total_score = 0
    # As long as there are still letters left in the hand:
    while True:
    # Display the hand
        print("Current hand: ", end=" ")
        display_hand(hand_copy)
    # Ask user for input
        word_input = input("Enter word, or a '.' to indicate that you are finished: ")
        while word_input == "":
            print("You have not inputted a word.")
            word_input = input("Enter word, or a '.' to indicate that you are finished: ")
    # If the input is a single period:
        if word_input == ".":
    # End the game (break out of the loop)
            print("Goodbye! Total score:", str(total_score), "points.")
            print("")
            break
    # Otherwise (the input is not a single period):
        else:
    # If the word is not valid:
            if is_valid_word(word_input, hand_copy, word_list) == False:
    # Reject invalid word (print a message followed by a blank line)
                print("Invalid word, please try again.")
                print("")
    # Otherwise (the word is valid):
            else:
    # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                score = get_word_score(word_input, n)
                total_score += score
                print("'" + word_input + "'", "earned", str(score), "points. Total:", str(total_score), "points")
                print("")
    # Update the hand
                hand_copy = update_hand(hand_copy, word_input)
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
        if calculate_hand_len(hand_copy) == 0:
            print("Run out of letters.", "Total Score:", str(total_score), "points.")
            print("")
            break

#
# Problem #5: Playing a game
#

def play_game(word_list):
    """
    Allow the user to play an arbitrary number of hands.
    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
    2) When done playing the hand, repeat from step 1    
    """
    # TO DO ... <-- Remove this comment when you code this function
    # <-- Remove this line when you code the function
    hand = {}
    while True:
        input_letter = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        if input_letter == "n":
            hand = deal_hand(8)
            play_hand(hand, word_list, 8)
        elif input_letter == "r":
            if hand == {}:
                print("You have not played a hand yet. Please play a new hand first!")
                print("")
            else:
                play_hand(hand, word_list, 8)
        elif input_letter == "e":
            break
        else:
            print("Invalid command.")

#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
