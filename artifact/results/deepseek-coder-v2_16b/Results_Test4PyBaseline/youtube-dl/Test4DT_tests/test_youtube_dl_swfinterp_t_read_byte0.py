
import pytest
from io import BytesIO
import socket
from youtube_dl.swfinterp import _read_byte

# Test reading a byte from a file object
def test_read_byte_from_file():
    with open('test.bin', 'wb') as f:
        f.write(b'\x1A')
    with open('test.bin', 'rb') as file:
        value = _read_byte(file)