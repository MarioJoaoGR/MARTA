
import pytest
from youtube_dl.downloader.f4m import FlvReader, DataTruncatedError


def test_invalid_input():
    reader = FlvReader()
    # Mocking the private method to return an insufficient byte string
    reader._read_bytes = lambda: b''
    with pytest.raises(DataTruncatedError):
        reader.read_unsigned_int()