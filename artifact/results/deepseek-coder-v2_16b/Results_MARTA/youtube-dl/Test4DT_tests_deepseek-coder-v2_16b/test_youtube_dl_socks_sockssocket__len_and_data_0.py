
import pytest
from youtube_dl.socks import sockssocket

def test_len_and_data_with_bytes():
    data = b'example'
    packed_data = sockssocket._len_and_data(data)
    assert packed_data == b'\x07example'
