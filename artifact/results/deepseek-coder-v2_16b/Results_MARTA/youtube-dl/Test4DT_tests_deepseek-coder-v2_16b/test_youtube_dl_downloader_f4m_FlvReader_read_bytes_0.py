
import pytest
from youtube_dl.downloader.f4m import FlvReader, DataTruncatedError

def test_flv_reader_read_bytes():
    reader = FlvReader()
    # Test reading exactly n bytes
    with pytest.raises(DataTruncatedError) as excinfo:
        data = reader.read_bytes(1024)
    assert str(excinfo.value) == 'FlvReader error: need 1024 bytes while only 0 bytes got'

def test_flv_reader_read_bytes_less():
    reader = FlvReader()
    # Test reading less than n bytes
    with pytest.raises(DataTruncatedError) as excinfo:
        data = reader.read_bytes(1024)
    assert str(excinfo.value) == 'FlvReader error: need 1024 bytes while only 0 bytes got'
