
import re
from string_utils.validation import words_count

def test_words_count_hello_world():
    assert words_count('hello world') == 2

def test_words_count_punctuation_no_spaces():
    assert words_count('one,two,three.stop') == 4

def test_words_count_only_punctuation():
    assert words_count('! @ # % ... []') == 0

def test_words_count_alphanumeric_with_underscore():
    assert words_count('abc123_def456') == 2

def test_words_count_numbers_separated_by_punctuation():
    assert words_count('1,2,3.4;5:6') == 6
