
import pytest
from string_utils.validation import is_snake_case

# Test cases for valid snake case strings
def test_valid_snake_case():
    assert is_snake_case('foo_bar_baz') == True, f"Expected True, but got False for 'foo_bar_baz'"
    assert is_snake_case('foo_123_bar') == True, f"Expected True, but got False for 'foo_123_bar'"  # Contains digits but not at the start