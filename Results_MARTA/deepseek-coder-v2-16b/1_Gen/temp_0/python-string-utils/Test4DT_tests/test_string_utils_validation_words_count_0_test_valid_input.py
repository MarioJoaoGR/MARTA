
import pytest
from string_utils.validation import words_count, InvalidInputError

def test_valid_input():
    # Test with a simple string containing multiple words separated by spaces
    input_string = 'hello world'
    assert words_count(input_string) == 2

    # Test with a string containing punctuation and multiple words
    input_string = 'one,two,three.stop'
    assert words_count(input_string) == 4

    # Test with a string that should return zero because it contains only non-alphanumeric characters
    input_string = '! @ # % ... []'
    assert words_count(input_string) == 0
