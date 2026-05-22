
import pytest
from unittest.mock import patch
from httpie.plugins.manager import PluginManager
from typing import List, Type
from httpie.plugins.formatter_plugin import FormatterPlugin

class TestInvalidInputs:
    def test_invalid_inputs(self):
        manager = PluginManager()
        
        with patch.object(manager, 'get_formatters', return_value=[str]):
            with pytest.raises(TypeError):
                manager.get_formatters()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_plugins_manager_PluginManager_get_formatters_3_test_invalid_inputs
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_plugins_manager_PluginManager_get_formatters_3_test_invalid_inputs.py:6:0: E0401: Unable to import 'httpie.plugins.formatter_plugin' (import-error)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_plugins_manager_PluginManager_get_formatters_3_test_invalid_inputs.py:6:0: E0611: No name 'formatter_plugin' in module 'httpie.plugins' (no-name-in-module)


"""