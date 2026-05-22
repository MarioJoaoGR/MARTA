
import pytest
from httpie.plugins.builtin import HTTPBasicAuth
from base64 import b64encode

def test_empty_inputs():
    with pytest.raises(ValueError):
        assert HTTPBasicAuth.make_header('', '') == 'Basic dXNlcjpwYXNz'

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_plugins_builtin_HTTPBasicAuth_make_header_3_test_empty_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_empty_inputs _______________________________

    def test_empty_inputs():
        with pytest.raises(ValueError):
>           assert HTTPBasicAuth.make_header('', '') == 'Basic dXNlcjpwYXNz'
E           AssertionError: assert 'Basic Og==' == 'Basic dXNlcjpwYXNz'
E             
E             - Basic dXNlcjpwYXNz
E             + Basic Og==

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_plugins_builtin_HTTPBasicAuth_make_header_3_test_empty_inputs.py:8: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_plugins_builtin_HTTPBasicAuth_make_header_3_test_empty_inputs.py::test_empty_inputs
============================== 1 failed in 0.20s ===============================
"""