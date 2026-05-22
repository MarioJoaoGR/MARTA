
import unittest
from httpie.plugins.manager import PluginManager
from unittest.mock import patch, MagicMock

class TestPluginManagerStr(unittest.TestCase):
    
    @patch('httpie.plugins.manager.PluginManager.get_transport_plugins', return_value=['tp1', 'tp2'])
    @patch('httpie.plugins.manager.PluginManager.get_auth_plugins', return_value=['ap1', 'ap2'])
    @patch('httpie.plugins.manager.PluginManager.get_converters', return_value=['c1', 'c2'])
    @patch('httpie.plugins.manager.PluginManager.get_formatters', return_value=['f1', 'f2'])
    def test_invalid_inputs(self, mock_get_formatters, mock_get_converters, mock_get_auth_plugins, mock_get_transport_plugins):
        manager = PluginManager()
        
        expected_str = repr_dict({
            'adapters': ['tp1', 'tp2'],
            'auth': ['ap1', 'ap2'],
            'converters': ['c1', 'c2'],
            'formatters': ['f1', 'f2']
        })
        
        self.assertEqual(str(manager), expected_str)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_plugins_manager_PluginManager___str___0_test_invalid_inputs
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_plugins_manager_PluginManager___str___0_test_invalid_inputs.py:15:23: E0602: Undefined variable 'repr_dict' (undefined-variable)


"""