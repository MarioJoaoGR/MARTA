# Module: pytutils.rand
import pytest
import random
from pytutils.rand import rand_hex

# Test cases for rand_hex function
def test_rand_hex_default_length():
    """Test the default length of the hex string."""
    result = rand_hex()
    assert len(result) == 8, f"Expected length 8 but got {len(result)}"

def test_rand_hex_specified_length():
    """Test a specific length of the hex string."""
    length = 10
    result = rand_hex(length)
    assert len(result) == length, f"Expected length {length} but got {len(result)}"

def test_rand_hex_string():
    """Test if the generated hex string is a valid hex string."""
    length = 8
    result = rand_hex(length)
    try:
        int(result, 16)
    except ValueError:
        pytest.fail("Generated string is not a valid hex string.")

def test_rand_hex_different_lengths():
    """Test multiple lengths to ensure randomness and correctness."""
    length = 5
    result1 = rand_hex(length)
    result2 = rand_hex(length)
    assert result1 != result2, "Generated hex strings are the same for the same length."

def test_rand_hex_large_length():
    """Test a very large length to ensure performance and correctness."""
    length = 1000
    result = rand_hex(length)
    assert len(result) == length, f"Expected length {length} but got {len(result)}"
