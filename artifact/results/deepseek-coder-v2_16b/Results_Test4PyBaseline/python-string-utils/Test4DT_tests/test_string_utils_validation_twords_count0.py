# Module: string_utils.validation
import pytest
from string_utils.validation import words_count

# Test cases for the words_count function
def test_words_count_simple_sentence():
    assert words_count('hello world') == 2

def test_words_count_with_punctuation():
    assert words_count('one,two,three.stop') == 4

def test_words_count_empty_string():
    assert words_count('') == 0

def test_words_count_only_punctuation():
    assert words_count('! @ # % ... []') == 0

# Additional edge cases to consider:
def test_words_count_single_letter():
    assert words_count('a b c') == 3

def test_words_count_multiple_spaces():
    assert words_count('hello   world') == 2

def test_words_count_mixed_content():
    assert words_count('one, two; three: four.') == 4

# Test for case sensitivity
def test_words_count_case_sensitivity():
    assert words_count('Hello HELLO hello') == 3

# Test for numbers considered as words
def test_words_count_numbers_as_words():
    assert words_count('123 456 789') == 3

if __name__ == "__main__":
    pytest.main()
