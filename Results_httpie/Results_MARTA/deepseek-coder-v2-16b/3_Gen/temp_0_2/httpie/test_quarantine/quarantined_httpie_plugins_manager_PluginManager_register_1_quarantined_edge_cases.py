
import unittest
from httpie.plugins.manager import PluginManager
from httpie.plugins.base import BasePlugin

class TestPluginManagerRegister(unittest.TestCase):
    def test_register(self):
        plugin_manager = PluginManager()
        
        class ExamplePlugin(BasePlugin):
            def execute(self):
                pass
        
        with unittest.mock.patch('httpie.plugins.manager.PluginManager.append', return_value=None):
            plugin_manager.register(ExamplePlugin)
            
            self.assertEqual(len(plugin_manager._registered_plugins), 1)
            self.assertIsInstance(plugin_manager._registered_plugins[0], ExamplePlugin)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_plugins_manager_PluginManager_register_1_test_edge_cases
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_plugins_manager_PluginManager_register_1_test_edge_cases.py:17:33: E1101: Instance of 'PluginManager' has no '_registered_plugins' member (no-member)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_plugins_manager_PluginManager_register_1_test_edge_cases.py:18:34: E1101: Instance of 'PluginManager' has no '_registered_plugins' member (no-member)


"""