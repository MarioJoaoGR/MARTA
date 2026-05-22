
import pytest
from httpie.plugins.builtin import HTTPBasicAuth
from base64 import b64encode

def test_empty_string_input():
    with pytest.raises(ValueError):
        HTTPBasicAuth.make_header('', '')

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

httpie/Test4DT_tests_codestral/test_httpie_plugins_builtin_HTTPBasicAuth_make_header_0_test_empty_string_input.py F [100%]

=================================== FAILURES ===================================
___________________________ test_empty_string_input ____________________________

    def test_empty_string_input():
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

httpie/Test4DT_tests_codestral/test_httpie_plugins_builtin_HTTPBasicAuth_make_header_0_test_empty_string_input.py:7: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_plugins_builtin_HTTPBasicAuth_make_header_0_test_empty_string_input.py::test_empty_string_input
============================== 1 failed in 0.13s ===============================
"""