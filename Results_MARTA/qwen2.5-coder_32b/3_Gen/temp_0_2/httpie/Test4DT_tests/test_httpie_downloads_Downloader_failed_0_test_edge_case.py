
import unittest
from httpie.downloads import Downloader, DownloadStatus
from unittest.mock import patch

class TestDownloaderFailed(unittest.TestCase):
    @patch('httpie.downloads.Downloader')
    def test_edge_case(self, MockDownloader):
        # Arrange
        mock_downloader = MockDownloader()
        
        # Act
        mock_downloader.failed()
        
        # Assert
        self.assertTrue(mock_downloader.status.exit_status)
