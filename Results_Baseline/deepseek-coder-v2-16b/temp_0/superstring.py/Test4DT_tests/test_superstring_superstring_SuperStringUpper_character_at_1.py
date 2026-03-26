
import pytest
from superstring.superstring import SuperStringUpper

# Test initialization of SuperStringUpper class
def test_init():
    str_upper = SuperStringUpper("Hello World")
    assert str_upper._base == "Hello World"

# Test character_at method with valid index
def test_character_at_valid_index():
    str_upper = SuperStringUpper("Hello World")