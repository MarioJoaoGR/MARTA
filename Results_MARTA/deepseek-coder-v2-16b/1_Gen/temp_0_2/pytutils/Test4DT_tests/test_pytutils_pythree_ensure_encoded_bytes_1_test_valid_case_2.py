
import pytest
from pytutils.pythree import ensure_encoded_bytes

def test_valid_case_2():
    # Test case where the input is a string that needs to be encoded
    result = ensure_encoded_bytes("привет", encoding='utf-8', errors='strict')
    assert isinstance(result, bytes)
    assert result == b'\xd0\xbf\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82'

    # Test case where the input is already a byte-like object
    input_bytes = b"world"
    result = ensure_encoded_bytes(input_bytes)
    assert isinstance(result, type(input_bytes))
    assert result == input_bytes
