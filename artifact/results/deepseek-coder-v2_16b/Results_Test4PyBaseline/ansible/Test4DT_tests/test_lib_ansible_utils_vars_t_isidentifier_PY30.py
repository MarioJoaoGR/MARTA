# Module: ansible.utils.vars
import pytest
from ansible.utils.vars import _isidentifier_PY3
from six import string_types
import keyword

# Test cases for valid identifiers
def test_valid_identifier():
    assert _isidentifier_PY3("my_variable") == True

# Test cases for invalid identifiers starting with a digit
def test_invalid_starts_with_digit():
    assert _isidentifier_PY3("123abc") == False

# Test cases for invalid identifiers being Python keywords
def test_invalid_keyword():
    assert _isidentifier_PY3("if") == False

# Test cases for non-string input type
def test_non_string_input():
    assert _isidentifier_PY3(123) == False

# Additional test case to check if the function correctly handles strings with non-ASCII characters
def test_invalid_non_ascii():
    # Assuming 'é' is a non-ASCII character, this should return False
    assert _isidentifier_PY3("my_variableé") == False
