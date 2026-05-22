
from httpie.plugins.manager import PluginManager
import unittest.mock as mock

class TestPluginManagerStr(unittest.TestCase):
    @mock.patch('httpie.plugins.manager.PluginManager.get_transport_plugins', return_value=['tp1', 'tp2'])
    @mock.patch('httpie.plugins.manager.PluginManager.get_auth_plugins', return_value=['ap1', 'ap2'])
    @mock.patch('httpie.plugins.manager.PluginManager.get_converters', return_value=['c1', 'c2'])
    @mock.patch('httpie.plugins.manager.PluginManager.get_formatters', return_value=['f1', 'f2'])
    def test_str(self, mock_get_formatters, mock_get_converters, mock_get_auth_plugins, mock_get_transport_plugins):
        manager = PluginManager()
        
        expected_repr = {
            'adapters': ['tp1', 'tp2'],
            'auth': ['ap1', 'ap2'],
            'converters': ['c1', 'c2'],
            'formatters': ['f1', 'f2']
        }
        
        self.assertEqual(str(manager), str(expected_repr))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_plugins_manager_PluginManager___str___0_test_edge_cases
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_plugins_manager_PluginManager___str___0_test_edge_cases.py:5:27: E0602: Undefined variable 'unittest' (undefined-variable)


"""