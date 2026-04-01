
import os
import binascii
import pytest

def secure_random_hex(byte_count: int) -> str:
    """
    Generates a random hexadecimal string using a secure low-level random generator (os.urandom).

    **Note**: Due to hex conversion, the length of the returned string will be exactly double the given `byte_count`.

    *Example:*

    >>> secure_random_hex(9) # Possible output: 'aac4cf1d1d87bd5036'

    :param byte_count: Number of random bytes to generate. This parameter must be an integer greater than or equal to 1.
    :type byte_count: int
    :raises ValueError: If `byte_count` is not a positive integer, the function raises a ValueError with the message 'byte_count must be >= 1'.
    :return: Hexadecimal string representation of generated random bytes.
    """
    if not isinstance(byte_count, int) or byte_count < 1:
        raise ValueError('byte_count must be >= 1')

    random_bytes = os.urandom(byte_count)
    hex_bytes = binascii.hexlify(random_bytes)
    hex_string = hex_bytes.decode()

    return hex_string

def test_valid_input():
    byte_count = 10
    result = secure_random_hex(byte_count)
    assert isinstance(result, str), "The function should return a string"
    assert len(result) == byte_count * 2, f"Expected length of {byte_count * 2}, but got {len(result)}"
