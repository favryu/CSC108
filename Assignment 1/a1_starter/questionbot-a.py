"""CSC108/CSCA08: Winter 2023 -- Assignment 1: Question Bot

This code is provided solely for the personal and private use of
students taking the CSC108/CSCA08 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2023 Paul Gries, Sophia Huynh, Kaveh Mahdaviani, and Sadia Sharmin

====

This module has the code for a simple chatbot that rephrases questions
as statements and statements as questions.

Load the program into the Python shell by clicking the green triangle
in Wing101. Then you can chat as follows at the Python shell.

>>> chat('The dog ate my homework!')
'Homework is a meme.'
"""

# This tells Python to give us access to the functions in chat_utilities.py.
from chat_utilities import *

# Whether to run doctests. See the bottom of this file to see it in action.
DOCTEST_MODE = True

# Punctuation.
SEPARATOR = '|'
SPACE = ' '
PERIOD = '.'
QUESTION_SYMBOL = '?'
EXCLAMATION_SYMBOL = '!'

# Key terms.
HOMEWORK_KEYWORD = 'homework'

# A list of helping verbs.
HELPING_VERBS = '|have|has|had|should|would|could|might|may|will|' + \
                'is|am|are|was|be|do|does|did|'

# Special Canadian words.
CANADIAN_WORD_1 = 'snow'
CANADIAN_WORD_2 = 'ice'
CANADIAN_WORD_3 = 'hockey'

# Question words that start a sentence.
QUESTION_KEYWORD_1 = 'Will'
QUESTION_KEYWORD_2 = 'Can'

# Response fragments.
HOMEWORK_RESPONSE = 'Homework is a meme.'

EXCLAMATION_RESPONSE = ' ate my homework.'

CANADIAN_RESPONSE = ', eh?'

QUESTION_RESPONSE_0A = 'Is '
QUESTION_RESPONSE_0B = ' the homework topic?'

QUESTION_RESPONSE_1 = 'The future is opaque.'

QUESTION_RESPONSE_2A = ' is as '
QUESTION_RESPONSE_2B = ' does.'

QUESTION_RESPONSE_3A = 'Why do you say "'
QUESTION_RESPONSE_3B = '" and "'
QUESTION_RESPONSE_3C = '"?'

ALL_OTHER_RESPONSE = 'What do you mean?'
####################################
# TASK 1.1: Homework-related Inputs
# Complete the docstring examples below.
# You do not have to write any code for this task, but rather, read
# the code we have provided, understand it, and pay attention to our
# use of constants. You are expected to use constants accordingly, when
# appropriate, for the rest of the tasks.
####################################


def contains_homework(sentence: str) -> bool:
    """
    Return whether `sentence` contains the word 'homework', regardless of case.

    >>> contains_homework('The dog has eaten my Homework!')
    True
    >>> contains_homework('The dog has eaten my lunch!')
    False
    >>> contains_homework('The dog has eaten my hoMewOrK.')
    True
    """

    # Below, we are using the constant HOMEWORK_KEYWORD defined at the beginning
    # of this file, and the function get_lowercase_version which
    # we imported from chat_utilities.py
    return HOMEWORK_KEYWORD in get_lowercase_version(sentence)


def do_homework() -> str:
    """
    Return 'Homework is a meme.'

    >>> do_homework()
    'Homework is a meme.'
    """

    return HOMEWORK_RESPONSE


####################################
# TASK 2: Exclamations
####################################

def is_exclamation(sentence: str) -> bool:
    """
    Return True if `sentence` ends with a ! symbol, and False otherwise.
    
    Precondition: sentence is a properly-formed English sentence

    >>> is_exclamation('Test sentense with exclamation symbol!')
    True
    >>> is_exclamation('Test sentense with ?! symbol?!')
    True
    >>> is_exclamation('Test sentense without exclamation symbol.')
    False
    """
    
    return sentence[-1] == EXCLAMATION_SYMBOL


def do_exclamation(sentence: str) -> str:
    """
    Return the last word of sentense, capitalized, plus " ate my homework.".
    
    Precondition: sentence is a properly-formed English sentence and ends 
    with an exclamation symbol 
    
    >>> do_exclamation('Test sentense with exclamation symbol!')
    'Symbol ate my homework.'
    >>> do_exclamation('Come on!')
    'On ate my homework.'
    >>> do_exclamation('Test!')
    'Test ate my homework.'
    """
    
    return get_capitalized_word(get_last_word(sentence)) + EXCLAMATION_RESPONSE

####################################
# TASK 3: Helping Verbs
####################################

# The following helper function is already completed for you
# Do not add or change anything in this function


