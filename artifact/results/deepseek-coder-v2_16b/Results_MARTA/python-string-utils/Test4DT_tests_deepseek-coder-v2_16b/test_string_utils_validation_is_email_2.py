
import pytest
from string_utils.validation import is_email

def test_valid_email():
    input_string = 'my.email@the-provider.com'
    assert is_email(input_string) == True, f"Expected valid email '{input_string}' to be recognized as valid."

def test_invalid_starts_with_dot():
    input_string = '.invalid@example.com'
    assert is_email(input_string) == False, f"Expected invalid email '{input_string}' to be recognized as invalid."

def test_invalid_multiple_ats():
    input_string = 'user@domain@example.com'
    assert is_email(input_string) == False, f"Expected invalid email '{input_string}' to be recognized as invalid."
