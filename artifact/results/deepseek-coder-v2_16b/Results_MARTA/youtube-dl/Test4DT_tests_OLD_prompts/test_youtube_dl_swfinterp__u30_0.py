
import pytest
from io import BytesIO
from youtube_dl.swfinterp import _u30, _read_int
from unittest.mock import patch

def test_valid_input():
    buffer = BytesIO(b'\x81\x82\x83\x84')
    with patch('youtube_dl.swfinterp._read_int', return_value=0x123456):
        result = _u30(buffer)
        assert result == 0x123456
