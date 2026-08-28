
import pytest
from youtube_dl.downloader.f4m import FlvReader, DataTruncatedError

def test_flv_reader_read_bytes():
    reader = FlvReader()
    with pytest.raises(DataTruncatedError):
        reader.read_bytes(10)  # Attempt to read 10 bytes when the implementation only reads up to available data
