
import pytest
from httpie.plugins.base import AuthPlugin
import requests.auth

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_plugins_base_AuthPlugin_get_auth_1.py F [100%]

=================================== FAILURES ===================================
___________________________ test_missing_credentials ___________________________

    def test_missing_credentials():
        class MyAuthPlugin(AuthPlugin):
            def get_auth(self, username=None, password=None):
                if username is None and password is None:
                    return requests.auth.HTTPBasicAuth("default_user", "default_pass")
                raise ValueError("Username and password are required for this authentication type.")
    
        my_plugin = MyAuthPlugin()
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

/opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_plugins_base_AuthPlugin_get_auth_1.py:14: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_plugins_base_AuthPlugin_get_auth_1.py::test_missing_credentials
============================== 1 failed in 0.13s ===============================
"""