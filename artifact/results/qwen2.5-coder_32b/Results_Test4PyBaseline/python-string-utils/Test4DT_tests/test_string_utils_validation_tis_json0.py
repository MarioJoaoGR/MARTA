# Module: string_utils.validation
import pytest
from string_utils.validation import is_json

def test_is_json_valid_json_strings():
    assert is_json('{"name": "Peter"}') == True
    assert is_json('[1, 2, 3]') == True
    assert is_json('{"key": "value", "number": 42}') == True
    assert is_json('{}') == True  # Empty object is valid JSON
    assert is_json('[]') == True  # Empty array is valid JSON

def test_is_json_invalid_json_strings():
    assert is_json('{nope}') == False
    assert is_json('["missing closing bracket")') == False
    assert is_json('just a string') == False

def test_is_json_non_string_inputs():
    assert is_json(None) == False
    assert is_json(12345) == False
    assert is_json([1, 2, 3]) == False
    assert is_json({}) == False
    assert is_json([]) == False

def test_is_json_empty_string():
    assert is_json('') == False
    assert is_json('   ') == False  # String with only spaces should be invalid

def test_is_json_malformed_json():
    assert is_json('{ "key": "value", }') == False  # Trailing comma in object
    assert is_json('[1, 2, 3,]') == False  # Trailing comma in array
