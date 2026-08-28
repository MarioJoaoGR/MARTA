
import pytest
from string_utils.validation import is_camel_case

def test_is_camel_case_none():
    assert is_camel_case(None) is False

def test_is_camel_case_empty_string():
    assert is_camel_case('') is False

def test_is_camel_case_single_uppercase_letter():
    assert is_camel_case('A') is False

def test_is_camel_case_single_lowercase_letter():
    assert is_camel_case('a') is False

def test_is_camel_case_single_digit():
    assert is_camel_case('1') is False

def test_is_camel_case_lowercase_with_number():
    assert is_camel_case('a1') is False

def test_is_camel_case_uppercase_start():
    assert is_camel_case('Astring') is True

def test_is_camel_case_no_uppercase():
    assert is_camel_case('mystring') is False

def test_is_camel_case_valid_camel_case():
    assert is_camel_case('MyString') is True

def test_is_camel_case_with_numbers():
    assert is_camel_case('MyString123') is True

def test_is_camel_case_multiple_words():
    assert is_camel_case('ThisIsACamelCaseString') is True

def test_is_camel_case_invalid_starting_number():
    assert is_camel_case('1stString') is False

def test_is_camel_case_with_underscores():
    assert is_camel_case('this_is_not_camel_case') is False
