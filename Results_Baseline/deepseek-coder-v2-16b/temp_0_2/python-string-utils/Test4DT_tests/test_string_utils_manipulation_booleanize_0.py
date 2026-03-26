
# Module: string_utils.manipulation
import pytest
from string_utils.manipulation import booleanize
from unittest.mock import patch

# Test cases for the booleanize function
def test_basic_usage():
    assert booleanize("true") == True
    assert booleanize("YES") == True
    assert booleanize("nope") == False

def test_case_insensitivity():
    assert booleanize("true") == True
    assert booleanize("YES") == True
    assert booleanize("nope") == False

def test_empty_string():
    assert booleanize("") == False

# Edge case for non-string input to ensure error handling is working correctly
def test_invalid_input():
    from pytest import raises
    from string_utils.manipulation import InvalidInputError
    with pytest.raises(InvalidInputError):
        booleanize(123)
