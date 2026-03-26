
import pytest
from superstring.superstring import SuperStringLower

# Test initialization with a valid base string
def test_init_with_valid_base():
    str_lower = SuperStringLower("Hello World")
    assert isinstance(str_lower._base, str), "The _base should be an instance of str"

# Test character_at method with a valid index
def test_character_at_valid_index():
    str_lower = SuperStringLower("Hello World")