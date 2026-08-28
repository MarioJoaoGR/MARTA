
import pytest
from youtube_dl.downloader.common import FileDownloader
from unittest.mock import patch, MagicMock

# Test 1: Basic Initialization with Minimal Parameters
def test_file_downloader_basic_initialization():
    ydl = MagicMock()
    params = {'verbose': True}
    downloader = FileDownloader(ydl, params)
    assert downloader.params == params
    assert downloader.ydl is ydl

# Test 2: Full Initialization with All Parameters
def test_file_downloader_full_initialization():
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
        'http_chunk_size': None
    }
    downloader = FileDownloader(ydl, params)
    assert downloader.params == params
    assert downloader.ydl is ydl

# Test 3: Report Destination Filename