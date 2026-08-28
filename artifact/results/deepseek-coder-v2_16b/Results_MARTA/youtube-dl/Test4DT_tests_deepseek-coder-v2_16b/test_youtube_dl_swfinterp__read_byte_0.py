
import pytest
from youtube_dl.swfinterp import _read_byte, _read_bytes, compat_struct_unpack
import os



def test_valid_file():
    with open('test.bin', 'wb') as f:
        f.write(b'\x1A')  # Write a single byte to the file
    
    with open('test.bin', 'rb') as f:
        assert _read_byte(f) == 0x1A