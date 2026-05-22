
import pytest
from unittest.mock import patch
from httpie.plugins.manager import PluginManager

def test_invalid_inputs():
    manager = PluginManager()
    
    with patch('httpie.plugins.manager.PluginManager.get_auth_plugins', return_value=[]):
        with pytest.raises(KeyError):
            manager.get_auth_plugin_mapping()

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_plugins_manager_PluginManager_get_auth_plugin_mapping_0_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        manager = PluginManager()
    
        with patch('httpie.plugins.manager.PluginManager.get_auth_plugins', return_value=[]):
>           with pytest.raises(KeyError):
E           Failed: DID NOT RAISE <class 'KeyError'>

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_plugins_manager_PluginManager_get_auth_plugin_mapping_0_test_invalid_inputs.py:10: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_plugins_manager_PluginManager_get_auth_plugin_mapping_0_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.13s ===============================
"""