
import unittest
from unittest.mock import patch, MagicMock
from httpie.downloads import Downloader, Environment, DownloadStatus
from io import BytesIO

class TestDownloaderInit(unittest.TestCase):
    @patch('httpie.downloads.Environment')
    def test_init_with_resume_and_output_file(self, MockEnvClass):
        mock_env = MockEnvClass.return_value
        output_file = BytesIO()
        downloader = Downloader(env=mock_env, output_file=output_file, resume=True)
        
        self.assertFalse(downloader.finished)
        self.assertIsInstance(downloader.status, DownloadStatus)
        self.assertEqual(downloader._output_file, output_file)
        self.assertTrue(downloader._resume)
        self.assertEqual(downloader._resumed_from, 0)

    @patch('httpie.downloads.Environment')
    def test_init_without_resume_and_with_output_file(self, MockEnvClass):
        mock_env = MockEnvClass.return_value
        output_file = BytesIO()
        downloader = Downloader(env=mock_env, output_file=output_file, resume=False)
        
        self.assertFalse(downloader.finished)
        self.assertIsInstance(downloader.status, DownloadStatus)
        self.assertEqual(downloader._output_file, output_file)
        self.assertFalse(downloader._resume)
        self.assertEqual(downloader._resumed_from, 0)

    @patch('httpie.downloads.Environment')
    def test_init_without_output_file_and_with_resume(self, MockEnvClass):
        mock_env = MockEnvClass.return_value
        downloader = Downloader(env=mock_env, resume=True)
        
        self.assertFalse(downloader.finished)
        self.assertIsInstance(downloader.status, DownloadStatus)
        self.assertIsNone(downloader._output_file)
        self.assertTrue(downloader._resume)
        self.assertEqual(downloader._resumed_from, 0)

    @patch('httpie.downloads.Environment')
    def test_init_without_output_file_and_without_resume(self, MockEnvClass):
        mock_env = MockEnvClass.return_value
        downloader = Downloader(env=mock_env)
        
        self.assertFalse(downloader.finished)
        self.assertIsInstance(downloader.status, DownloadStatus)
        self.assertIsNone(downloader._output_file)
        self.assertFalse(downloader._resume)
        self.assertEqual(downloader._resumed_from, 0)
