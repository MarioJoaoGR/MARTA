
import re
from string_utils.validation import InvalidInputError

# Assuming WORDS_COUNT_RE is defined somewhere in a module or imported correctly
WORDS_COUNT_RE = re.compile(r'\b\w+\b')

def words_count(input_string: str) -> int:
    """
    Returns the number of words contained into the given string.
    
    This method considers sequences of one or more letters and/or numbers as "words", ignoring punctuation and other non-alphanumeric characters. It is aware that a sequence of alphanumeric characters separated by punctuation can be considered a word.
    
    *Examples:*
    
    - For the string `'hello world'`, the function will return `2`.
    - For the string `'one,two,three.stop'`, the function will return `4`.
    
    :param input_string: The string to analyze for word count. This should be a sequence of letters and/or numbers with optional punctuation in between.
    :type input_string: str
    :return: The number of words identified in the input string based on the criteria described.
    """
    if not is_string(input_string):
        raise InvalidInputError(input_string)
    
    return len(WORDS_COUNT_RE.findall(input_string))

# Assuming this function exists and returns True if input is a string, otherwise False
def is_string(input_str: str) -> bool:
    return isinstance(input_str, str)

import pytest

@pytest.mark.parametrize("test_input, expected", [
    ('hello world', 2),
    ('one,two,three.stop', 4),
    ('! @ # % ... []', 0),  # Test with punctuation only string
    ('', 0),                 # Test empty string
    ('   ', 0),              # Test whitespace string
])
def test_valid_input_hello_world(test_input, expected):
    assert words_count(test_input) == expected
