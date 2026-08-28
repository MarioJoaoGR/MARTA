
import pytest
from unittest.mock import patch, MagicMock
from youtube_dl.downloader.common import FileDownloader

# Test scenario 1: Testing the initialization of FileDownloader with default parameters
def test_file_downloader_initialization():
    ydl = MagicMock()
    params = {}
    
    downloader = FileDownloader(ydl, params)
    
    assert hasattr(downloader, 'ydl')
    assert hasattr(downloader, 'params')
    assert hasattr(downloader, '_progress_hooks')
    assert downloader.params == {}

# Test scenario 2: Testing the initialization of FileDownloader with custom parameters
def test_file_downloader_initialization_with_custom_parameters():
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
    assert downloader.params == {
        'verbose': True,
        'ratelimit': 10240,
        'retries': 3,
        'buffersize': 8192,
        'test': False
    }

# Test scenario 3: Testing the report_unable_to_resume method
def test_report_unable_to_resume():
    ydl = MagicMock()
    params = {}
    
    downloader = FileDownloader(ydl, params)
    
    with patch('youtube_dl.downloader.common.FileDownloader.to_screen') as mock_to_screen:
        downloader.report_unable_to_resume()
        mock_to_screen.assert_called_with('[download] Unable to resume')
