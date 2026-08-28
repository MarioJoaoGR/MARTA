
import pytest
from youtube_dl.downloader.common import FileDownloader
from unittest.mock import patch, MagicMock

# Test 1: Initialize FileDownloader with valid parameters
def test_file_downloader_init():
    ydl = MagicMock()
    params = {
        'verbose': True,
        'ratelimit': 10240,
        'retries': 3,
        'buffersize': 8192,
        'test': False
    }
    downloader = FileDownloader(ydl, params)
    assert downloader.params == params
    assert downloader.ydl is ydl

# Test 2: Undo temporary name with .part extension
def test_undo_temp_name():
    downloader = FileDownloader(None, {})
    filename_with_part = 'testfile.part'
    filename_without_part = downloader.undo_temp_name(filename_with_part)
    assert filename_without_part == 'testfile'

# Test 3: Undo temporary name without .part extension
def test_undo_temp_name_no_extension():
    downloader = FileDownloader(None, {})
    filename_without_part = 'testfile'
    assert downloader.undo_temp_name(filename_without_part) == 'testfile'
