
import pytest
from ansible.utils.vars import _isidentifier_PY2

# Test cases for _isidentifier_PY2 function

def test_invalid_type():
    assert _isidentifier_PY2(123) == False, "Expected False when input is not a string"

def test_empty_string():
    assert _isidentifier_PY2("") == False, "Expected False for an empty string"

def test_reserved_keyword_in_python_2():
    assert _isidentifier_PY2("if") == False, "Expected False when identifier is a reserved keyword in Python 2"

def test_starts_with_digit():
    assert _isidentifier_PY2("1invalid") == False, "Expected False for an identifier starting with a digit"

def test_contains_special_character():
    assert _isidentifier_PY2("in#valid") == False, "Expected False when identifier contains a special character"

def test_valid_identifier():
    assert _isidentifier_PY2("valid_ident") == True, "Expected True for a valid identifier"

def test_valid_identifier_with_digits():
    assert _isidentifier_PY2("val1d_ident") == True, "Expected True for a valid identifier with digits"

def test_valid_identifier_with_underscore():
    assert _isidentifier_PY2("_valid_ident") == True, "Expected True for a valid identifier with an underscore"
