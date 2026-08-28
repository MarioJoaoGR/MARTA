
import pytest
import base64
from typing import Tuple, Union

_ByteString = Union[bytes, bytearray, memoryview]
_STR = str

def decode(
        data: _ByteString,
        errors: _STR = 'strict'
) -> Tuple[str, int]:
    """Convert the given ``data`` into base64 Characters.

    Args:
        data (bytes or bytearray or memoryview): Bytes to be converted
            to a string of base64 characters.
        errors (str or :obj:`~UserString`): Not used.  This argument exists
            to meet the interface requirements.  Any value given to this
            argument is ignored.

    Returns:
        str: of base64 Characters
        int: the number of the given ``data`` bytes consumed.
    """
    data_bytes = bytes(data)
    encoded_bytes = base64.b64encode(data_bytes)
    encoded_str = encoded_bytes.decode('utf-8')
    return encoded_str, len(data_bytes)

# Test cases for the decode function

def test_decode_with_bytes():
    result = decode(b'Hello, World!')
    assert isinstance(result[0], str), "Expected a base64 string"
    assert isinstance(result[1], int), "Expected an integer count of bytes consumed"
    assert result[0] == 'SGVsbG8sIFdvcmxkIQ==', "Unexpected base64 encoding result"
    assert result[1] == 13, "Unexpected number of bytes consumed"

def test_decode_with_bytearray():
    result = decode(bytearray(b'Hello, World!'))
    assert isinstance(result[0], str), "Expected a base64 string"
    assert isinstance(result[1], int), "Expected an integer count of bytes consumed"
    assert result[0] == 'SGVsbG8sIFdvcmxkIQ==', "Unexpected base64 encoding result"
    assert result[1] == 13, "Unexpected number of bytes consumed"

def test_decode_with_memoryview():
    data_bytes = b'Hello, World!'
    memview = memoryview(data_bytes)
    result = decode(memview)
    assert isinstance(result[0], str), "Expected a base64 string"
    assert isinstance(result[1], int), "Expected an integer count of bytes consumed"
    assert result[0] == 'SGVsbG8sIFdvcmxkIQ==', "Unexpected base64 encoding result"
    assert result[1] == 13, "Unexpected number of bytes consumed"

def test_decode_with_string():
    data_str = 'Hello, World!'
    result = decode(data_str.encode())
    assert isinstance(result[0], str), "Expected a base64 string"
    assert isinstance(result[1], int), "Expected an integer count of bytes consumed"
    assert result[0] == 'SGVsbG8sIFdvcmxkIQ==', "Unexpected base64 encoding result"
    assert result[1] == 13, "Unexpected number of bytes consumed"
