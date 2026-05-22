
import unittest
from unittest.mock import patch
from httpie.downloads import trim_filename_if_needed

class TestTrimFilenameIfNeeded(unittest.TestCase):
    
    @patch('httpie.downloads.get_filename_max_length')
    def test_valid_input(self, mock_get_filename_max_length):
        # Set up the mock to return a fixed value for max length
        mock_get_filename_max_length.return_value = 20
        
        # Test case where filename length exceeds max length by extra amount
        result = trim_filename_if_needed("longfilenamewithextension.txt", directory='/home/user', extra=5)
        self.assertEqual(result, "longfilenam.txt")
        
        # Test case where filename length does not exceed max length
        result = trim_filename_if_needed("shortfile", directory='/home/user', extra=0)
        self.assertEqual(result, "shortfile")
        
        # Test case where filename is exactly the max length
        mock_get_filename_max_length.return_value = 25
        result = trim_filename_if_needed("longfilenamewithextension.txt", directory='/home/user', extra=0)
        self.assertEqual(result, "longfilenamewithextension.txt")

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_downloads_trim_filename_if_needed_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
__________________ TestTrimFilenameIfNeeded.test_valid_input ___________________

self = <test_httpie_downloads_trim_filename_if_needed_0_test_valid_input.TestTrimFilenameIfNeeded testMethod=test_valid_input>
mock_get_filename_max_length = <MagicMock name='get_filename_max_length' id='139747771680912'>

    @patch('httpie.downloads.get_filename_max_length')
    def test_valid_input(self, mock_get_filename_max_length):
        # Set up the mock to return a fixed value for max length
        mock_get_filename_max_length.return_value = 20
    
        # Test case where filename length exceeds max length by extra amount
        result = trim_filename_if_needed("longfilenamewithextension.txt", directory='/home/user', extra=5)
        self.assertEqual(result, "longfilenam.txt")
    
        # Test case where filename length does not exceed max length
        result = trim_filename_if_needed("shortfile", directory='/home/user', extra=0)
        self.assertEqual(result, "shortfile")
    
        # Test case where filename is exactly the max length
        mock_get_filename_max_length.return_value = 25
        result = trim_filename_if_needed("longfilenamewithextension.txt", directory='/home/user', extra=0)
>       self.assertEqual(result, "longfilenamewithextension.txt")
E       AssertionError: 'longfilenamewithexten.txt' != 'longfilenamewithextension.txt'
E       - longfilenamewithexten.txt
E       + longfilenamewithextension.txt
E       ?                      ++++

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_downloads_trim_filename_if_needed_0_test_valid_input.py:24: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_downloads_trim_filename_if_needed_0_test_valid_input.py::TestTrimFilenameIfNeeded::test_valid_input
============================== 1 failed in 0.25s ===============================
"""