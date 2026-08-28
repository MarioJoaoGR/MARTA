
import pytest
from youtube_dl.downloader.common import FileDownloader
from unittest.mock import patch, MagicMock

# Test 1: Instantiation of FileDownloader with valid parameters
def test_file_downloader_instantiation():
    ydl = MagicMock()
    params = {
        'verbose': True,
        'ratelimit': 10240,
        'retries': 3,
        'buffersize': 8192,
        'test': False
    }
    downloader = FileDownloader(ydl, params)
    assert isinstance(downloader, FileDownloader), "FileDownloader instance creation failed"

# Test 2: Report error method should call ydl.report_error with appropriate arguments
def test_file_downloader_report_error():
    ydl = MagicMock()
    params = {}
    downloader = FileDownloader(ydl, params)
    downloader.report_error("some_error", "additional_info")
    ydl.report_error.assert_called_with("some_error", "additional_info")

# Test 3: Adding a progress hook and verifying it is added correctly
def test_file_downloader_add_progress_hook():
    ydl = MagicMock()
    params = {}
    downloader = FileDownloader(ydl, params)
    mock_hook = MagicMock()
    downloader.add_progress_hook(mock_hook)
    assert mock_hook in downloader._progress_hooks, "Progress hook was not added correctly"

# Test 4: Verifying the report_error method with a different set of arguments
def test_file_downloader_report_error_with_different_args():
    ydl = MagicMock()
    params = {}
    downloader = FileDownloader(ydl, params)
    downloader.report_error("another_error", "more_info")
    ydl.report_error.assert_called_with("another_error", "more_info")
