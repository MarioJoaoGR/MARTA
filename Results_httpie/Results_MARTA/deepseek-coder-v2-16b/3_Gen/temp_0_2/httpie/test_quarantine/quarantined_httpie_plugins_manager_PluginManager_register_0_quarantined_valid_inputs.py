
from httpie.plugins.manager import PluginManager
import unittest.mock as mock

class TestPluginManagerRegister(unittest.TestCase):
    def test_register_valid_inputs(self):
        plugin_manager = PluginManager()
        
        class ExamplePlugin(object):
            pass
        
        with mock.patch('httpie.plugins.manager.PluginManager.append', return_value=None) as mock_append:
            plugin_manager.register(ExamplePlugin)
            mock_append.assert_called_once_with(ExamplePlugin)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_plugins_manager_PluginManager_register_0_test_valid_inputs
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_plugins_manager_PluginManager_register_0_test_valid_inputs.py:5:32: E0602: Undefined variable 'unittest' (undefined-variable)


"""