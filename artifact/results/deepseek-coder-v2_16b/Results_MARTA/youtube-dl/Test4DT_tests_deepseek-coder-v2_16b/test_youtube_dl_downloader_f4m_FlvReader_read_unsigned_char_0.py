
import pytest
from youtube_dl.downloader.f4m import FlvReader, DataTruncatedError

def test_valid_input():
    reader = FlvReader()
    # Assuming read_bytes is a method that returns some bytes or raises an error if not enough bytes are available
    with pytest.raises(DataTruncatedError):
        assert reader.read_unsigned_char() == 10

