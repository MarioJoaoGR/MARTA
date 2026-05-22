
import os
from unittest.mock import MagicMock, patch
from httpie.downloads import get_unique_filename

def test_get_unique_filename_custom_exists_callable():
    filename = "existingfile.txt"
    exists_mock = MagicMock(side_effect=[True, False])  # First call returns True (existing), second call returns False (not existing)
    
    with patch('httpie.downloads.os.path.exists', return_value=False):
        result = get_unique_filename(filename, exists_mock)
        assert result == 'existingfile-1.txt'

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

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_downloads_get_unique_filename_0_test_custom_exists_callable.py F [100%]

=================================== FAILURES ===================================
_______________ test_get_unique_filename_custom_exists_callable ________________

    def test_get_unique_filename_custom_exists_callable():
        filename = "existingfile.txt"
        exists_mock = MagicMock(side_effect=[True, False])  # First call returns True (existing), second call returns False (not existing)
    
        with patch('httpie.downloads.os.path.exists', return_value=False):
            result = get_unique_filename(filename, exists_mock)
>           assert result == 'existingfile-1.txt'
E           AssertionError: assert 'existingfile.txt-1' == 'existingfile-1.txt'
E             
E             - existingfile-1.txt
E             ?             --
E             + existingfile.txt-1
E             ?                 ++

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_downloads_get_unique_filename_0_test_custom_exists_callable.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_downloads_get_unique_filename_0_test_custom_exists_callable.py::test_get_unique_filename_custom_exists_callable
============================== 1 failed in 0.29s ===============================
"""