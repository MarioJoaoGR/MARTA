
import pytest
from dataclasses_json.core import Json
from datetime import datetime

class _ExtendedEncoder:
    def default(self, obj):
        raise TypeError(f'Type {type(obj)} not serializable')

def _encode_json_type(value, default=_ExtendedEncoder().default):
    if isinstance(value, Json.__args__):  # type: ignore
        return value
    return default(value)

# Test function for standard input with native types
def test_happy_path():
    setup = {"key": "value", "number": 42, "is_active": True}
    result = _encode_json_type(setup)
    assert result == setup

# Test function for edge cases including None, empty lists, and boundary values
def test_edge_cases():
    setup = [None, [], {}, 0, -1, 1, '', 'a', 3.14]
    result = [_encode_json_type(item) for item in setup]
    assert result == setup

# Test function for invalid inputs and error handling with custom default encoder
def test_invalid_inputs():
    def encode_datetime(obj):
        raise TypeError(f'Type {type(obj)} not serializable')
    
    with pytest.raises(TypeError, match="Type <class 'datetime.datetime'> not serializable"):
        _encode_json_type(datetime.now(), default=encode_datetime)
