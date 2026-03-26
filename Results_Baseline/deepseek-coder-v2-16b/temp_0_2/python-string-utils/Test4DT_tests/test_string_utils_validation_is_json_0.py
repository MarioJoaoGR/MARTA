# Module: string_utils.validation
import pytest
from string_utils.validation import is_json
import json

# Test cases for the is_json function
def test_is_json_valid_json():
    assert is_json('{"name": "Peter"}') == True
    assert is_json('[1, 2, 3]') == True

def test_is_json_invalid_json():
    assert is_json('{nope}') == False
    assert is_json('invalid json') == False

def test_is_json_non_string():
    assert is_json(None) == False
    assert is_json(123) == False
    assert is_json({}) == False

def test_is_json_empty_string():
    assert is_json('') == False

def test_is_json_whitespace_string():
    assert is_json(' ') == False

# Additional edge cases can be added to cover more scenarios
