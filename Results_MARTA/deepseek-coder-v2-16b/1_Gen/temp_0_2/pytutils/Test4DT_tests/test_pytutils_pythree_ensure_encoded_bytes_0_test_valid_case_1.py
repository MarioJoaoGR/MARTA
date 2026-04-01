
import pytest
from pytutils.pythree import ensure_encoded_bytes

def test_valid_case_1():
    # Test case for converting a string to bytes using default 'utf-8' encoding and 'strict' errors
    result = ensure_encoded_bytes("hello")
    assert isinstance(result, bytes)
    assert result == b"hello"

    # Test case for returning the byte string as is since it's already in allowed type
    original_bytes = b"world"
    result = ensure_encoded_bytes(original_bytes)
    assert isinstance(result, bytes)
    assert result == original_bytes

    # Test case for converting a string to bytes using 'utf-8' and ignores errors
    result = ensure_encoded_bytes("привет", encoding='utf-8', errors='ignore')
    assert isinstance(result, bytes)
    assert result == b"\xd0\xbf\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82"
