
import pytest
from string_utils.validation import is_snake_case

def is_full_string(input_string: str) -> bool:
    return isinstance(input_string, str) and len(input_string.strip()) > 0

# Test for valid snake case strings with default separator '_'
def test_valid_snake_case():
    assert is_snake_case('foo_bar_baz') == True, "Expected True for string 'foo_bar_baz'"

# Test for invalid snake case strings with default separator '_'

# Test for invalid snake case strings with default separator '_' starting with a number
def test_invalid_starts_with_number():
    input_string = '1foo_bar_baz'
    assert is_snake_case(input_string) == False, f"Expected False for string starting with a number '{input_string}'"

# Test for valid snake case strings with custom separator '-'
def test_valid_snake_case_with_dash():
    assert is_snake_case('foo-bar-baz', '-') == True, "Expected True for string 'foo-bar-baz'"

# Test for invalid snake case strings with custom separator '-' containing uppercase letters