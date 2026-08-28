# Module: string_utils.generation
import pytest
from string_utils.generation import secure_random_hex

def test_secure_random_hex_valid_byte_counts():
    # Test with minimum valid byte count
    result = secure_random_hex(1)
    assert isinstance(result, str)
    assert len(result) == 2

    # Test with a typical byte count
    result = secure_random_hex(8)
    assert isinstance(result, str)
    assert len(result) == 16

    # Test with a larger byte count
    result = secure_random_hex(16)
    assert isinstance(result, str)
    assert len(result) == 32

def test_secure_random_hex_invalid_byte_counts():
    # Test with zero bytes (should raise ValueError)
    with pytest.raises(ValueError):
        secure_random_hex(0)

    # Test with negative byte count (should raise ValueError)
    with pytest.raises(ValueError):
        secure_random_hex(-1)

    # Test with non-integer byte count (should raise ValueError)
    with pytest.raises(ValueError):
        secure_random_hex(3.5)

    # Test with None as byte count (should raise ValueError)
    with pytest.raises(ValueError):
        secure_random_hex(None)

def test_secure_random_hex_output_format():
    # Test that the output is a valid hexadecimal string
    result = secure_random_hex(10)
    assert all(c in '0123456789abcdef' for c in result.lower())
