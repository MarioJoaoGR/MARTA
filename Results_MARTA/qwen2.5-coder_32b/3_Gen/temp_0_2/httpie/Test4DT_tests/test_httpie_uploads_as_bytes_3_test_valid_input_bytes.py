
import pytest
from typing import Union

def as_bytes(data: Union[str, bytes]) -> bytes:
    if isinstance(data, str):
        return data.encode()
    else:
        return data

def test_valid_input_bytes():
    # Test with a string input
    assert as_bytes("hello") == b"hello"
    
    # Test with a bytes input
    assert as_bytes(b"world") == b"world"
