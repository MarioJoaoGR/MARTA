
import pytest
from dataclasses_json.core import _encode_overrides

# Mocking the _encode_json_type function for testing purposes
def mock_encode_json_type(value):
    if isinstance(value, dict):
        return f'"{str(value).replace(" ", "")}"'
    return value

@pytest.fixture(autouse=True)
def patch_encode_json_type(monkeypatch):
    monkeypatch.setattr('dataclasses_json.core._encode_json_type', mock_encode_json_type)

# Simple class to mimic the expected structure of overrides
class Override:
    def __init__(self, exclude=None, letter_case=None, encoder=None):
        self.exclude = exclude
        self.letter_case = letter_case
        self.encoder = encoder

def test_basic_usage_without_json_encoding():
    kvs = {'name': 'Alice', 'age': 30}
    overrides = {
        'name': Override(letter_case=str.upper),
        'age': Override(encoder=lambda x: f"{x} years old")
    }
    result = _encode_overrides(kvs, overrides)
    assert result == {'NAME': 'Alice', 'age': '30 years old'}

def test_usage_with_json_encoding():
    kvs = {'name': 'Bob', 'details': {'height': 5.9}}
    overrides = {
        'details': Override(encoder=lambda x: mock_encode_json_type(x))
    }
    result = _encode_overrides(kvs, overrides, encode_json=True)
    assert result == {'name': 'Bob', 'details': '"{\'height\':5.9}"'}

def test_excluding_a_key_based_on_value():
    kvs = {'name': 'Charlie', 'age': 25, 'status': 'active'}
    overrides = {
        'age': Override(exclude=lambda x: x < 30),
        'status': Override(letter_case=str.upper)
    }
    result = _encode_overrides(kvs, overrides)