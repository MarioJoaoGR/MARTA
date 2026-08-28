
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

def test_encode_empty_string():
    assert _encode_json_type('') == ''

def test_encode_single_character_string():
    assert _encode_json_type('a') == 'a'

def test_encode_float():
    assert _encode_json_type(3.14) == 3.14

def test_encode_false_boolean():
    assert _encode_json_type(False) == False
