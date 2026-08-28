
import pytest
from io import BytesIO
from youtube_dl.swfinterp import _read_string, _u30, _read_int




def test__u30_invalid():
    # Example data: invalid 30-bit length (MSB not set)
    data = b'\x81\x82\x83\x84' + b''
    reader = BytesIO(data)
    
    with pytest.raises(AssertionError):
        _u30(reader)


def test__read_int_invalid():
    # Example data: invalid byte sequence (not enough bytes to read an integer)
    data = b'\x81\x82\x83'
    reader = BytesIO(data)
    
    with pytest.raises(AssertionError):
        _read_int(reader)