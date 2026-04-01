
import pytest
from pytutils.pythree import ensure_encoded_bytes

def test_valid_case_3():
    # Test case where the input is a string that needs to be encoded
    result = ensure_encoded_bytes("привет", encoding='utf-8', errors='strict')
    expected_output = b'\xd0\xbf\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82'
    assert result == expected_output
