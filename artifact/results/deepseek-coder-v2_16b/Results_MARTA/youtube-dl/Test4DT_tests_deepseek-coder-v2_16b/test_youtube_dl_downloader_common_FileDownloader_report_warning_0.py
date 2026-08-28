
import pytest
from youtube_dl.downloader.common import FileDownloader
from unittest.mock import patch, MagicMock

# Test 1: Instantiation of FileDownloader with valid parameters
def test_file_downloader_instantiation():
    ydl = MagicMock()
    params = {
        'verbose': True,
        'quiet': False,
        'ratelimit': 10240,
        'retries': 3,
        'buffersize': 8192,
        'noresizebuffer': False,
        'continuedl': True,
        'noprogress': False,
        'logtostderr': False,
        'consoletitle': True,
        'nopart': False,
        'updatetime': False,
        'test': False,
        'min_filesize': 0,
        'max_filesize': float('inf'),
        'xattr_set_filesize': False,
        'external_downloader_args': [],
        'hls_use_mpegts': False,
        'http_chunk_size': None,
    }
    
    downloader = FileDownloader(ydl, params)
    
    assert isinstance(downloader, FileDownloader), "FileDownloader instance was not created correctly."
    assert downloader.params == params, "Parameters were not set correctly in the FileDownloader instance."

# Test 2: Reporting a warning during file download
def test_report_warning():
    ydl = MagicMock()
    params = {}
    downloader = FileDownloader(ydl, params)
    
    with patch.object(ydl, 'report_warning') as mock_report_warning:
        downloader.report_warning("Test warning")
        mock_report_warning.assert_called_once_with("Test warning")
