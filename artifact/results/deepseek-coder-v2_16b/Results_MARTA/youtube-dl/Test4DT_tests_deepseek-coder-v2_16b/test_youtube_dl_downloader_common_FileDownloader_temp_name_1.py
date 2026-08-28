
import os
from unittest.mock import patch
import pytest
from youtube_dl.downloader.common import FileDownloader
from youtube_dl import YoutubeDL

# Test for temp_name method when nopart is True
def test_temp_name_nopart():
    ydl = YoutubeDL()
    params = {'nopart': True}
    downloader = FileDownloader(ydl, params)
    filename = 'testfile'
    assert downloader.temp_name(filename) == 'testfile'

# Test for temp_name method when filename is '-'
def test_temp_name_dash():
    ydl = YoutubeDL()
    params = {}
    downloader = FileDownloader(ydl, params)
    filename = '-'
    assert downloader.temp_name(filename) == '-'

# Test for temp_name method when file exists and is not a file

# Test for temp_name method when file does not exist and nopart is False
def test_temp_name_non_existing_file():
    ydl = YoutubeDL()
    params = {}
    downloader = FileDownloader(ydl, params)
    filename = 'testfile'
    with patch('os.path.exists', return_value=False):
        assert downloader.temp_name(filename) == f"{filename}.part"