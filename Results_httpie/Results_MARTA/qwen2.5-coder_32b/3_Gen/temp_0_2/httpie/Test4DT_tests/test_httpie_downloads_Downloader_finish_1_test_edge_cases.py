
from unittest.mock import patch
import pytest
from httpie.downloads import Downloader, Environment

class TestDownloaderFinish:
    @patch('httpie.downloads.Environment')
    @patch('httpie.downloads.Downloader')
    def test_finish(self, MockDownloader, MockEnvironment):
        # Create a mock environment and downloader instances
        env = MockEnvironment.return_value
        downloader = MockDownloader.return_value
    
        # Call the finish method
        downloader.finish()
    
        # Check that the status is marked as finished
        assert downloader.finished, "Download should be marked as finished"
        assert downloader.status.finished(), f"Status should indicate completion but got {downloader.status.finished()}"
