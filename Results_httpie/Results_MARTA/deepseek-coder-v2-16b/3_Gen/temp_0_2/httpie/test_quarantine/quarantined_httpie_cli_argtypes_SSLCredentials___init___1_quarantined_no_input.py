
from httpie.cli.argtypes import SSLCredentials
from unittest.mock import patch

def test_no_input():
    with patch('httpie.cli.argtypes.SSLCredentials.__init__', return_value=None):
        ssl_credentials = SSLCredentials(None)
        assert ssl_credentials.value is None

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_argtypes_SSLCredentials___init___1_test_no_input.py F [100%]

=================================== FAILURES ===================================
________________________________ test_no_input _________________________________

    def test_no_input():
        with patch('httpie.cli.argtypes.SSLCredentials.__init__', return_value=None):
            ssl_credentials = SSLCredentials(None)
>           assert ssl_credentials.value is None
E           AttributeError: 'SSLCredentials' object has no attribute 'value'

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_argtypes_SSLCredentials___init___1_test_no_input.py:8: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_argtypes_SSLCredentials___init___1_test_no_input.py::test_no_input
============================== 1 failed in 0.17s ===============================
"""