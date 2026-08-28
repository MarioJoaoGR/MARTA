
import os
import binascii
import pytest
from string_utils.generation import secure_random_hex

def test_valid_byte_count():
    byte_count = 9
    hex_string = secure_random_hex(byte_count)
    assert len(hex_string) == byte_count * 2, "Hex string length should be twice the byte count"

def test_edge_cases():
    # Test with minimum reasonable value
    byte_count_min = 1
    hex_string_min = secure_random_hex(byte_count_min)
    assert len(hex_string_min) == byte_count_min * 2, "Hex string length for min byte count should be correct"
    
    # Test with maximum reasonable value (example: 256 bytes)
    byte_count_max = 256
    hex_string_max = secure_random_hex(byte_count_max)
    assert len(hex_string_max) == byte_count_max * 2, "Hex string length for max byte count should be correct"

def test_invalid_byte_count():
    invalid_inputs = [-1, 0, 'string', None, 2.5]
    for input_value in invalid_inputs:
        with pytest.raises(ValueError):
            secure_random_hex(input_value)
