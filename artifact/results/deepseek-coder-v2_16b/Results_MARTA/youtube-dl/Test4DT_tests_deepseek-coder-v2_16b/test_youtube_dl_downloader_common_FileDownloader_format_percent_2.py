
import pytest
from youtube_dl.downloader.common import FileDownloader

# Test for valid percent input
def test_valid_percent():
    percent = 50.0
    result = FileDownloader.format_percent(percent)
    assert result == '%6s' % ('%3.1f%%' % percent)

# Test for invalid percent input (negative value)