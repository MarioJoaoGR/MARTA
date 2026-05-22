
from httpie.downloads import filename_from_content_disposition
from unittest.mock import patch, MagicMock
import os

class TestHttpieDownloadsFilenameFromContentDisposition:
    @patch('httpie.downloads.os')
    def test_valid_input(self, mock_os):
        # Mock os.path.basename to return a specific value
        mock_os.path.basename = MagicMock(return_value='example.txt')
    
        # Test cases
        assert filename_from_content_disposition('attachment; filename=example.txt') == 'example.txt'
        assert filename_from_content_disposition('form-data; name="file"; filename=example.txt') == 'example.txt'
        assert filename_from_content_disposition('inline; filename=no-extension') == 'no-extension'

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_downloads_filename_from_content_disposition_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
______ TestHttpieDownloadsFilenameFromContentDisposition.test_valid_input ______

self = <test_httpie_downloads_filename_from_content_disposition_0_test_valid_input.TestHttpieDownloadsFilenameFromContentDisposition object at 0x7f4b77d49510>
mock_os = <MagicMock name='os' id='139962105769872'>

    @patch('httpie.downloads.os')
    def test_valid_input(self, mock_os):
        # Mock os.path.basename to return a specific value
        mock_os.path.basename = MagicMock(return_value='example.txt')
    
        # Test cases
        assert filename_from_content_disposition('attachment; filename=example.txt') == 'example.txt'
        assert filename_from_content_disposition('form-data; name="file"; filename=example.txt') == 'example.txt'
>       assert filename_from_content_disposition('inline; filename=no-extension') == 'no-extension'
E       AssertionError: assert 'example.txt' == 'no-extension'
E         
E         - no-extension
E         + example.txt

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_downloads_filename_from_content_disposition_0_test_valid_input.py:15: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_downloads_filename_from_content_disposition_0_test_valid_input.py::TestHttpieDownloadsFilenameFromContentDisposition::test_valid_input
============================== 1 failed in 0.17s ===============================
"""