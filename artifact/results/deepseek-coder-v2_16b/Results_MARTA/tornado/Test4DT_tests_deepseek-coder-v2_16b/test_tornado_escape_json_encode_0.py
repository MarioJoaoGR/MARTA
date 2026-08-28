
import pytest
import json
from tornado import escape

def test_json_encode_string():
    value = "This is a test string"
    result = escape.json_encode(value)
    assert isinstance(result, str), f"Expected str but got {type(result)}"
    assert result == json.dumps(value).replace("</", "<\\/"), "JSON encoding failed for string"

def test_json_encode_dict():
    value = {"key": "This is a test string"}
    result = escape.json_encode(value)
    assert isinstance(result, str), f"Expected str but got {type(result)}"
    expected_json = json.dumps(value).replace("</", "<\\/")
    assert result == expected_json, "JSON encoding failed for dictionary"

def test_json_encode_list():
    value = [1, 2, 3]
    result = escape.json_encode(value)
    assert isinstance(result, str), f"Expected str but got {type(result)}"
    expected_json = json.dumps(value).replace("</", "<\\/")
    assert result == expected_json, "JSON encoding failed for list"

def test_json_encode_int():
    value = 123
    result = escape.json_encode(value)
    assert isinstance(result, str), f"Expected str but got {type(result)}"
    expected_json = json.dumps(value).replace("</", "<\\/")
    assert result == expected_json, "JSON encoding failed for integer"

def test_json_encode_float():
    value = 123.45
    result = escape.json_encode(value)
    assert isinstance(result, str), f"Expected str but got {type(result)}"
    expected_json = json.dumps(value).replace("</", "<\\/")
    assert result == expected_json, "JSON encoding failed for float"

def test_json_encode_complex():
    value = {"num": 123, "str": "example", "nested": {"key": "value"}}
    result = escape.json_encode(value)
    assert isinstance(result, str), f"Expected str but got {type(result)}"
    expected_json = json.dumps(value).replace("</", "<\\/")
    assert result == expected_json, "JSON encoding failed for complex structure"
