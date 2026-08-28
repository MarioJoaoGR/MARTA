
import pytest
from string_utils.validation import is_snake_case

def is_full_string(input_string: str) -> bool:
    return isinstance(input_string, str) and len(input_string.strip()) > 0

# Test for invalid uppercase letters

# Test for valid snake case with only lowercase letters and digits

# Test for invalid starting with a number
def test_invalid_starting_with_number():
    assert not is_snake_case('1foo_bar_baz')

# Test for valid snake case with custom separator
def test_valid_custom_separator():
    assert is_snake_case('foo-bar-baz', '-')