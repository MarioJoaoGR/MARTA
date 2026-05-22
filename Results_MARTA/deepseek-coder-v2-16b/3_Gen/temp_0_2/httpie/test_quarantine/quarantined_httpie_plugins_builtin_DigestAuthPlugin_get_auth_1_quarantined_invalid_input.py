
import pytest
from httpie.plugins.builtin import DigestAuthPlugin
import requests.auth

def test_invalid_input():
    auth_plugin = DigestAuthPlugin()
    
    with pytest.raises(TypeError):
        # Test the function with invalid input types (non-string)
        auth_plugin.get_auth(username=123, password="password")

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_plugins_builtin_DigestAuthPlugin_get_auth_1_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        auth_plugin = DigestAuthPlugin()
    
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_plugins_builtin_DigestAuthPlugin_get_auth_1_test_invalid_input.py:9: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_plugins_builtin_DigestAuthPlugin_get_auth_1_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.13s ===============================
"""