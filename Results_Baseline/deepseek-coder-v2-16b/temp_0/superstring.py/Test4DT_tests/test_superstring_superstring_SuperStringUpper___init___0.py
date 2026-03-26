
import pytest
from superstring.superstring import SuperStringUpper

# Test Case 1: Instantiating an Instance with a Base String
def test_instantiate_with_base():
    str_upper = SuperStringUpper("Hello World")
    assert str_upper._base == "Hello World"

# Test Case 2: Converting the Wrapped String to Lowercase
def test_convert_to_lowercase():
    str_upper = SuperStringUpper("Hello World")
    processed_str = str_upper.lower()