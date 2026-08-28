
import pytest
from unittest.mock import patch, MagicMock
from youtube_dl.downloader.f4m import FlvReader, DataTruncatedError

# Test 1: Read bytes from FLV file successfully
def test_read_bytes_success():
    reader = FlvReader()
    with patch('youtube_dl.downloader.f4m.FlvReader.read', return_value=b'a'*1024):
        data = reader.read_bytes(1024)
        assert len(data) == 1024

# Test 2: Read bytes from FLV file with truncation error
def test_read_bytes_truncation_error():
    reader = FlvReader()
    with patch('youtube_dl.downloader.f4m.FlvReader.read', return_value=b'a'*512):
        with pytest.raises(DataTruncatedError):
            reader.read_bytes(1024)