def is_helping_verb(word: str) -> bool:
    """
    Return whether word is a lowercase helping verb in HELPING_VERBS.
    Every word in HELPING_VERBS is surrounded by SEPARATOR characters,
    for example '|will|'.

    >>> is_helping_verb('do')
    True
    >>> is_helping_verb('i')
    False
    """

    return (SEPARATOR + word + SEPARATOR) in HELPING_VERBS


def contains_helping_verb(sentence: str) -> bool:
    """
    return True if sentence ends with a period and contains a lowercase helping 
    verb as its third word, and False otherwise. If there are less than three 
    words in the given sentence, return False.
    
    Precondition: sentence is a properly-formed English sentence
    
    >>> contains_helping_verb('The dog has eaten my notes.')
    True
    >>> contains_helping_verb('The big dog has eaten my notes.')
    False
    >>> contains_helping_verb('The dog.')
    False
    """
    
    if count_words(sentence) < 3 or sentence[-1] != PERIOD:
        return False
    return is_helping_verb(get_word(sentence, 2))


def do_helping_verb(sentence: str) -> str:
    """
    Return a question generated by moving the helping verb to the front
    
    Precondition: sentence is a properly-formed English sentence ends with a . 
    and the third word is a helping verb
    
    >>> do_helping_verb('The dog has eaten my notes.')
    'Has the dog eaten my notes?'
    >>> do_helping_verb('Poor Clara had slept through her test.')
    'Had poor Clara slept through her test?'
    >>> do_helping_verb('The computer is on a desk.')
    'Is the computer on a desk?'
    """
    
    helping_verb = get_word(sentence, 2)
    sentence = sentence.replace(SPACE + helping_verb, EMPTY_STRING, 1)
    return get_capitalized_word(helping_verb) + SPACE \
        + get_uncapitalized_word(sentence[:-1]) + QUESTION_SYMBOL

####################################
# TASK 4: Canadian
####################################


def is_canadian_question(sentence: str) -> bool:
    """
    Return True if sentence is a question (ends with a QUESTION_SYMBOL) and 
    contains at least one Canadian word (even as part of another word), 
    and False otherwise.
    
    Precondition: sentence is a properly-formed English sentence

    >>> is_canadian_question('Is it snowing the whole day?')
    True
    >>> is_canadian_question('Too many ice on the road.')
    False
    >>> is_canadian_question("Hockey is fun, isn't it?")
    False
    >>> is_canadian_question("Is hockey fun?")
    True
    """
    
    canadian_words = [CANADIAN_WORD_1, CANADIAN_WORD_2, CANADIAN_WORD_3]
    if sentence[-1] == QUESTION_SYMBOL:
        return any(x in sentence for x in canadian_words)
    return False


def do_canadian_question(sentence: str) -> str:
    """
    Return the same sentence back except that it should end with ', eh?'.
    
    Precondition: sentence is a properly-formed English sentence ends with a 
    QUESTION_SYMBOL and contains at least one Canadian word

    >>> do_canadian_question('Is it snowing the whole day?')
    'Is it snowing the whole day, eh?'
    >>> do_canadian_question('Too many ice on the road?')
    'Too many ice on the road, eh?'
    >>> do_canadian_question("Hockey is fun, isn't it?")
    "Hockey is fun, isn't it, eh?"
    >>> do_canadian_question("Is hockey fun?")
    'Is hockey fun, eh?'
    """
    return sentence[:-1] + CANADIAN_RESPONSE
    
####################################
# TASK 5: Questions
####################################


def is_question(sentence: str) -> bool:
    """
    Return True if sentence ends with a question mark.
    
    Precondition: sentence is a properly-formed English sentence

    >>> is_question('Where will you go?')
    True
    >>> is_question('I will go to Freshco tomorrow morning.')
    False
    >>> is_question("Hockey is fun, isn't it?")
    True
    """
        
    return sentence[-1] == QUESTION_SYMBOL


