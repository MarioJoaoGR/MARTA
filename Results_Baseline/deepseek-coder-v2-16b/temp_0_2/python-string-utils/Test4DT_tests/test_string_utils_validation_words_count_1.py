
# Module: string_utils.validation
import pytest
from string_utils.validation import words_count, InvalidInputError
import re

# Assuming WORDS_COUNT_RE is a predefined regular expression for counting words in the input string
WORDS_COUNT_RE = re.compile(r'\b\w+\b')

def test_words_count_simple_sentence():
    assert words_count('hello world') == 2

def test_words_count_with_punctuation():
    assert words_count('one,two,three.stop') == 4

def test_words_count_empty_string():
    assert words_count('') == 0

def test_words_count_only_punctuation():
    assert words_count('! @ # % ... []') == 0

# Test for non-string input, which should raise InvalidInputError
def test_words_count_non_string_input():
    with pytest.raises(InvalidInputError):
        words_count(None)

# Test for string with multiple spaces
def test_words_count_multiple_spaces():
    assert words_count('hello   world') == 2

# Test for string with mixed case letters
def test_words_count_mixed_case():
    assert words_count('Hello WORLD') == 2

# Test for string with numbers and punctuation
def test_words_count_numbers_and_punctuation():
    assert words_count('one1 two2 three3.stop') == 4

# Test for string with leading/trailing spaces
def test_words_count_spaces():
    assert words_count(' hello world ') == 2
