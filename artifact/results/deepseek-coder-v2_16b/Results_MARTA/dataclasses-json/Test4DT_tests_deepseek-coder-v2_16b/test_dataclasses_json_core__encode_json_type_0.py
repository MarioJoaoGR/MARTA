
import pytest
from dataclasses_json.core import _encode_json_type, Json, _ExtendedEncoder

def test_valid_inputs():
    # Test encoding an integer
    assert _encode_json_type(42) == 42
    
    # Test encoding a string
    assert _encode_json_type("hello") == "hello"
    
    # Test encoding a list
    assert _encode_json_type([1, 2, 3]) == [1, 2, 3]
    
    # Test encoding a dictionary
    assert _encode_json_type({"key": "value"}) == {"key": "value"}
    
    # Test encoding a float
    assert _encode_json_type(3.14) == 3.14
    
    # Test encoding a boolean
    assert _encode_json_type(True) is True

