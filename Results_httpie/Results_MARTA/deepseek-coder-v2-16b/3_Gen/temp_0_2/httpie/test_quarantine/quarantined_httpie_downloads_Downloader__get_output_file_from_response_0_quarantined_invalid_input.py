
import unittest
from unittest.mock import patch, MagicMock
from httpie.downloads import Downloader
from io import BytesIO

class TestDownloader(unittest.TestCase):
    @patch('httpie.downloads.requests')
    def test_get_output_file_from_response_invalid_input(self, mock_requests):
        # Create a mock response with no Content-Disposition header
        mock_response = MagicMock()
        mock_response.headers = {}
        
        # Call the method under test
        downloader = Downloader(env=None, output_file=BytesIO(), resume=False)
        with self.assertRaises(ValueError):
            downloader._get_output_file_from_response("http://example.com", mock_response)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_downloads_Downloader__get_output_file_from_response_0_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
_______ TestDownloader.test_get_output_file_from_response_invalid_input ________

self = <test_httpie_downloads_Downloader__get_output_file_from_response_0_test_invalid_input.TestDownloader testMethod=test_get_output_file_from_response_invalid_input>
mock_requests = <MagicMock name='requests' id='140658420513872'>

    @patch('httpie.downloads.requests')
    def test_get_output_file_from_response_invalid_input(self, mock_requests):
        # Create a mock response with no Content-Disposition header
        mock_response = MagicMock()
        mock_response.headers = {}
    
        # Call the method under test
        downloader = Downloader(env=None, output_file=BytesIO(), resume=False)
>       with self.assertRaises(ValueError):
E       AssertionError: ValueError not raised

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_downloads_Downloader__get_output_file_from_response_0_test_invalid_input.py:16: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_downloads_Downloader__get_output_file_from_response_0_test_invalid_input.py::TestDownloader::test_get_output_file_from_response_invalid_input
============================== 1 failed in 0.48s ===============================
"""