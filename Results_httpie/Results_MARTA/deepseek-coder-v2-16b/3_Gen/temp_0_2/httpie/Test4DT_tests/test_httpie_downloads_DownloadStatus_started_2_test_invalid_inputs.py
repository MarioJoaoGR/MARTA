
import unittest
from unittest.mock import patch, MagicMock
from httpie.downloads import DownloadStatus

class TestDownloadStatus(unittest.TestCase):
    def setUp(self):
        self.download_status = DownloadStatus(env="test_env")

    @patch('httpie.downloads.DownloadStatus.start_display')
    def test_started_with_total_size(self, mock_start_display):
        total_size = 102400
        output_file = MagicMock()
        
        self.download_status.started(output_file=output_file, resumed_from=0, total_size=total_size)
        
        self.assertEqual(self.download_status.total_size, total_size)
        self.assertEqual(self.download_status.resumed_from, 0)
        self.assertIsNotNone(self.download_status.time_started)
        mock_start_display.assert_called_once_with(output_file=output_file)

    @patch('httpie.downloads.DownloadStatus.start_display')
    def test_started_without_total_size(self, mock_start_display):
        output_file = MagicMock()
        
        self.download_status.started(output_file=output_file, resumed_from=0, total_size=None)
        
        self.assertIsNone(self.download_status.total_size)
        self.assertEqual(self.download_status.resumed_from, 0)
        self.assertIsNotNone(self.download_status.time_started)
        mock_start_display.assert_called_once_with(output_file=output_file)
