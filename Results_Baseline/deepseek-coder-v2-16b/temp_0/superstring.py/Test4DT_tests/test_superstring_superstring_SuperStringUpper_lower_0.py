
import pytest
from superstring.superstring import SuperStringUpper

# Test initialization with valid base string
def test_init_valid():
    str_upper = SuperStringUpper("Hello World")
    assert str_upper._base == "Hello World"

# Test lower method with uppercase string
def test_lower_uppercase():
    str_upper = SuperStringUpper("HELLO WORLD")
    result = str_upper.lower()