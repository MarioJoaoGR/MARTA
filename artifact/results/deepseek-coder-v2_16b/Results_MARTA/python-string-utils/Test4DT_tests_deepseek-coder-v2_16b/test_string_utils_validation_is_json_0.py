
import pytest
import json
from string_utils.validation import is_json

def is_full_string(input_string: str) -> bool:
    return isinstance(input_string, str) and len(input_string.strip()) > 0

# Test for valid JSON strings (object or array)
def test_valid_json():
    assert is_json('{"name": "Peter"}') == True
    assert is_json('[1, 2, 3]') == True

# Test for invalid JSON strings
def test_invalid_json():
    assert is_json('{nope}') == False

# Test for non-string input which should raise TypeError