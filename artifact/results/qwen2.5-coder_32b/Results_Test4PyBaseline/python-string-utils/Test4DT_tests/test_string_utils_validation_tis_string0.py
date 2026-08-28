# Module: string_utils.validation
import pytest
from string_utils.validation import is_string

def test_is_string_with_string():
    assert is_string('hello') == True, "Should be True for a non-empty string"
    assert is_string('') == True, "Should be True for an empty string"

def test_is_string_with_non_string_types():
    assert is_string(123) == False, "Should be False for an integer"
    assert is_string([1, 2, 3]) == False, "Should be False for a list"
    assert is_string(b'binary') == False, "Should be False for bytes"
    assert is_string(3.14) == False, "Should be False for a float"
    assert is_string(None) == False, "Should be False for NoneType"

def test_is_string_with_other_objects():
    assert is_string({'key': 'value'}) == False, "Should be False for a dictionary"
    assert is_string(set([1, 2, 3])) == False, "Should be False for a set"
    assert is_string(tuple((1, 2, 3))) == False, "Should be False for a tuple"

def test_is_string_with_custom_objects():
    class CustomObject:
        pass
    obj = CustomObject()
    assert is_string(obj) == False, "Should be False for a custom object"
