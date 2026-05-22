
import pytest
from httpie.plugins.builtin import DigestAuthPlugin
import requests.auth

def test_none_input():
    auth_plugin = DigestAuthPlugin()
    username = None
    password = None
    
    with pytest.raises(TypeError):
        auth_plugin.get_auth(username, password)

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

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_plugins_builtin_DigestAuthPlugin_get_auth_2_test_none_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_none_input ________________________________

    def test_none_input():
        auth_plugin = DigestAuthPlugin()
        username = None
        password = None
    
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_plugins_builtin_DigestAuthPlugin_get_auth_2_test_none_input.py:11: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_plugins_builtin_DigestAuthPlugin_get_auth_2_test_none_input.py::test_none_input
============================== 1 failed in 0.15s ===============================
"""