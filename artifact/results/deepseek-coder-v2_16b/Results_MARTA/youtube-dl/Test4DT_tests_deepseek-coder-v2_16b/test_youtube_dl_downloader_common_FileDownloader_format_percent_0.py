
import pytest
from youtube_dl.downloader.common import FileDownloader

# Test for valid input in format_percent method

# Test for None input in format_percent method
def test_none_input():
    ydl = None  # Assuming ydl is already defined or passed in some way
    params = {}
    downloader = FileDownloader(ydl, params)
    percent = None
    result = downloader.format_percent(percent)
    assert result == '---.-%'