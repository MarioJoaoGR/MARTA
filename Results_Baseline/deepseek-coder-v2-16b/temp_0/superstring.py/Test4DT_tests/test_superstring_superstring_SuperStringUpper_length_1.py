
import pytest
from superstring.superstring import SuperStringUpper

# Test initialization with a base string
def test_initialization():
    str_upper = SuperStringUpper("Hello World")
    assert isinstance(str_upper._base, str)  # Ensure _base is a string

# Test conversion to lowercase if length is greater than or equal to 10
def test_lower_when_length_greater_than_or_equal_to_10():
    str_upper = SuperStringUpper("Hello, World!")
    processed_str = str_upper.lower()