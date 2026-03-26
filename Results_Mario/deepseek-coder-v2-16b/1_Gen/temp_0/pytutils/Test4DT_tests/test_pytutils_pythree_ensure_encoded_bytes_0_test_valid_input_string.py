
from pytutils.pythree import ensure_encoded_bytes

def test_valid_input_string():
    # Test case for valid input string
    result = ensure_encoded_bytes("hello")
    assert isinstance(result, bytes)
    assert result == b"hello"

    # Test case for already byte-like object
    result = ensure_encoded_bytes(b"world")
    assert isinstance(result, bytes)
    assert result == b"world"

    # Test case for string with specified encoding and error handling
    result = ensure_encoded_bytes("привет", encoding='utf-8', errors='ignore')
    assert isinstance(result, bytes)
    assert result == b'\xd0\xbf\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82'
