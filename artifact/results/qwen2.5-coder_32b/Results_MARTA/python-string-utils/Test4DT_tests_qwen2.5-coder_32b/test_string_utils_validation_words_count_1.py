
import re
from string_utils.validation import words_count

# Define a regular expression pattern for finding words as per the function's logic
WORDS_COUNT_RE = re.compile(r'\b\w+\b')

def test_valid_case_simple_sentence():
    assert words_count('hello world') == 2

def test_valid_case_punctuation_without_spaces():
    assert words_count('one,two,three.stop') == 4

def test_valid_case_only_punctuation_and_symbols():
    assert words_count('! @ # % ... []') == 0

def test_valid_case_mixed_alphanumeric_with_underscore():
    assert words_count('abc123_def456') == 2

def test_valid_case_numbers_separated_by_punctuation():
    assert words_count('1,2,3.4;5:6') == 6


def test_valid_case_empty_string():
    assert words_count('') == 0

def test_valid_case_single_word():
    assert words_count('singleword') == 1

def test_valid_case_multiple_underscores():
    assert words_count('a__b__c') == 3