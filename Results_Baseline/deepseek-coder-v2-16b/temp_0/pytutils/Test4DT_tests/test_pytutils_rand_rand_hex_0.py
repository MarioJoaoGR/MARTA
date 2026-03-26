
import pytest
import random
from pytutils.rand import rand_hex

def test_rand_hex_default():
    result = rand_hex()
    assert len(result) == 8, "Default length should be 8"
    assert isinstance(result, str), "Result should be a string"

def test_rand_hex_specific_length():
    specific_length = 10
    result = rand_hex(specific_length)
    assert len(result) == specific_length, f"Length should be {specific_length}"
    assert isinstance(result, str), "Result should be a string"

def test_rand_hex_invalid_length():
    with pytest.raises(TypeError):
        rand_hex("string")  # Should raise TypeError as length must be an integer

def test_rand_hex_large_length():
    large_length = 100
    result = rand_hex(large_length)
    assert len(result) == large_length, f"Length should be {large_length}"
    assert isinstance(result, str), "Result should be a string"

def test_rand_hex_zero_length():
    zero_length = 0
    result = rand_hex(zero_length)