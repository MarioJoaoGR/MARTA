
import pytest
import os
import binascii
from string_utils.generation import secure_random_hex

def test_valid_input():
    # Test with a valid byte count
    result = secure_random_hex(9)
    assert isinstance(result, str), "The result should be a hexadecimal string"
    assert len(result) == 2 * 9, "The length of the hex string should be double the byte count"
    
    # Test with another valid byte count
    result = secure_random_hex(10)
    assert isinstance(result, str), "The result should be a hexadecimal string"
    assert len(result) == 2 * 10, "The length of the hex string should be double the byte count"
