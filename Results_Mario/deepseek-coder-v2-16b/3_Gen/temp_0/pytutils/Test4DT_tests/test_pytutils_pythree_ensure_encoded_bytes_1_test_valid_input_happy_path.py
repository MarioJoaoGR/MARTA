
import pytest
from pytutils.pythree import ensure_encoded_bytes

def test_valid_input_happy_path():
    # Test converting a string to bytes using default encoding and error handling
    assert ensure_encoded_bytes("hello") == b"hello"
    
    # Test returning the byte string as is since it's already a byte type
    assert ensure_encoded_bytes(b"world") == b"world"
    
    # Test converting a string to bytes with specified encoding and error handling
    assert ensure_encoded_bytes("привет", encoding='utf-8', errors='ignore') == b'\xd0\xbf\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82'
    
    # Test with a bytearray input, which should return it as is since it's already a byte-like type
    assert ensure_encoded_bytes(bytearray(b"hello")) == b"hello"
    
    # Test with a memoryview input, which should return it as is since it's already a byte-like type
    assert ensure_encoded_bytes(memoryview(b"hello")) == b"hello"
