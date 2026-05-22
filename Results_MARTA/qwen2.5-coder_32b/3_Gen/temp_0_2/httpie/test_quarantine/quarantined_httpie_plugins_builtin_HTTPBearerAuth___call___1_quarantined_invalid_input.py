
from httpie.plugins.builtin import HTTPBearerAuth
import pytest
from unittest.mock import patch

def test_invalid_input():
    with patch('httpie.plugins.builtin.HTTPBearerAuth.__init__', return_value=None):
        with pytest.raises(ValueError) as excinfo:
            auth = HTTPBearerAuth("your_bearer_token")
            assert False, "Expected ValueError but did not raise"

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

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_plugins_builtin_HTTPBearerAuth___call___1_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        with patch('httpie.plugins.builtin.HTTPBearerAuth.__init__', return_value=None):
            with pytest.raises(ValueError) as excinfo:
                auth = HTTPBearerAuth("your_bearer_token")
>               assert False, "Expected ValueError but did not raise"
E               AssertionError: Expected ValueError but did not raise
E               assert False

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_plugins_builtin_HTTPBearerAuth___call___1_test_invalid_input.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_plugins_builtin_HTTPBearerAuth___call___1_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.17s ===============================
"""