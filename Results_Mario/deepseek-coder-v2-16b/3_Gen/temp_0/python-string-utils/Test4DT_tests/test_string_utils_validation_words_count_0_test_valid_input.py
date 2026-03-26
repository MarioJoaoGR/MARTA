
import pytest
from string_utils.validation import words_count, InvalidInputError

def test_valid_input():
    # Test with a simple string containing two words
    input_string = 'hello world'
    assert words_count(input_string) == 2

    # Test with a string containing punctuation and still should return the correct word count
    input_string = 'one,two,three.stop'
    assert words_count(input_string) == 4
