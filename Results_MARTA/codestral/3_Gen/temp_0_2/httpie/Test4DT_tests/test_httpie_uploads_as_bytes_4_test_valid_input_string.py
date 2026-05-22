
import pytest
from typing import Union

def as_bytes(data: Union[str, bytes]) -> bytes:
    if isinstance(data, str):
        return data.encode()
    else:
        return data

def test_valid_input_string():
    # Test with a valid string input
    result = as_bytes("hello")
    assert result == b'hello'
    
    # Test with a valid bytes input
    result = as_bytes(b"world")
    assert result == b"world"
