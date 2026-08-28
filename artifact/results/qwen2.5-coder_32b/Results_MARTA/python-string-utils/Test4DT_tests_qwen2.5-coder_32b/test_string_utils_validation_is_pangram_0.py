
import string
from string_utils.validation import is_pangram



def test_all_lowercase_pangram():
    assert is_pangram('the quick brown fox jumps over the lazy dog') == True

def test_non_pangram_with_spaces():
    assert is_pangram('hello world') == False

def test_non_pangram_without_spaces():
    assert is_pangram('helloworld') == False

def test_empty_string():
    assert is_pangram('') == False

def test_string_with_numbers():
    assert is_pangram('1234567890!@#$%^&*()') == False

def test_string_with_missing_letters():
    assert is_pangram('the quick brown fox jumps over the lazy cat') == False