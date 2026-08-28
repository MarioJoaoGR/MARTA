
import pytest
from youtube_dl.postprocessor.common import PostProcessor
from youtube_dl import YoutubeDL
import os
from unittest.mock import patch, MagicMock

# Test for try_utime method in PostProcessor class
def test_try_utime():
    # Create a mock downloader instance
    mock_downloader = YoutubeDL()
    mock_downloader.report_warning = MagicMock()
    
    # Instantiate the PostProcessor with the mock downloader
    post_processor = PostProcessor(mock_downloader)
    
    # Test case where updating utime is successful
    with patch('os.utime', return_value=None):
        post_processor.try_utime("test_path", 1, 2)
        assert mock_downloader.report_warning.call_count == 0
    
    # Test case where updating utime fails
    with patch('os.utime', side_effect=Exception()):
        post_processor.try_utime("test_path", 1, 2)
        mock_downloader.report_warning.assert_called_once_with('Cannot update utime of file')
