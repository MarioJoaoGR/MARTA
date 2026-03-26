
import pytest
from pytutils.pythree import ensure_encoded_bytes

def test_ensure_encoded_bytes():
    # Test case for converting a string to bytes using default encoding and error handling
    assert ensure_encoded_bytes("hello") == b"hello"
    
    # Test case for returning the byte string as is since it's already a byte type
    assert ensure_encoded_bytes(b"world") == b"world"
    
    # Test case for converting a string to bytes using specified encoding and error handling
    assert ensure_encoded_bytes("привет", encoding='utf-8', errors='ignore') == b"\xd0\xbf\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82"
    
    # Test case for handling invalid encoding and error handling
    with pytest.raises(UnicodeEncodeError):
        ensure_encoded_bytes("привет", encoding='ascii', errors='strict')
