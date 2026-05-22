
import os
from unittest.mock import patch
from httpie.downloads import get_unique_filename

def test_custom_exists_callable():
    filename = "example.txt"
    expected_filename = "example-0.txt"
    
    with patch('os.path.exists', return_value=False):
        assert get_unique_filename(filename) == expected_filename

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_downloads_get_unique_filename_0_test_custom_exists_callable.py F [100%]

=================================== FAILURES ===================================
_________________________ test_custom_exists_callable __________________________

    def test_custom_exists_callable():
        filename = "example.txt"
        expected_filename = "example-0.txt"
    
        with patch('os.path.exists', return_value=False):
>           assert get_unique_filename(filename) == expected_filename
E           AssertionError: assert 'example.txt-5' == 'example-0.txt'
E             
E             - example-0.txt
E             ?        --
E             + example.txt-5
E             ?            ++

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_downloads_get_unique_filename_0_test_custom_exists_callable.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_downloads_get_unique_filename_0_test_custom_exists_callable.py::test_custom_exists_callable
============================== 1 failed in 0.38s ===============================
"""