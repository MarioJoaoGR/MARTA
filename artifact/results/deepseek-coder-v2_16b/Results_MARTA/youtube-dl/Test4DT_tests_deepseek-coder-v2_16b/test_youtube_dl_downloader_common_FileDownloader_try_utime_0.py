
import os
import time
from unittest.mock import patch
from youtube_dl.downloader.common import FileDownloader


def test_try_utime_invalid_timestamp():
    downloader = FileDownloader(None, {})
    with patch('os.path.isfile', return_value=True):
        with patch('time.time', return_value=1234567890.0):
            result = downloader.try_utime('existing_file', 'invalid_timestamp')
            assert result is None

def test_try_utime_nonexistent_file():
    downloader = FileDownloader(None, {})
    with patch('os.path.isfile', return_value=False):
        result = downloader.try_utime('non_existent_file', '1234567890')
        assert result is None