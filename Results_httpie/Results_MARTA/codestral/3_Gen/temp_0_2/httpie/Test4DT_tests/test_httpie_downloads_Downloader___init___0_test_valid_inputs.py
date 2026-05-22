
import unittest
from unittest.mock import patch, MagicMock
from httpie.downloads import Downloader, Environment, DownloadStatus
from io import BytesIO

class TestDownloaderInit(unittest.TestCase):
    @patch('httpie.downloads.Environment')
    def test_valid_inputs(self, MockEnvClass):
        mock_env = MockEnvClass.return_value
        output_file = BytesIO()
        downloader = Downloader(env=mock_env, output_file=output_file, resume=True)
        
        self.assertFalse(downloader.finished)
        self.assertIsInstance(downloader.status, DownloadStatus)
        self.assertEqual(downloader._output_file, output_file)
        self.assertTrue(downloader._resume)
        self.assertEqual(downloader._resumed_from, 0)