def do_question(sentence: str) -> str:
    """
    Return various value as follows depends on the sentence:
    1: If there is only one word in the argument, the returned response 
       should be ' Is ' followed by the lowercase version of the word followed 
       by ' the homework topic?';

    2: If the first word of the question is:
       Will, the response should be'The future is opaque.'
       Can, the response should be the last word of the sentence capitalized, 
            followed by is as, followed by the last word again, followed by 
            does. For example, Rain is as rain does. is a possible response.

    3: In all other cases:
       3.1: If the last word and second word are the same (ignoring case) the 
            response should be: Why do you say " followed by the second word 
            from the argument, followed by "?.
       3.2: If the last word and second word are different, the response should 
            be Why do you say " followed by the second word, then " and " 
            followed by the last word from the argument, followed by "?.
    
    Precondition: sentence is a properly-formed English sentence ends with a 
    question mark.
    
    >>> do_question("Yes! Do you think the pictures are awesome?")
    'Why do you say "Do" and "awesome"?'
    >>> do_question("Hungry?")
    'Is hungry the homework topic?'
    >>> do_question("Is raining dog go to raining?")
    'Why do you say "raining"?'
    >>> do_question("Will you help me with the cleaning?")
    'The future is opaque.'
    >>> do_question("Can a dog go to the gym?")
    'Gym is as gym does.'
    """
    first_word = get_first_word(sentence)
    last_word = get_last_word(sentence)
    if count_words(sentence) == 1:
        return QUESTION_RESPONSE_0A + get_lowercase_version(first_word) \
            + QUESTION_RESPONSE_0B
    if first_word == QUESTION_KEYWORD_1:
        return QUESTION_RESPONSE_1
    if first_word == QUESTION_KEYWORD_2:        
        return get_capitalized_word(last_word) + QUESTION_RESPONSE_2A \
            + last_word + QUESTION_RESPONSE_2B
    second_word = get_word(sentence, 1)
    if get_lowercase_version(second_word) == get_lowercase_version(last_word):
        return QUESTION_RESPONSE_3A + second_word + QUESTION_RESPONSE_3C
    else:
        return QUESTION_RESPONSE_3A + second_word + QUESTION_RESPONSE_3B \
            + last_word + QUESTION_RESPONSE_3C
    
####################################
# TASK 6: Question Exclamations
####################################


def is_question_exclamation(sentence: str) -> bool:
    """
    Return True if sentence ends with a question exclamation symbol,
           False otherwise.
    
    Precondition: sentence is a properly-formed English sentence

    >>> is_question_exclamation('Where will you go?!')
    True
    >>> is_question_exclamation('I will go to Freshco tomorrow morning!')
    False
    >>> is_question_exclamation("Hockey is fun, isn't it!?")
    False
    """
        
    return sentence[-2:] == QUESTION_SYMBOL + EXCLAMATION_SYMBOL


def do_question_exclamation(sentence: str) -> str:
    """
    Return same result as do_question() does by removing the end exclamation 
    symbol from the input argument sentence
    
    Precondition: sentence is a properly-formed English sentence end with a 
    question exclamation symbol.
    
    >>> do_question_exclamation('Where will you go?!')
    'Why do you say "will" and "go"?'
    >>> do_question_exclamation("Now?!")
    'Is now the homework topic?'
    
    """
    return do_question(sentence[:-1])
    
####################################
# TASK 8: None of the above
####################################


def do_unmatched() -> str:
    """
    return 'What do you mean?'
    
    >>> do_unmatched()
    'What do you mean?'
    """
    return ALL_OTHER_RESPONSE

####################################
# Chat Functionality
####################################


# TASK 7: Make sure the chat function has the correct order for all checks
def chat(sentence: str) -> str:
    """Return a question if `sentence` is a statement or exclamation, and
    return a statement if `sentence` is a question.

    >>> chat('The dog ate my homework!')
    'Homework is a meme.'
    >>> chat('The thing is due tomorrow!')
    'Tomorrow ate my homework.'
    >>> chat('The dog has eaten my shoe.')
    'Has the dog eaten my shoe?'
    >>> chat('You watching the hockey game?')
    'You watching the hockey game, eh?'
    >>> chat('How much wood could a woodchuck chuck?')
    'Why do you say "much" and "chuck"?'
    >>> chat("Yes! Don't you think the pictures are awesome?")
    'Why do you say "Don\\'t" and "awesome"?'
    >>> chat("Will you study for the midterm?!")
    'The future is opaque.'
    >>> chat("Can a dog go to the gym?!")
    'Gym is as gym does.'
    >>> chat('There is snow outside.')
    'What do you mean?'
    """

    if contains_homework(sentence):
        return do_homework()
    
    # 2: Input is a question exclamation (ends with ?!)
    if is_question_exclamation(sentence):
        return do_question_exclamation(sentence)    
    # 3: Input is an exclamation (ends with !)
    if is_exclamation(sentence):
        return do_exclamation(sentence)
    # 4: Input has a helping verb (these are: has, should, would, could, might, 
    #    may or will) as the third word
    if contains_helping_verb(sentence):
        return do_helping_verb(sentence)
    # 5: Input is a "Canadian question" (contains the word snow, ice or hockey, 
    #    and ends with ?)
    if is_canadian_question(sentence):
        return do_canadian_question(sentence)
    # 6: Input is a question (ends with ?)
    if is_question(sentence):
        return do_question(sentence)
    return do_unmatched()
    

if __name__ == '__main__':

    if DOCTEST_MODE:
        import doctest
        doctest.testmod()
