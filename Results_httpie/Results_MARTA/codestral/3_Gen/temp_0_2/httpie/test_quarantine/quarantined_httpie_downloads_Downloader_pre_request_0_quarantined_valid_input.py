
import unittest
from unittest.mock import patch, MagicMock
from httpie.downloads import Downloader
from httpie.environment import Environment
from io import BytesIO

class TestDownloader(unittest.TestCase):
    @patch('httpie.downloads.os.path.getsize', return_value=1024)
    def test_pre_request_with_resume(self, mock_getsize):
        env = Environment()
        output_file = BytesIO()
        downloader = Downloader(env=env, output_file=output_file, resume=True)
        
        request_headers = {}
        downloader.pre_request(request_headers)
        
        self.assertEqual(request_headers['Accept-Encoding'], 'identity')
        self.assertEqual(request_headers['Range'], 'bytes=1024-')
        self.assertTrue(downloader._resume)
        self.assertEqual(downloader._resumed_from, 1024)

    @patch('httpie.downloads.os.path.getsize', return_value=0)
    def test_pre_request_without_resume(self, mock_getsize):
        env = Environment()
        output_file = BytesIO()
        downloader = Downloader(env=env, output_file=output_file, resume=False)
        
        request_headers = {}
        downloader.pre_request(request_headers)
        
        self.assertEqual(request_headers['Accept-Encoding'], 'identity')
        self.assertNotIn('Range', request_headers)
        self.assertFalse(downloader._resume)
        self.assertEqual(downloader._resumed_from, 0)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_downloads_Downloader_pre_request_0_test_valid_input
httpie/Test4DT_tests_codestral/test_httpie_downloads_Downloader_pre_request_0_test_valid_input.py:5:0: E0401: Unable to import 'httpie.environment' (import-error)
httpie/Test4DT_tests_codestral/test_httpie_downloads_Downloader_pre_request_0_test_valid_input.py:5:0: E0611: No name 'environment' in module 'httpie' (no-name-in-module)


"""