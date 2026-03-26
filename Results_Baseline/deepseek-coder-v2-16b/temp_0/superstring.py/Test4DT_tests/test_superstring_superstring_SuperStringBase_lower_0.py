
import pytest
from superstring.superstring import SuperStringBase, SuperStringLower

# Test initialization of SuperStringLower with a valid base string
def test_init_with_valid_base():
    str_lower = SuperStringLower("Hello World")
    assert isinstance(str_lower._base, str), "The _base should be an instance of str"

# Test lower method with length less than SUPERSTRING_MINIMAL_LENGTH
def test_lower_method_with_short_string():
    short_str = SuperStringLower("hi")
    assert short_str.lower()._base == "hi", "Expected 'hi' but got {}".format(short_str.lower()._base)

# Test lower method with length greater than or equal to SUPERSTRING_MINIMAL_LENGTH
def test_lower_method_with_long_string():
    long_str = SuperStringLower("Hello World")