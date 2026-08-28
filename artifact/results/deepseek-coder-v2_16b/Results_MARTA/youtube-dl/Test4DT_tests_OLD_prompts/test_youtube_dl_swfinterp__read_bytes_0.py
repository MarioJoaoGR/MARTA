
import pytest
from youtube_dl.swfinterp import _read_bytes

def test_valid_input():
    class ValidReader:
        def read(self, count):
            return b'a' * count
    
    reader = ValidReader()
    assert _read_bytes(5, reader) == b'aaaaa'

def test_zero_count():
    class ZeroCountReader:
        def read(self, count):
            return b''
    
    reader = ZeroCountReader()
    assert _read_bytes(0, reader) == b''

def test_negative_count():
    class NegativeCountReader:
        def read(self, count):
            return b'a' * count
    
    reader = NegativeCountReader()
    with pytest.raises(AssertionError):
        _read_bytes(-1, reader)
