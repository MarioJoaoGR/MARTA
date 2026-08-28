
import pytest
from string_utils.validation import is_palindrome



def test_single_character_with_ignore_case_true():
    assert is_palindrome('A', ignore_case=True) == True


def test_simple_palindrome_with_ignore_case_true():
    assert is_palindrome('LoL', ignore_case=True) == True

def test_non_palindrome_string():
    assert is_palindrome('Hello') == False

def test_palindrome_with_numbers_ignoring_spaces():
    assert is_palindrome('123 21', ignore_spaces=True) == True

def test_palindrome_with_special_characters_ignoring_case():
    assert is_palindrome('Able was I ere I saw Elba!', ignore_case=True) == False


def test_empty_string():
    assert is_palindrome('') == False

def test_whitespace_only_string():
    assert is_palindrome('   ') == False


def test_mixed_case_palindrome_without_ignoring_case():
    assert is_palindrome('Racecar', ignore_case=False) == False

def test_mixed_case_palindrome_with_ignoring_case():
    assert is_palindrome('Racecar', ignore_case=True) == True