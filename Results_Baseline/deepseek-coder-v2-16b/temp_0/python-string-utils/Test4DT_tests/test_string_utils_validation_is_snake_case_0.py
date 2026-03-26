
import pytest
from string_utils.validation import is_snake_case

# Test cases for valid snake case strings
def test_valid_snake_case():
    assert is_snake_case('foo_bar') == True
    assert is_snake_case('foo_bar_baz') == True
    assert is_snake_case('foo123_bar456') == True

# Test cases for invalid snake case strings without separator
def test_invalid_without_separator():
    assert is_snake_case('foobar') == False
    assert is_snake_case('FooBar') == False  # Contains uppercase letters