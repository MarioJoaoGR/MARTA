
import pytest
from string_utils.validation import words_count, InvalidInputError

def is_string(obj):
    return isinstance(obj, str)

# Test for invalid input
def test_invalid_input():
    with pytest.raises(InvalidInputError):
        words_count(None)

# Test for valid string with expected word count
def test_valid_string_with_expected_word_count():
    assert words_count('hello world') == 2

# Test for valid string with punctuation and multiple words
def test_valid_string_with_punctuation_and_multiple_words():
    assert words_count('one,two,three.stop') == 4

# Test for empty string
def test_empty_string():
    assert words_count('') == 0

# Test for string with only punctuation and no letters or numbers
def test_string_with_only_punctuation():
    assert words_count('! @ # % ... []') == 0
