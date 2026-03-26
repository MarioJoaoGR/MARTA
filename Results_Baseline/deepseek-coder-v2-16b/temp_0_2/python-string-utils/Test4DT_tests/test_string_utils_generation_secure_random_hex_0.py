# Module: string_utils.generation
import pytest
import os
import binascii
from string_utils import secure_random_hex

# Test cases for secure_random_hex function
def test_secure_random_hex_valid():
    # Test with byte_count set to 9
    result = secure_random_hex(9)
    assert isinstance(result, str), "The result should be a string"
    assert len(result) == 2 * 9, f"Expected length of {2*9}, but got {len(result)}"

def test_secure_random_hex_invalid():
    # Test with invalid input (non-integer and negative integers)
    with pytest.raises(ValueError):
        secure_random_hex(-1)
    with pytest.raises(ValueError):
        secure_random_hex(0)
    with pytest.raises(ValueError):
        secure_random_hex(1.5)  # float, not allowed by the function's type hint

def test_secure_random_hex_edge():
    # Test with edge case of byte_count set to 1
    result = secure_random_hex(1)
    assert isinstance(result, str), "The result should be a string"
    assert len(result) == 2 * 1, f"Expected length of {2*1}, but got {len(result)}"
