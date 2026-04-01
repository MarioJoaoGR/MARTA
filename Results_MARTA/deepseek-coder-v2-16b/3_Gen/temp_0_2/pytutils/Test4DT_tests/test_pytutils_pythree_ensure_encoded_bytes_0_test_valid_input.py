
import pytest
from pytutils.pythree import ensure_encoded_bytes

def test_valid_input():
    # Test with a string which should be encoded to bytes
    assert ensure_encoded_bytes("Hello") == b'Hello'
    
    # Test with an already byte-like object (bytes)
    assert ensure_encoded_bytes(b"Hello") == b'Hello'
    
    # Test with a string and specifying a different encoding
    assert ensure_encoded_bytes("Hello", encoding="latin1") == b'Hello'
    
    # Test with a string and handling errors by ignoring them
    assert ensure_encoded_bytes("Hello", errors="ignore") == b'Hello'
