
import pytest
from youtube_dl.downloader.common import FileDownloader
from unittest.mock import patch, MagicMock

# Test 1: Initialize FileDownloader with default parameters
def test_file_downloader_default_parameters():
    ydl = MagicMock()
    params = {}
    downloader = FileDownloader(ydl, params)
    assert hasattr(downloader, 'ydl')
    assert hasattr(downloader, 'params')
    assert hasattr(downloader, '_progress_hooks')
    assert downloader.params == {}

# Test 2: Initialize FileDownloader with specific parameters
def test_file_downloader_specific_parameters():
    ydl = MagicMock()
    params = {
        'verbose': True,
        'ratelimit': 10240,
        'retries': 3,
        'buffersize': 8192,
        'test': False
    }
    downloader = FileDownloader(ydl, params)
    assert hasattr(downloader, 'ydl')
    assert hasattr(downloader, 'params')
    assert hasattr(downloader, '_progress_hooks')
    assert downloader.params == params

# Test 3: Add a progress hook to FileDownloader

# Test 4: Report destination filename