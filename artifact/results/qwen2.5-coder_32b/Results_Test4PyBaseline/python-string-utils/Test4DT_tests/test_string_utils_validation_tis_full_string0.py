# Module: string_utils.validation
import pytest
from string_utils.validation import is_full_string

def test_is_full_string_non_string_inputs():
    assert is_full_string(None) == False
    assert is_full_string(123) == False
    assert is_full_string([]) == False
    assert is_full_string({}) == False
    assert is_full_string(3.14) == False

def test_is_full_string_empty_strings():
    assert is_full_string('') == False
    assert is_full_string(' ') == False
    assert is_full_string('   ') == False
    assert is_full_string('\t\n') == False

def test_is_full_string_valid_non_empty_strings():
    assert is_full_string('hello') == True
    assert is_full_string(' world ') == True
    assert is_full_string('123') == True
    assert is_full_string('!@#') == True
    assert is_full_string('a b c') == True

def test_is_full_string_mixed_cases():
    assert is_full_string('   hello   ') == True
    assert is_full_string('\tworld\n') == True
    assert is_full_string(' 123 ') == True
