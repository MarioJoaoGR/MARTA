
import pytest
from youtube_dl.downloader.common import FileDownloader

# Test for valid initialization of FileDownloader class
def test_valid_initialization():
    ydl = "example_ydl"
    params = {
        'verbose': True,
        'ratelimit': 10240,
        'retries': 3,
        'buffersize': 8192,
        'test': False
    }
    downloader = FileDownloader(ydl, params)
    assert isinstance(downloader, FileDownloader), "Initialization failed: Expected a FileDownloader instance"

# Test for invalid parameter in initialization