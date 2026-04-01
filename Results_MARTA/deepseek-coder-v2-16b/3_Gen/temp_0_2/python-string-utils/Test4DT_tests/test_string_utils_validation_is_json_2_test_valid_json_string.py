
import pytest
from string_utils.validation import is_json  # Assuming this is the correct import path for the function
import re

def test_valid_json_string():
    assert is_json('{"name": "Peter"}') == True
    assert is_json('[1, 2, 3]') == True
    assert is_json('{nope}') == False
    assert is_json(None) == False
    assert is_json('') == False
    assert is_json(' ') == False
