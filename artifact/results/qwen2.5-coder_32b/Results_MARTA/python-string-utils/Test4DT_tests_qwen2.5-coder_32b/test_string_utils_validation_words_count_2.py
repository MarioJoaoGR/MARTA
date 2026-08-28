
import pytest
from string_utils.validation import is_string, InvalidInputError
import re

# Assuming WORDS_COUNT_RE is defined somewhere in your module
WORDS_COUNT_RE = re.compile(r'\b\w+\b')

def words_count(input_string: str) -> int:
    """
    Returns the number of words contained into the given string.

    This method is smart, it does consider only sequence of one or more letter and/or numbers
    as "words", so a string like this: "! @ # % ... []" will return zero!
    Moreover it is aware of punctuation, so the count for a string like "one,two,three.stop"
    will be 4 not 1 (even if there are no spaces in the string).

    *Examples:*

    >>> words_count('hello world') # returns 2
    >>> words_count('one,two,three.stop') # returns 4

    :param input_string: String to check.
    :type input_string: str
    :return: Number of words.
    """
    if not is_string(input_string):
        raise InvalidInputError(input_string)

    return len(WORDS_COUNT_RE.findall(input_string))

def test_words_count_basic():
    assert words_count('hello world') == 2
    assert words_count('one,two,three.stop') == 4
    assert words_count('! @ # % ... []') == 0
