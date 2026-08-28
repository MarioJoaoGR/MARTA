
import pytest
from string_utils.validation import is_email

# Test valid email
def test_valid_email():
    input_string = 'my.email@the-provider.com'
    assert is_email(input_string) == True, f"Expected {input_string} to be a valid email"

# Test invalid email starting with a dot
def test_invalid_start_with_dot():
    input_string = '.invalid@example.com'
    assert is_email(input_string) == False, f"Expected {input_string} to be an invalid email"

# Test invalid email containing multiple '@' signs
def test_invalid_multiple_ats():
    input_string = 'user@domain@example.com'
    assert is_email(input_string) == False, f"Expected {input_string} to be an invalid email"
