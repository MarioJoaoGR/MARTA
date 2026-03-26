
# Module: superstring.superstring
# Import the function from the module
from superstring.superstring import SuperStringUpper
import pytest

# Test cases for the SuperStringUpper class
def test_init():
    ssu = SuperStringUpper("hello world")
    assert ssu._base == "hello world"

def test_upper_lowercase():
    ssu = SuperStringUpper("hello world")
    result = ssu.upper()