
import pytest
from unittest.mock import patch, MagicMock
from youtube_dl.swfinterp import _read_byte, _read_bytes, compat_struct_unpack

def test_none_input():
    with pytest.raises(TypeError):
        with patch('youtube_dl.swfinterp._read_bytes', new=MagicMock()):
            _read_byte(None)

class InvalidReader:
    pass
