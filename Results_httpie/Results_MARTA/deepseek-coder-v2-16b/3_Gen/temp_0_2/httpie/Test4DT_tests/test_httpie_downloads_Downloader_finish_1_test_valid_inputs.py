
import unittest
from unittest.mock import patch
from httpie.downloads import Downloader, Environment, DownloadStatus
from io import BytesIO

class TestDownloaderFinish(unittest.TestCase):
    def test_finish_with_valid_inputs(self):
        # Arrange
        env = Environment(config={"network": "example.com"})
        output_file = BytesIO()
        downloader = Downloader(env=env, output_file=output_file, resume=False)
        
        # Act
        with patch('httpie.downloads.DownloadStatus.finished') as mock_finished:
            downloader.finish()
            
            # Assert
            self.assertTrue(downloader.finished)
            mock_finished.assert_called_once()
