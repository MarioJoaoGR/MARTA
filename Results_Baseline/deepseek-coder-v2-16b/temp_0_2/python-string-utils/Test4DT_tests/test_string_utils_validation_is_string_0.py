# Module: string_utils.validation
# Import the function from the module
from string_utils.validation import is_string

import pytest
from typing import Any

# Test cases for is_string function
def test_is_string_with_string():
    assert is_string('foo') == True

def test_is_string_with_integer():
    assert is_string(42) == False

def test_is_string_with_bytes():
    assert is_string(b'foo') == False

# Additional edge cases to consider:
def test_is_string_with_none():
    assert is_string(None) == False

def test_is_string_with_list():
    assert is_string([1, 2, 3]) == False

def test_is_string_with_dict():
    assert is_string({'key': 'value'}) == False
