
import pytest
import json
from unittest.mock import patch
from tornado.escape import json_encode

def test_json_encode_string():
    value = "test string"
    encoded_value = json_encode(value)
    assert isinstance(encoded_value, str), "Expected a JSON string representation of the input Python object."
    try:
        json.loads(encoded_value)  # This should not raise an error if the encoding is correct
    except ValueError as e:
        pytest.fail(f"Encoding failed with error: {e}")

def test_json_encode_dict():
    value = {"key": "value", "script": "<script>alert('danger!');</script>"}
    encoded_value = json_encode(value)
    assert isinstance(encoded_value, str), "Expected a JSON string representation of the input Python object."
    try:
        json.loads(encoded_value)  # This should not raise an error if the encoding is correct
    except ValueError as e:
        pytest.fail(f"Encoding failed with error: {e}")

def test_json_encode_list():
    value = [1, 2, 3]
    encoded_value = json_encode(value)
    assert isinstance(encoded_value, str), "Expected a JSON string representation of the input Python object."
    try:
        json.loads(encoded_value)  # This should not raise an error if the encoding is correct
    except ValueError as e:
        pytest.fail(f"Encoding failed with error: {e}")

def test_json_encode_int():
    value = 123
    encoded_value = json_encode(value)
    assert isinstance(encoded_value, str), "Expected a JSON string representation of the input Python object."
    try:
        json.loads(encoded_value)  # This should not raise an error if the encoding is correct
    except ValueError as e:
        pytest.fail(f"Encoding failed with error: {e}")

def test_json_encode_float():
    value = 123.45
    encoded_value = json_encode(value)
    assert isinstance(encoded_value, str), "Expected a JSON string representation of the input Python object."
    try:
        json.loads(encoded_value)  # This should not raise an error if the encoding is correct
    except ValueError as e:
        pytest.fail(f"Encoding failed with error: {e}")

def test_json_encode_complex():
    value = {"num": 1, "str": "example", "nested": {"key": "value"}}
    encoded_value = json_encode(value)
    assert isinstance(encoded_value, str), "Expected a JSON string representation of the input Python object."
    try:
        json.loads(encoded_value)  # This should not raise an error if the encoding is correct
    except ValueError as e:
        pytest.fail(f"Encoding failed with error: {e}")
