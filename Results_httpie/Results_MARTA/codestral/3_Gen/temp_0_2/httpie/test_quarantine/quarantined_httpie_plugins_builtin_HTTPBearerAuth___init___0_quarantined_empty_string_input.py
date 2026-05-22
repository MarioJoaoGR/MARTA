
import pytest
from unittest.mock import patch
from httpie.plugins.builtin import HTTPBearerAuth

def test_empty_string_input():
    with patch('httpie.plugins.builtin.HTTPBearerAuth.__init__', return_value=None):
        auth = HTTPBearerAuth("")
        assert auth.token == ""

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

httpie/Test4DT_tests_codestral/test_httpie_plugins_builtin_HTTPBearerAuth___init___0_test_empty_string_input.py F [100%]

=================================== FAILURES ===================================
___________________________ test_empty_string_input ____________________________

    def test_empty_string_input():
        with patch('httpie.plugins.builtin.HTTPBearerAuth.__init__', return_value=None):
            auth = HTTPBearerAuth("")
>           assert auth.token == ""
E           AttributeError: 'HTTPBearerAuth' object has no attribute 'token'

httpie/Test4DT_tests_codestral/test_httpie_plugins_builtin_HTTPBearerAuth___init___0_test_empty_string_input.py:9: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_plugins_builtin_HTTPBearerAuth___init___0_test_empty_string_input.py::test_empty_string_input
============================== 1 failed in 0.13s ===============================
"""