
import pytest
from dataclasses_json.core import _encode_json_type

def test_encode_none():
    assert _encode_json_type(None) == None

def test_encode_empty_list():
    assert _encode_json_type([]) == []

def test_encode_empty_dict():
    assert _encode_json_type({}) == {}

def test_encode_zero():
    assert _encode_json_type(0) == 0

def test_encode_negative_one():
    assert _encode_json_type(-1) == -1

def test_encode_positive_one():
    assert _encode_json_type(1) == 1

def test_encode_float():
    assert _encode_json_type(3.14) == 3.14

def test_encode_empty_string():
    assert _encode_json_type('') == ''

def test_encode_non_empty_string():
    assert _encode_json_type('non-empty string') == 'non-empty string'

def test_encode_list_of_various_types():
    input_data = [None, [], {}, 0, -1, 1, 3.14, '', 'non-empty string']
    expected_output = [None, [], {}, 0, -1, 1, 3.14, '', 'non-empty string']
    assert _encode_json_type(input_data) == expected_output

def test_encode_dict_of_various_types():
    input_data = {
        "none": None,
        "empty_list": [],
        "empty_dict": {},
        "zero": 0,
        "negative_one": -1,
        "positive_one": 1,
        "float": 3.14,
        "empty_string": '',
        "non_empty_string": 'non-empty string'
    }
    expected_output = {
        "none": None,
        "empty_list": [],
        "empty_dict": {},
        "zero": 0,
        "negative_one": -1,
        "positive_one": 1,
        "float": 3.14,
        "empty_string": '',
        "non_empty_string": 'non-empty string'
    }
    assert _encode_json_type(input_data) == expected_output
