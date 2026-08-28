
import pytest
from string_utils.validation import is_snake_case

def is_full_string(input_string: str) -> bool:
    return isinstance(input_string, str) and len(input_string.strip()) > 0

# Test for valid snake case strings with default separator '_'
def test_valid_snake_case():
    assert is_snake_case('foo_bar_baz')

# Test for invalid snake case strings that do not contain any separators
def test_invalid_no_separator():
    assert not is_snake_case('foobarbaz')

# Test for valid snake case strings with custom separator '-'
def test_valid_snake_case_custom_separator():
    assert is_snake_case('foo-bar-baz', '-')

# Test for invalid snake case strings that start with a number
def test_invalid_starts_with_number():
    assert not is_snake_case('1foo_bar_baz')

# Test for invalid snake case strings that contain uppercase letters