
import os
import binascii
import pytest

def secure_random_hex(byte_count: int) -> str:
    """
    Generates a random string using secure low level random generator (os.urandom).

    **Bear in mind**: due to hex conversion, the returned string will have a size that is exactly\
    the double of the given `byte_count`.

    *Example:*

    >>> secure_random_hex(9) # possible output: 'aac4cf1d1d87bd5036'

    :param byte_count: Number of random bytes to generate
    :type byte_count: int
    :return: Hexadecimal string representation of generated random bytes
    """
    if not isinstance(byte_count, int) or byte_count < 1:
        raise ValueError('byte_count must be >= 1')

    random_bytes = os.urandom(byte_count)
    hex_bytes = binascii.hexlify(random_bytes)
    hex_string = hex_bytes.decode()

    return hex_string

def test_valid_input():
    # Test with a valid byte count
    assert isinstance(secure_random_hex(1), str)  # Ensure the output is a string
    assert len(secure_random_hex(1)) == 2 * 1  # Ensure the length matches the expected hex length

    # Additional test to ensure it works with different byte counts
    for i in range(1, 10):
        hex_string = secure_random_hex(i)
        assert isinstance(hex_string, str), f"Expected a string but got {type(hex_string)} for byte count {i}"
        assert len(hex_string) == 2 * i, f"Expected length {2*i} but got {len(hex_string)} for byte count {i}"
