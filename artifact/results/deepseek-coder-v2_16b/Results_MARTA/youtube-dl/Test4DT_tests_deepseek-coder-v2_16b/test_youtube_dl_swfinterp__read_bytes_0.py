
import pytest
from io import BytesIO
from youtube_dl.swfinterp import _read_bytes

def test_valid_input():
    data = b'abcdefghij'
    reader = BytesIO(data)
    result = _read_bytes(5, reader)
    assert len(result) == 5
    assert result == b'abcde'

def test_edge_case_zero_count():
    data = b'abcdefghij'
    reader = BytesIO(data)
    result = _read_bytes(0, reader)
    assert len(result) == 0
    assert result == b''

def test_invalid_input():
    with pytest.raises(AssertionError):
        _read_bytes(-1, None)
