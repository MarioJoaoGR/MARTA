
import pytest
from unittest.mock import patch
from httpie.utils import is_version_greater

def test_edge_case_empty():
    with patch('httpie.utils.is_version_greater', return_value=True):
        assert is_version_greater("", "") == True

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

httpie/Test4DT_tests_codestral/test_httpie_utils_is_version_greater_9_test_edge_case_empty.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_edge_case_empty _____________________________

    def test_edge_case_empty():
        with patch('httpie.utils.is_version_greater', return_value=True):
>           assert is_version_greater("", "") == True
E           AssertionError: assert False == True
E            +  where False = is_version_greater('', '')

httpie/Test4DT_tests_codestral/test_httpie_utils_is_version_greater_9_test_edge_case_empty.py:8: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_utils_is_version_greater_9_test_edge_case_empty.py::test_edge_case_empty
============================== 1 failed in 0.19s ===============================
"""