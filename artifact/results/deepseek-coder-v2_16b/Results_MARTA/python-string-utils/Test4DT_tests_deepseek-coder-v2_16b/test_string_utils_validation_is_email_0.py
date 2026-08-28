
import pytest
from string_utils.validation import is_email

# Test for a valid email address
def test_valid_email():
    input_string = 'my.email@the-provider.com'
    assert is_email(input_string) == True, f"Expected True for '{input_string}', but got False"

# Test for an invalid email that starts with a dot
def test_invalid_start_with_dot():
    input_string = '.invalid@example.com'
    assert is_email(input_string) == False, f"Expected False for '{input_string}', but got True"

# Test for an invalid email with multiple '@' signs
def test_invalid_multiple_at_signs():
    input_string = 'user@domain@example.com'
    assert is_email(input_string) == False, f"Expected False for '{input_string}', but got True"
