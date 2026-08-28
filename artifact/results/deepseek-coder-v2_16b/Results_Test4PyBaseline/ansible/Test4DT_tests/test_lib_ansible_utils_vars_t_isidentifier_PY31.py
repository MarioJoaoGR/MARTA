
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

# Test cases for invalid identifiers that are not strings or Python keywords
@pytest.mark.parametrize("ident", [None, True, False, 123, [], {}])
def test_invalid_types(ident):
    assert _isidentifier_PY3(ident) == False

# Test case to check if the function correctly handles strings that are valid identifiers but contain uppercase letters
def test_valid_identifier_with_uppercase():
    # 'MyVariable' is a valid identifier because it starts with an uppercase letter followed by lowercase and underscores
    assert _isidentifier_PY3("MyVariable") == True

# Test case to check if the function correctly handles empty strings
def test_empty_string():
    assert _isidentifier_PY3("") == False

# Test case to check if the function correctly handles special characters in identifiers
@pytest.mark.parametrize("ident", ["my-variable", "my variable", "my$variable"])
def test_special_characters(ident):
    # These should all be invalid identifiers
    assert _isidentifier_PY3(ident) == False
