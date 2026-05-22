
import pytest
from unittest.mock import patch, MagicMock
import importlib_metadata
from httpie.compat import get_dist_name

def test_error_handling():
    with patch('importlib_metadata.metadata', side_effect=importlib_metadata.PackageNotFoundError):
        ep = MagicMock()
        ep.pattern = MagicMock(match=lambda x: None)
        assert get_dist_name(ep) is None

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

httpie/Test4DT_tests_codestral/test_httpie_compat_get_dist_name_1_test_error_handling.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_error_handling ______________________________

    def test_error_handling():
        with patch('importlib_metadata.metadata', side_effect=importlib_metadata.PackageNotFoundError):
            ep = MagicMock()
            ep.pattern = MagicMock(match=lambda x: None)
>           assert get_dist_name(ep) is None
E           AssertionError: assert <MagicMock name='mock.dist.name' id='140637770671888'> is None
E            +  where <MagicMock name='mock.dist.name' id='140637770671888'> = get_dist_name(<MagicMock id='140637775795664'>)

httpie/Test4DT_tests_codestral/test_httpie_compat_get_dist_name_1_test_error_handling.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_compat_get_dist_name_1_test_error_handling.py::test_error_handling
============================== 1 failed in 0.08s ===============================
"""