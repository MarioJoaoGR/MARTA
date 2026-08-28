
import pytest
from unittest.mock import patch, MagicMock
from youtube_dl.downloader.common import FileDownloader
from youtube_dl import YoutubeDL
import os

# Helper function to encode filename for mocking
def encodeFilename(filename):
    return filename.encode('utf-8')

@pytest.fixture
def setup_file_downloader():
    ydl = YoutubeDL()
    params = {}
    downloader = FileDownloader(ydl, params)
    yield downloader

# Test case for default behavior without nopart option
def test_temp_name_default(setup_file_downloader):
    downloader = setup_file_downloader
    filename = "sample.mp4"
    assert downloader.temp_name(filename) == "sample.mp4.part"

# Test case for existing file not being a regular file

# Test case for nopart option set to True
def test_temp_name_nopart_true():
    ydl = YoutubeDL()
    params = {'nopart': True}
    downloader = FileDownloader(ydl, params)
    filename = "sample.mp4"
    assert downloader.temp_name(filename) == "sample.mp4"

# Test case for downloading a file with '-' as the filename
def test_temp_name_dash():
    ydl = YoutubeDL()
    params = {}
    downloader = FileDownloader(ydl, params)
    filename = "-"
    assert downloader.temp_name(filename) == "-"

# Test case for existing file which is not a regular file but nopart option is ignored due to non-existent check