
import pytest
from unittest.mock import patch, MagicMock
import importlib_metadata
from httpie.compat import get_dist_name

def test_error_case():
    with patch('importlib_metadata.metadata', side_effect=importlib_metadata.PackageNotFoundError):
        ep = MagicMock()
        ep.pattern = MagicMock()
        ep.value = 'invalid_module'
    
        result = get_dist_name(ep)
        assert result is None

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

httpie/Test4DT_tests_codestral/test_httpie_compat_get_dist_name_5_test_error_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_error_case ________________________________

    def test_error_case():
        with patch('importlib_metadata.metadata', side_effect=importlib_metadata.PackageNotFoundError):
            ep = MagicMock()
            ep.pattern = MagicMock()
            ep.value = 'invalid_module'
    
            result = get_dist_name(ep)
>           assert result is None
E           AssertionError: assert <MagicMock name='mock.dist.name' id='140595394564048'> is None

httpie/Test4DT_tests_codestral/test_httpie_compat_get_dist_name_5_test_error_case.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_compat_get_dist_name_5_test_error_case.py::test_error_case
============================== 1 failed in 0.17s ===============================
"""