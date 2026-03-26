
import pytest
import os
import binascii

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

def test_invalid_input():
    with pytest.raises(ValueError):
        secure_random_hex("invalid")  # Test string input
        secure_random_hex(0)           # Test zero as input
        secure_random_hex(-1)          # Test negative integer input
        secure_random_hex(3.5)         # Test float input
