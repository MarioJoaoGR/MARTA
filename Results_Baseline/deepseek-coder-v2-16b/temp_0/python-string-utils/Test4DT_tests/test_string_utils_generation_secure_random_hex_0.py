# Module: string_utils.generation
import pytest
import os
import binascii
from string_utils import secure_random_hex

def test_secure_random_hex_valid():
    # Test with a valid byte count of 9
    result = secure_random_hex(9)
    assert isinstance(result, str), "The result should be a string"
    assert len(result) == 2 * 9, f"Expected length of {2*9}, but got {len(result)}"

def test_secure_random_hex_minimum():
    # Test with the minimum valid byte count of 1
    result = secure_random_hex(1)
    assert isinstance(result, str), "The result should be a string"
    assert len(result) == 2 * 1, f"Expected length of {2*1}, but got {len(result)}"

def test_secure_random_hex_invalid():
    # Test with an invalid byte count (should raise ValueError)
    with pytest.raises(ValueError):
        secure_random_hex(-5)

# Additional tests to cover different edge cases and potential failure points can be added here.
