
import pytest
from string_utils.validation import is_snake_case

# Test valid snake case input
def test_valid_snake_case():
    assert is_snake_case('foo_bar_baz') == True

# Test invalid characters (uppercase letters and spaces)

# Test input starting with a number
def test_starts_with_number():
    assert is_snake_case('1foo_bar_baz') == False

# Test input without any separator
def test_no_separator():
    assert is_snake_case('foobarbaz') == False