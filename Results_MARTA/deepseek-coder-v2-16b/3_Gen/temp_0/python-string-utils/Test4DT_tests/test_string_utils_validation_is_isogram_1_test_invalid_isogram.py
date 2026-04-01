
import pytest
from string_utils.validation import is_isogram

def test_invalid_isogram():
    input_string = 'hello'
    assert not is_isogram(input_string), f"Expected {input_string} to be an invalid isogram"
