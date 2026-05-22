
import pytest
from unittest.mock import patch
from plugin_manager import PluginManager, BasePlugin

def test_invalid_inputs():
    plugin_manager = PluginManager()
    
    with pytest.raises(TypeError):
        # Test registering a non-plugin type (e.g., int)
        plugin_manager.register(int)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_plugins_manager_PluginManager_register_1_test_invalid_inputs
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_plugins_manager_PluginManager_register_1_test_invalid_inputs.py:4:0: E0401: Unable to import 'plugin_manager' (import-error)


"""