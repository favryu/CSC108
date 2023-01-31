"""A simple checker for types of functions in mm_functions.py."""

from typing import Any, Dict, Union
import pytest
import checker_generic
import questionbot

FILENAME = 'questionbot.py'
PYTA_CONFIG = 'a1_pythonta.json'
TARGET_LEN = 79
SEP = '='

CONSTANTS = {'SEPARATOR': '|',
             'SPACE': ' ',
             'PERIOD': '.',
             'QUESTION_SYMBOL': '?',
             'EXCLAMATION_SYMBOL': '!',
             'HOMEWORK_KEYWORD': 'homework',
             'HELPING_VERBS':
                 '|have|has|had|should|would|could|might|may|will|is|am|are|was|be|do|does|did|',
             'CANADIAN_WORD_1': 'snow',
             'CANADIAN_WORD_2': 'ice',
             'CANADIAN_WORD_3': 'hockey',
             'QUESTION_KEYWORD_1': 'Will',
             'QUESTION_KEYWORD_2': 'Can',
             'HOMEWORK_RESPONSE': 'Homework is a meme.',
             'EXCLAMATION_RESPONSE': ' ate my homework.',
             'CANADIAN_RESPONSE': ', eh?',
             'QUESTION_RESPONSE_0A': 'Is ',
             'QUESTION_RESPONSE_0B': ' the homework topic?',
             'QUESTION_RESPONSE_1': 'The future is opaque.',
             'QUESTION_RESPONSE_2A': ' is as ',
             'QUESTION_RESPONSE_2B': ' does.',
             'QUESTION_RESPONSE_3A': 'Why do you say "',
             'QUESTION_RESPONSE_3B': '" and "',
             'QUESTION_RESPONSE_3C': '"?'}


class TestChecker:
    """Sanity checker for assignment functions."""

    def test_is_exclamation(self) -> None:
        """Function is_exclamation"""
        self._check(questionbot.is_exclamation,
                    ['Wow how nice!'], bool)

    def test_do_exclamation(self) -> None:
        """Function do_exclamation"""
        self._check(questionbot.do_exclamation,
                    ['Wow how nice!'], str)

    def test_contains_helping_verb(self) -> None:
        """Function contains_helping_verb"""
        self._check(questionbot.contains_helping_verb,
                    ['We are having lunch.'], bool)

    def test_do_helping_verb(self) -> None:
        """Function do_helping_verb"""
        self._check(questionbot.do_helping_verb,
                    ['We are having lunch.'], str)

    def test_is_canadian_question(self) -> None:
        """Function is_canadian_question"""
        self._check(questionbot.is_canadian_question,
                    ['Are things nice today?'], bool)

    def test_do_canadian_question(self) -> None:
        """Function do_canadian_question"""
        self._check(questionbot.do_canadian_question,
                    ['Are things nice today?'], str)

    def test_is_question(self) -> None:
        """Function is_question"""
        self._check(questionbot.is_question,
                    ['Are things nice today?'], bool)

    def test_do_question(self) -> None:
        """Function do_question"""
        self._check(questionbot.do_question,
                    ['Are things nice today?'], str)

    def test_is_question_exclamation(self) -> None:
        """Function is_question_exclamation"""
        self._check(questionbot.is_question_exclamation,
                    ['Oh really?!'], bool)

    def test_do_question_exclamation(self) -> None:
        """Function do_question_exclamation"""
        self._check(questionbot.do_question_exclamation,
                    ['Oh really?!'], str)

    def test_do_unmatched(self) -> None:
        """Function do_unmatched"""
        self._check(questionbot.do_unmatched,
                    [], str)

    def test_chat(self) -> None:
        """Function chat"""
        self._check(questionbot.chat,
                    ['Are things nice today?'], str)

    def _check(self, func: callable, args: list, ret_type: Union[type, tuple]) -> None:
        """Check that func called with arguments args returns a value of type
        ret_type. Display the progress and the result of the check.
        """
        print('\nChecking {}...'.format(func.__name__))
        result = checker_generic.type_check_simple(func, args, ret_type)
        assert result[0] is True, result[1]
        print('  check complete')

    def _check_constants(self, name2value: Dict[str, object], mod: Any) -> None:
        """Check that, for each (name, value) pair in name2value, the value of
        a variable named name in module mod is value.
        """

        for name, expected in name2value.items():
            actual = getattr(mod, name)
            msg = 'The value of constant {} should be {} but is {}.'.format(
                name, expected, actual)
            assert expected == actual, msg


print(''.center(TARGET_LEN, SEP))
print(' Start: checking coding style with PythonTA '.center(TARGET_LEN, SEP))
checker_generic.run_pyta(FILENAME, PYTA_CONFIG)
print(' End checking coding style with PythonTA '.center(TARGET_LEN, SEP))

print(' Start: checking type contracts '.center(TARGET_LEN, SEP))
pytest.main(['--show-capture', 'no', '--disable-warnings', '--tb=short',
             'a1_checker.py'])
print(' End checking type contracts '.center(TARGET_LEN, SEP))

print('\nScroll up to see ALL RESULTS:')
print('  - checking coding style with Python TA')
print('  - checking type contract\n')
