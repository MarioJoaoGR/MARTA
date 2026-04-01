
import re
from string_utils.validation import is_camel_case
import pytest

def test_valid_camel_case():
    # Test cases where the input should be considered camel case
    assert is_camel_case('myString')  # True
    assert is_camel_case('MyString123')  # True
    
    # Test cases where the input should not be considered camel case
    assert not is_camel_case('MYSTRING')  # False, no lowercase letters
    assert not is_camel_case('mystring')  # False, already in camel case
    assert not is_camel_case('123MyString')  # False, starts with a number
    assert not is_camel_case('my string')  # False, contains whitespace
    assert not is_camel_case('my-string')  # False, contains non-alphanumeric character
