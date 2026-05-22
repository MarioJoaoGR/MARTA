
import unittest
from unittest.mock import patch, MagicMock
from httpie.downloads import Downloader, Environment, DownloadStatus

class TestDownloaderFailed(unittest.TestCase):
    @patch('httpie.downloads.Environment')
    def test_valid_inputs(self, MockEnvClass):
        mock_env = MockEnvClass.return_value
        downloader = Downloader(env=mock_env)
        
        with patch('httpie.downloads.DownloadStatus', autospec=True) as MockDownloadStatus:
            mock_status = MockDownloadStatus.return_value
            downloader.status = mock_status
            
            # Call the failed method to trigger the status termination
            downloader.failed()
            
            # Assert that the terminate method of DownloadStatus was called
            self.assertTrue(mock_status.terminate.called)
