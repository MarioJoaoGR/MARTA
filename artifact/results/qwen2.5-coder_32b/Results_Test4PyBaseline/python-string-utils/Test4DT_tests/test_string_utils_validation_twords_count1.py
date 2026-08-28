
import pytest
from string_utils.validation import words_count, InvalidInputError

def test_words_count_empty_string():
    """Test words_count with an empty string."""
    assert words_count('') == 0

def test_words_count_punctuation_only():
    """Test words_count with a string containing only punctuation."""
    assert words_count('!@#$%^&*()') == 0

def test_words_count_mixed_alphanumeric_characters_and_punctuation():
    """Test words_count with mixed alphanumeric characters and punctuation."""
    assert words_count('example,string,with,punctuation123') == 4

def test_words_count_no_spaces():
    """Test words_count with no spaces between words."""
    assert words_count('onewordtwothreefour') == 1
    assert words_count('one,two,three,four') == 4

def test_words_count_with_numbers():
    """Test words_count with numbers as words."""
    assert words_count('123 456 789') == 3

def test_words_count_with_special_characters():
    """Test words_count with special characters."""
    assert words_count('hello-world!this_is,a_test') == 6

def test_words_count_invalid_input_non_string():
    """Test words_count with invalid input (non-string)."""
    with pytest.raises(InvalidInputError):
        words_count(None)

def test_words_count_invalid_input_integer():
    """Test words_count with invalid input (integer)."""
    with pytest.raises(InvalidInputError):
        words_count(12345)

def test_words_count_invalid_input_list():
    """Test words_count with invalid input (list)."""
    with pytest.raises(InvalidInputError):
        words_count(['hello', 'world'])

def test_words_count_invalid_input_dict():
    """Test words_count with invalid input (dict)."""
    with pytest.raises(InvalidInputError):
        words_count({'key': 'value'})

def test_words_count_invalid_input_float():
    """Test words_count with invalid input (float)."""
    with pytest.raises(InvalidInputError):
        words_count(123.456)

def test_words_count_invalid_input_boolean():
    """Test words_count with invalid input (boolean)."""
    with pytest.raises(InvalidInputError):
        words_count(True)
