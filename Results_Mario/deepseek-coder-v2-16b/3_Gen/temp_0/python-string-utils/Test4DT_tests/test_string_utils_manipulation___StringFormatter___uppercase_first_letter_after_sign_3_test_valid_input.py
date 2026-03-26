
import pytest
from string_utils.manipulation import __StringFormatter

def test_valid_input():
    # Test with a valid input string
    formatter = __StringFormatter("hello world")
    assert formatter.input_string == "hello world"

    # Test with another valid input string
    formatter = __StringFormatter("uppercase me after the comma, here")
    assert formatter.input_string == "uppercase me after the comma, here"
