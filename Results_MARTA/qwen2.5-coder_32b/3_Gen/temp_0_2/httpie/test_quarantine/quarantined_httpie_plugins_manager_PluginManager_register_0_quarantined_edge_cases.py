
from httpie.plugins.manager import PluginManager
import unittest.mock as mock

class TestPluginManager(unittest.TestCase):
    @mock.patch('httpie.plugins.manager.PluginManager')
    def test_register(self, mock_plugin_manager):
        plugin_manager = mock_plugin_manager()

        class BasePlugin:
            pass

        class ExamplePlugin(BasePlugin):
            def execute(self):
                print("Executing ExamplePlugin")

        plugin_manager.register(ExamplePlugin)
        self.assertIn(ExamplePlugin, plugin_manager._registered_plugins)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_plugins_manager_PluginManager_register_0_test_edge_cases
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_plugins_manager_PluginManager_register_0_test_edge_cases.py:5:24: E0602: Undefined variable 'unittest' (undefined-variable)


"""