
import pytest
from ansible.module_utils.common.collections import is_iterable

# Test if a list is considered iterable
def test_valid_case_list():
    assert is_iterable([1, 2, 3]) == True

# Test if a string is considered iterable with include_strings=True
def test_valid_case_string():
    assert is_iterable("Hello, World!", include_strings=True) == True

# Test if an integer is not considered iterable
def test_invalid_case_int():
    assert is_iterable(123) == False
