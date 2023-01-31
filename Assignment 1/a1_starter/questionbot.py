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

    >>> contains_homework('The dog has eaten my lunch!')

    >>> contains_homework('The dog has eaten my hoMewOrK.')

    """

    # Below, we are using the constant HOMEWORK_KEYWORD defined at the beginning
    # of this file, and the function get_lowercase_version which
    # we imported from chat_utilities.py
    return HOMEWORK_KEYWORD in get_lowercase_version(sentence)


def do_homework() -> str:
    """
    Return 'Homework is a meme.'

    >>> do_homework()

    """

    return HOMEWORK_RESPONSE


####################################
# TASK 2: Exclamations
####################################

def is_exclamation():
    """

    """
    # TODO: complete this function.


def do_exclamation():
    """

    """
    # TODO: complete this function.


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


def contains_helping_verb():
    """

    """
    # TODO: complete this function.


def do_helping_verb():
    """

    """
    # TODO: complete this function.

####################################
# TASK 4: Canadian
####################################

# TODO: write functions is_canadian_question and do_canadian_question.


####################################
# TASK 5: Questions
####################################

# TODO: write functions is_question and do_question.


####################################
# TASK 6: Question Exclamations
####################################

# TODO: write functions is_question_exclamation and do_question_exclamation.


####################################
# TASK 8: None of the above
####################################

# TODO: write function do_unmatched.


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
    """

    if contains_homework(sentence):
        return do_homework()
    # TODO: write more here to handle other kinds of sentences.


if __name__ == '__main__':

    if DOCTEST_MODE:
        import doctest
        doctest.testmod()
