
# Module: string_utils.validation
# test_string_utils.py
from string_utils.validation import words_count

def test_words_count_with_simple_string():
    assert words_count('hello world') == 2

def test_words_count_with_punctuation():
    assert words_count('one,two,three.stop') == 4

def test_words_count_with_no_words():
    assert words_count('! @ # % ... []') == 0

def test_words_count_with_empty_string():
    assert words_count('') == 0

def test_words_count_with_only_numbers():
    assert words_count('123 456 789') == 3

def test_words_count_with_mixed_characters():
    assert words_count('hello, world! this is a test.') == 6
