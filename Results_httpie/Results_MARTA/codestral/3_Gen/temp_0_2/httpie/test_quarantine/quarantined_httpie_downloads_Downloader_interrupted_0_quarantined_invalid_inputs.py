
import unittest
from unittest.mock import patch, MagicMock
from httpie.downloads import Downloader
from httpie.environment import Environment

class TestDownloader(unittest.TestCase):
    @patch('httpie.downloads.Downloader')
    def test_interrupted_when_download_is_finished_and_total_size_equals_downloaded(self, MockDownloader):
        mock_env = MagicMock()
        mock_output_file = MagicMock()
        downloader = MockDownloader(env=mock_env, output_file=mock_output_file, resume=False)
        
        # Set the status attributes to simulate a finished download with total size equal to downloaded size
        downloader.status.total_size = 100
        downloader.status.downloaded = 100
        downloader.finished = True
        
        self.assertFalse(downloader.interrupted())

    @patch('httpie.downloads.Downloader')
    def test_interrupted_when_download_is_finished_and_total_size_not_equal_to_downloaded(self, MockDownloader):
        mock_env = MagicMock()
        mock_output_file = MagicMock()
        downloader = MockDownloader(env=mock_env, output_file=mock_output_file, resume=False)
        
        # Set the status attributes to simulate a finished download with total size not equal to downloaded size
        downloader.status.total_size = 100
        downloader.status.downloaded = 90
        downloader.finished = True
        
        self.assertTrue(downloader.interrupted())

    @patch('httpie.downloads.Downloader')
    def test_interrupted_when_download_is_not_finished(self, MockDownloader):
        mock_env = MagicMock()
        mock_output_file = MagicMock()
        downloader = MockDownloader(env=mock_env, output_file=mock_output_file, resume=False)
        
        # Set the status attributes to simulate a not finished download
        downloader.status.total_size = 100
        downloader.status.downloaded = 50
        downloader.finished = False
        
        self.assertFalse(downloader.interrupted())

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_downloads_Downloader_interrupted_0_test_invalid_inputs
httpie/Test4DT_tests_codestral/test_httpie_downloads_Downloader_interrupted_0_test_invalid_inputs.py:5:0: E0401: Unable to import 'httpie.environment' (import-error)
httpie/Test4DT_tests_codestral/test_httpie_downloads_Downloader_interrupted_0_test_invalid_inputs.py:5:0: E0611: No name 'environment' in module 'httpie' (no-name-in-module)


"""