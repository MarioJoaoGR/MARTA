
import pytest
from youtube_dl.downloader.f4m import FlvReader, DataTruncatedError

def test_flv_reader_read_bytes():
    reader = FlvReader()
    with pytest.raises(DataTruncatedError):
        reader.read_bytes(1024)


def test_flv_reader_read_bytes_short_read():
    reader = FlvReader()
    with pytest.raises(DataTruncatedError):
        reader.read_bytes(5)