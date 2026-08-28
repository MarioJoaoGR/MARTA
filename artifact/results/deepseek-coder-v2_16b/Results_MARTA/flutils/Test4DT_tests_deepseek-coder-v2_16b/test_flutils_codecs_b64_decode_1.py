
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
    # Convert memoryview and bytearray objects to bytes.
    data_bytes = bytes(data)

    # Encode the 'data_bytes' into base64 bytes.
    encoded_bytes = base64.b64encode(data_bytes)

    # Decode the 'base64_bytes' as utf8 into a string.
    encoded_str = encoded_bytes.decode('utf-8')

    return encoded_str, len(data)

# Test cases for decode function

def test_empty_input():
    with pytest.raises(TypeError):
        decode()

def test_valid_input():
    data = b'Hello, World!'
    expected_output = ('SGVsbG8sIFdvcmxkIQ==', 13)
    result = decode(data)
    assert result == expected_output

def test_bytearray_input():
    data = bytearray(b'Hello, World!')
    expected_output = ('SGVsbG8sIFdvcmxkIQ==', 13)
    result = decode(data)
    assert result == expected_output

def test_memoryview_input():
    data = memoryview(b'Hello, World!')
    expected_output = ('SGVsbG8sIFdvcmxkIQ==', 13)
    result = decode(data)
    assert result == expected_output

def test_string_input():
    data = 'Hello, World!'
    expected_output = ('SGVsbG8sIFdvcmxkIQ==', 13)
    result = decode(data.encode())
    assert result == expected_output
