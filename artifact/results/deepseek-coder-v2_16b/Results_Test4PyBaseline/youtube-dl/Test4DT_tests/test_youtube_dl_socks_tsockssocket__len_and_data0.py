# Module: youtube_dl.socks
import pytest
from youtube_dl.socks import sockssocket

# Test cases for the `_len_and_data` function
def test__len_and_data():
    # Basic usage
    data = b'example'
    packed_data = sockssocket._len_and_data(data)
    assert packed_data == b'\x07example'

    # Using different data types
    data = "test string".encode('utf-8')
    packed_data = sockssocket._len_and_data(data)
    assert packed_data == b'\x0b' + b'test string'

    data = bytearray([1, 2, 3, 4])
    packed_data = sockssocket._len_and_data(data)
    assert packed_data == b'\x04' + bytearray([1, 2, 3, 4])

    # Edge cases
    data = b''
    packed_data = sockssocket._len_and_data(data)
    assert packed_data == b'\x00'

    data = b'a' * 128
    packed_data = sockssocket._len_and_data(data)
    assert packed_data == b'\x80' + b'a' * 128
